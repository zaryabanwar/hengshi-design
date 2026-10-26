"""Create one isolated matching-runtime candidate; no app or machine adoption."""
from pathlib import Path
from datetime import datetime, timezone
import urllib.request
import json
import hashlib
import shutil
import os
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PRIOR = ROOT / 'output/research/frontend-build-evaluation-2026-10-06'
CANDIDATE = OUT / 'candidate'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    path = OUT / name
    if path.exists(): raise RuntimeError(f'Refusing overwrite {path}')
    path.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Hengshi-v1-isolated-compatibility'}),timeout=40) as response:
        return response.read()

def main():
    if CANDIDATE.exists(): raise RuntimeError('Candidate already exists')
    payload = fetch('https://registry.npmjs.org/three')
    (OUT / 'three-registry.json').write_bytes(payload)
    registry = json.loads(payload)
    stable184 = [v for v in registry['versions'] if v.startswith('0.184.') and all(part.isdigit() for part in v.split('.'))]
    version = max(stable184, key=lambda v: tuple(int(i) for i in v.split('.')))
    save('runtime-version-observation.json', {'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'registry_latest':registry['dist-tags']['latest'], 'three_184_candidate':version,
        'selected_types_for_probe':'0.184.1','status':'isolated candidate, not selected production versions',
        'record':registry['versions'][version], 'published_at':registry['time'][version]})
    CANDIDATE.mkdir()
    manifest = json.loads((PRIOR / 'candidate/package.json').read_text(encoding='utf-8'))
    manifest['name'] = 'hengshi-v1-isolated-three-remedy-evaluation'
    manifest['description'] = 'Isolated matched stable Three runtime/types compatibility evidence; no application adoption or newest-release exception approval'
    manifest['dependencies']['three'] = version
    manifest['devDependencies']['@types/three'] = '0.184.1'
    (CANDIDATE / 'package.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    for name in ('index.html','vite.config.mjs','tsconfig.json','tsconfig.invalid.json','tsconfig.loader-control.json'):
        shutil.copyfile(PRIOR / 'candidate' / name, CANDIDATE / name)
    shutil.copytree(PRIOR / 'candidate/src', CANDIDATE / 'src')
    protected = json.loads((PRIOR / 'protected-before.json').read_text(encoding='utf-8'))
    for item in protected: item['sha256'] = sha(ROOT / item['path'])
    save('protected-before.json', protected)
    save('source-correspondence.json', [{'file':name,'prior_sha256':sha(PRIOR/'candidate'/name),'copied_sha256':sha(CANDIDATE/name)}
        for name in ('index.html','vite.config.mjs','tsconfig.json','tsconfig.invalid.json','tsconfig.loader-control.json','src/fixture.tsx','src/invalid-control.tsx','src/loader-declaration-control.ts','src/fixture.css')])
    for name in ('empty-user.npmrc','empty-global.npmrc'): (OUT/name).write_bytes(b'')
    env={k:os.environ[k] for k in ('SystemRoot','WINDIR','COMSPEC','TEMP','TMP') if k in os.environ}
    env['PATH']=str(PRIOR/'runtime')+os.pathsep+str(Path(env['SystemRoot'])/'System32')
    common=[str(PRIOR/'runtime/node.exe'),str(PRIOR/'runtime/package/bin/npm-cli.js')]
    flags=['--ignore-scripts','--strict-peer-deps','--engine-strict','--audit=false','--fund=false','--workspaces=false','--include=dev','--include=optional',
           f'--prefix={CANDIDATE}','--registry=https://registry.npmjs.org',f'--userconfig={OUT / "empty-user.npmrc"}',f'--globalconfig={OUT / "empty-global.npmrc"}',
           f'--cache={PRIOR / "metadata-cache"}','--loglevel=error']
    for action,args in [('resolution',['install','--package-lock-only']),('frozen-install',['ci'])]:
        command=common+args+flags
        started=datetime.now(timezone.utc).isoformat()
        before=sha(CANDIDATE/'package-lock.json') if (CANDIDATE/'package-lock.json').exists() else None
        proc=subprocess.run(command,cwd=CANDIDATE,env=env,capture_output=True,timeout=240)
        for stream in ('stdout','stderr'): (OUT/f'{action}.{stream}.txt').write_bytes(getattr(proc,stream))
        save(f'{action}-receipt.json',{'started_at_utc':started,'ended_at_utc':datetime.now(timezone.utc).isoformat(),'command':command,
            'cwd':str(CANDIDATE),'exit_code':proc.returncode,'node':'26.10.0','npm':'12.2.0','lock_before':before,'lock_after':sha(CANDIDATE/'package-lock.json') if (CANDIDATE/'package-lock.json').exists() else None,
            'environment':'Narrow OS/runtime allowlist, portable candidate PATH; empty npm configs; prior research cache reused, not deleted.',
            'scope':'Research-only resolution and first frozen install; scripts disabled. No app/machine/provider/production selection changes.'})
        if proc.returncode: raise RuntimeError(f'{action} rejected candidate')
        if action=='frozen-install' and before!=sha(CANDIDATE/'package-lock.json'): raise RuntimeError('Frozen install changed lock')
    print('Candidate resolved and installed; not selected for production.')

if __name__=='__main__': main()
