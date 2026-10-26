"""Finite public-protocol probe. A new output directory is mandatory per run.

Inputs are read-only reviewed React fixtures. Changes use LSP buffers only.
This is not an editor extension, performance, build or adoption test.
"""
import argparse
import datetime
import hashlib
import json
import os
import pathlib
import queue
import subprocess
import threading
import time
import traceback


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    evidence = pathlib.Path(__file__).resolve().parent
    repo = evidence.parents[2]
    fixtures = repo / 'output/research/typescript-react-parity-2026-10-06'
    out = pathlib.Path(args.output).resolve()
    if not out.is_relative_to(repo / 'output/research'):
        raise ValueError('output must be a new directory under output/research')
    out.mkdir(exist_ok=False)
    identity = json.loads((evidence / 'executable-identity.json').read_text())
    exe = pathlib.Path(identity['executable'])
    assert sha(exe) == identity['exe_sha256']
    protected = json.loads((fixtures / 'unchanged-inputs.json').read_text())
    paths = [repo / item['path'] for item in protected]
    paths += list((fixtures / 'node_modules').rglob('*'))
    paths += list(fixtures.glob('*/fixture.tsx')) + list(fixtures.glob('*/tsconfig.json'))
    paths += [fixtures / 'fixture-oracles.json', exe, evidence / 'probe_lsp.py']
    guards = [{'path': str(path.relative_to(repo)).replace('\\', '/'), 'sha256': sha(path)}
              for path in sorted(set(paths)) if path.is_file()]
    (out / 'guards.before.json').write_text(json.dumps(guards, indent=2) + '\n')
    env = {key: value for key, value in os.environ.items()
           if key.upper() in {'SYSTEMROOT', 'WINDIR', 'COMSPEC', 'PATHEXT', 'PROGRAMFILES',
                             'PROGRAMFILES(X86)', 'COMMONPROGRAMFILES', 'PROGRAMDATA'}}
    # No npm/Node directory or provider/auth variables are passed to this process.
    # This is environment containment, not an OS network sandbox.
    env['PATH'] = str(pathlib.Path(os.environ['SYSTEMROOT']) / 'System32')
    for key, name in [('TEMP', 'tmp'), ('TMP', 'tmp'), ('USERPROFILE', 'profile'),
                      ('APPDATA', 'appdata'), ('LOCALAPPDATA', 'localappdata')]:
        directory = out / 'runtime' / name
        directory.mkdir(parents=True, exist_ok=True)
        env[key] = str(directory)
    (out / 'environment.json').write_text(json.dumps(env, indent=2) + '\n')
    events = []
    incoming = queue.Queue()
    stderr = bytearray()
    stdout = bytearray()
    stdin = bytearray()
    started = time.monotonic()
    def event(direction, message):
        events.append({'seconds': round(time.monotonic() - started, 6),
                       'direction': direction, 'message': message})
    process = subprocess.Popen([str(exe), '--lsp', '--stdio'], cwd=fixtures, env=env,
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
    (out / 'process.json').write_text(json.dumps({'pid': process.pid, 'parent_pid': os.getpid(),
        'command': [str(exe), '--lsp', '--stdio'], 'cwd': str(fixtures)}, indent=2) + '\n')
    def reader():
        try:
            while True:
                headers = {}
                while True:
                    line = process.stdout.readline()
                    if not line:
                        incoming.put({'_transport_eof': True})
                        return
                    stdout.extend(line)
                    if line == b'\r\n':
                        break
                    key, value = line.decode('ascii').split(':', 1)
                    headers[key.lower()] = value.strip()
                size = int(headers['content-length'])
                data = process.stdout.read(size)
                stdout.extend(data)
                if len(data) != size:
                    raise EOFError('truncated frame')
                message = json.loads(data.decode('utf-8'))
                event('server', message)
                incoming.put(message)
        except Exception as error:
            incoming.put({'_transport_error': repr(error)})
    def read_stderr():
        while chunk := process.stderr.read(4096):
            stderr.extend(chunk)
    threads = [threading.Thread(target=reader, daemon=True),
               threading.Thread(target=read_stderr, daemon=True)]
    for thread in threads:
        thread.start()
    def send(message):
        event('client', message)
        data = json.dumps(message, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
        frame = f'Content-Length: {len(data)}\r\n\r\n'.encode('ascii') + data
        stdin.extend(frame)
        process.stdin.write(frame)
        process.stdin.flush()
    def notify(method, params=None):
        payload = {'jsonrpc': '2.0', 'method': method}
        if params is not None:
            payload['params'] = params
        send(payload)
    next_id = 0
    def request(method, params=None):
        nonlocal next_id
        next_id += 1
        payload = {'jsonrpc': '2.0', 'id': next_id, 'method': method}
        if params is not None:
            payload['params'] = params
        send(payload)
        deadline = time.monotonic() + 30
        while True:
            # A deadline is an observation failure; cleanup records the actual process outcome.
            message = incoming.get(timeout=max(0.01, deadline - time.monotonic()))
            if '_transport_eof' in message or '_transport_error' in message:
                raise RuntimeError(message)
            if message.get('id') == next_id and 'method' not in message:
                if 'error' in message:
                    raise RuntimeError(message)
                return message['result']
            if 'id' in message and 'method' in message:
                if message['method'] in {'workspace/diagnostic/refresh', 'window/workDoneProgress/create'}:
                    send({'jsonrpc': '2.0', 'id': message['id'], 'result': None})
                else:
                    send({'jsonrpc': '2.0', 'id': message['id'], 'error': {
                        'code': -32601, 'message': 'Not supported by finite probe client'}})
                    raise RuntimeError('unexpected server request: ' + message['method'])
            if time.monotonic() >= deadline:
                raise TimeoutError('response deadline: ' + method)
    result = {'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'observations': [], 'buffer_transitions': [], 'success': False,
              'limits': 'finite native7 public LSP React diagnostics only; no editor UI, emit, bundler, runtime, plugins, whole-graph compatibility or adoption proof'}
    initialized = False
    shutdown = False
    try:
        init = request('initialize', {'processId': os.getpid(),
            'clientInfo': {'name': 'Hengshi isolated compatibility probe', 'version': '1'},
            'rootUri': fixtures.as_uri(), 'workspaceFolders': [{'uri': fixtures.as_uri(), 'name': 'synthetic-react-fixtures'}],
            'capabilities': {'general': {'positionEncodings': ['utf-16']},
                'workspace': {'diagnostics': {'refreshSupport': True}},
                'textDocument': {'diagnostic': {'dynamicRegistration': False, 'relatedDocumentSupport': False},
                                 'synchronization': {'dynamicRegistration': False}}}})
        result['initialize'] = init
        initialized = True
        notify('initialized', {})
        capabilities = init['capabilities']
        assert capabilities.get('diagnosticProvider'), 'pull diagnostic capability is not advertised'
        sync = capabilities['textDocumentSync']
        sync_kind = sync if isinstance(sync, int) else sync.get('change', 0)
        assert sync_kind in (1, 2), sync
        assert capabilities.get('positionEncoding', 'utf-16') == 'utf-16'
        def diagnostics(uri):
            params = {'textDocument': {'uri': uri}}
            provider = capabilities['diagnosticProvider']
            if isinstance(provider, dict) and 'identifier' in provider:
                params['identifier'] = provider['identifier']
            report = request('textDocument/diagnostic', params)
            assert report['kind'] == 'full', report
            return {'codes': sorted(int(item['code']) for item in report['items']), 'report': report}
        opened = []
        oracles = json.loads((fixtures / 'fixture-oracles.json').read_text())['fixtures']
        for oracle in oracles:
            path = fixtures / oracle['name'] / 'fixture.tsx'
            uri = path.as_uri()
            text = path.read_text(encoding='utf-8')
            notify('textDocument/didOpen', {'textDocument': {'uri': uri,
                'languageId': 'typescriptreact', 'version': 1, 'text': text}})
            opened.append(uri)
            observed = diagnostics(uri)
            result['observations'].append({'name': oracle['name'], 'expected_codes': oracle['expected_codes'],
                'observed': observed, 'match': observed['codes'] == oracle['expected_codes']})
        path = fixtures / 'invalid-prop/fixture.tsx'
        uri = path.as_uri()
        original = path.read_text(encoding='utf-8')
        corrected = original.replace('title={42}', 'title={"Welcome"}')
        assert corrected != original
        current = original
        for version, text, expected in [(2, corrected, []), (3, original, [2322])]:
            if sync_kind == 1:
                changes = [{'text': text}]
            else:
                lines = current.split('\n')
                end = {'line': len(lines) - 1, 'character': len(lines[-1].encode('utf-16-le')) // 2}
                changes = [{'range': {'start': {'line': 0, 'character': 0}, 'end': end}, 'text': text}]
            notify('textDocument/didChange', {'textDocument': {'uri': uri, 'version': version},
                                           'contentChanges': changes})
            current = text
            observed = diagnostics(uri)
            result['buffer_transitions'].append({'version': version, 'expected_codes': expected,
                'observed': observed, 'match': observed['codes'] == expected})
        for uri in opened:
            notify('textDocument/didClose', {'textDocument': {'uri': uri}})
        result['success'] = all(row['match'] for row in result['observations'] + result['buffer_transitions'])
    except Exception:
        result['error'] = traceback.format_exc()
    finally:
        try:
            if initialized and process.poll() is None:
                result['shutdown_response'] = request('shutdown')
                shutdown = True
                notify('exit')
                process.stdin.close()
                process.wait(timeout=10)
        except Exception:
            result['cleanup_error'] = traceback.format_exc()
        if process.poll() is None:
            result['explicit_probe_cleanup'] = 'terminate own direct server process'
            process.terminate()
            process.wait(timeout=10)
        for thread in threads:
            thread.join(timeout=2)
        result['process_exit_code'] = process.returncode
        result['shutdown_then_exit'] = shutdown
        result['process_gone'] = process.poll() is not None
        result['input_guards'] = [{'path': row['path'], 'unchanged': sha(repo / row['path']) == row['sha256']}
                                  for row in guards]
        assert all(row['unchanged'] for row in result['input_guards'])
        (out / 'protocol.json').write_text(json.dumps(events, indent=2) + '\n', encoding='utf-8')
        (out / 'client.frames').write_bytes(stdin)
        (out / 'server.frames').write_bytes(stdout)
        (out / 'server.stderr.txt').write_bytes(stderr)
        (out / 'observations.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'success': result['success'], 'cases': len(result['observations']),
        'transitions': len(result['buffer_transitions']), 'exit': result['process_exit_code'],
        'gone': result['process_gone'], 'error': result.get('error')}))
    return 0 if result['success'] and result['process_exit_code'] == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
