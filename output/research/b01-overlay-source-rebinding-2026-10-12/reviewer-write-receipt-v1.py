"""Save the bounded receipt from independently produced local audit evidence."""
import hashlib, json
from pathlib import Path
folder=Path(__file__).resolve().parent
root=folder.parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
audit=json.loads((folder/'reviewer-check-results-v1.json').read_text(encoding='utf-8'))
manifest=json.loads((folder/'review-inputs-v1.json').read_text(encoding='utf-8-sig'))
for b in audit['bindings']:
    snapshot=folder/b['snapshot']; current=root/b['source']
    assert snapshot.stat().st_size==b['bytes'] and sha(snapshot)==b['sha256']
    assert current.read_bytes()==snapshot.read_bytes(),b['source']
current_hash=sha(root/manifest['inputs'][14]['source'])
candidate_hash=sha(folder/manifest['inputs'][15]['snapshot'])
assert current_hash=='85736b6db6801ffdc529143085c20346193dc4904eef01e09d2074524211f98a'
assert candidate_hash=='a8358be02d6fbca42a167b19395a4a2cd9b2fe318eaaec3b78e8141f4244aacd'
receipt={
 'product':'Hengshi Design v1','date':'2026-10-12','status':'DOING','verdict':'PASS',
 'reviewer_id':'/root/review_overlay_source_binding_v1','producer_id':'/root',
 'authorization':{'questionId':'call_3b44cedc9e7c4e03a4c36632e1d561a1','answer':'Approve this source-binding review','scope':'One independent read-only review of the proposed D-092 source-binding successor, with receipt and temporary evidence writes confined to this research folder. Replacement reviewer handle retains identical approved scope. No candidate adoption, canonical change, Figma/account/application/Git action or subdelegation.'},
 'manifest':{'path':'review-inputs-v1.json','sha256':audit['manifest_sha256'],'inputs':24,'all_bytes_and_hashes_verified':True,'all24_current_sources_match_frozen_inputs':True,'rechecked_immediately_before_receipt':True},
 'input_bindings':audit['bindings'],
 'registry_binding':{'current_path':manifest['inputs'][14]['source'],'current_snapshot':manifest['inputs'][14]['snapshot'],'current_sha256':current_hash,'candidate_path':manifest['inputs'][15]['source'],'candidate_snapshot':manifest['inputs'][15]['snapshot'],'candidate_sha256':candidate_hash,'canonical_registry_unchanged':True,'candidate_adopted':False},
 'findings':[],'open_critical':0,'open_high':0,'open_medium':0,
 'artifact_integrity':{
   'independent_recursive_diff':'PASS: exact47 scalar changes only:41 sources.quoted_fact,3 timing_criterion.process_source.quoted_fact,3 source_snapshots.raw_sha256. No object-key/list-membership/type/length changes or any other leaf changes.',
   'producer_diff_reconciliation':'PASS: independently generated before/after witness objects, process objects and pin list equal the frozen producer diff exactly; reported registry/candidate hashes and zero declared/timing-policy deltas independently verified.',
   'preserved_contract':'All1146 records,22 declared-column definitions,14 source paths, declared values, selectors, supports, rationale, criterion IDs, timing applicability/selected branch/obligations/implementation_truth are unchanged. No stream/profile/allocation or timing-policy change is introduced by the candidate.',
   'changed_record_indices_zero_based':audit['changed_record_indices'],
   'changed_records':audit['changed_records'],
   'changed_witness_groups':audit['changed_witness_groups'],
   'snapshot_changes':audit['pin_changes'],
   'all_source_witnesses':'PASS:18925 source occurrences,4765 unique witness objects independently resolved against the14 pinned source snapshots using a separate selector implementation. Every candidate quote belongs to the exact selected fact; all41 changed quotes equal the complete selected CSV field or DF-01 section after allowed newline/trailing-section normalization. Exactly those41 predecessor occurrences fail quote membership against current frozen sources.',
   'witnesses_by_source':audit['witnesses_by_source'],
   'selector_kinds':audit['selector_kinds'],
   'copied_timing_process_witnesses':'PASS: zero-based records319,334,864 retain process_source equality with a recorded sources witness. Their copied quotes change identically. All164 timing criteria retain every policy field and future_qa_required truth boundary.',
   'timing_policy_detail':'319 COV-FLOW-NAVIGATION-SEARCH and864 TPL-DIRECTORY-SEARCH retain TL-NOT-APPLICABLE/no_user_limit_declared/empty obligations.334 COV-FLOW-WORLD-HUD-STREAM retains TL-REMOVABLE-ADJUSTABLE/protection_required_if_user_limit_introduced plus preservation, accessible reauthentication and before-start turn-off/adjustment obligations. No visitor30-minute clock, extension count or absolute-lifetime policy is changed.'
 },
 'approved_direction_consistency':{
   'D092':'Frozen22 DECISIONS.md:1377-1397 approves deliberate modal opening over retained current location, visible Close, invoker-focus return, inactive surroundings, semantic static directory without overlay/JavaScript, no automatic homepage gate and preserved content/Book/privacy/stream/World boundaries. It expressly withholds appearance, construction/external writes and B01/Phase1 acceptance.',
   'source_rows':'Frozen09 FLOWS.md:237-269 DF-01, frozen04 PRIM-004 required_anatomy/responsive_and_mode_obligations and frozen07 TPL-DIRECTORY-SEARCH interaction_focus_notes consistently carry this modal direction. Added modal heading/containment/inactive-background/Close/static fallback source wording does not rewrite assigned stream or profile values.',
   'earlier_correction3':'Frozen23 proposal:21-25 and frozen24 prior PASS are bounded truthful-gap/held-construction evidence only. They neither validate the unchanged predecessor registry against D-092 sources nor approve this successor. This review does not inherit registry-adoption authority from them.'
 },
 'existing_verifier':{
   'path':manifest['inputs'][18]['source'],'sha256':manifest['inputs'][18]['sha256'],'frozen_equals_current':True,
   'execution':'Unmodified pinned ui_column_authority.validate_registry executed against reviewer-frozen14-source-root-v1 containing exact14 pinned source snapshots. Additional DECISIONS.md and temporary candidate-as-canonical file used only for the predecessor-approval rejection probe.',
   'candidate_artifact_result':'PASS','source_bound_records':audit['verified_records'],
   'fail_closed_probes':audit['fail_closed_probes'],
   'no_hidden_weakening':'Current verifier bytes match frozen19. Candidate contains no verifier/code/guard change, no altered selectors/support/rationale/criteria, no source-list removal, no unpinning and no changed target value. Existing closed-schema, exact cell inventory/value checks, quote/source-hash membership, process-source equality and approval hash gate remain operative.',
   'evidence_lines':'Frozen19:152 quote membership;159 copied process equality;160 future QA truth;202 stale-pin failure;222 target-cell equality;242 exact record inventory;266 approval hash gate;278 review findings gate. Frozen22:345-362 D-063 requires fail-stale and separate acceptance.'
 },
 'limitations':[
   'This is a bounded successor source-binding review. It rechecks complete registry source integrity and the33 affected existing records; it does not reopen or independently reapprove all existing product/design/timing policies or every historical rationale.',
   'Artifact byte/hash/selector/diff validation and verifier negative probes do not establish runtime functionality, accessibility, native DOM/AT/focus/inertness, timing enforcement, security, browser behavior or product readiness.',
   'No Figma, browser, native prototype, visual appearance, source/control IDs, external-write capability, restore, Presentation path or interaction execution was inspected by this reviewer. Evidence outside the frozen24-input packet cannot inherit this PASS.',
   'Current D-063 remains bound to the predecessor hash and rejects the candidate as stale registry approval. Canonical adoption and an applicable pinned founder acceptance remain held. This bounded receipt is not the closed-schema acceptance review consumed by validate_approval.',
   'No application feature, full B01/Phase1 acceptance, publication, account/provider change, paid activation, commit, push or deployment is authorized or claimed.'
 ],
 'held':{'canonical_adoption':'BLOCKED pending applicable explicit founder authorization and exact successor acceptance binding; current canonical registry preserved','prototype_construction':'BLOCKED under separate exact-source preparation/external-write gates','runtime_and_accessibility_proof':'BLOCKED; outside this artifact review','B01_Phase1_acceptance':'BLOCKED; separate complete evidence, independent reviews and founder acceptance'},
 'temporary_evidence':{'audit_script':'reviewer-check-v1.py','audit_script_sha256':sha(folder/'reviewer-check-v1.py'),'audit_results':'reviewer-check-results-v1.json','audit_results_sha256':sha(folder/'reviewer-check-results-v1.json'),'receipt_writer':'reviewer-write-receipt-v1.py','frozen_source_root':'reviewer-frozen14-source-root-v1'},
 'actions':{'canonical_files_modified':False,'previous_evidence_modified':False,'candidate_modified':False,'figma_browser_account_application_git_actions':False,'subdelegation':False,'writes_confined_to_research_folder':True},
 'conclusion':'PASS for the exact frozen D-092 source-binding candidate only, with no actionable findings in that scope. Founder acceptance and canonical adoption remain held; all predecessor evidence stays preserved.'
}
out=folder/'independent-review-source-binding-v1.json'
assert not out.exists(),'Do not overwrite prior review evidence'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'verdict':receipt['verdict'],'receipt':str(out),'sha256':sha(out),'current_sha256':current_hash,'candidate_sha256':candidate_hash,'inputs':len(receipt['input_bindings'])},indent=2))
