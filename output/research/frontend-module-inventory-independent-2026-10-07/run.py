from pathlib import Path
import os,json,subprocess
out=Path(__file__).resolve().parent
root=out.parents[2]
node=root/'output/research/frontend-build-evaluation-2026-10-06/runtime/node.exe'
env={k:os.environ[k] for k in ('SYSTEMROOT','WINDIR','COMSPEC','PATHEXT','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMDATA') if k in os.environ}
env['PATH']=str(node.parent)+os.pathsep+str(Path(env['SYSTEMROOT'])/'System32')
for key,folder in [('TEMP','tmp'),('TMP','tmp'),('USERPROFILE','profile'),('APPDATA','appdata'),('LOCALAPPDATA','localappdata')]:
    p=out/'runtime'/folder
    p.mkdir(parents=True,exist_ok=True)
    env[key]=str(p)
(out/'environment.json').write_text(json.dumps(env,indent=2)+'\n',encoding='utf8')
with (out/'build.stdout.txt').open('xb') as stdout,(out/'build.stderr.txt').open('xb') as stderr:
    result=subprocess.run([str(node),str(out/'inspect.mjs')],cwd=out,env=env,stdout=stdout,stderr=stderr,timeout=120)
receipt={'exitCode':result.returncode,'command':[str(node),str(out/'inspect.mjs')],'environmentKeys':sorted(env),'scope':'One existing-vendor synthetic build only; no network request by reviewer scripts, installation, package or lock modification.'}
(out/'run-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt))
raise SystemExit(result.returncode)
