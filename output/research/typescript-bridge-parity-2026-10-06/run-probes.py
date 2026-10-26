import os, pathlib, subprocess, json, hashlib, re, datetime
root = pathlib.Path(__file__).resolve().parent
repo = root.parents[2]
candidate = repo / 'output/research/react-lint-approved-evaluation-2026-10-06/candidate'
node = 'C:/nvm4w/nodejs/node.exe'
allowed = {'SYSTEMROOT','WINDIR','COMSPEC','PATH','PATHEXT','TEMP','TMP','USERPROFILE','APPDATA','LOCALAPPDATA','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMDATA'}
env = {key:value for key,value in os.environ.items() if key.upper() in allowed}
records = []
def run(name, args, cwd=candidate):
    result = subprocess.run(args, cwd=cwd, env=env, capture_output=True, timeout=30)
    (root / f'{name}.stdout.txt').write_bytes(result.stdout)
    (root / f'{name}.stderr.txt').write_bytes(result.stderr)
    entry = {'name':name,'command':args,'cwd':str(cwd),'exit_code':result.returncode,'stdout':f'{name}.stdout.txt','stderr':f'{name}.stderr.txt'}
    records.append(entry)
    return result
lock = candidate / 'package-lock.json'
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
before = digest(lock)
executables = {'api6':[node,str(candidate/'node_modules/typescript/bin/tsc6')], 'native7':[node,str(candidate/'node_modules/@typescript/native/bin/tsc')]}
for name,command in executables.items(): run(f'version-{name}',command+['--version'])
for name in ['tsc','tsc6']:
    run(f'version-shim-{name}', ['cmd.exe','/d','/c',f'{name}.cmd','--version'], candidate/'node_modules/.bin')
api = run('api-probe',[node,str(root/'api-probe.cjs'),str(candidate)])
assert api.returncode == 0, api.stderr.decode(errors='replace')
api_result = json.loads(api.stdout)
oracles = json.loads((root/'fixture-oracles.json').read_text(encoding='utf-8'))
observations = []
for fixture in oracles['fixtures']:
    name = fixture['name']; result = {'name':name,'expected':fixture,'cli':{}}
    for compiler,command in executables.items():
        p=run(f'{name}-{compiler}',command+['--project',str(root/name/'tsconfig.json'),'--pretty','false'])
        text=p.stdout.decode(errors='replace')
        result['cli'][compiler]={'exit_code':p.returncode,'codes':[int(v) for v in re.findall(r'error TS(\d+):',text)]}
    api_fixture = next(f for f in api_result['results'] if f['name']==name)
    result['api_compiler_codes']=[d['code'] for d in api_fixture['compiler']]
    result['api_language_service_codes']=[d['code'] for d in api_fixture['languageService']]
    result['oracle_match']=all(x['codes']==fixture['expected_semantic_codes'] and x['exit_code']==fixture['expected_cli_exit'] for x in result['cli'].values()) and result['api_compiler_codes']==fixture['expected_semantic_codes'] and result['api_language_service_codes']==fixture['expected_semantic_codes']
    observations.append(result)
receipt={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'environment':'allowlisted OS/runtime variables only; no provider/npm auth variables','commands':records,'lock_before':before,'lock_after':digest(lock),'api_version':api_result['version'],'observations':observations,'limits':'finite plain TypeScript subset; no React types, native LSP/editor UI, Vite/build or complete graph parity'}
(root/'observations.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'api_version':api_result['version'],'fixture_matches':[x['oracle_match'] for x in observations],'lock_unchanged':before==digest(lock),'version_outputs':{p.stem:p.read_text(encoding='utf-8').strip() for p in root.glob('version*.stdout.txt')}}))
