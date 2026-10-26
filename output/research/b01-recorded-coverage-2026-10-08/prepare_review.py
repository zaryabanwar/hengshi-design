from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
obs=json.loads((out/'recorded-coverage.json').read_bytes())
paths=[x['path'] for x in obs['sources']]+[
 'AGENTS.md','.specify/memory/constitution.md','DECISIONS.md','PROJECT_STATE.yaml','TASKS.md',
 'scripts/validation/ui-stream-mapping.ps1',
 'docs/phase-1-ui-reference-design/component-primitives.csv',
 'output/research/b01-recorded-coverage-2026-10-08/inventory.py',
 'output/research/b01-recorded-coverage-2026-10-08/reconcile_brief.py',
 'output/research/b01-recorded-coverage-2026-10-08/recorded-coverage.json',
 'output/research/b01-recorded-coverage-2026-10-08/B01_EXECUTION_BRIEF.before.md'
]
target=out/'review-inputs.json'
assert not target.exists()
inputs=[]
for rel in sorted(set(paths)):
 raw=(root/rel).read_bytes()
 snap=out/'review-inputs'/rel
 snap.parent.mkdir(parents=True,exist_ok=True)
 assert not snap.exists()
 snap.write_bytes(raw)
 inputs.append({'source':rel,'snapshot':snap.relative_to(out).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
manifest={'product':'Hengshi Design v1','status':'DOING','scope':'Recorded frame name/axis correlation and existing profile obligations only; no live canvas, pixels, behavior, complete B01 coverage or adoption','inputs':inputs}
target.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'manifest_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))
