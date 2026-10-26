from pathlib import Path
import hashlib, json

root=Path.cwd()
base=root/'output/research/security-feature-rights-incidents-2026-10-09'
prior=base/'review/review-inputs.json'
m=json.loads(prior.read_bytes())
assert all((root/i['path']).read_bytes()==(root/i['snapshot']).read_bytes() for i in m['inputs'])
p=root/'specs/001-platform-security-hardening/spec.md'
before=p.read_bytes()
old=b'| Semantic/browser and process-boundary cases |\n\n| Handle rights and incidents |'
new=b'| Semantic/browser and process-boundary cases |\n| Handle rights and incidents |'
assert before.count(old)==1
after=before.replace(old,new)
target=base/'review/inspected'
assert not target.exists()
target.mkdir()
p.write_bytes(after)
metadata=base/'producer-inspection.json'
metadata.write_text(json.dumps({'status':'DOING','scope':'Remove only an unintended blank table separator before first independent review','before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(after).hexdigest(),'old':old.decode(),'new':new.decode()},indent=2)+'\n',encoding='utf-8')
paths=[i['path'] for i in m['inputs']]+[prior.relative_to(root).as_posix(),metadata.relative_to(root).as_posix(),Path(__file__).relative_to(root).as_posix()]
inputs=[]
for rel in paths:
    raw=(root/rel).read_bytes()
    snap=target/'inputs'/rel
    snap.parent.mkdir(parents=True,exist_ok=True)
    snap.write_bytes(raw)
    inputs.append({'path':rel,'snapshot':snap.relative_to(root).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
out=target/'review-inputs.json'
out.write_text(json.dumps({'status':'DOING','revision_cycle':0,'scope':'First independent review of inspected security feature rights/incident bindings and checklist; original producer packet preserved','inputs':inputs},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'manifest_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'only_blank_separator_removed':after.replace(new,old)==before}))
