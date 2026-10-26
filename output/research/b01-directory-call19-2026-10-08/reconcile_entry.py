from pathlib import Path
import json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
task=root/'TASKS.md'
shutil.copyfile(task,out/'TASKS.before.md')
raw=task.read_bytes().decode('utf-8')
old='Directory call17 failed authentication. Founder-approved retry18 returned INVALID_ARGUMENT: 43790-byte return exceeds20480 and canvas edits were not committed; no IDs/previews. Permission consumed; [report-only compact recovery](output/research/b01-directory-return-recovery-2026-10-08/preparation.json) retains52 views/two components and checks lossless node IDs; next call needs fresh approval. October attempts18/conservative metered15; actual balance unknown.'
new='Corrected approved call19 created52 directory references/two components, with2674 unique returned IDs, zero reported bounds findings and two scaled previews. [Independent15-input review](docs/phase-1-ui-reference-production/reviews/B01-directory-references-v1-2026-10-08.md) passes its bounded construction/structure/visible-preview scope; all52 full-resolution pixels remain held. [Prepared single comparison export](output/research/b01-directory-full-resolution-2026-10-08/preparation.json) uses five temporary sheets with checked cleanup and needs fresh per-call approval. October attempts19/conservative metered16; actual balance unknown; permission consumed, no further call.'
assert raw.count(old)==1
task.write_bytes(raw.replace(old,new).encode('utf-8'))
assert len(task.read_text(encoding='utf-8').splitlines())<=50
entry=root/'docs/phase-1-ui-reference-production/README.md'
shutil.copyfile(entry,out/'README.before.md')
raw=entry.read_bytes().decode('utf-8').replace('## Current authority — reconciled 2026-10-07','## Current authority — reconciled 2026-10-08')
needle='The [shared recovery composition preparation]'
assert raw.count(needle)==1
raw=raw.replace(needle,'''The later [directory call19 receipt](../../output/research/b01-directory-call19-2026-10-08/receipt.json)
supersedes the directory-unexecuted/count16 checkpoint above. Corrected call19
created52 views/two components;2,674 unique returned IDs and zero reported bounds
findings were decoded from the complete15,080-byte report. [Independent15-input
review](reviews/B01-directory-references-v1-2026-10-08.md) passes construction,
decoded structure and visible composition in two scaled PNGs only. All52
full-resolution pixels and other B01 coverage/runtime/native restore/_EXIT and
acceptance remain held. October attempts19/conservative metered16; actual balance
unknown. A [single comparison export](../../output/research/b01-directory-full-resolution-2026-10-08/preparation.json)
is prepared but unexecuted: five temporary clone sheets, scale1 images and checked
cleanup, without original correction. Fresh immediate approval remains required.

'''+needle)
entry.write_bytes(raw.encode('utf-8'))
print(json.dumps({'task_lines':len(task.read_text(encoding='utf-8').splitlines()),'entry_current_checkpoint':'call19 success with bounded review and unresolved full resolution'}))
