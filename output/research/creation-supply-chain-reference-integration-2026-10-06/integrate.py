"""Three separate reference-only slices, each limited to two canonical documents."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def packet(relative):
    return {row['path']: row['sha256'] for row in json.loads((ROOT / relative).read_text(encoding='utf-8'))}

def before(path):
    with (OUT / (path.name + '.before')).open('xb') as file:
        file.write(path.read_bytes())

def append(relative, expected, text):
    path = ROOT / relative
    if sha(path) != expected:
        raise RuntimeError(f'Unexpected current input: {relative}')
    before(path)
    with path.open('ab') as file:
        file.write(text.replace('\n', '\r\n').encode('utf-8'))

supply = packet('output/research/frontend-supply-chain-2026-10-06/review-inputs.json')
booking = packet('output/research/booking-creation-request-2026-10-06/review-inputs.json')
receipts = {
    'docs/phase-1-compatibility/reviews/frontend-supply-chain-v1-2026-10-06.md': '30f77b62b080c1ee7a6ee64479c50be59d3c249384b101b0d7362b3db071bbb6',
    'docs/phase-1-architecture/contracts/reviews/booking-creation-request-v1-2026-10-06.md': 'c8e65a4f4d9c6a5130c28b3b573e1fe882c3864d3d98a06efdc6bb2121916914',
}
for name, expected in receipts.items():
    if sha(ROOT / name) != expected:
        raise RuntimeError('Receipt identity differs')

# Slice one: completed supply-chain evidence navigation in its two documents.
supply_note = '''
The [independent supply-chain review](reviews/frontend-supply-chain-v1-2026-10-06.md)
records bounded evidence-accuracy PASS without revision. Saved command outcomes,
package/SBOM identities, available attestation correlations and retained top-level
licence texts reproduce; the reviewer did not rerun remote CLI verification.
The [inspected snapshots](../../output/research/frontend-supply-chain-2026-10-06/)
remain preserved. This later reference is outside those reviewed bytes and grants
no full-platform inventory, recursive notice completeness, cryptographic/security/
legal clearance, D-072 conformance, production selection or Phase 1 acceptance.
'''
for name in ('docs/phase-1-compatibility/README.md', 'docs/phase-1-compatibility/refresh-evidence-2026-10-04.md'):
    append(name, supply[name], supply_note)

# Slice two: completed booking request definition navigation in two documents.
proof_name = 'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md'
append(proof_name, booking[proof_name], '''
Review reference added 2026-10-06: the [independent booking-request receipt](reviews/booking-creation-request-v1-2026-10-06.md)
records bounded PASS for this proposed direction and eight new plus seven common
validator tests. The [exact inspected proof bytes](../../../output/research/booking-creation-request-2026-10-06/PRIVATE_PROCESS_PROOF.md.reviewed)
remain preserved; this later reference is outside them. Shape/definition review
does not prove allocation, random generation, current admission, raw decoding,
HTTP/proof/CSRF, atomic promotion, retention or full wire/Phase 1 acceptance.
''')
catalog_name = 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
append(catalog_name, booking[catalog_name], '''
The later [IF-BOOK-01 request encoding proposal](PRIVATE_PROCESS_PROOF.md#booking-creation-request-encoding-proposal--2026-10-06)
and [closed client schema](booking-creation-request.schema.json) have their own
[bounded independent review PASS](reviews/booking-creation-request-v1-2026-10-06.md).
They refine phase-only bootstrap and empty-lineage creation references, excluding
personal, consent, qualification and credential JSON. Server responses, transport,
expiry/work policies and actual admission remain held. This later navigation is
outside the receipt; chat, qualification and full Phase 1 authority remain separate.
''')

# Slice three: current checkpoint and the existing coverage map.
state = ROOT / 'PROJECT_STATE.yaml'
mapping = ROOT / 'docs/software-definition/04-reconciliation-map.md'
before(state)
before(mapping)
lines = state.read_bytes().splitlines(keepends=True)
for index, line in enumerate(lines):
    if line.startswith(b'    compatibility:'):
        value = '    compatibility: D072_lint_only_exception_expiry_2027_01_05_bounded_lint_TS_bridge_React_types_native_LSP_reviews_PASS_latest_coupled_candidate_strict_loader_FAIL_matched_Three184_compiler_build_browser_and_supply_chain_accuracy_reviews_PASS_warnings_browser_tool_mismatch_virtual_optional_WASM_inventory_gap_partial_attestations_licence_notice_limits_retained_complete_graph_conformance_exclusion_MA013_D069_selection_exception_rollback_recheck_held'
        lines[index] = value.encode('utf-8') + b'\r\n'
    elif line.startswith(b'    contract_reviews:'):
        value = line.rstrip(b'\r\n').replace(b'exact_inputs_remaining_schemas_', b'booking_creation_closed_request_encoding_eight_plus_seven_validator_tests_bounded_review_PASS_exact_inputs_remaining_response_schemas_')
        lines[index] = value + b'\r\n'
    elif line.startswith(b'next_safe_action:'):
        value = 'next_safe_action: Define_World_numeric_measurement_and_loading_profiles_and_remaining_private_response_transport_retention_contracts_from_approved_boundaries_prepare_production_reference_gate_preserve_D069_D072_QA_B01_legal_and_integrated_acceptance_no_app_selection_changes'
        lines[index] = value.encode('utf-8') + b'\r\n'
if len(lines) != 50:
    raise RuntimeError('State length differs')
state.write_bytes(b''.join(lines))
map_lines = mapping.read_bytes().splitlines(keepends=True)
for index, line in enumerate(map_lines):
    if line.startswith(b'| 9. API/data/publication contracts |'):
        addition = ' The later [booking creation request schema](../phase-1-architecture/contracts/booking-creation-request.schema.json) and [independent review](../phase-1-architecture/contracts/reviews/booking-creation-request-v1-2026-10-06.md) close the proposed bootstrap/create client bodies only; eight new and seven common validator tests pass. Server responses, transport/proof policies and actual promotion remain held.'
        map_lines[index] = line.rstrip(b'\r\n').removesuffix(b' |') + addition.encode('utf-8') + b' |\r\n'
    elif line.startswith(b'| 12. Compatibility graph |'):
        row = '| 12. Compatibility graph | DOING | The [compatibility entry](../phase-1-compatibility/README.md#current-authority-and-dated-evidence) controls dated candidates and preserved scoped receipts. The newest coupled frontend candidate fails loader declarations; the matching Three184 candidate has [independent compiler/build/browser evidence PASS](../phase-1-compatibility/reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md), retaining bundle/Clock warnings and browser/tool mismatch. Its separate [supply-chain accuracy review PASS](../phase-1-compatibility/reviews/frontend-supply-chain-v1-2026-10-06.md) retains the failed virtual optional-WASM inventory, partial attestations and licence/notice limits; zero reported known advisories is no security clearance. D-072 is lint-only through 2027-01-05. Complete conformance, provenance/licences/deployed inventory and exclusion, supported-platform/rollback evidence, full graph/MA-013 and any D-069 exception/founder selection remain. D-068 keeps hosting/packaging conditional without changing Entra/private-AI constraints. |'
        map_lines[index] = row.encode('utf-8') + b'\r\n'
mapping.write_bytes(b''.join(map_lines))
guards = json.loads((ROOT / 'output/research/frontend-supply-chain-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
changed = [row['path'] for row in guards if sha(ROOT / row['path']) != row['sha256']]
if changed != ['PROJECT_STATE.yaml']:
    raise RuntimeError(f'Unexpected protected change {changed}')
with (OUT / 'reference-integration.json').open('x', encoding='utf-8') as file:
    json.dump({'receipt_identities': receipts, 'protected_checked': len(guards),
       'intentional_protected_changes': changed, 'state_lines': len(lines),
       'slices': [['compatibility README', 'compatibility refresh'], ['private proof', 'interface catalogue'],
                  ['project state', 'reconciliation map']],
       'scope': 'Later reference integration only; preserved snapshots and app/model bytes unchanged; no selection, adoption or full Phase1 acceptance.'}, file, indent=2)
print('Three reference slices integrated; state50; all77 other protected inputs unchanged.')
