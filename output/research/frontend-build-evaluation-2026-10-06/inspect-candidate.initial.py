"""Read-only compiler/module observations for an isolated research candidate."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = Path(__file__).resolve().parent
CANDIDATE = EVIDENCE / 'candidate'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    target = EVIDENCE / name
    if target.exists():
        raise RuntimeError(f'Refusing to overwrite {target}')
    target.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def observe_control():
    observations = []
    env = {k: os.environ[k] for k in ('SystemRoot', 'WINDIR', 'COMSPEC', 'TEMP', 'TMP') if k in os.environ}
    env['PATH'] = str(EVIDENCE / 'runtime') + os.pathsep + str(Path(env['SystemRoot']) / 'System32')
    for compiler, entry in (
        ('api6', 'typescript/bin/tsc6'),
        ('native7', '@typescript/native/bin/tsc'),
    ):
        command = [str(EVIDENCE / 'runtime/node.exe'), str(CANDIDATE / 'node_modules' / entry),
                   '--project', str(CANDIDATE / 'tsconfig.loader-control.json'), '--pretty', 'false']
        result = subprocess.run(command, cwd=CANDIDATE, env=env, capture_output=True, timeout=90)
        for stream in ('stdout', 'stderr'):
            path = EVIDENCE / f'loader-control-{compiler}.{stream}.txt'
            if path.exists():
                raise RuntimeError(f'Refusing to overwrite {path}')
            path.write_bytes(getattr(result, stream))
        codes = [int(v) for v in re.findall(rb'error TS(\d+):', result.stdout + result.stderr)]
        observations.append({'compiler': compiler, 'command': command, 'exit_code': result.returncode,
                             'diagnostic_codes': codes, 'expected_codes': [2430, 2416],
                             'reproduces_observed_declaration_failure': result.returncode != 0 and codes == [2430, 2416]})
    save('loader-control-observations.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
         'scope': 'finite public type entries, no loader execution, build or browser', 'commands': observations})
    if not all(o['reproduces_observed_declaration_failure'] for o in observations):
        raise RuntimeError('Loader control did not reproduce the observed failure')

def inspect():
    protected = json.loads((EVIDENCE / 'protected-before.json').read_text(encoding='utf-8'))
    differences = [{'path': item['path'], 'before': item['sha256'], 'after': digest(ROOT / item['path'])}
                   for item in protected if digest(ROOT / item['path']) != item['sha256']]
    save('protected-after.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
         'inputs': len(protected), 'differences': differences})
    if differences:
        raise RuntimeError('Protected inputs changed')
    lock = json.loads((CANDIDATE / 'package-lock.json').read_text(encoding='utf-8'))
    relevant = [
        'typescript/package.json', '@typescript/typescript6/package.json', '@typescript/old/package.json',
        '@typescript/native/package.json', '@typescript/typescript-win32-x64/package.json',
        'typescript/bin/tsc6', '@typescript/old/lib/_tsc.js', '@typescript/native/bin/tsc',
        '@typescript/typescript-win32-x64/lib/tsc.exe',
        '@react-three/drei/package.json', '@react-three/drei/index.d.ts',
        '@react-three/drei/core/OrbitControls.d.ts', 'three/package.json', '@types/three/package.json',
        'three-stdlib/package.json', 'three-stdlib/loaders/SVGLoader.d.ts', 'three-stdlib/loaders/TGALoader.d.ts',
        '@types/three/src/extras/core/ShapePath.d.ts', '@types/three/src/loaders/DataTextureLoader.d.ts',
        '@types/three/src/textures/Texture.d.ts', '@types/three/src/textures/DataTexture.d.ts',
        '@types/three/src/constants.d.ts', '@react-three/fiber/package.json',
        'vite/package.json', '@vitejs/plugin-react/package.json', '@vitejs/plugin-react/dist/index.js',
        '@vitejs/plugin-react/dist/reactCompilerPreset.js', '@tailwindcss/vite/package.json',
        'gensync/package.json', '@babel/core/package.json', 'eslint-plugin-react-hooks/package.json',
    ]
    installed = []
    for relative in relevant:
        file = CANDIDATE / 'node_modules' / relative
        installed.append({'path': file.relative_to(ROOT).as_posix(), 'exists': file.is_file(),
                          'sha256': digest(file) if file.is_file() else None})
    save('installed-relevant-inputs.json', installed)
    versions = {}
    for relative in relevant:
        if relative.endswith('package.json'):
            file = CANDIDATE / 'node_modules' / relative
            if file.is_file():
                obj = json.loads(file.read_text(encoding='utf-8'))
                versions[relative] = {'name': obj['name'], 'version': obj['version']}
    save('installed-version-observations.json', versions)
    save('candidate-inspection.json', {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'lock_sha256': digest(CANDIDATE / 'package-lock.json'),
        'lock_records': len(lock['packages']), 'protected_inputs_unchanged': len(protected),
        'claim': 'Strict resolved/installed observation with independently reproducible declaration failure; not a selected graph.',
        'type_gate': 'REJECTED for this exact candidate and strict declaration-check policy',
        'vite_invoked': False, 'browser_invoked': False,
        'limits': ['No runtime loader failure established', 'No package scripts ran during frozen install',
                   'No full supply-chain, licence or advisory clearance', 'No lint conformance or gensync execution/exclusion proof',
                   'No application, model, production lock, account, machine runtime or adoption changes'],
    })

if __name__ == '__main__':
    observe_control()
    inspect()
    print('Loader declaration failure reproduced; protected inputs unchanged.')
