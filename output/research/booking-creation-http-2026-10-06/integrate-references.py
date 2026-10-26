"""Reference the bounded profile receipt, then update the checkpoint separately."""
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / 'reference-integration'
OUT.mkdir(exist_ok=False)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
for row in json.loads((OUT.parent / 'review-inputs.json').read_text()):
    if sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Reviewed input changed: ' + row['path'])
receipt = ROOT / 'docs/phase-1-architecture/contracts/reviews/booking-creation-http-v1-2026-10-06.md'
if sha(receipt) != 'dff714932faa22aefe1e9b221f4a9c7248e16cf0c9c95382ce260b22daadf349':
    raise RuntimeError('Receipt changed')
changes = []
def save(path, text, slice_number):
    path = ROOT / path
    (OUT / (path.name + '.before')).write_bytes(path.read_bytes())
    path.write_bytes(text.replace('\n', '\r\n').encode())
    changes.append({'path': path.relative_to(ROOT).as_posix(), 'slice': slice_number,
                    'sha256': sha(path)})
proof_path = 'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md'
text = (ROOT / proof_path).read_text()
old = '''The corresponding server bootstrap/admitted/pending/denied response encodings,
cookie/CSRF profile, expiry/work limits and HTTP error/status mappings remain
explicit inputs before implementation. Chat creation keeps its distinct release/'''
new = '''The subsequent [booking transport/response profile proposal](#booking-creation-transport-and-response-profile-proposal--2026-10-06)
now proposes server projections, cookie/CSRF representation, lifetime/work bounds
and status/error mappings for this boundary. Acceptance and actual enforcement
remain required; this later reference is outside the request review's preserved
inputs. Chat creation keeps its distinct release/'''
assert text.count(old) == 1
text = text.replace(old, new)
text += '''
Review reference added 2026-10-06: [booking creation profile review PASS](reviews/booking-creation-http-v1-2026-10-06.md)
covers the exact appended profile, response schema and actual validator boundary
at frozen inputs. Eight response, eight request and seven common-value methods
pass independently. The [inspected proof document](../../../output/research/booking-creation-http-2026-10-06/PRIVATE_PROCESS_PROOF.md.reviewed)
is preserved; this reference reconciliation is outside those bytes. Numerical
capacities/lifetimes remain unmeasured proposals. No actual HTTP/cookie/CSRF,
distributed fencing/store/expiry/recovery, full graph or founder approval follows.
'''
save(proof_path, text, 1)
catalogue = 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
text = (ROOT / catalogue).read_text()
text += '''
The subsequent [booking creation transport/response profile](PRIVATE_PROCESS_PROOF.md#booking-creation-transport-and-response-profile-proposal--2026-10-06)
and [closed server projections](booking-creation-response.schema.json) now have
[bounded independent review PASS](reviews/booking-creation-http-v1-2026-10-06.md).
They refine this existing boundary's same-origin/media/raw input, separate
generation-bound bearer/CSRF transport, bootstrap/created/pending/safe-error
projections and finite proposed capacity/lifetime rules. Twenty-three actual
validator-boundary methods pass, not HTTP or distributed enforcement tests.
This ordinary reference does not claim the prior catalogue body was reviewed
anew or alter its fields/routes. The profile receipt names
its exact inputs, including the existing catalogue. Measured capacity, legal
class mapping, stable graph, actual mechanisms and integrated/founder acceptance
remain. Chat/qualification/email/provider/status protocols stay separate.
'''
save(catalogue, text, 1)
state_path = 'PROJECT_STATE.yaml'
text = (ROOT / state_path).read_text()
old = 'booking_creation_closed_request_encoding_eight_plus_seven_validator_tests_bounded_review_PASS_exact_inputs_remaining_response_schemas_origins_permissions_policies_stable_graph_and_actual_enforcement_held'
new = 'booking_creation_request_and_response_transport_lifetime_work_profile_twenty_three_validator_tests_bounded_review_PASS_unmeasured_targets_remaining_chat_and_private_protocols_legal_binding_origins_mechanisms_graph_and_actual_enforcement_held'
assert text.count(old) == 1
text = text.replace(old, new)
old = 'Define_World_numeric_measurement_and_loading_profiles_and_remaining_private_response_transport_retention_contracts_from_approved_boundaries_prepare_production_reference_gate_preserve_D069_D072_QA_B01_legal_and_integrated_acceptance_no_app_selection_changes'
new = 'Define_mouse_touch_World_traversal_camera_clearance_and_remaining_chat_private_protocols_from_primary_research_and_approved_boundaries_prepare_production_reference_gate_preserve_D069_D072_QA_B01_legal_and_integrated_acceptance_no_app_selection_changes'
assert text.count(old) == 1
text = text.replace(old, new)
assert len(text.splitlines()) == 50
save(state_path, text, 2)
map_path = 'docs/software-definition/04-reconciliation-map.md'
text = (ROOT / map_path).read_text()
old = 'Server responses, transport/proof policies and actual promotion remain held. |'
new = 'The subsequent [server projection schema](../phase-1-architecture/contracts/booking-creation-response.schema.json) and [transport/lifetime/work profile](../phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md#booking-creation-transport-and-response-profile-proposal--2026-10-06) have [bounded independent review PASS](../phase-1-architecture/contracts/reviews/booking-creation-http-v1-2026-10-06.md): eight response, eight request and seven common validator methods pass. Proposed capacities/lifetimes are unmeasured; legal/store/ingress/Origin/cookie/CSRF/fencing enforcement, other private protocols, stable graph and integrated/founder acceptance remain. |'
assert text.count(old) == 1
save(map_path, text.replace(old, new), 2)
guards = json.loads((OUT.parent / 'protected-before.json').read_text())
for row in guards:
    if row['path'] != state_path and sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Protected input changed: ' + row['path'])
(OUT / 'reference-integration.json').write_text(json.dumps({'changes': changes,
    'scope': 'Two reference/reconciliation documents, then separate two-document checkpoint slice; no extension of receipt scope.',
    'state_lines': 50, 'other_guards_match': 77}, indent=2) + '\n')
print('Profile references integrated; state remains 50 lines, 77 other guards unchanged.')
