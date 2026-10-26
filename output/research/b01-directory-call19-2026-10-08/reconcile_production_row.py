"""Reconcile a stale current-standing row to existing call19 evidence."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
p=root/'docs/phase-1-ui-reference-production/README.md'
raw=p.read_bytes()
text=raw.decode('utf-8')
lines=text.splitlines()
positions=[i for i,line in enumerate(lines) if line.startswith('| Review and execution |')]
assert len(positions)==1
before=out/'UI_REFERENCE_PRODUCTION_README.before-current-row.md'
assert not before.exists()
before.write_bytes(raw)
lines[positions[0]]='| Review and execution | D-061 closes MA-029/R-035; D-075 approves B01 execution/organisation, not acceptance. Native PRE and six initial draft views are verified. Call16 recovered the missing navigation pixels: [all20 navigation references have producer inspection](validation/capability-evidence.md#b01-single-image-navigation-recovery--2026-10-07), with temporary-copy cleanup and source geometry/text, positions and parent order checked unchanged. Corrected call19 created52 directory/search views and two components; [independent15-input review](reviews/B01-directory-references-v1-2026-10-08.md) passes source/decoded structure and visible composition in two scaled previews only. All52 full-resolution directory pixels remain held. [Prepared five-sheet export](../../output/research/b01-directory-full-resolution-2026-10-08/preparation.json) is unexecuted and needs fresh immediate CB-06/CB-07 approval. October attempts19/conservatively metered16, actual debit/balance unknown. Ceiling-refusal fixtures remain TODO. Complete coverage, interaction/accessibility, editable exports/restore, _EXIT and founder pilot acceptance remain; no later batch/application release follows. |'
newline='\r\n' if b'\r\n' in raw else '\n'
p.write_bytes((newline.join(lines)+newline).encode('utf-8'))
print(json.dumps({'document':p.relative_to(root).as_posix(),'rows_reconciled':1,'external_call':False}))
