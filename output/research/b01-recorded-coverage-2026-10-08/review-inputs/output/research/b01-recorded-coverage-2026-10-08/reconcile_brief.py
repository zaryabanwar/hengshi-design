"""Reference-only B01 coverage correction; preserve earlier brief bytes."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
p=root/'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md'
raw=p.read_bytes()
before=out/'B01_EXECUTION_BRIEF.before.md'
assert not before.exists()
before.write_bytes(raw)
x=json.loads((out/'recorded-coverage.json').read_bytes())
assert x['summary']=={'recorded_frames':78,'explicit_axis_frames':72,'required_stream_state_subset':56,'subset_with_recorded_names':36,'subset_without_recorded_names':20}
text=raw.decode('utf-8')
old='Status: DOING. Six initial views inspected after successful reflow; full B01 exit remains held.'
assert text.count(old)==1
text=text.replace(old,'Status: DOING. Six initial and twenty navigation views inspected;52 directory views created with full-resolution inspection held. Full B01 exit remains held.',1)
old='Returned bounds pass and two representative previews are inspected; remaining views/full B01 review are held.'
assert text.count(old)==1
text=text.replace(old,'That dated return supplied two representative previews; approved call16 subsequently recovered the remaining navigation pixels, so all20 are now inspected. Full B01 review remains held.',1)
addition='''
## Recorded coverage reconciliation — 2026-10-08

The [receipt/name inventory](../../output/research/b01-recorded-coverage-2026-10-08/recorded-coverage.json)
correlates78 recorded frame IDs: six generic initial drafts, twenty navigation
references and52 directory/search references. This is not a fresh canvas read;
names/axes alone prove no pixel quality, prototype operation or accessibility.

The preserved stream/state focus subset has56 requirements.36 have explicitly
matching recorded names;20 do not: four ceiling-refusal stream cases on each of
navigation and directory/search (eight host bindings), plus ERROR, STREAM-CHANGED
and PREFERENCE-WRITE-FAILED across four streams on shared recovery (twelve).
Four reusable refusal cases do not automatically evidence both required hosts.
Generic initial draft names receive no invented explicit stream/state credit.
The subset is not a complete B01 denominator or a Cartesian-product instruction.

Recorded named references currently identify MODE-KEYBOARD and VP-320/VP-DESKTOP.
Other state/viewport/mode evidence must be adjudicated against its full profile,
including applicable landscape,400% stress, forced colours, font/asset and
screen-reader/prototype specifications. Missing names do not establish absent
annotations; existing frames cannot inherit unverified profile evidence.
The prepared48 shared recovery specimens are unexecuted grammar supplements,
not full host/stream/profile coverage. Native exports/restore/_EXIT, independent
design/accessibility review and founder acceptance remain required. World HUD,
movement and cross-boundary content remain assigned to B07/B09.

The inventory's independent review is pending. No Figma call or design correction
ran; the separately prepared directory pixel export still requires fresh approval.
This reconciliation grants no later batch, application or integrated acceptance.
'''
nl='\r\n' if '\r\n' in text else '\n'
text+=addition.replace('\n',nl)
p.write_bytes(text.encode('utf-8'))
print(json.dumps({'brief_reconciled':True,'focused_subset':x['summary'],'external_call':False}))
