"""Freeze definition-only record-purpose binding inputs; no runtime qualification."""
from pathlib import Path
import hashlib, json
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
paths=[
 'AGENTS.md','.specify/memory/constitution.md','PROJECT.md','DECISIONS.md',
 'PROJECT_STATE.yaml','TASKS.md','docs/software-definition/README.md',
 'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
 'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
 'docs/phase-1-architecture/contracts/data-entities.csv',
 'docs/phase-1-architecture/contracts/data-classification.csv',
 'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md',
 'docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md',
 'docs/phase-1-architecture/contracts/CHAT_EVENT_PROTOCOL.md',
 'docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md',
 'docs/phase-1-architecture/contracts/AVAILABILITY_WRITE_HTTP.md',
 'docs/phase-1-architecture/contracts/AVAILABILITY_CONSISTENCY.md',
 'docs/phase-1-architecture/contracts/reviews/eu-privacy-retention-v1-2026-10-07.md',
 'specs/001-platform-security-hardening/spec.md',
 'output/research/record-purpose-binding-2026-10-08/DATA_CONTRACT.before.md',
 'output/research/record-purpose-binding-2026-10-08/SECURITY_PRIVACY_CONTRACT.before.md',
]
target=out/'review-inputs.json'
assert not target.exists()
sources={
 'checked_on':'2026-10-08',
 'primary_sources':[
  {'url':'https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en',
   'observation':'Purpose limitation, necessary/proportionate data, retention per purpose and deletion when no longer necessary; does not prescribe Hengshi periods.'},
  {'url':'https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en',
   'observation':'Purpose, minimisation, storage limitation and transparency including periods/bases/recipients; does not adopt Hengshi field bindings.'}
 ],
 'failed_fetches':['EUR-Lex official text returned browser verification page; EDPB FAQ429; obsolete Commission nested route404'],
 'scope':'Dated browser observations, not copied full sources or legal clearance'
}
sp=out/'primary-source-observations.json'
expected=(json.dumps(sources,indent=2)+'\n').encode('utf-8')
if sp.exists(): assert json.loads(sp.read_bytes())==sources
else: sp.write_bytes(expected)
paths.append(sp.relative_to(root).as_posix())
items=[]
for rel in paths:
 raw=(root/rel).read_bytes()
 p=out/'review-inputs-exact'/rel
 p.parent.mkdir(parents=True,exist_ok=True)
 assert not p.exists()
 p.write_bytes(raw)
 items.append({'source':rel,'snapshot':p.relative_to(out).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
for name in ['DATA_CONTRACT','SECURITY_PRIVACY_CONTRACT']:
 before=(out/(name+'.before.md')).read_bytes()
 after=(root/'docs/phase-1-architecture/contracts'/(name+'.md')).read_bytes()
 assert after.startswith(before),name
manifest={'product':'Hengshi Design v1','status':'DOING','scope':'Proposed logical field-purpose bindings only; periods/bases remain unadopted, no physical design or implementation','inputs':items}
target.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(items),'manifest_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'predecessors_preserved':True}))
