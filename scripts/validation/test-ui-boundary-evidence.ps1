#Requires -Version 7.0
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'ui-stream-mapping.ps1')
$root = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$design = Join-Path $root 'docs/phase-1-ui-reference-design'
$templates = @(Import-Csv (Join-Path $design 'reference-template-inventory.csv'))
$profiles = @(Import-Csv (Join-Path $design 'responsive-state-mode-matrix.csv'))
$context = [pscustomobject]@{
    Batches=@(Import-Csv (Join-Path $design 'design-batch-plan.csv')); Templates=$templates; Profiles=$profiles
    Mapping=(Get-UiStreamMapping @(Import-Csv (Join-Path $design 'component-primitives.csv')) $templates)
    Routes=@(Import-Csv (Join-Path $design 'foundation-route-coverage.csv')); Flows=@(Import-Csv (Join-Path $design 'foundation-flow-coverage.csv'))
    BoundaryAllocations=@(Import-Csv (Join-Path $design 'boundary-evidence-allocation.csv'))
}
$script:checks = 0
function Check([bool]$Condition, [string]$Name) { if (-not $Condition) { throw "FAIL $Name" }; $script:checks++ }
function Reject([scriptblock]$Action, [string]$Name) { $caught=$false; try { & $Action | Out-Null } catch { $caught=$true }; Check $caught $Name }
$frames = @(Get-UiBoundaryAllocations $context.BoundaryAllocations $context)
Check ($frames.Count -eq 8) 'eight destination triples'
Check (@($frames | ForEach-Object { $_.origin_streams.Split(';') }).Count -eq 12) 'twelve directed cases'
foreach ($index in 0..3) {
    Reject { Get-UiBoundaryAllocations @($context.BoundaryAllocations | Where-Object state_id -CNE $context.BoundaryAllocations[$index].state_id) $context } 'deleted allocation rejects'
}
foreach ($field in @('batch_id','template_id','state_id','destination_streams','origin_streams')) {
    $changed=@($context.BoundaryAllocations | ForEach-Object { $_.PSObject.Copy() }); $changed[0].$field='OTHER'
    Reject { Get-UiBoundaryAllocations $changed $context } "wrong allocation $field"
}
$originalProfiles = $context.Profiles
$context.Profiles=@($profiles | ForEach-Object { $_.PSObject.Copy() })
($context.Profiles | Where-Object profile_id -CEQ SP-NAVIGATION).required_values += ';STATE-BOUNDARY-TO-SEMANTIC'
Reject { Get-UiBoundaryAllocations $context.BoundaryAllocations $context } 'shared profile leakage rejected'
Reject { Get-UiFrameObligations $context.Mapping $templates $context.Profiles } 'ordinary axis generation rejects leaked states'
$context.Profiles=$originalProfiles
$ordinary=@(Get-UiFrameObligations $context.Mapping $templates $profiles)
Check ($ordinary.Count -eq 440 -and @($ordinary | Where-Object state_id -CMATCH '^STATE-(BOUNDARY|ANCESTOR)-TO-').Count -eq 0) 'ordinary obligations unchanged'
$rows=@();$annotations=@{}
foreach ($frame in $frames) {
    $template=@($templates | Where-Object template_id -CEQ $frame.template_id)[0]
    $id=$template.baseline_frame_name -replace '^HSD_UIR_B\d{2}_','HSD_UIR_B07_'
    $id=[regex]::Replace($id,'_STATE_.+?_VP_',('_'+$frame.state_id.Replace('-','_')+'_VP_'))
    $id=[regex]::Replace($id,'_STREAM_(HIGH|MEDIUM|LOW|SEMANTIC)_',('_STREAM_'+$frame.stream_id.Substring(2)+'_'))
    $vp=[regex]::Match($id,'_VP_(.+?)_MODE_').Groups[1].Value.Replace('_','-')
    $mode=[regex]::Match($id,'_MODE_(.+?)_STREAM_').Groups[1].Value.Replace('_','-')
    $row=[pscustomobject]@{ evidence_id=$id;batch_id='B07';template_id=$frame.template_id;state_id=$frame.state_id;stream_id=$frame.stream_id;instance_id='REF';viewport_id=('VP-'+$vp);mode_id=('MODE-'+$mode);revision='1';evidence_type='FRAME' }
    Check ($null -ne (Get-UiResolvedManifestRow $row $context)) 'allocation-only identity resolves'
    $wrong=$row.PSObject.Copy();$wrong.evidence_id=$id.Replace('B07','B01');$wrong.batch_id='B01'
    Check ($null -eq (Get-UiResolvedManifestRow $wrong $context)) 'wrong batch cannot resolve allocation-only state'
    $rows += $row
    $annotation=$row.PSObject.Copy();$annotation.evidence_id=$id.Replace('_V01','_V02');$annotation.revision='2';$annotation.evidence_type='ANNOTATION';$rows+=$annotation
    $cases=@($frame.origin_streams.Split(';') | ForEach-Object {
        $last=if($frame.stream_id -ceq 'S-SEMANTIC'){'no_canvas'}else{'add_canvas_after_announcement'}
        [pscustomobject]@{origin_stream=$_;destination_stream=$frame.stream_id;ordered_steps=@('remove_outgoing_shell','add_incoming_empty_status_restore_process','focus_visible_stream_control','announce_stream_location',$last);visible_destination_focus=$true;arrival_location='synthetic-arrival';announcement='synthetic stream and location';requested_location='synthetic-request';mapping_failure_reason='synthetic mapping failure';chosen_ancestor='synthetic-arrival';substitution_wording='synthetic substitution fixture'}
    })
    $annotations[$annotation.evidence_id]=[pscustomobject]@{cases=$cases}
}
Check (@(Get-UiBoundaryCoverageGaps B07 $rows $context $annotations).Count -eq 0) 'complete synthetic directed annotations'
Check (@(Get-UiBoundaryCoverageGaps B01 @() $context @{}).Count -eq 0) 'B01 inherits no boundary obligations'
Check (@(Get-UiBoundaryCoverageGaps B07 @($rows | Where-Object evidence_type -CNE FRAME) $context $annotations).Count -gt 0) 'missing distinct frames rejects'
Check (@(Get-UiBoundaryCoverageGaps B07 $rows $context @{}).Count -gt 0) 'missing directed annotation rejects'
$key=@($annotations.Keys)[0];$case=$annotations[$key].cases[0]
$steps=$case.ordered_steps;$case.ordered_steps=@('focus_visible_stream_control')
Check ('invalid-boundary-step-order' -cin @(Get-UiBoundaryCoverageGaps B07 $rows $context $annotations)) 'ordered steps cannot be omitted or reordered'
$case.ordered_steps=$steps;$case.visible_destination_focus=$false
Check ('missing-destination-visible-focus' -cin @(Get-UiBoundaryCoverageGaps B07 $rows $context $annotations)) 'visible focus required'
$case.visible_destination_focus=$true
$ancestorKey=@($annotations.Keys | Where-Object { $_ -clike '*STATE_ANCESTOR_*' })[0]
$annotations[$ancestorKey].cases[0].substitution_wording=''
Check ('missing-ancestor-substitution_wording' -cin @(Get-UiBoundaryCoverageGaps B07 $rows $context $annotations)) 'ancestor substitution wording required'
$semanticKey=@($annotations.Keys | Where-Object { $_ -clike '*STREAM_SEMANTIC*' })[0]
$originalCases=$annotations[$semanticKey].cases
$extra=$originalCases[0].PSObject.Copy();$extra.origin_stream='S-SEMANTIC';$extra.destination_stream='S-SEMANTIC'
$annotations[$semanticKey].cases=@($originalCases)+$extra
Check ('undeclared-boundary-direction' -cin @(Get-UiBoundaryCoverageGaps B07 $rows $context $annotations)) 'undeclared semantic-to-semantic case rejects'
$annotations[$semanticKey].cases=@($originalCases | Select-Object -Skip 1)
Check (@(Get-UiBoundaryCoverageGaps B07 $rows $context $annotations | Where-Object { $_ -clike 'missing-or-duplicate-directed-case:*' }).Count -gt 0) 'one directed origin cannot disappear'
$annotations[$semanticKey].cases=@($originalCases)+$originalCases[0]
Check (@(Get-UiBoundaryCoverageGaps B07 $rows $context $annotations | Where-Object { $_ -clike 'missing-or-duplicate-directed-case:*' }).Count -gt 0) 'duplicated directed case rejects'
$annotations[$semanticKey].cases=$originalCases
$changed=@($rows | ForEach-Object { $_.PSObject.Copy() });$changed[0].state_id='STATE-STREAM-CHANGED'
Check (@(Get-UiBoundaryCoverageGaps B07 $changed $context $annotations | Where-Object { $_ -clike 'missing-boundary-frame:*' }).Count -gt 0) 'same-shell frame cannot substitute for boundary frame'
$trace=@(Import-Csv (Join-Path $design 'traceability.csv'))
Assert-UiAcceptedStreamCopy $context.Batches $trace
Check $true 'accepted stream and reset copy stays authoritative'
$changed=@($context.Batches | ForEach-Object { $_.PSObject.Copy() })
($changed | Where-Object batch_id -CEQ B01).required_visual_evidence += '; exact public copy remains gated'
Reject { Assert-UiAcceptedStreamCopy $changed $trace } 'batch cannot reopen accepted copy'
$changedTrace=@($trace | ForEach-Object { $_.PSObject.Copy() })
($changedTrace | Where-Object trace_id -CEQ TR-REQ-103).required_future_evidence += '; exact public copy remains gated'
Reject { Assert-UiAcceptedStreamCopy $context.Batches $changedTrace } 'trace cannot reopen accepted copy'
Write-Output "RESULT=PASS CHECKS=$script:checks ORDINARY_FRAMES=$($ordinary.Count) BOUNDARY_FRAMES=$($frames.Count) DIRECTED_CASES=12"
