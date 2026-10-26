"""Evaluate normal npm installation at unchanged npm12 policy; retain lock-only failure."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess
import hashlib
import shutil
import os
import json

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
PRIOR=ROOT/'output/research/frontend-build-evaluation-2026-10-06'
CANDIDATE=OUT/'candidate'

def sha(file):return hashlib.sha256(file.read_bytes()).hexdigest()
def save(name,value):
    file=OUT/name
    if file.exists():raise RuntimeError(f'Refusing overwrite {file}')
    file.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')

def run(name,action,path,env):
    command=[str(PRIOR/'runtime/node.exe'),str(PRIOR/'runtime/package/bin/npm-cli.js'),action,
        '--ignore-scripts','--strict-peer-deps','--engine-strict','--audit=false','--fund=false','--workspaces=false','--include=dev','--include=optional',
        f'--prefix={path}','--registry=https://registry.npmjs.org',f'--userconfig={OUT/"empty-user.npmrc"}',f'--globalconfig={OUT/"empty-global.npmrc"}',
        f'--cache={PRIOR/"metadata-cache"}','--loglevel=error']
    before=sha(path/'package-lock.json') if (path/'package-lock.json').exists() else None
    started=datetime.now(timezone.utc).isoformat()
    proc=subprocess.run(command,cwd=path,env=env,capture_output=True,timeout=240)
    for stream in ('stdout','stderr'):(OUT/f'{name}.{stream}.txt').write_bytes(getattr(proc,stream))
    save(f'{name}-receipt.json',{'started_at_utc':started,'ended_at_utc':datetime.now(timezone.utc).isoformat(),'command':command,
        'cwd':str(path),'exit_code':proc.returncode,'node':'26.10.0','npm':'12.2.0','lock_before':before,
        'lock_after':sha(path/'package-lock.json') if (path/'package-lock.json').exists() else None,
        'policy':'Default npm12 remote policy unchanged; no allow-remote, force or peer override. Strict peers/engines and lifecycle scripts disabled.',
        'scope':'Research-only, no app or machine settings changes.'})
    if proc.returncode:raise RuntimeError(f'{name} failed')
    if action=='ci' and before!=sha(path/'package-lock.json'):raise RuntimeError('Frozen lock changed')

def main():
    failed=json.loads((OUT/'resolution-receipt.json').read_text(encoding='utf-8'))
    if failed['exit_code']==0 or (CANDIDATE/'node_modules').exists() or (CANDIDATE/'package-lock.json').exists():raise RuntimeError('Expected uninstalled failed lock-only candidate')
    env={k:os.environ[k] for k in ('SystemRoot','WINDIR','COMSPEC','TEMP','TMP') if k in os.environ}
    env['PATH']=str(PRIOR/'runtime')+os.pathsep+str(Path(env['SystemRoot'])/'System32')
    run('normal-install','install',CANDIDATE,env)
    reproduction=OUT/'frozen-candidate'
    if reproduction.exists():raise RuntimeError('Frozen reproduction already exists')
    reproduction.mkdir()
    for name in ('package.json','package-lock.json','index.html','vite.config.mjs','tsconfig.json','tsconfig.invalid.json','tsconfig.loader-control.json'):
        shutil.copyfile(CANDIDATE/name,reproduction/name)
    shutil.copytree(CANDIDATE/'src',reproduction/'src')
    run('frozen-reproduction','ci',reproduction,env)
    save('installation-correspondence.json',{'normal_lock':sha(CANDIDATE/'package-lock.json'),'fresh_frozen_lock':sha(reproduction/'package-lock.json'),
        'both_locks_equal':sha(CANDIDATE/'package-lock.json')==sha(reproduction/'package-lock.json'),
        'lock_only_failure_preserved':True,'limits':'Two actual installation paths, not file-wide integrity or security clearance.'})
    print('Normal installation and separate fresh frozen reproduction completed under unchanged npm12 defaults.')

if __name__=='__main__':main()
