from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
sources=[
 'AGENTS.md','.specify/memory/constitution.md','DECISIONS.md',
 'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md',
 'docs/phase-1-ui-reference-design/reference-template-inventory.csv',
 'docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv',
 'docs/phase-1-ui-reference-design/component-primitives.csv',
 'docs/phase-1-ui-reference-design/accessibility/UG-3_CONTROL_COPY_PROPOSAL.md',
 'docs/phase-1-foundation/06-canonical-route-inventory.json',
 'output/research/b01-navigation-composition-2026-10-06/state-ledger.json',
 'output/research/b01-directory-call19-2026-10-08/executed-call.js',
 'output/research/b01-directory-call19-2026-10-08/decoded-design-result.json',
 'output/research/b01-directory-call19-2026-10-08/receipt.json',
 'output/research/b01-directory-call19-2026-10-08/narrow-results.png',
 'output/research/b01-directory-call19-2026-10-08/wide-open.png'
]
items=[]
for name in sources:
    raw=(root/name).read_bytes()
    snapshot=out/'review-inputs'/name
    snapshot.parent.mkdir(parents=True,exist_ok=True)
    assert not snapshot.exists()
    snapshot.write_bytes(raw)
    items.append({'source':name,'snapshot':snapshot.relative_to(out).as_posix(),
      'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
manifest={'product':'Hengshi Design v1','status':'DOING',
 'scope':'Independent bounded directory source/returned structure/two representative preview review; remaining50 pixels and runtime inaccessible; no full B01 acceptance',
 'inputs':items}
path=out/'review-inputs.json'
path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(items),'manifest_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
