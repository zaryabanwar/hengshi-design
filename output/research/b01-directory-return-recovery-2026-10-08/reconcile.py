from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
source=root/'output/research/b01-directory-preflight-refresh-2026-10-07/figma-call.js'
target=out/'figma-call.js'
marker='await frames.find((node,index)=>input.frames[index].state_id'
original=source.read_text(encoding='utf-8')
current=target.read_text(encoding='utf-8')
prefix=original.split(marker,1)[0]
assert current.startswith(prefix)
assert current.split('// Report-only lossless encoding.',1)[1].split('const groupedBounds',1)[0] == (out/'codec.js').read_text(encoding='utf-8').split('// Report-only lossless encoding.',1)[1]
meta=json.loads((out/'preparation.json').read_text(encoding='utf-8'))
meta['script_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
meta['all_ids']='Lossless prefix groups: numeric singleton suffixes or inclusive [start,end] ranges; exact in-call round-trip equality and literal fallback'
meta['local_checks']=json.loads((out/'codec-check.json').read_text(encoding='utf-8'))
(out/'preparation.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')

# Slice: current retry brief and active task reference only. Earlier failed-call
# evidence remains historical; no application or design construction is executed.
brief=root/'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md'
shutil.copyfile(brief,out/'B01_EXECUTION_BRIEF.before.md')
raw=brief.read_bytes().decode('utf-8')
needle='## Calls, costs and authority'
assert raw.count(needle)==1
addition='''## Current retry boundary — 2026-10-08

The founder reconnected and approved one retry. Attempt18 reached Figma, but its
43,790-byte return exceeded the 20,480-byte limit. The provider explicitly reports
that canvas edits were not committed and permits retry without a canvas read.
The [exact receipt](../../output/research/b01-directory-call18-2026-10-08/receipt.json)
contains no created IDs or preview images. That permission is consumed.

A [prepared report-only recovery](../../output/research/b01-directory-return-recovery-2026-10-08/preparation.json)
retains the same 52 views, two components, preflight and two native previews.
Construction bytes are unchanged. Every created node ID is losslessly represented
by a prefix and numeric singleton/inclusive range; the script checks exact
round-trip equality. Frame names resolve through the unchanged input ordinal;
all bounds findings remain represented. A 19,000-byte UTF-8 return guard precedes
preview/return. Local checks conserve 1,006 prior construction IDs, 183 recovery
IDs and 4,006 unique synthetic IDs; these are codec/syntax checks, not Figma or
visual validation. Another scoped call requires fresh immediate approval.

'''
raw=raw.replace(needle,addition+needle)
raw=raw.replace('October attempts 17, conservatively metered 14.','October attempts 18, conservatively metered 15.')
brief.write_bytes(raw.encode('utf-8'))
task=root/'TASKS.md'
shutil.copyfile(task,out/'TASKS.before.md')
raw=task.read_bytes().decode('utf-8')
old='Approved directory call17 returned UNAUTHORIZED requiring reauthentication; no design receipt or previews. Its permission is consumed; attempt18 needs reconnection and fresh per-call approval. October attempts17/conservative metered14; actual balance unknown.'
new='Directory call17 failed authentication. Founder-approved retry18 returned INVALID_ARGUMENT: 43790-byte return exceeds20480 and canvas edits were not committed; no IDs/previews. Permission consumed; [report-only compact recovery](output/research/b01-directory-return-recovery-2026-10-08/preparation.json) retains52 views/two components and checks lossless node IDs; next call needs fresh approval. October attempts18/conservative metered15; actual balance unknown.'
assert raw.count(old)==1
task.write_bytes(raw.replace(old,new).encode('utf-8'))
assert len(task.read_text(encoding='utf-8').splitlines())<=50
print(json.dumps({'script_sha256':meta['script_sha256'],'construction_prefix_unchanged':True,'active_task_lines':len(task.read_text(encoding='utf-8').splitlines()),'external_calls':0}))
