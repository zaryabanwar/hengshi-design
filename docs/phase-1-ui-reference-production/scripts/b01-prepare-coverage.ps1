# Prepare B01 from accepted tables. No Figma, application or acceptance writes.
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../../..')).Path
$designRoot = Join-Path $repoRoot 'docs/phase-1-ui-reference-design'
$productionRoot = Join-Path $repoRoot 'docs/phase-1-ui-reference-production'
$outputDirectory = Join-Path $repoRoot 'output/research/b01-coverage-preparation-2026-10-06'
. (Join-Path $repoRoot 'scripts/validation/ui-stream-mapping.ps1')
$templates = @(Import-Csv -LiteralPath (Join-Path $designRoot 'reference-template-inventory.csv'))
$profiles = @(Import-Csv -LiteralPath (Join-Path $designRoot 'responsive-state-mode-matrix.csv'))
$primitives = @(Import-Csv -LiteralPath (Join-Path $designRoot 'component-primitives.csv'))
$batches = @(Import-Csv -LiteralPath (Join-Path $designRoot 'design-batch-plan.csv'))
$b01 = @($batches | Where-Object batch_id -CEQ 'B01')
if ($b01.Count -ne 1) { throw 'B01 must resolve uniquely' }
$templateIds = @($b01[0].primary_template_ids.Split(';') | Where-Object { $_ })
$b01Templates = @($templates | Where-Object template_id -CIn $templateIds)
if ($b01Templates.Count -ne $templateIds.Count) { throw 'Missing primary template' }
$mapping = Get-UiStreamMapping -Primitives $primitives -Templates $templates
$allStreamFocus = @(Get-UiFrameObligations -Mapping $mapping -Templates $templates -Profiles $profiles)
$b01StreamFocus = @($allStreamFocus | Where-Object template_id -CIn $templateIds)
$repairPath = Join-Path $repoRoot 'output/research/b01-text-reflow-2026-10-06/retry-11/provider-result.json'
$repair = Get-Content -LiteralPath $repairPath -Raw | ConvertFrom-Json
if ($repair.isError -ne $false) { throw 'Repair success is not established' }
$repairText = @($repair.content | Where-Object type -CEQ 'text')
if ($repairText.Count -ne 1) { throw 'Ambiguous repair result' }
$repairResult = $repairText[0].text | ConvertFrom-Json
if ($repairResult.B01Complete -ne $false -or @($repairResult.frames).Count -ne 6) {
    throw 'Unexpected draft checkpoint; inspect instead of guessing'
}
$screenshotRelativePath = 'output/research/b01-text-reflow-2026-10-06/screenshot-12/result.json'
$screenshotPath = Join-Path $repoRoot $screenshotRelativePath
$screenshot = $null
if (Test-Path -LiteralPath $screenshotPath) {
    $screenshot = Get-Content -LiteralPath $screenshotPath -Raw | ConvertFrom-Json
    $imagePath = Join-Path (Split-Path $screenshotPath) $screenshot.image
    if ($screenshot.isError -ne $false -or $screenshot.nodeId -cne '14:124' -or
        (Get-FileHash -LiteralPath $imagePath -Algorithm SHA256).Hash.ToLowerInvariant() -cne $screenshot.sha256) {
        throw 'Narrow recovery screenshot receipt does not match its image'
    }
}
$primitiveIds = @($b01Templates | ForEach-Object { $_.primitive_dependencies.Split(';') } |
    Where-Object { $_ } | Sort-Object -Unique -CaseSensitive)
