import os, pathlib, subprocess, json, hashlib, re, datetime
root = pathlib.Path(__file__).resolve().parent
repo = root.parents[2]
candidate = repo / 'output/research/react-lint-approved-evaluation-2026-10-06/candidate'
node = 'C:/nvm4w/nodejs/node.exe'
allowed = {'SYSTEMROOT','WINDIR','COMSPEC','PATH','PATHEXT','TEMP','TMP','USERPROFILE','APPDATA','LOCALAPPDATA','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMDATA'}
env = {key:value for key,value in os.environ.items() if key.upper() in allowed}
records = []
def run(name,args,cwd=root):
 result=subprocess.run(args,cwd=cwd,env=env,capture_output=True,timeout=45)
 (root/f'{name}.stdout.txt').write_bytes(result.stdout)
 (root/f'{name}.stderr.txt').write_bytes(result.stderr)
 records.append({'name':name,'args':args,'exit_code':result.returncode,'stdout':f'{name}.stdout.txt','stderr':f'{name}.stderr.txt'})
 return result
api=run('api-probe',[node,str(root/'api-probe.cjs'),str(candidate)])
assert api.returncode==0,api.stderr.decode(errors='replace')
api_result=json.loads(api.stdout)
commands={'api6':[node,str(candidate/'node_modules/typescript/bin/tsc6')],'native7':[node,str(candidate/'node_modules/@typescript/native/bin/tsc')]}
observations=[]
for fixture in json.loads((root/'fixture-oracles.json').read_text(encoding='utf-8'))['fixtures']:
 row={'name':fixture['name'],'expected':fixture,'cli':{}}
 for compiler,command in commands.items():
  p=run(f'{fixture["name"]}-{compiler}',command+['--project',str(root/fixture['name']/'tsconfig.json'),'--pretty','false'])
  row['cli'][compiler]={'exit_code':p.returncode,'codes':[int(v) for v in re.findall(r'error TS(\d+):',p.stdout.decode(errors='replace'))]}
 api_fixture=next(f for f in api_result['results'] if f['name']==fixture['name'])
 row['api_compiler_codes']=[d['code'] for d in api_fixture['compiler']]
 row['api_language_service_codes']=[d['code'] for d in api_fixture['languageService']]
 row['diagnostic_oracle_match']=all(x['codes']==fixture['expected_codes'] and ((x['exit_code']==0)==fixture['expected_acceptance']) for x in row['cli'].values()) and row['api_compiler_codes']==fixture['expected_codes'] and row['api_language_service_codes']==fixture['expected_codes']
 row['numeric_cli_exits_equal']=len({x['exit_code'] for x in row['cli'].values()})==1
 observations.append(row)
checks=[]
for row in json.loads((root/'unchanged-inputs.json').read_text(encoding='utf-8')):
 matched=hashlib.sha256((repo/row['path']).read_bytes()).hexdigest()==row['sha256']; checks.append({'path':row['path'],'unchanged':matched})
 assert matched,row['path']
result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'environment':'allowlisted OS/runtime variables, no provider/npm auth; no install/application change','api_version':api_result['version'],'type_packages':'type-packages.json','observations':observations,'commands':records,'guard_results':checks,'limits':'finite declaration/type-diagnostic and in-process API6 service subset; no React runtime/bundler/browser/native-LSP/editor/emit/full graph proof'}
(root/'observations.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'api_version':api_result['version'],'matches':[x['diagnostic_oracle_match'] for x in observations],'numeric_exit_equal':[x['numeric_cli_exits_equal'] for x in observations],'guards_unchanged':all(x['unchanged'] for x in checks)}))
