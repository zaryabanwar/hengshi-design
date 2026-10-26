"""Check the actual candidate and build only after both strict paths accept it."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib
import re
import os
import subprocess

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
PRIOR=ROOT/'output/research/frontend-build-evaluation-2026-10-06'
CANDIDATE=OUT/'candidate'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name,value):
    target=OUT/name
    if target.exists():raise RuntimeError(f'Refusing overwrite {target}')
    target.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')

def main():
    install=json.loads((OUT/'normal-install-receipt.json').read_text(encoding='utf-8'))
    frozen=json.loads((OUT/'frozen-reproduction-receipt.json').read_text(encoding='utf-8'))
    if frozen['exit_code'] or frozen['lock_before']!=frozen['lock_after'] or frozen['lock_after']!=install['lock_after']:raise RuntimeError('Separate frozen reproduction not established')
    if install['exit_code'] or sha(CANDIDATE/'package-lock.json')!=install['lock_after']:raise RuntimeError('Frozen installation not established')
    env={k:os.environ[k] for k in ('SystemRoot','WINDIR','COMSPEC') if k in os.environ}
    env['PATH']=str(PRIOR/'runtime')+os.pathsep+str(Path(env['SystemRoot'])/'System32')
    for name in ('profile','tmp'):(OUT/name).mkdir(exist_ok=False)
    env.update({'USERPROFILE':str(OUT/'profile'),'TEMP':str(OUT/'tmp'),'TMP':str(OUT/'tmp')})
    commands=[]
    for case,config in [('valid','tsconfig.json'),('invalid','tsconfig.invalid.json'),('loader-control','tsconfig.loader-control.json')]:
        for compiler,entry in [('api6','typescript/bin/tsc6'),('native7','@typescript/native/bin/tsc')]:
            command=[str(PRIOR/'runtime/node.exe'),str(CANDIDATE/'node_modules'/entry),'--project',str(CANDIDATE/config),'--pretty','false']
            proc=subprocess.run(command,cwd=CANDIDATE,env=env,capture_output=True,timeout=100)
            for stream in ('stdout','stderr'):(OUT/f'{case}-{compiler}.{stream}.txt').write_bytes(getattr(proc,stream))
            codes=[int(v) for v in re.findall(rb'error TS(\d+):',proc.stdout+proc.stderr)]
            expected=[2322] if case=='invalid' else []
            acceptance=proc.returncode!=0 if case=='invalid' else proc.returncode==0
            commands.append({'case':case,'compiler':compiler,'command':command,'exit_code':proc.returncode,'diagnostic_codes':codes,'expected_codes':expected,'matches_finite_oracle':acceptance and codes==expected})
    save('checker-observations.json',{'checked_at_utc':datetime.now(timezone.utc).isoformat(),'commands':commands,
        'gate':'Run the build only when both checkers accept valid and loader-control inputs and reject the independently invalid prop.'})
    if not all(c['matches_finite_oracle'] for c in commands):raise RuntimeError('Type gate rejected the candidate; no build invoked')
    dist=(CANDIDATE/'fixture-dist').resolve()
    if not dist.is_relative_to(CANDIDATE.resolve()) or dist.exists():raise RuntimeError('Build output is not a fresh isolated path')
    coverage=OUT/'build-v8-coverage';coverage.mkdir()
    env['NODE_V8_COVERAGE']=str(coverage)
    command=[str(PRIOR/'runtime/node.exe'),str(CANDIDATE/'node_modules/vite/bin/vite.js'),'build','--outDir','fixture-dist']
    start=datetime.now(timezone.utc).isoformat()
    proc=subprocess.run(command,cwd=CANDIDATE,env=env,capture_output=True,timeout=180)
    for stream in ('stdout','stderr'):(OUT/f'build.{stream}.txt').write_bytes(getattr(proc,stream))
    modules=[]
    for file in coverage.glob('*.json'):
        obj=json.loads(file.read_text(encoding='utf-8'))
        for item in obj.get('result',[]):
            url=item.get('url','')
            if url.startswith('file:'):modules.append({'url':url,'executed_ranges':sum(r['count']>0 for fn in item.get('functions',[]) for r in fn.get('ranges',[]))})
    save('build-receipt.json',{'started_at_utc':start,'ended_at_utc':datetime.now(timezone.utc).isoformat(),'command':command,'cwd':str(CANDIDATE),
        'exit_code':proc.returncode,'strict_type_gate_passed':True,'build_output':str(dist),
        'node_v8_coverage_files':len(list(coverage.glob('*.json'))),'coverage_file_modules':modules,
        'gensync_observed_modules':[item for item in modules if '/gensync/' in item['url']],
        'limits':'Finite synthetic default build with V8 JS observations, not lint conformance, universal deployed exclusion, private rendering/worker, all exports, real application build, production selection or release approval.'})
    if proc.returncode:raise RuntimeError('Actual build failed')
    files=[{'path':str(f.relative_to(CANDIDATE).as_posix()),'bytes':f.stat().st_size,'sha256':sha(f)} for f in dist.rglob('*') if f.is_file()]
    save('build-output-identities.json',files)
    protected=json.loads((OUT/'protected-before.json').read_text(encoding='utf-8'))
    changed=[item['path'] for item in protected if sha(ROOT/item['path'])!=item['sha256']]
    save('protected-after-build.json',{'inputs':len(protected),'changed':changed})
    if changed:raise RuntimeError('Protected input changed')
    print(json.dumps({'type_controls':len(commands),'build_exit':proc.returncode,'output_files':len(files),'protected_inputs_unchanged':len(protected)}))

if __name__=='__main__':main()