$b01Primitives = @($primitives | Where-Object primitive_id -CIn $primitiveIds)
if ($b01Primitives.Count -ne $primitiveIds.Count) { throw 'Unresolved primitive dependency' }
$profileBindings = @()
foreach ($template in $b01Templates) {
    $ownProfiles = @($template.state_profile,$template.viewport_profile,$template.mode_profile,
        $template.browser_profile,$template.time_limit_branch)
    foreach ($stream in @(Get-UiEvidenceScopes -Mapping $mapping -TemplateId $template.template_id)) {
        if ($stream -cne 'STREAM-SCOPE-EXCLUDED') { $ownProfiles += 'DS-' + $stream }
    }
    foreach ($profileId in @($ownProfiles | Sort-Object -Unique -CaseSensitive)) {
        $owned = @($profiles | Where-Object profile_id -CEQ $profileId)
        if ($owned.Count -ne 1) { throw "Unresolved profile: $profileId" }
        $profileBindings += [pscustomobject]@{
            template_id = $template.template_id
            profile = $owned[0]
            evidence_status = 'TODO'
            evidence_limit = 'Preparation only; profile text or a frame label is not proof of its represented behavior'
        }
    }
}
$candidateStreamFrames = @()
foreach ($focus in $b01StreamFocus) {
    $template = @($b01Templates | Where-Object template_id -CEQ $focus.template_id)[0]
    $baseline = [regex]::Match($template.baseline_frame_name,'_VP_(?<vp>.+?)_MODE_(?<mode>.+?)_STREAM_')
    if (-not $baseline.Success) { throw 'Unexpected baseline naming; do not invent identity' }
    $candidateStreamFrames += [pscustomobject]@{
        name = 'HSD_UIR_B01_' + $focus.template_id.Replace('-','_') + '_REF_' +
            $focus.state_id.Replace('-','_') + '_VP_' + $baseline.Groups['vp'].Value +
            '_MODE_' + $baseline.Groups['mode'].Value + '_' +
            $focus.stream_id.Replace('S-','STREAM_') + '_V01'
        template_id = $focus.template_id
        state_id = $focus.state_id
        stream_id = $focus.stream_id
        viewport_id = 'VP-' + $baseline.Groups['vp'].Value.Replace('_','-')
        mode_id = 'MODE-' + $baseline.Groups['mode'].Value.Replace('_','-')
        evidence_status = 'TODO'
        purpose = 'Candidate for one required stream/state focus, not complete template/profile coverage'
    }
}
$sourcePaths = @(
    'docs/phase-1-ui-reference-design/design-batch-plan.csv',
    'docs/phase-1-ui-reference-design/reference-template-inventory.csv',
    'docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv',
    'docs/phase-1-ui-reference-design/component-primitives.csv',
    'docs/phase-1-ui-reference-production/batch-production-plan.csv',
    'scripts/validation/ui-stream-mapping.ps1',
    'docs/phase-1-ui-reference-production/scripts/b01-prepare-coverage.ps1',
    'output/research/b01-text-reflow-2026-10-06/retry-11/provider-result.json'
)
if ($screenshot) { $sourcePaths += $screenshotRelativePath }
$sources = @($sourcePaths | ForEach-Object {
    [pscustomobject]@{ path=$_; sha256=(Get-FileHash -LiteralPath (Join-Path $repoRoot $_) -Algorithm SHA256).Hash.ToLowerInvariant() }
})
$plan = [ordered]@{
    product = 'Hengshi Design v1'
    date = '2026-10-06'
    status = 'DOING'
    scope = 'Local B01 coverage preparation; no external execution or acceptance'
    execution_authority = 'D-075 permits B01 execution; each actual Figma call still requires fresh immediate approval'
    sources = $sources
    batch = $b01[0]
    templates = $b01Templates
    primitives = $b01Primitives
    profile_bindings = $profileBindings
    required_stream_state_focus = $b01StreamFocus
    candidate_stream_focus_frames = $candidateStreamFrames
    observed_draft_checkpoint = [ordered]@{
        frames = @($repairResult.frames)
        returned_preview_count = @($repair.content | Where-Object type -CEQ 'image').Count
        B01_complete = $false
        narrow_recovery_screenshot = $screenshot
        inspection_hold = if ($screenshot) { 'All six initial draft views inspected; full contracted coverage and independent review remain held.' } else { 'Narrow recovery 14:124 has no returned preview; separate browser attachment failure is recorded in retry-11/browser-inspection.json' }
        coverage = 'Not adjudicated or accepted. Six unvalidated drafts are not a substitute for full contracted evidence.'
    }
    preparation_findings = @(
        'Current narrow drafts are 390px; the required complete VP-320 references remain to be authored.',
        'Current previewed stream selector uses Quick Access; all four required stream/state focuses remain to be evidenced.',
        'Required profiles retain every state, viewport and mode value. Stream-focus candidates are only one subset, not a complete frame count or Cartesian-product instruction.',
        'All contracted primitive dependencies are carried. World HUD/content is explicitly outside B01 under its batch row; no B01 evidence discharges B07.',
        'Light/dark/forced-color recovery, navigation disclosure, search outcomes, semantics and interaction/prototype evidence remain required.',
        'Platform/browser behavior, forced-colors, screen reader, physical mobile and accessibility claims require their contracted evidence; Figma labels or screenshots cannot establish them.',
        'Use D-057 accepted stream copy. Other exact legal/security/provider facts remain held; references must identify synthetic fixtures.',
        'Actual component creation, tokens, full frame composition, inspection, exports, independent reviews, restore/EXIT and founder pilot acceptance are not performed by this preparation.'
    )
}
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
$planPath = Join-Path $outputDirectory 'coverage-preparation.json'
$plan | ConvertTo-Json -Depth 16 | Set-Content -LiteralPath $planPath -Encoding utf8NoBOM
[pscustomobject]@{
    output = $planPath
    primary_templates = $b01Templates.Count
    primitive_dependencies = $b01Primitives.Count
    profile_bindings = $profileBindings.Count
    required_stream_state_focus = $b01StreamFocus.Count
    candidate_names_unique = @($candidateStreamFrames.name | Sort-Object -Unique -CaseSensitive).Count -eq $candidateStreamFrames.Count
    external_calls = 0
    B01_complete = $false
} | ConvertTo-Json -Depth 3
