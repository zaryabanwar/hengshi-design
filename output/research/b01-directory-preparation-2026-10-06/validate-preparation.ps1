# Prepared identifier validation only; no Figma or application execution.
$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../../..')).Path
. (Join-Path $taskRoot 'scripts/validation/ui-stream-mapping.ps1')
$taskDesign = Join-Path $taskRoot 'docs/phase-1-ui-reference-design'
$taskTemplates = @(Import-Csv -LiteralPath (Join-Path $taskDesign 'reference-template-inventory.csv'))
$taskPrimitives = @(Import-Csv -LiteralPath (Join-Path $taskDesign 'component-primitives.csv'))
$taskProfiles = @(Import-Csv -LiteralPath (Join-Path $taskDesign 'responsive-state-mode-matrix.csv'))
$taskBatches = @(Import-Csv -LiteralPath (Join-Path $taskDesign 'design-batch-plan.csv'))
$taskContext = [pscustomobject]@{
    Batches=$taskBatches; Templates=$taskTemplates; Profiles=$taskProfiles
    Mapping=(Get-UiStreamMapping -Primitives $taskPrimitives -Templates $taskTemplates)
}
$taskInput = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'input.json') -Raw | ConvertFrom-Json
$taskRecords = @($taskInput.frames | ForEach-Object {
    $taskResolved = Get-UiResolvedEvidenceId -EvidenceId $_.name -StreamId $_.stream_id -Context $taskContext
    [pscustomobject]@{ name=$_.name; resolves_to_approved_context=($null -ne $taskResolved) }
})
$taskResult = [pscustomobject]@{
    prepared_only=$true; external_calls=0; frames=$taskRecords.Count
    all_frame_names_resolve=(@($taskRecords | Where-Object resolves_to_approved_context -EQ $false).Count -eq 0)
    records=$taskRecords
    evidence_limit='Identifiers only; no Figma composition, layout, keyboard, accessibility, runtime or pilot acceptance'
}
$taskTarget = Join-Path $PSScriptRoot 'identifier-observation.json'
if (Test-Path -LiteralPath $taskTarget) { throw 'Preserve existing observation' }
$taskResult | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $taskTarget -Encoding utf8
$taskResult | Select-Object prepared_only,external_calls,frames,all_frame_names_resolve | ConvertTo-Json
if (-not $taskResult.all_frame_names_resolve) { exit 1 }
