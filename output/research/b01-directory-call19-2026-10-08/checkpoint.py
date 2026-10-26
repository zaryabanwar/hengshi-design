from pathlib import Path
import json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
state=root/'PROJECT_STATE.yaml'
manual=root/'MANUAL_ACTIONS.md'
for file in [state,manual]:shutil.copyfile(file,out/(file.name+'.before'))
lines=state.read_bytes().decode('utf-8').splitlines(keepends=True)
for i,line in enumerate(lines):
    end='\r\n' if line.endswith('\r\n') else '\n'
    if line.startswith('next_safe_action:'):
        lines[i]='next_safe_action: Phase1_only_B01_call19_created52_directory_views2_components15_input_bounded_review_PASS_full_resolution_export5_temporary_sheets_prepared_attempt20_requires_fresh_approval_no_application_or_integrated_acceptance'+end
    elif line.startswith('  figma_calls:'):
        lines[i]='  figma_calls: D075_B01_call19_success_complete15080_byte_report2674_created_IDs52_views2_components_zero_reported_bounds_two_scaled_PNGs_October_attempts19_conservative_metered16_actual_balance_unknown_permission_consumed_no_further_call_output/research/b01-directory-call19-2026-10-08/receipt.json'+end
    elif line.startswith('  figma_production:'):
        lines[i]='  figma_production: D075_execution_approved_PRE_verified_six_initial_drafts_20_navigation_views_inspected_directory52_views2_components_created15_input_source_structure_two_scaled_preview_independent_bounded_PASS_all52_full_resolution_and_complete_profiles_interaction_review_restore_EXIT_acceptance_held'+end
    elif line.startswith('    visual_definition:'):
        lines[i]=line.replace('52_directory_views2_components_attempt18_return_size_rejected_canvas_not_committed_compact_report_recovery_prepared','call19_directory52_views2_components2674_unique_IDs_zero_reported_bounds_two_scaled_previews15_input_independent_bounded_PASS_all52_full_resolution_inspection_held')
state.write_bytes(''.join(lines).encode('utf-8'))
lines=manual.read_bytes().decode('utf-8').splitlines(keepends=True)
for i,line in enumerate(lines):
    if line.startswith('| B01; CB-06/CB-07 |'):
        end='\r\n' if line.endswith('\r\n') else '\n'
        lines[i]='| B01; CB-06/CB-07 | DOING | Directory construction succeeded; full pilot exit held | D-075 grants execution. PRE/six initial drafts/twenty navigation views retain evidence. Approved corrected call19 created52 directory views/two local components, returning2674 unique IDs and zero reported bounds findings. Two scaled previews are inspected;15-input independent construction/structure/visible-preview review passes. Full-resolution legibility and other50 pixels remain unverified. October attempts19/conservative metered16; actual debit/balance unknown; permission consumed, no further call or spend. | [Call19 receipt](output/research/b01-directory-call19-2026-10-08/receipt.json), [bounded review](docs/phase-1-ui-reference-production/reviews/B01-directory-references-v1-2026-10-08.md), [prepared full-resolution export](output/research/b01-directory-full-resolution-2026-10-08/preparation.json) and [ledger](docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv). One proposed attempt20 exports all52 through five temporary sheets with checked cleanup, without original correction; fresh approval required. Full coverage, interactions, native exports/restore/_EXIT and pilot acceptance remain; later batches gated. |'+end
manual.write_bytes(''.join(lines).encode('utf-8'))
for file in [state,manual]:assert len(file.read_text(encoding='utf-8').splitlines())<=50
print(json.dumps({'state_lines':len(state.read_text(encoding='utf-8').splitlines()),'manual_lines':len(manual.read_text(encoding='utf-8').splitlines()),'next_external_call':'fresh approval required'}))
