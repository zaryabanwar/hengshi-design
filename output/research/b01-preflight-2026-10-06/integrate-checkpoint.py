from pathlib import Path
import hashlib
import json

root = Path.cwd()
base = root / 'output/research/b01-preflight-2026-10-06'
out = base / 'checkpoint-integration'
out.mkdir(exist_ok=False)
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
receipts = {
 'docs/phase-1-ui-reference-production/reviews/b01-preflight-v1-2026-10-06.md': '92100eb17a725280b7459fb9c752f8161083169f8634e7136d7d3b48c2935e4c',
 'docs/phase-1-ui-reference-production/reviews/first-file-ordering-correction1-v1-2026-10-06.md': '73099b611978492e8410dfebeb3e472cf260f6fe2c30e81db178834ff1ba54b7',
}
assert all(digest(root / p) == h for p,h in receipts.items())
guards = json.loads((base / 'protected-current.json').read_text(encoding='utf-8'))
assert all(digest(root / g['path']) == g['sha256'] for g in guards)
state = root / 'PROJECT_STATE.yaml'
mapping = root / 'docs/software-definition/04-reconciliation-map.md'
(out / 'PROJECT_STATE.before.yaml').write_bytes(state.read_bytes())
(out / 'reconciliation-map.before.md').write_bytes(mapping.read_bytes())
text = state.read_text(encoding='utf-8')
old = '    visual_definition: Walking_loading_walkthrough_source_pixels_bounded_PASS_'
new = '    visual_definition: B01_preflight_bounded_PASS_first_file_ordering_correction1_proposed_PASS_unapplied_pilot_file_privacy_archives_held_Walking_loading_walkthrough_source_pixels_bounded_PASS_'
assert text.count(old) == 1
text = text.replace(old,new)
old = '  figma_calls: authenticated_Starter_Full_2026_10_05_identity_only_approval_consumed_each_further_call_requires_immediate_approval'
new = '  figma_calls: authenticated_one_Starter_Full_plan_2026_10_06_October_project_calls_2_documented_metered_0_account_usage_unknown_whoami_permission_consumed_no_file_metadata_or_design_each_call_gate_retained'
assert text.count(old) == 1
text = text.replace(old,new)
old = 'next_safe_action: Complete_remaining_chat_private_protocols_and_full_compatibility_conformance_prepare_production_reference_gate_integrate_reviewed_definitions_preserve_D069_D072_QA_B01_legal_no_app_selection_changes'
new = 'next_safe_action: Await_first_file_amendment_and_create_call_decision_while_complete_remaining_chat_private_protocols_and_compatibility_preserve_D069_D072_QA_B01_legal_no_app_selection_changes'
assert text.count(old) == 1
text = text.replace(old,new)
assert len(text.splitlines()) == 50
state.write_text(text,encoding='utf-8',newline='\n')
text = mapping.read_text(encoding='utf-8')
old = '| Production UI references | [Reference design](../phase-1-ui-reference-design/README.md) and [reference production](../phase-1-ui-reference-production/README.md) | Definitions are not completed screen production. |'
new = '| Production UI references | [Reference design](../phase-1-ui-reference-design/README.md) and [reference production](../phase-1-ui-reference-production/README.md) | Definitions are not completed screen production. The [B01 execution read-back](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md) has [bounded review PASS](../phase-1-ui-reference-production/reviews/b01-preflight-v1-2026-10-06.md). The founder confirms there is no file; an individually approved identity/plan check succeeded and is [recorded separately](../phase-1-ui-reference-production/validation/capability-evidence.md#subsequent-approved-identity-observation--2026-10-06). The [first-file ordering amendment](../../output/research/b01-preflight-2026-10-06/bootstrap-proposal/correction-1/first-file-ordering.patch) has [correction-1 proposal review PASS](../phase-1-ui-reference-production/reviews/first-file-ordering-correction1-v1-2026-10-06.md), remains unapplied and needs founder approval. No file creation, inventory/privacy/archive proof, pilot release or production screen follows from these receipts. |'
assert text.count(old) == 1
mapping.write_text(text.replace(old,new),encoding='utf-8',newline='\n')
other = [x['path'] for x in guards if x['path'] != 'PROJECT_STATE.yaml' and digest(root/x['path']) != x['sha256']]
assert not other, other
record = {'scope':'Ordinary later checkpoint/navigation references only; outside frozen proposal/receipt bytes. No new acceptance or provider operation.', 'state_lines':50, 'other_guards_unchanged':len(guards)-1, 'receipts':receipts, 'state_sha256':digest(state), 'map_sha256':digest(mapping)}
(out/'observations.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
