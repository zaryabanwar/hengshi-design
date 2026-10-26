"""Serve only isolated built output on loopback; stdin 'quit' stops this child."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess
import json
import os

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
PRIOR=ROOT/'output/research/frontend-build-evaluation-2026-10-06'
CANDIDATE=OUT/'candidate'

def main():
    result=json.loads((OUT/'build-receipt.json').read_text(encoding='utf-8'))
    if result['exit_code']!=0:raise RuntimeError('No successful build')
    env={k:os.environ[k] for k in ('SystemRoot','WINDIR','COMSPEC') if k in os.environ}
    env.update({'PATH':str(PRIOR/'runtime')+os.pathsep+str(Path(env['SystemRoot'])/'System32'),
                'USERPROFILE':str(OUT/'profile'),'TEMP':str(OUT/'tmp'),'TMP':str(OUT/'tmp')})
    command=[str(PRIOR/'runtime/node.exe'),str(CANDIDATE/'node_modules/vite/bin/vite.js'),'preview','--outDir','fixture-dist','--host','127.0.0.1','--port','5277','--strictPort']
    started=datetime.now(timezone.utc).isoformat()
    with (OUT/'preview.stdout.txt').open('xb') as stdout,(OUT/'preview.stderr.txt').open('xb') as stderr:
        child=subprocess.Popen(command,cwd=CANDIDATE,env=env,stdout=stdout,stderr=stderr)
        record={'command':command,'cwd':str(CANDIDATE),'pid':child.pid,'started_at_utc':started,'url':'http://127.0.0.1:5277/','scope':'Fresh isolated fixture preview only, not a project service'}
        (OUT/'preview-start.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
        print(f'Preview PID {child.pid}; send quit to stop.',flush=True)
        try:
            while child.poll() is None:
                if input().strip()=='quit':break
        except (EOFError,KeyboardInterrupt):pass
        finally:
            if child.poll() is None:child.terminate()
            child.wait(timeout=15)
            (OUT/'preview-stop.json').write_text(json.dumps({'pid':child.pid,'ended_at_utc':datetime.now(timezone.utc).isoformat(),'exit_code':child.returncode,'requested_child_stop':True},indent=2)+'\n',encoding='utf-8')
        print('Isolated preview stopped.',flush=True)

if __name__=='__main__':main()
