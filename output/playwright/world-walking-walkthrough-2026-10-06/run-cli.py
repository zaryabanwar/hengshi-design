"""Use already installed CLI/browser in an isolated evidence profile."""
from pathlib import Path
import os, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
CLI=Path('C:/Users/Zaryab/AppData/Local/npm-cache/_npx/31e32ef8478fbf80/node_modules/@playwright/cli/playwright-cli.js')
NODE=ROOT/'output/research/frontend-build-evaluation-2026-10-06/runtime/node.exe'
env={k:os.environ[k] for k in ('SystemRoot','WINDIR','COMSPEC','ProgramFiles','ProgramFiles(x86)','PROGRAMDATA') if k in os.environ}
for folder in ('profile','tmp','appdata','localappdata'):(OUT/folder).mkdir(exist_ok=True)
env.update({'USERPROFILE':str(OUT/'profile'),'TEMP':str(OUT/'tmp'),'TMP':str(OUT/'tmp'),'APPDATA':str(OUT/'appdata'),'LOCALAPPDATA':str(OUT/'localappdata'),'PATH':str(NODE.parent)+os.pathsep+str(Path(env['SystemRoot'])/'System32'),'PLAYWRIGHT_BROWSERS_PATH':'C:/Users/Zaryab/AppData/Local/ms-playwright'})
command=[str(NODE),str(CLI),'-s=hengshi-world-explanation-20261006',*sys.argv[1:]]
result=subprocess.run(command,cwd=OUT,env=env,capture_output=True,timeout=100)
stem=f'command-{len(list(OUT.glob("command-*.json")))+1:02}'
for stream in ('stdout','stderr'):(OUT/f'{stem}.{stream}.txt').write_bytes(getattr(result,stream))
(OUT/f'{stem}.json').write_text(json.dumps({'command':command,'exit_code':result.returncode,'scope':'Existing cached browser/CLI, isolated local static board; no installation or production tool selection.'},indent=2)+'\n',encoding='utf-8')
print(result.stdout.decode('utf-8',errors='replace'))
if result.stderr: print(result.stderr.decode('utf-8',errors='replace'),file=sys.stderr)
sys.exit(result.returncode)
