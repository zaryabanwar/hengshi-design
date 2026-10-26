"""Correct a route-reference contradiction; no contract or runtime redesign."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
TARGET=ROOT/'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md'
before=TARGET.read_bytes()
if (OUT/'PRIVATE_PROCESS_PROOF.md.before').exists(): raise SystemExit('Already applied; inspect rather than rerun.')
old=b'Messages belong to IF-CHAT-02; handoff to IF-CHAT-04.'
new=b'Messages use the separately reviewed IF-CHAT-03 event protocol; consent changes use IF-CHAT-02 and handoff uses IF-CHAT-04.'
assert before.count(old)==1
after=before.replace(old,new,1)
assert after.replace(new,old,1)==before
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
guard_paths=json.loads((ROOT/'output/playwright/world-walking-walkthrough-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
guards=[{'path':x['path'],'sha256':digest(ROOT/x['path'])} for x in guard_paths]
(OUT/'protected-before.json').write_text(json.dumps(guards,indent=2)+'\n',encoding='utf-8')
(OUT/'PRIVATE_PROCESS_PROOF.md.before').write_bytes(before)
TARGET.write_bytes(after)
(OUT/'PRIVATE_PROCESS_PROOF.md.reviewed').write_bytes(after)
observation={'cause':'PRIVATE_PROCESS_PROOF.md:137 attributed messages to IF-CHAT-02, but the canonical operation and field dictionaries reserve IF-CHAT-02 for consent and IF-CHAT-03 for typed guidance events.','change':'Exactly one reference clause; no endpoint, schema, phase, proof, consent, message body, authority, lifetime or runtime behavior changed.','correction_cycle':1,'revision_limit':2,'predecessor_restoration_equal':True,'tests':'No prose test required or run; source-reference reconciliation only.'}
(OUT/'scope-observations.json').write_text(json.dumps(observation,indent=2)+'\n',encoding='utf-8')
sources=['AGENTS.md','.specify/memory/constitution.md','PROJECT.md','PROJECT_STATE.yaml','DECISIONS.md','TASKS.md','docs/software-definition/README.md','docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md','docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md','docs/phase-1-architecture/contracts/interface-catalog.csv','docs/phase-1-architecture/contracts/process-fields.csv','docs/phase-1-architecture/contracts/reviews/private-creation-boundary-v1-2026-10-05.md']
files=[p for p in OUT.iterdir() if p.is_file() and p.name!='review-inputs.json']
inputs=[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)} for p in files]+[{'path':p,'sha256':digest(ROOT/p)} for p in sources]
packet={'scope':'Only the one corrected reference clause in the Client chat create row at line 137; current later appended profiles and prior review bytes are context, not re-reviewed. Correction 1 for the directional-creation reference.','inputs':inputs,'protected_guard_count':len(guards)}
(OUT/'review-inputs.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
result=subprocess.run(['git','-c','core.autocrlf=false','-c','core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol','diff','--check','--',str(TARGET)],cwd=ROOT,capture_output=True)
assert result.returncode==0,result.stdout+result.stderr
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards)
print(json.dumps({'packet_sha256':digest(OUT/'review-inputs.json'),'input_count':len(inputs),'guard_count':len(guards),'whitespace_pass':True}))
