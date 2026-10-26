"""Isolated published-tool recheck, with no install or application changes."""
import base64
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
OLD = ROOT / 'output/research/native-lint-conformance-2026-10-05/receipt.json'
prior = json.loads(OLD.read_text())
guards = prior['protected_after']
for name, digest in guards.items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name

tool = OUT / 'tool/node_modules'
if tool.exists():
    raise SystemExit('Tool directory already exists; inspect before overwrite')
tool.mkdir(parents=True)
packages = []
for name in ['oxlint', '@oxlint/binding-win32-x64-msvc']:
    with urllib.request.urlopen('https://registry.npmjs.org/' + name + '/1.87.0', timeout=25) as response:
        metadata = json.load(response)
    assert metadata['version'] == '1.87.0'
    with urllib.request.urlopen(metadata['dist']['tarball'], timeout=25) as response:
        data = response.read()
    integrity = 'sha512-' + base64.b64encode(hashlib.sha512(data).digest()).decode()
    assert integrity == metadata['dist']['integrity']
    stem = name.replace('@', '').replace('/', '-')
    (OUT / (stem + '-metadata.json')).write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    (OUT / (stem + '.tgz')).write_bytes(data)
    target = tool / name
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        for member in archive.getmembers():
            assert member.name.startswith('package/'), member.name
            relative = Path(member.name[len('package/'):])
            assert not relative.is_absolute() and '..' not in relative.parts
            assert ':' not in str(relative) and '\\' not in member.name
            destination = (target / relative).resolve()
            assert destination.is_relative_to(target.resolve())
            if member.isdir():
                destination.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(archive.extractfile(member).read())
            else:
                raise RuntimeError('Unsupported archive member: ' + member.name)
    packages.append({'name': name, 'version': '1.87.0', 'tarball': metadata['dist']['tarball'], 'integrity_matched': True, 'sha256': hashlib.sha256(data).hexdigest(), 'scope': 'Tarball integrity only; signatures/attestation/build provenance not verified'})
    print('Integrity-verified isolated unpack:', name, flush=True)

new_tool = tool / 'oxlint/bin/oxlint'
rows = []
for record in prior['cases']:
    command = record['command'][:]
    assert 'oxlint/bin/oxlint' in command[1].replace('\\', '/')
    command[1] = str(new_tool)
    completed = subprocess.run(command, cwd=OLD.parent, capture_output=True, text=True, timeout=30)
    label = record['case']
    (OUT / (label + '-stdout.txt')).write_text(completed.stdout, encoding='utf-8')
    (OUT / (label + '-stderr.txt')).write_text(completed.stderr, encoding='utf-8')
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError:
        result = {}
    rows.append({'case': label, 'command': command, 'cwd': str(OLD.parent), 'prior_exit_code': record['exit_code'], 'exit_code': completed.returncode, 'codes': [d['code'] for d in result.get('diagnostics', [])], 'prior_codes': record.get('codes', []), 'number_of_files': result.get('number_of_files'), 'number_of_rules': result.get('number_of_rules'), 'stdout_sha256': hashlib.sha256(completed.stdout.encode()).hexdigest(), 'stderr_sha256': hashlib.sha256(completed.stderr.encode()).hexdigest()})
    print(label, completed.returncode, rows[-1]['codes'], flush=True)

inventory_run = subprocess.run([command[0], str(new_tool), '--rules', '--format', 'json'], capture_output=True, text=True, timeout=30)
assert inventory_run.returncode == 0
(OUT / 'rules-inventory.json').write_text(inventory_run.stdout, encoding='utf-8')
inventory = json.loads(inventory_run.stdout)
names = {row['value'] for row in inventory if row['scope'] == 'react'}
missing = [name for name in ['component-hook-factories', 'config', 'gating'] if name not in names]
after = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in guards}
assert after == guards
(OUT / 'receipt.json').write_text(json.dumps({'status': 'DOING', 'date': '2026-10-05', 'scope': 'Exact existing synthetic CLI fixtures against fresh 1.87.0 isolated Windows tool; no selection, install, experimental rules or app test', 'packages': packages, 'cases': rows, 'missing_identical_recommended_rule_ids': missing, 'guard_hashes_before_and_after': after, 'old_receipt_sha256': hashlib.sha256(OLD.read_bytes()).hexdigest()}, indent=2) + '\n', encoding='utf-8')
print('Completed', len(rows), 'commands; protected guards unchanged:', len(after), flush=True)
