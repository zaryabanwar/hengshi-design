"""Read-only candidate supply-chain observations; never fix or reinstall."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json
import os
import subprocess
import shutil

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = ROOT / 'output/research/frontend-three-remedy-evaluation-2026-10-06'
CANDIDATE = BASE / 'candidate'
RUNTIME = ROOT / 'output/research/frontend-build-evaluation-2026-10-06/runtime'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    with (OUT / name).open('x', encoding='utf-8', newline='\n') as file:
        json.dump(value, file, indent=2)
        file.write('\n')

def command(name, arguments, env):
    args = [str(RUNTIME / 'node.exe'), str(RUNTIME / 'package/bin/npm-cli.js'), *arguments,
            '--ignore-scripts', '--workspaces=false', '--include=dev', '--include=optional',
            '--registry=https://registry.npmjs.org', f'--prefix={CANDIDATE}',
            f'--userconfig={BASE / "empty-user.npmrc"}', f'--globalconfig={BASE / "empty-global.npmrc"}',
            f'--cache={OUT / "metadata-cache"}', '--loglevel=error']
    started = datetime.now(timezone.utc).isoformat()
    process = subprocess.Popen(args, cwd=CANDIDATE, env=env,
                               stdout=(OUT / f'{name}.stdout.json').open('xb'),
                               stderr=(OUT / f'{name}.stderr.txt').open('xb'))
    print(f'{name} PID {process.pid}', flush=True)
    code = process.wait()
    save(f'{name}-receipt.json', {'started_at_utc': started,
         'ended_at_utc': datetime.now(timezone.utc).isoformat(), 'command': args,
         'exit_code': code, 'scope': 'Read-only research candidate. No audit fix, install, script or policy override.'})
    print(f'{name} terminal exit {code}', flush=True)

def main():
    if (OUT / 'input-guard.json').exists():
        raise RuntimeError('Evidence exists; refusing overwrite')
    frozen = json.loads((BASE / 'review-inputs.json').read_text(encoding='utf-8'))
    mismatches = [row['path'] for row in frozen if sha(ROOT / row['path']) != row['sha256']]
    save('input-guard.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
         'packet_sha256': sha(BASE / 'review-inputs.json'), 'checked': len(frozen), 'mismatches': mismatches})
    if mismatches:
        raise RuntimeError('Frozen input changed')
    for name in ('audit.js', 'sbom.js'):
        source = RUNTIME / 'package/lib/commands' / name
        shutil.copyfile(source, OUT / f'npm12-{name}')
    for name in ('verify-signatures.js', 'sbom-spdx.js'):
        shutil.copyfile(RUNTIME / 'package/lib/utils' / name, OUT / f'npm12-{name}')
    lock = json.loads((CANDIDATE / 'package-lock.json').read_text(encoding='utf-8'))
    licence_rows = []
    for relative, entry in lock['packages'].items():
        if not relative:
            continue
        package_root = CANDIDATE / relative
        metadata = package_root / 'package.json'
        installed = metadata.exists()
        package = json.loads(metadata.read_text(encoding='utf-8')) if installed else {}
        texts = []
        if installed:
            for path in sorted(package_root.iterdir()):
                if path.is_file() and path.name.lower().startswith(('license', 'licence', 'copying', 'notice')):
                    destination = OUT / 'licence-texts' / relative / path.name
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(path, destination)
                    texts.append({'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path),
                                  'saved': destination.relative_to(ROOT).as_posix(), 'bytes': path.stat().st_size})
        licence_rows.append({'lock_path': relative, 'version': entry.get('version'),
             'installed': installed, 'name': package.get('name'), 'lock_licence': entry.get('license'),
             'installed_licence': package.get('license'), 'integrity': entry.get('integrity'),
             'resolved': entry.get('resolved'), 'optional': entry.get('optional', False),
             'metadata_sha256': sha(metadata) if installed else None,
             'top_level_licence_and_notice_files': texts})
    save('licence-inventory.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
         'lock_sha256': sha(CANDIDATE / 'package-lock.json'), 'records': licence_rows,
         'licence_counts_from_lock': dict(Counter(str(row['lock_licence']) for row in licence_rows)),
         'limits': 'Metadata declarations and top-level texts only; not recursive bundled-source clearance, legal advice, notices assembly, full-file archive integrity or deployment inventory.'})
    env = {key: os.environ[key] for key in ('SystemRoot', 'WINDIR', 'COMSPEC', 'TEMP', 'TMP') if key in os.environ}
    env['PATH'] = str(RUNTIME) + os.pathsep + str(Path(env['SystemRoot']) / 'System32')
    command('advisory-audit', ['audit', '--json', '--package-lock-only'], env)
    command('lock-sbom', ['sbom', '--sbom-format=spdx', '--package-lock-only'], env)
    command('installed-signatures', ['audit', 'signatures', '--json'], env)
    after = [row['path'] for row in frozen if sha(ROOT / row['path']) != row['sha256']]
    save('post-command-guard.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
         'checked': len(frozen), 'mismatches': after})
    if after:
        raise RuntimeError('Read-only commands changed frozen inputs')
    print('Supply-chain commands and frozen-input guard completed.', flush=True)

if __name__ == '__main__':
    main()
