"""Navigate to independently reviewed work; reviewed snapshots remain frozen."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent/'reference-integration'
OUT.mkdir(exist_ok=True)
if (OUT/'reference-integration.json').exists():raise SystemExit('Already integrated; inspect rather than rerun.')
walking=ROOT/'docs/software-definition/reviews/world-walking-walkthrough-correction1-v1-2026-10-06.md'
chat=ROOT/'docs/phase-1-architecture/contracts/reviews/chat-interface-reference-v1-2026-10-06.md'
assert walking.exists() and chat.exists(), 'Independent review receipts still absent'
assert 'PASS' in walking.read_text(encoding='utf-8') and 'PASS' in chat.read_text(encoding='utf-8'), 'Inspect receipt verdict before integration'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for packet in [ROOT/'output/playwright/world-walking-walkthrough-2026-10-06/correction-1/review-inputs.json',ROOT/'output/research/chat-interface-reference-2026-10-06/review-inputs.json']:
    data=json.loads(packet.read_text(encoding='utf-8'))
    assert all(digest(ROOT/x['path'])==x['sha256'] for x in data['inputs']), 'Reviewed bytes drifted'
guards=json.loads((ROOT/'output/playwright/world-walking-walkthrough-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards)
readme=ROOT/'docs/software-definition/README.md'
before=readme.read_bytes()
needle=b'| Optional World sound |'
assert before.count(needle)==1
row=('| World walking and loading | [Visual explanation](definition-walkthrough.html#walking), [controlling traversal proposal](../phase-1-3d/WORLD_EXPERIENCE.md), [measurement targets](../phase-1-3d/WORLD_MEASUREMENT_PROFILE.md) and [bounded translation review after link correction](reviews/world-walking-walkthrough-correction1-v1-2026-10-06.md) | Source/pixel review covers the new explanation only. Producer desktop/narrow-width layout, keyboard and link checks are separate; resized Chromium is not physical touch or mobile qualification. No walking engine or production controls are present. Exact pad mapping, screens, geometry/rights, stable graph, measured budgets and final appearance/acceptance remain held. |\r\n').encode('utf-8')
after=before.replace(needle,row+needle,1)
assert after.replace(row,b'',1)==before
state=ROOT/'PROJECT_STATE.yaml'
state_before=state.read_bytes()
s=state_before.decode('utf-8')
old='visual_definition: Staff_signin_walkthrough_source_pixels_bounded_PASS_'
new='visual_definition: Walking_loading_walkthrough_source_pixels_bounded_PASS_desktop_narrow_keyboard_links_no_runtime_or_physical_mobile_proof_Staff_signin_walkthrough_source_pixels_bounded_PASS_'
assert s.count(old)==1
s=s.replace(old,new,1)
old='contract_reviews: Scoped_amendment_'
new='contract_reviews: Chat_IF02_consent_IF03_events_reference_correction1_bounded_PASS_Scoped_amendment_'
assert s.count(old)==1
s=s.replace(old,new,1)
old='next_safe_action: Define_mouse_touch_World_traversal_camera_clearance_and_remaining_chat_private_protocols_from_primary_research_and_approved_boundaries_prepare_production_reference_gate_preserve_D069_D072_QA_B01_legal_and_integrated_acceptance_no_app_selection_changes'
new='next_safe_action: Complete_remaining_chat_private_protocols_and_full_compatibility_conformance_prepare_production_reference_gate_integrate_reviewed_definitions_preserve_D069_D072_QA_B01_legal_no_app_selection_changes'
assert s.count(old)==1
s=s.replace(old,new,1)
assert len(s.splitlines())<=50
(OUT/'README.md.before').write_bytes(before)
(OUT/'PROJECT_STATE.yaml.before').write_bytes(state_before)
readme.write_bytes(after)
state.write_bytes(s.encode('utf-8'))
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards if x['path']!='PROJECT_STATE.yaml')
r=subprocess.run(['git','-c','core.autocrlf=false','-c','core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol','diff','--check','--','docs/software-definition/README.md','PROJECT_STATE.yaml'],cwd=ROOT,capture_output=True)
assert r.returncode==0,r.stdout+r.stderr
obs={'scope':'Two-document ordinary reference/checkpoint slice only; no canonical proposal/runtime/model change. Later navigation does not extend earlier exact review scope.','state_lines':len(s.splitlines()),'other_77_guards_match':True,'whitespace_pass':True,'walking_receipt_sha256':digest(walking),'chat_reference_receipt_sha256':digest(chat),'current_README_sha256':digest(readme),'current_state_sha256':digest(state)}
(OUT/'reference-integration.json').write_text(json.dumps(obs,indent=2)+'\n',encoding='utf-8')
print(json.dumps(obs))
