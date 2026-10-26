# Local preparation only. Resolve names with the existing approved mapping; no Figma call.
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../../..')).Path
. (Join-Path $repoRoot 'scripts/validation/ui-stream-mapping.ps1')
$designRoot = Join-Path $repoRoot 'docs/phase-1-ui-reference-design'
$coveragePath = Join-Path $repoRoot 'output/research/b01-coverage-preparation-2026-10-06/coverage-preparation.json'
$coverage = Get-Content -LiteralPath $coveragePath -Raw | ConvertFrom-Json
$templates = @(Import-Csv -LiteralPath (Join-Path $designRoot 'reference-template-inventory.csv'))
$primitives = @(Import-Csv -LiteralPath (Join-Path $designRoot 'component-primitives.csv'))
$profiles = @(Import-Csv -LiteralPath (Join-Path $designRoot 'responsive-state-mode-matrix.csv'))
$batches = @(Import-Csv -LiteralPath (Join-Path $designRoot 'design-batch-plan.csv'))
$context = [pscustomobject]@{
    Batches=$batches; Templates=$templates; Profiles=$profiles
    Mapping=(Get-UiStreamMapping -Primitives $primitives -Templates $templates)
}
$copyRelativePath = 'docs/phase-1-ui-reference-design/accessibility/UG-3_CONTROL_COPY_PROPOSAL.md'
$copyText = Get-Content -LiteralPath (Join-Path $repoRoot $copyRelativePath) -Raw
function Get-AcceptedCopy([string]$ContextName) {
    $matchingLines = @($copyText -split '\r?\n' | Where-Object {
        $_.StartsWith('| ' + $ContextName + ' | ',[StringComparison]::Ordinal)
    })
    if ($matchingLines.Count -ne 1) { throw "Unresolved accepted copy context: $ContextName" }
    $cell = $matchingLines[0].Split('|')[2].Trim()
    $match = [regex]::Match($cell,'^“(?<copy>.+)”(?: — target `/privacy`)?$')
    if (-not $match.Success) { throw "Unexpected copy syntax: $ContextName" }
    $match.Groups['copy'].Value
}
$peerMatch = [regex]::Match($copyText,'Proposed persistent peer explanation: \*\*“(?<copy>.+?)”\*\*')
if (-not $peerMatch.Success) { throw 'Unresolved accepted peer explanation' }
$copy = [ordered]@{
    legend=(Get-AcceptedCopy 'Legend / group accessible name')
    apply=(Get-AcceptedCopy 'Apply visible label and accessible name')
    advisement=(Get-AcceptedCopy 'Persistent advance advisement, before Apply')
    peer_explanation=$peerMatch.Groups['copy'].Value
    privacy=(Get-AcceptedCopy 'Privacy link visible/accessibility name')
    'STATE-STREAM-CHANGED'=(Get-AcceptedCopy 'Changed selection, same shell')
    'STATE-PREFERENCE-WRITE-FAILED'=(Get-AcceptedCopy 'Preference write failed, after session application')
    'STATE-PREFERENCE-READ-FAILED'=(Get-AcceptedCopy 'Preference read failed, destination shell')
}
$labels = @(
    [pscustomobject]@{id='S-HIGH';label='Detailed 3D'},
    [pscustomobject]@{id='S-MEDIUM';label='Balanced 3D'},
    [pscustomobject]@{id='S-LOW';label='Simplified 3D'},
    [pscustomobject]@{id='S-SEMANTIC';label='Quick Access'}
)
foreach ($label in $labels) {
    if ($copyText -notmatch ('\|\s*\d+\s*\|\s*' + [regex]::Escape($label.id) + '\s*\|\s*' + [regex]::Escape($label.label) + '\s*\|')) {
        throw 'Label does not resolve to accepted order table'
    }
}
$navFocus = @($coverage.candidate_stream_focus_frames | Where-Object template_id -CEQ 'TPL-GLOBAL-NAVIGATION')
$held = @($navFocus | Where-Object state_id -CEQ 'STATE-STREAM-CEILING-REFUSED' | ForEach-Object {
    [pscustomobject]@{name=$_.name;status='TODO';reason='Requires a coherent synthetic capability/prior-stream fixture and established reason under D-057; this preparation does not invent device facts or claim this required focus is discharged.'}
})
$frames = @($navFocus | Where-Object state_id -CNE 'STATE-STREAM-CEILING-REFUSED' | ForEach-Object {
    [pscustomobject]@{name=$_.name;state_id=$_.state_id;stream_id=$_.stream_id;width=320}
})
$controls = @($frames | ForEach-Object {
    $streamIndex = [array]::IndexOf(@($labels.id),$_.stream_id)
    if ($streamIndex -lt 0) { throw 'Unresolved control stream' }
    [pscustomobject]@{
        state_id=$_.state_id;stream_id=$_.stream_id
        selected_stream_id=if ($_.state_id -ceq 'STATE-OPEN') { $labels[($streamIndex+1)%4].id } else { $_.stream_id }
    }
})
$frames += @($frames | Where-Object state_id -CEQ 'STATE-OPEN' | ForEach-Object {
    [pscustomobject]@{name=$_.name.Replace('_VP_320_','_VP_DESKTOP_');state_id=$_.state_id;stream_id=$_.stream_id;width=1440}
})
foreach ($frame in $frames) {
    if ($null -eq (Get-UiResolvedEvidenceId -EvidenceId $frame.name -StreamId $frame.stream_id -Context $context)) {
        throw "Prepared identity does not resolve to approved context: $($frame.name)"
    }
}
if ($frames.Count -ne 20 -or $controls.Count -ne 16 -or $held.Count -ne 4) { throw 'Unexpected navigation scope' }
$sourceRelativePath = 'docs/phase-1-ui-reference-production/scripts/b01-navigation-stream-states.js'
$source = Get-Content -LiteralPath (Join-Path $repoRoot $sourceRelativePath) -Raw
$marker = '/*B01_NAVIGATION_INPUTS*/ null'
if ([regex]::Matches($source,[regex]::Escape($marker)).Count -ne 1) { throw 'Ambiguous script input marker' }
$inputDefinition = [ordered]@{
    product='Hengshi Design v1'; fileKey='GOmLP6Cv96l768ueSrZ5Dg'
    componentSetName='PRIM-001 / Delivery stream control / B01 v1'
    fixture='Synthetic capability fixture: all four choices are available. This does not assert any actual client device capability or automatic initial selection.'
    labels=$labels;copy=$copy;controls=$controls;frames=$frames;held=$held
}
$prepared = $source.Replace($marker,($inputDefinition | ConvertTo-Json -Depth 8 -Compress))
$outputDirectory = Join-Path $repoRoot 'output/research/b01-navigation-preparation-2026-10-06'
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
$callPath = Join-Path $outputDirectory 'figma-call.js'
$prepared | Set-Content -LiteralPath $callPath -Encoding utf8NoBOM
$sourcePaths = @($sourceRelativePath,$copyRelativePath,
    'docs/phase-1-ui-reference-production/scripts/b01-prepare-navigation.ps1',
    'output/research/b01-coverage-preparation-2026-10-06/coverage-preparation.json',
    'docs/phase-1-ui-reference-design/reference-template-inventory.csv',
    'docs/phase-1-ui-reference-design/component-primitives.csv',
    'docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv',
    'docs/phase-1-ui-reference-design/design-batch-plan.csv','scripts/validation/ui-stream-mapping.ps1')
