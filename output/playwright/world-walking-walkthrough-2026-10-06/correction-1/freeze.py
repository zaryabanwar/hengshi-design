from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
INITIAL=OUT.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
raw=(INITIAL/'command-06.stdout.txt').read_text(encoding='utf-8')
obs=json.JSONDecoder().raw_decode(raw.split('### Result',1)[1].lstrip())[0]
assert obs['pass']
(OUT/'link-observations.json').write_text(json.dumps(obs,indent=2)+'\n',encoding='utf-8')
guards=json.loads((INITIAL/'protected-before.json').read_text(encoding='utf-8'))
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards)
old=json.loads((INITIAL/'review-inputs.json').read_text(encoding='utf-8'))
entries=[]
for x in old['inputs']:
    if x['path']=='docs/software-definition/definition-walkthrough.html':
        entries.append({'path':x['path'],'sha256':digest(ROOT/x['path'])})
    else:
        assert digest(ROOT/x['path'])==x['sha256']
        entries.append(x)
for p in OUT.iterdir():
    if p.is_file() and p.name!='review-inputs.json' and not p.name.endswith('.log'): entries.append({'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)})
for name in [f'command-{n:02}.{suffix}' for n in range(4,8) for suffix in ('json','stdout.txt','stderr.txt')]:
    p=INITIAL/name
    assert p.exists()
    entries.append({'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)})
r=subprocess.run(['git','-c','core.autocrlf=false','-c','core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol','diff','--check','--','docs/software-definition/definition-walkthrough.html'],cwd=ROOT,capture_output=True)
assert r.returncode==0,r.stdout+r.stderr
packet={'scope':'Correction1: one source-link fragment removed, no other rendered content or mechanics changed. Original snapshots/pixels retained as initial contextual evidence; focused link check is new. Initial review is copied, mutable disposition excluded.','inputs':entries,'protected_guard_count':78,'guard_match':True,'whitespace_pass':True}
(OUT/'review-inputs.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(entries),'sha256':digest(OUT/'review-inputs.json'),'guards':78}))
