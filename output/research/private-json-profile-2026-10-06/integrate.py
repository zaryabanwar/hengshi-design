"""Ordinary map/checkpoint references, with Phase1/later-proof distinction."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent/'reference-integration'
OUT.mkdir(exist_ok=True)
if (OUT/'observations.json').exists():raise SystemExit('Already integrated; inspect rather than rerun.')
receipt=ROOT/'docs/phase-1-architecture/contracts/reviews/private-json-profile-v1-2026-10-06.md'
assert receipt.exists(), 'Wait for independent review'
assert 'Verdict: **PASS' in receipt.read_text(encoding='utf-8'), 'Inspect bounded verdict before integration'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
packet=json.loads((OUT.parent/'review-inputs.json').read_text(encoding='utf-8'))
assert all(digest(ROOT/x['path'])==x['sha256'] for x in packet['inputs'])
guards=json.loads((OUT.parent/'protected-before.json').read_text(encoding='utf-8'))
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards)
mapfile=ROOT/'docs/software-definition/04-reconciliation-map.md'
before=mapfile.read_bytes();s=before.decode('utf-8')
old='''Completing this map does not complete Phase 1. Missing production designs,
provider/legal evidence and implementation remain visible obligations rather than
being silently inferred or marked complete.'''.replace('\n','\r\n')
new='''Phase 1 closes through the controlling [task exit contract](../../TASKS.md#exit-and-later-phases):
coherent non-deferred definitions, required production UI references, a complete
compatible stable graph or approved dated exception, proportionate validation and
independent review, and founder acceptance. Define actual HTTP, movement, recovery
and other runtime qualification methods and criteria here; application feature
implementation and its runtime qualification follow in the later approved phases.
They are not circular prerequisites for Phase 1 acceptance, and remain unauthorized
before that acceptance. Missing required designs, material contracts and legal-policy
choices cannot be inferred as approved. D-068 still defers hosting/provider/region/
cost selection. This clarification changes no acceptance or later implementation gate.'''.replace('\n','\r\n')
assert s.count(old)==1
s=s.replace(old,new,1)
lines=s.splitlines(keepends=True)
rows=[i for i,line in enumerate(lines) if line.startswith('| 9.')]
assert len(rows)==1
i=rows[0];line=lines[i];assert line.endswith(' |\r\n')
addition=' The [shared private-browser JSON profile](../phase-1-architecture/contracts/DATA_CONTRACT.md#private-browser-json-admission-profile-proposal--2026-10-06) has [bounded definition review PASS](../phase-1-architecture/contracts/reviews/private-json-profile-v1-2026-10-06.md); its finite limits are unmeasured proposals, with no decoder or HTTP enforcement implemented.'
lines[i]=line[:-4]+addition+' |\r\n'
map_after=''.join(lines).encode('utf-8')
state=ROOT/'PROJECT_STATE.yaml';state_before=state.read_bytes();ss=state_before.decode('utf-8')
old='contract_reviews: Chat_IF02_'
new='contract_reviews: Private_browser_JSON_profile_bounded_review_PASS_unmeasured_caps_no_decoder_HTTP_proof_Chat_IF02_'
assert ss.count(old)==1;ss=ss.replace(old,new,1)
assert len(ss.splitlines())<=50
(OUT/'map.before.md').write_bytes(before)
(OUT/'state.before.yaml').write_bytes(state_before)
mapfile.write_bytes(map_after);state.write_bytes(ss.encode('utf-8'))
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards if x['path']!='PROJECT_STATE.yaml')
r=subprocess.run(['git','-c','core.autocrlf=false','-c','core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol','diff','--check','--','PROJECT_STATE.yaml','docs/software-definition/04-reconciliation-map.md'],cwd=ROOT,capture_output=True)
assert r.returncode==0,r.stdout+r.stderr
obs={'scope':'Two-document ordinary navigation/checkpoint update; distinction restates TASKS Phase1-before-implementation contract and D068, no new gate/approval.','receipt_sha256':digest(receipt),'state_lines':len(ss.splitlines()),'other_77_guard_match':True,'whitespace_pass':True,'map_sha256':digest(mapfile),'state_sha256':digest(state)}
(OUT/'observations.json').write_text(json.dumps(obs,indent=2)+'\n',encoding='utf-8')
print(json.dumps(obs))
