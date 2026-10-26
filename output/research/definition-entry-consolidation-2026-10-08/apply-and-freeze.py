from pathlib import Path
import hashlib, json, re, shutil

root=Path.cwd()
out=root/'output/research/definition-entry-consolidation-2026-10-08'
readme=root/'docs/software-definition/README.md'
mapping=root/'docs/software-definition/04-reconciliation-map.md'
assert not (out/'README.before.md').exists()
shutil.copyfile(readme,out/'README.before.md')
shutil.copyfile(mapping,out/'reconciliation-map.before.md')
readme.write_bytes((out/'README.prepared.md').read_bytes().replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'))
data=mapping.read_bytes()
old=data
lines=data.decode('utf-8').splitlines(keepends=True)
for i,line in enumerate(lines):
    if line.startswith('| QA and recovery |'):
        lines[i]=line.rstrip('\r\n').removesuffix(' |')+' The availability and recovery measurement proposals now have separate bounded independent definition and visual reviews; see the coverage row below. Exact operating bindings, authorized drills and adoption remain held. |\r\n'
    if line.startswith('| 11. QA/recovery strategy |'):
        line=line.replace('Physical-phone access, exact measurement/SLI/recovery/retention inputs, isolated test authorization, runtime evidence and feature/integrated/founder acceptance remain held.', 'The [monthly availability method](../phase-1-architecture/contracts/QA_RECOVERY.md#monthly-availability-measurement-proposal--2026-10-08) and [recovery clock method](../phase-1-architecture/contracts/QA_RECOVERY.md#recovery-clocks-and-safe-return-to-service-proposal--2026-10-08) now have separate bounded independent definition PASS receipts. Exact observation/recovery profiles, retention/storage/provider mechanisms, named devices, authorized isolated drills, runtime evidence and feature/integrated/founder acceptance remain held.')
        lines[i]=line
data=''.join(lines).encode('utf-8')
needle=b'### Later contract refinements\r\n'
assert data.count(needle)==1
paragraph='''### Later contract refinements

The [monthly availability definition review](../phase-1-architecture/contracts/reviews/monthly-availability-measurement-v1-2026-10-08.md)
and [recovery definition review](../phase-1-architecture/contracts/reviews/recovery-measurement-v1-2026-10-08.md)
record separate corrected-input bounded PASS verdicts. Their methods retain the
accepted targets as unmeasured obligations: separate surface coverage with
unknown evidence for availability, and conservative recovery clocks with current
passing evidence across all affected required boundaries. Neither adopts an SLA,
selects hosting, changes retention or authorizes monitoring/backup/restore activity.
The [availability walkthrough review](reviews/monthly-availability-walkthrough-v1-2026-10-08.md)
and [recovery walkthrough review](reviews/recovery-measurement-walkthrough-v1-2026-10-08.md)
separately cover their supplied source and desktop/narrow pixels. Producer browser
observations remain distinct. Exact operating profiles and integrated acceptance
remain held; implementation and drill evidence belong to later authorized work.
'''.replace('\n','\r\n').encode('utf-8')
data=data.replace(needle,paragraph)
mapping.write_bytes(data)
oldlines=old.decode('utf-8').splitlines()
newlines=data.decode('utf-8').splitlines()
assert len([s for s in oldlines if s.startswith('|') and s not in newlines])==2

paths=[
 'docs/software-definition/README.md','docs/software-definition/04-reconciliation-map.md',
 'output/research/definition-entry-consolidation-2026-10-08/README.before.md',
 'output/research/definition-entry-consolidation-2026-10-08/reconciliation-map.before.md',
 'AGENTS.md','.specify/memory/constitution.md','PROJECT.md','DECISIONS.md','PROJECT_STATE.yaml','TASKS.md',
 'docs/active/Documentation_Index.md','specs/README.md',
 'docs/phase-1-architecture/contracts/QA_RECOVERY.md',
 'docs/phase-1-architecture/contracts/reviews/monthly-availability-measurement-v1-2026-10-08.md',
 'docs/phase-1-architecture/contracts/reviews/recovery-measurement-v1-2026-10-08.md',
 'docs/software-definition/reviews/monthly-availability-walkthrough-v1-2026-10-08.md',
 'docs/software-definition/reviews/recovery-measurement-walkthrough-v1-2026-10-08.md'
]
snapshots=out/'review-snapshots'
snapshots.mkdir(exist_ok=False)
inputs=[]
for i,p in enumerate(paths):
    src=root/p; dest=snapshots/f'{i:02d}-{src.name}'
    shutil.copyfile(src,dest); raw=src.read_bytes()
    inputs.append({'source':p,'snapshot':dest.relative_to(root).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
manifest=out/'review-inputs.json'
manifest.write_text(json.dumps({'product':'Hengshi Design v1','status':'DOING','scope':'Navigation consolidation, unchanged authority and two QA coverage rows plus review-reference paragraph; no subject definition or runtime change','inputs':inputs},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'readme_before_bytes':len((out/'README.before.md').read_bytes()),'readme_after_bytes':len(readme.read_bytes()),'inputs':len(inputs)}))
