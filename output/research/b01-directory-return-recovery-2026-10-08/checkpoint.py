from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
source=root/'output/research/b01-directory-preflight-refresh-2026-10-07/figma-call.js'
target=out/'figma-call.js'
prefix=source.read_bytes().split(b'await frames.find((node,index)=>input.frames[index].state_id',1)[0]
tail=b'// Report-only lossless encoding.'+target.read_bytes().split(b'// Report-only lossless encoding.',1)[1]
target.write_bytes(prefix+tail)
assert target.read_bytes().startswith(prefix)
meta=json.loads((out/'preparation.json').read_text(encoding='utf-8'))
meta['script_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
assert meta['unchanged_construction_prefix_sha256']==hashlib.sha256(prefix).hexdigest()
(out/'preparation.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')

# Slice: checkpoint and manual action only; keep both state records <=50 lines.
state=root/'PROJECT_STATE.yaml'
shutil.copyfile(state,out/'PROJECT_STATE.before.yaml')
raw=state.read_bytes().decode('utf-8')
lines=raw.splitlines(keepends=True)
for i,line in enumerate(lines):
    end='\r\n' if line.endswith('\r\n') else '\n'
    if line.startswith('next_safe_action:'):
        lines[i]='next_safe_action: Phase1_only_Figma_attempt18_return43790_exceeds20480_provider_canvas_not_committed_lossless_report_only_recovery_prepared_fresh_attempt19_approval_needed_notice_discovery8_input_bounded_review_PASS_no_application_or_integrated_acceptance'+end
    elif line.startswith('  figma_calls:'):
        lines[i]='  figma_calls: D075_B01_attempt18_INVALID_ARGUMENT_return43790_exceeds20480_provider_canvas_not_committed_safeToRetryWithoutCanvasRead_true_no_IDs_or_previews_October_attempts18_conservative_metered15_actual_balance_unknown_permission_consumed_no_retry_output/research/b01-directory-call18-2026-10-08/receipt.json'+end
    elif line.startswith('    compatibility:'):
        lines[i]=line.rstrip('\r\n')+'_installed_notice_discovery8_input_bounded_accuracy_PASS394_own_files_not_applicable_notice_completeness'+end
    elif line.startswith('    visual_definition:'):
        lines[i]=line.replace('52_directory_views2_components_prepared_unexecuted','52_directory_views2_components_attempt18_return_size_rejected_canvas_not_committed_compact_report_recovery_prepared')
state.write_bytes(''.join(lines).encode('utf-8'))
manual=root/'MANUAL_ACTIONS.md'
shutil.copyfile(manual,out/'MANUAL_ACTIONS.before.md')
raw=manual.read_bytes().decode('utf-8')
lines=raw.splitlines(keepends=True)
for i,line in enumerate(lines):
    if line.startswith('| B01; CB-06/CB-07 |'):
        end='\r\n' if line.endswith('\r\n') else '\n'
        lines[i]='| B01; CB-06/CB-07 | DOING | Execution approved; retry18 return-size failure; full pilot exit held | D-075 grants execution. Native PRE, six initial drafts and all twenty navigation views retain producer evidence. After reconnection the founder approved retry18 for52 views/two components. Provider INVALID_ARGUMENT reports43790-byte return exceeds20480; canvas edits were not committed; safeToRetryWithoutCanvasRead true. No IDs/previews. Permission consumed, no retry. October attempts18/conservative metered15; actual debit/balance unknown; zero spend. | [Exact attempt18 receipt](output/research/b01-directory-call18-2026-10-08/receipt.json), [prepared report-only recovery](output/research/b01-directory-return-recovery-2026-10-08/preparation.json) and [ledger](docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv). Approve one scoped attempt19: same52 views/two components, lossless compact return and two previews. No separate checking call needed. Full coverage, interactions, independent reviews, exports/restore, _EXIT and pilot acceptance remain; later batches gated. |'+end
manual.write_bytes(''.join(lines).encode('utf-8'))
for file in [state,manual]:assert len(file.read_text(encoding='utf-8').splitlines())<=50
print(json.dumps({'construction_bytes_unchanged':True,'final_script_sha256':meta['script_sha256'],'state_lines':len(state.read_text(encoding='utf-8').splitlines()),'manual_lines':len(manual.read_text(encoding='utf-8').splitlines()),'external_retry':False}))
