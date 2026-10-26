"""Run existing Playwright CLI for one synthetic preview with saved exact outputs."""
from pathlib import Path
import subprocess
import os
import sys
import json
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'output/playwright/frontend-three-remedy-2026-10-06'
RUNTIME=ROOT/'output/research/frontend-build-evaluation-2026-10-06/runtime/node.exe'
CLI=Path('C:/Users/Zaryab/AppData/Local/npm-cache/_npx/31e32ef8478fbf80/node_modules/@playwright/cli/playwright-cli.js')

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    OUT.mkdir(parents=True,exist_ok=True)
    env={k:os.environ[k] for k in ('SystemRoot','WINDIR','COMSPEC','ProgramFiles','ProgramFiles(x86)','PROGRAMDATA') if k in os.environ}
    for folder in ('profile','tmp','appdata','localappdata'):(OUT/folder).mkdir(exist_ok=True)
    env.update({'USERPROFILE':str(OUT/'profile'),'TEMP':str(OUT/'tmp'),'TMP':str(OUT/'tmp'),'APPDATA':str(OUT/'appdata'),'LOCALAPPDATA':str(OUT/'localappdata'),
        'PATH':str(RUNTIME.parent)+os.pathsep+str(Path(env['SystemRoot'])/'System32')})
    env['PLAYWRIGHT_BROWSERS_PATH']='C:/Users/Zaryab/AppData/Local/ms-playwright'
    command=[str(RUNTIME),str(CLI),'-s=hengshi-three-remedy-20261006',*sys.argv[1:]]
    result=subprocess.run(command,cwd=OUT,env=env,capture_output=True,timeout=100)
    index=len(list(OUT.glob('command-*.json')))+1
    stem=f'command-{index:02}'
    for stream in ('stdout','stderr'):(OUT/f'{stem}.{stream}.txt').write_bytes(getattr(result,stream))
    (OUT/f'{stem}.json').write_text(json.dumps({'observed_at_utc':datetime.now(timezone.utc).isoformat(),'command':command,'cwd':str(OUT),'exit_code':result.returncode,'scope':'Isolated synthetic browser preview only; existing CLI, no production tool selection or account/profile use.'},indent=2)+'\n',encoding='utf-8')
    print(result.stdout.decode('utf-8',errors='replace'))
    if result.stderr:print(result.stderr.decode('utf-8',errors='replace'),file=sys.stderr)
    sys.exit(result.returncode)

if __name__=='__main__':main()
