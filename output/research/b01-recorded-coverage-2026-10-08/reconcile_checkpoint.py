from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
p=root/'docs/software-definition/definition-walkthrough.html'
raw=p.read_bytes()
before=out/'definition-walkthrough.before-checkpoint.html'
assert not before.exists()
before.write_bytes(raw)
pattern=rb'<tr><th scope="row">Production UI references</th>.*?</tr>'
assert len(re.findall(pattern,raw))==1
row='''<tr><th scope="row">Production UI references</th><td>Six initial drafts and all twenty navigation views have producer pixel inspection. Corrected call19 created52 directory/search references and two components. Their independent review covers construction, decoded structure and two scaled previews only. October attempts19; conservatively metered16; actual balance unknown.</td><td>All52 directory views still need full-resolution pixel inspection; a prepared single export awaits fresh per-call approval. Ceiling-refusal and shared-recovery references and other required profiles remain. Complete B01 coverage, prototype/accessibility evidence, editable exports/restore, _EXIT and founder pilot acceptance are unfinished. <a href="../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#recorded-coverage-reconciliation--2026-10-08">Exact recorded coverage and remaining scope</a>; <a href="../phase-1-ui-reference-production/reviews/B01-directory-references-v1-2026-10-08.md">Bounded directory review</a>.</td></tr>'''
p.write_bytes(re.sub(pattern,lambda _:row.encode('utf-8'),raw,count=1))
print(json.dumps({'checkpoint_reference_only':True,'external_call':False}))
