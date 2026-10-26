"""Link preserved review bytes, then update two checkpoint references separately."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'output/research/frontend-three-remedy-evaluation-2026-10-06'
RECEIPT = ROOT / 'docs/phase-1-compatibility/reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save_before(path):
    name = path.name + '.before'
    with (OUT / name).open('xb') as file:
        file.write(path.read_bytes())

def append(path, expected, value):
    if sha(path) != expected:
        raise RuntimeError(f'Unexpected source {path}')
    save_before(path)
    with path.open('ab') as file:
        file.write(value.replace('\n', '\r\n').encode('utf-8'))

def main():
    if sha(RECEIPT) != 'd6e8f8c65394986fd4a74550e728d065e14583566c10b6c259c2bfad8d07269f':
        raise RuntimeError('Unexpected review receipt')
    packet = json.loads((SOURCE / 'review-inputs.json').read_text(encoding='utf-8'))
    if any(sha(ROOT / row['path']) != row['sha256'] for row in packet):
        raise RuntimeError('Frozen inputs changed before integration')
    note = '''
The [independent matched-candidate review](reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md)
records bounded PASS without a correction: six checker controls, two native type
comparisons, the default Vite build and finite built-page browser interactions
reproduce. Reviewer build artifacts also match the producer bytes. The
[exact reviewed snapshots](../../output/research/frontend-three-remedy-evaluation-2026-10-06/)
remain preserved; this later navigation reference is outside that receipt.
Warnings, existing browser/tool mismatch, complete graph and D-069 selection/
exception/rollback/recheck gates remain. Separate later supply-chain observations
are outside this review; no application adoption or Phase 1 acceptance follows.
'''
    append(ROOT / 'docs/phase-1-compatibility/README.md',
           'd2c2c5eca579377c5f5570e60a9a98e997dacbe247634147202b812f95fb6f31', note)
    append(ROOT / 'docs/phase-1-compatibility/refresh-evidence-2026-10-04.md',
           '085ff178e5528a45bb4011acc0cceda7d92e53a53597b0a36c8c0a6dddadde21', note)
    # The completed material slice above changes only the two compatibility docs.
    # This separate reference-only slice changes only the state and coverage map.
    state = ROOT / 'PROJECT_STATE.yaml'
    mapping = ROOT / 'docs/software-definition/04-reconciliation-map.md'
    save_before(state)
    save_before(mapping)
    lines = state.read_bytes().splitlines(keepends=True)
    replacements = {
        b'    compatibility:': '    compatibility: D072_lint_only_exception_expiry_2027_01_05_bounded_lint_TS_bridge_React_types_native_LSP_reviews_PASS_latest_coupled_candidate_strict_loader_FAIL_matched_Three184_candidate_compiler_build_browser_independent_evidence_PASS_large_chunk_Clock_warnings_browser_tool_mismatch_retained_supply_chain_full_conformance_deployed_exclusion_complete_graph_MA013_and_D069_selection_exception_rollback_recheck_held',
        b'next_safe_action:': 'next_safe_action: Complete_candidate_supply_chain_inventory_and_missing_optional_WASM_graph_definition_then_remaining_contracts_World_numeric_profiles_and_production_references_preserve_D069_D072_QA_B01_legal_and_integrated_acceptance_gates_no_app_or_selection_changes',
    }
    for index, line in enumerate(lines):
        for prefix, replacement in replacements.items():
            if line.startswith(prefix):
                lines[index] = replacement.encode('utf-8') + b'\r\n'
    if len(lines) != 50:
        raise RuntimeError('State length changed')
    state.write_bytes(b''.join(lines))
    row = '| 12. Compatibility graph | DOING | The [compatibility entry](../phase-1-compatibility/README.md#current-authority-and-dated-evidence) controls all dated candidates, preserved snapshots and exact scoped receipts. The newest coupled frontend candidate fails strict loader declarations. The later matching Three 0.184 candidate has [independent compiler/build/browser evidence PASS](../phase-1-compatibility/reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md), with large-chunk and Clock warnings and the existing browser/tool mismatch retained; it is not a selected production fallback. D-072 permits only the named lint exception through 2027-01-05. Complete conformance, supply-chain inventory/licences/provenance, deployed exclusion, supported platforms/rollback and full graph/MA-013 acceptance remain; any D-069 exception and founder selection require their own evidence. D-068 keeps hosting/packaging conditional without changing Entra/private-AI constraints. Later supply-chain work is outside this receipt. |'
    map_lines = mapping.read_bytes().splitlines(keepends=True)
    positions = [index for index, line in enumerate(map_lines) if line.startswith(b'| 12. Compatibility graph |')]
    if len(positions) != 1:
        raise RuntimeError('Expected one coverage row')
    map_lines[positions[0]] = row.encode('utf-8') + b'\r\n'
    mapping.write_bytes(b''.join(map_lines))
    protected = json.loads((SOURCE / 'protected-before.json').read_text(encoding='utf-8'))
    changed = [row['path'] for row in protected if sha(ROOT / row['path']) != row['sha256']]
    if changed != ['PROJECT_STATE.yaml']:
        raise RuntimeError(f'Unexpected protected changes: {changed}')
    with (OUT / 'reference-integration.json').open('x', encoding='utf-8') as file:
        json.dump({'receipt_sha256': sha(RECEIPT), 'protected_checked': len(protected),
                   'intentional_protected_changes': changed, 'state_lines': len(lines),
                   'material_slice': ['docs/phase-1-compatibility/README.md', 'docs/phase-1-compatibility/refresh-evidence-2026-10-04.md'],
                   'reference_slice': ['PROJECT_STATE.yaml', 'docs/software-definition/04-reconciliation-map.md'],
                   'limits': 'Reference integration only, not full graph/adoption/Phase1 acceptance; snapshots remain unchanged.'}, file, indent=2)
    print('Review references integrated; state remains 50 lines; 77 other protected inputs unchanged.')

if __name__ == '__main__':
    main()
