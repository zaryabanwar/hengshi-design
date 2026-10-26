Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
. (Join-Path $PSScriptRoot 'ui-stream-mapping.ps1')
$inventory = Get-Content (Join-Path $root 'docs/phase-1-foundation/06-canonical-route-inventory.json') -Raw | ConvertFrom-Json
$design = Join-Path $root 'docs/phase-1-ui-reference-design'
$routes = @(Import-Csv (Join-Path $design 'foundation-route-coverage.csv'))
$ux = @(Import-Csv (Join-Path $root 'docs/phase-1-ux-architecture/route-room-parity.csv'))
$batches = @(Import-Csv (Join-Path $design 'design-batch-plan.csv'))
$mapping = Get-UiStreamMapping -Primitives @(Import-Csv (Join-Path $design 'component-primitives.csv')) -Templates @(Import-Csv (Join-Path $design 'reference-template-inventory.csv'))
function Assert-PrivateDefinition([object]$Route) {
    if ($Route.path -cne '/privacy' -or $Route.activeSitemap -or $Route.releaseActivationStatus -cne 'inactive_no_approved_release' -or $Route.contentApprovalStatus -cne 'pending_specialist_evidence_and_founder_publication_approval') {
        throw 'Privacy definition must not activate or approve legal content'
    }
}
$privacy = @($inventory.routes | Where-Object id -CEQ 'ROUTE-PRIVACY')
if ($privacy.Count -ne 1) { throw 'Exactly one approved privacy route is required' }
Assert-PrivateDefinition $privacy[0]
$premature = $privacy[0].PSObject.Copy()
$premature.activeSitemap = $true
$rejected = $false
try { Assert-PrivateDefinition $premature } catch { $rejected = $true }
if (-not $rejected) { throw 'Premature sitemap activation was not rejected' }
$instance = @($routes | Where-Object route_id -CEQ 'ROUTE-PRIVACY')
if ($instance.Count -ne 1 -or @($ux | Where-Object { $_.route_id -ceq 'ROUTE-PRIVACY' -and $_.path -ceq '/privacy' }).Count -ne 1) { throw 'Privacy route parity is incomplete' }
if (($mapping.TemplatePresence[$instance[0].template_id] -join ';') -cne 'S-HIGH;S-LOW;S-MEDIUM;S-SEMANTIC') { throw 'Privacy instance must reach all four delivery streams' }
if (@($routes | Where-Object baseline_frame_name -CEQ $instance[0].baseline_frame_name).Count -ne 1) { throw 'Privacy evidence identity collides with another route' }
if (@($batches | Where-Object { $_.batch_id -ceq 'B02' -and 'ROUTE-PRIVACY' -cin $_.primary_source_ids.Split(';') }).Count -ne 1) { throw 'Privacy reference lacks its approved batch owner' }
if (@($inventory.routes | Where-Object { $_.id -ceq 'ROUTE-CREDITS' -and $_.path -ceq '/credits' -and $_.routeType -ceq 'attribution' }).Count -ne 1) { throw 'Attribution route was not preserved' }
function Assert-ResetContract([string]$Text) {
    foreach ($clause in @('visible accessible warning', 'Confirm reset or Cancel', 'no deletion before confirmation', 'Cancel preserves', 'does not change or reload', 'staff sign-out remains separate')) {
        if ($Text.IndexOf($clause, [StringComparison]::OrdinalIgnoreCase) -lt 0) { throw "Missing reset safeguard: $clause" }
    }
}
$recovery = Get-Content (Join-Path $root 'docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md') -Raw
$action = [regex]::Match($recovery, '(?m)^\| ACT-40 [^\r\n]+$')
if (-not $action.Success) { throw 'Preference-reset action definition is missing' }
Assert-ResetContract $action.Value
$flows = @(Import-Csv (Join-Path $design 'foundation-flow-coverage.csv'))
$resetFlow = @($flows | Where-Object source_id -CEQ 'ACT-40')
if ($resetFlow.Count -ne 1) { throw 'Preference-reset coverage is missing or duplicated' }
Assert-ResetContract $resetFlow[0].success_or_expected_state
$rejected = $false
try { Assert-ResetContract ($action.Value.Replace('no deletion before confirmation', '')) } catch { $rejected = $true }
if (-not $rejected) { throw 'Removing the confirmation safeguard was not rejected' }
$profiles = @(Import-Csv (Join-Path $design 'responsive-state-mode-matrix.csv'))
$returnProfile = @($profiles | Where-Object profile_id -CEQ 'SP-RETURN-VISIT')[0]
foreach ($state in @('STATE-PREFERENCE-RESET-PENDING', 'STATE-PREFERENCE-RESET-CANCELLED', 'STATE-PREFERENCE-CLEARED')) {
    if ($state -cnotin $returnProfile.required_values.Split(';') -or $state -cnotin $returnProfile.critical_distinct_frame_values.Split(';')) { throw "Reset outcome lacks distinct required evidence: $state" }
}
$srs = Get-Content (Join-Path $root 'docs/active/Hengshi_Design_SRS_v3.md') -Raw
function Assert-RecoveryRequirement([string]$Text, [string]$Id, [string[]]$Clauses) {
    $row = [regex]::Match($Text, ('(?m)^\| ' + [regex]::Escape($Id) + ' \|(?<body>[^|]+)\|'))
    if (-not $row.Success) { throw "Missing requirement: $Id" }
    foreach ($clause in $Clauses) { if (-not $row.Groups['body'].Value.Contains($clause)) { throw "Missing recovery safeguard: $Id $clause" } }
}
Assert-RecoveryRequirement $srs 'FR-3D-017' @('destination shell', 'offer stream reselection', 'absent/erased')
Assert-RecoveryRequirement $srs 'FR-3D-018' @('retain the prior in-force stream', 'verified client reason', 'Never silently substitute')
Assert-RecoveryRequirement $srs 'FR-3D-019' @('no deletion before confirmation', 'without verification', 'Staff sign-out remains separate')
$rejected = $false
try { Assert-RecoveryRequirement ($srs.Replace('retain the prior in-force stream', '')) 'FR-3D-018' @('retain the prior in-force stream') } catch { $rejected = $true }
if (-not $rejected) { throw 'Silent capability substitution safeguard removal accepted' }
Write-Output 'RESULT=PASS privacy definition and warn-confirm-cancel-reset safeguards; premature publication and unconfirmed clearing definitions rejected'