$receipt = [ordered]@{
    product='Hengshi Design v1';status='TODO';date='2026-10-06'
    purpose='Prepared local B01 navigation composition; not executed or accepted'
    prepared_call_sha256=(Get-FileHash -LiteralPath $callPath -Algorithm SHA256).Hash.ToLowerInvariant()
    external_calls=0;expected_reference_frames=20;expected_local_control_variants=16
    expected_spacing_variables=9;all_frame_names_resolve_to_approved_context=$true
    input=$inputDefinition
    source_hashes=@($sourcePaths | ForEach-Object {
        [pscustomobject]@{path=$_;sha256=(Get-FileHash -LiteralPath (Join-Path $repoRoot $_) -Algorithm SHA256).Hash.ToLowerInvariant()}
    })
    limitations='Names/copy resolution and syntax are preparation checks only. Actual creation, layout, text bounds, screenshots, interactions, full B01 coverage, independent review, EXIT and acceptance remain unproven. No application change or external library/font/provider/sharing operation.'
}
$receipt | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $outputDirectory 'preparation.json') -Encoding utf8NoBOM
[pscustomobject]@{status='TODO';prepared_script=$callPath;frames=$frames.Count;variants=$controls.Count;held=$held.Count;external_calls=0;B01_complete=$false} | ConvertTo-Json
