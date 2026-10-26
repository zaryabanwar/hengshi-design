"""Type-source substitution observations, not a coupled runtime selection."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import tarfile
import json
import os
import re
import hashlib
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
CURRENT = ROOT / 'output/research/frontend-build-evaluation-2026-10-06'
CANDIDATE = CURRENT / 'candidate'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    target = OUT / name
    if target.exists(): raise RuntimeError(f'Refusing overwrite {target}')
    target.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def extract(version):
    destination = OUT / version / 'declarations'
    reuse = destination.exists()
    if not reuse: destination.mkdir()
    seen = set()
    package_root = None
    with tarfile.open(OUT / version / 'types-three.tgz', 'r:gz') as archive:
        for member in archive.getmembers():
            relative = PurePosixPath(member.name)
            if relative.is_absolute() or '..' in relative.parts or '\\' in member.name:
                raise RuntimeError('Unsafe tar path')
            key = member.name.casefold()
            if key in seen: raise RuntimeError('Duplicate tar path')
            seen.add(key)
            path = destination.joinpath(*relative.parts).resolve()
            if not path.is_relative_to(destination.resolve()): raise RuntimeError('Escaping tar path')
            if member.isdir(): path.mkdir(parents=True, exist_ok=True); continue
            if not member.isfile(): raise RuntimeError('Non-regular tar member')
            path.parent.mkdir(parents=True, exist_ok=True)
            payload = archive.extractfile(member).read()
            if reuse:
                if not path.is_file() or path.read_bytes() != payload: raise RuntimeError('Retained declaration bytes differ')
            else: path.write_bytes(payload)
            if relative.name == 'package.json':
                meta = json.loads(path.read_text(encoding='utf-8'))
                if meta.get('name') == '@types/three': package_root = path.parent
    if package_root is None: raise RuntimeError('Package root absent')
    meta = json.loads((package_root / 'package.json').read_text(encoding='utf-8'))
    return package_root, package_root / meta.get('types', meta.get('typings', 'index.d.ts'))

def main():
    frozen = json.loads((CURRENT / 'review-inputs.json').read_text(encoding='utf-8'))
    before = {item['path']: sha(ROOT / item['path']) for item in frozen}
    if any(before[item['path']] != item['sha256'] for item in frozen): raise RuntimeError('Frozen input changed before observation')
    env = {key: os.environ[key] for key in ('SystemRoot','WINDIR','COMSPEC','TEMP','TMP') if key in os.environ}
    env['PATH'] = str(CURRENT / 'runtime') + os.pathsep + str(Path(env['SystemRoot']) / 'System32')
    observations = []
    for version in ('0.185.4', '0.184.1'):
        package, entry = extract(version)
        config = {'extends': str(CANDIDATE / 'tsconfig.json'),
                  'compilerOptions': {'types': [str(CANDIDATE / 'node_modules/vite/client'), 'react', 'react-dom'], 'typeRoots': [str(CANDIDATE / 'node_modules/@types')], 'paths': {'three': [entry.as_posix()], 'three/*': [package.as_posix() + '/*']}},
                  'files': [str(CANDIDATE / 'src/fixture.tsx')]}
        cfg = OUT / version / 'tsconfig.type-source-corrected.json'
        cfg.write_text(json.dumps(config, indent=2) + '\n', encoding='utf-8')
        for compiler, relative in (('api6','typescript/bin/tsc6'), ('native7','@typescript/native/bin/tsc')):
            command = [str(CURRENT / 'runtime/node.exe'), str(CANDIDATE / 'node_modules' / relative), '--project', str(cfg), '--pretty', 'false']
            proc = subprocess.run(command, cwd=CANDIDATE, env=env, capture_output=True, timeout=90)
            for stream in ('stdout','stderr'):
                (OUT / version / f'corrected-{compiler}.{stream}.txt').write_bytes(getattr(proc, stream))
            codes = [int(v) for v in re.findall(rb'error TS(\d+):', proc.stdout + proc.stderr)]
            observations.append({'types_version': version, 'compiler': compiler, 'command': command,
                                 'exit_code': proc.returncode, 'diagnostic_codes': codes})
    changed = [path for path, digest in before.items() if sha(ROOT / path) != digest]
    save('corrected-type-source-boundary-observations.json', {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'commands': observations,
        'frozen_inputs_checked': len(frozen), 'changed_frozen_inputs': changed,
        'limits': 'Type declarations only mapped through explicit paths. Installed Three runtime remains 0.186.1. Not a peer-resolved older runtime graph, build/browser proof or recommendation to mix old declarations with new runtime.'})
    if changed: raise RuntimeError('Frozen input changed')
    print(json.dumps(observations, indent=2))

if __name__ == '__main__': main()
