#Requires -Version 7.0
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'ui-stream-mapping.ps1')
$root = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$design = Join-Path $root 'docs/phase-1-ui-reference-design'
$primitives = @(Import-Csv (Join-Path $design 'component-primitives.csv'))
$templates = @(Import-Csv (Join-Path $design 'reference-template-inventory.csv'))
$mapping = Get-UiStreamMapping -Primitives $primitives -Templates $templates
$script:checks = 0
function Check([bool]$Condition, [string]$Name) {
    if (-not $Condition) { throw "FAIL: $Name" }
    $script:checks++
}
function Reject([scriptblock]$Action, [string]$Message, [string]$Name) {
    $caught = $null
    try { & $Action | Out-Null } catch { $caught = $_.Exception.Message }
    Check ($null -ne $caught -and $caught.Contains($Message)) $Name
}
function Copy-Rows([object[]]$Rows) { @($Rows | ForEach-Object { $_.PSObject.Copy() }) }
$all = 'S-HIGH;S-LOW;S-MEDIUM;S-SEMANTIC'
$world = @('TPL-FIRST-VISIT', 'TPL-RETURN-VISIT', 'TPL-WORLD-SHELL', 'TPL-WORLD-HUD')
$staff = @('TPL-STAFF-AUTH', 'TPL-STAFF-QUEUE', 'TPL-STAFF-WORK-DETAIL', 'TPL-PUBLICATION-EDITOR', 'TPL-PUBLICATION-REVIEW-RELEASE', 'TPL-AUDIT-INSPECTION')
Check ($templates.Count -eq 40) 'review the explicit expected mapping when screen inventory changes'
foreach ($t in $templates) {
    $expected = if ($t.template_id -cin $world) { 'S-HIGH;S-LOW;S-MEDIUM' } elseif ($t.template_id -cin $staff) { '' } else { $all }
    Check (($mapping.TemplatePresence[$t.template_id] -join ';') -ceq $expected) ("live screen: " + $t.template_id)
    $scope = if ($t.template_id -cin $staff) { 'STREAM-SCOPE-EXCLUDED' } else { 'PUBLIC' }
    Check ($mapping.TemplateScope[$t.template_id] -ceq $scope) ("scope: " + $t.template_id)
    if ($t.template_id -cin $staff) {
        Check ($t.baseline_frame_name -cmatch '_SCOPE_EXCLUDED_V\d{2}$') ("staff frame scope: " + $t.template_id)
        Check ((@(Get-UiEvidenceScopes -Mapping $mapping -TemplateId $t.template_id) -join ';') -ceq 'STREAM-SCOPE-EXCLUDED') ("staff evidence still required: " + $t.template_id)
    }
}
foreach ($route in @(Import-Csv (Join-Path $design 'foundation-route-coverage.csv'))) {
    Check ($mapping.TemplatePresence.ContainsKey($route.template_id) -and ($mapping.TemplatePresence[$route.template_id] -join ';') -ceq $all) ("public route: " + $route.route_id)
}
foreach ($flow in @(Import-Csv (Join-Path $design 'foundation-flow-coverage.csv'))) {
    foreach ($id in $flow.template_ids.Split(';')) {
        Check ($mapping.TemplatePresence.ContainsKey($id)) ("flow reference: " + $flow.coverage_id)
    }
}
# A required content component can restrict its screen, but a shared component cannot expand it.
$changed = Copy-Rows $primitives
($changed | Where-Object primitive_id -CEQ 'PRIM-059').stream_presence = 'S-SEMANTIC'
$limited = Get-UiStreamMapping -Primitives $changed -Templates $templates
Check (($limited.TemplatePresence['TPL-WORK-DETAIL'] -join ';') -ceq 'S-SEMANTIC') 'required content restriction reaches its consumer'
Check (($limited.TemplatePresence['TPL-PUBLIC-HOME'] -join ';') -ceq $all) 'unrelated screens retain their streams'

$changedTemplates = Copy-Rows $templates
($changedTemplates | Where-Object template_id -CEQ 'TPL-WORLD-HUD').primitive_dependencies += ';PRIM-062'
$expanded = Get-UiStreamMapping -Primitives $primitives -Templates $changedTemplates
Check (($expanded.TemplatePresence['TPL-WORLD-HUD'] -join ';') -ceq 'S-HIGH;S-LOW;S-MEDIUM') 'adding shared content cannot add semantic HUD'

foreach ($hostId in @('PRIM-042', 'PRIM-043', 'PRIM-044')) {
    $changed = Copy-Rows $primitives
    ($changed | Where-Object primitive_id -CEQ $hostId).stream_presence = $all
    Reject { Get-UiStreamMapping -Primitives $changed -Templates $templates } 'Host stream contract mismatch' "reject semantic claim on $hostId"
}
foreach ($bad in @('', 'S-HIGH;S-HIGH', 'S-UNKNOWN', 'S-SEMANTIC;S-HIGH', 'S-HIGH;STREAM-SCOPE-EXCLUDED')) {
    $changed = Copy-Rows $primitives
    ($changed | Where-Object primitive_id -CEQ 'PRIM-057').stream_presence = $bad
    Reject { Get-UiStreamMapping -Primitives $changed -Templates $templates } 'Invalid stream declaration' "reject malformed presence: $bad"
}
foreach ($case in @(
    @{ deps = 'PRIM-057;PRIM-058'; error = 'Missing host' },
    @{ deps = 'PRIM-001;PRIM-999'; error = 'Unresolved dependency' },
    @{ deps = 'PRIM-001;PRIM-001'; error = 'Duplicate dependency' },
    @{ deps = 'PRIM-001;PRIM-046'; error = 'Mixed public and staff hosts' },
    @{ deps = 'PRIM-001;PRIM-048'; error = 'Excluded component on public template' }
)) {
    $fixture = [pscustomobject]@{template_id='TPL-TEST'; primitive_dependencies=$case.deps}
    Reject { Get-UiStreamMapping -Primitives $primitives -Templates @($fixture) } $case.error $case.error
}
Reject { Get-UiStreamMapping -Primitives ($primitives + $primitives[0]) -Templates $templates } 'duplicate primitive ID' 'duplicate primitive identity'
Reject { Get-UiStreamMapping -Primitives $primitives -Templates ($templates + $templates[0]) } 'duplicate template ID' 'duplicate screen identity'
$changed = Copy-Rows $primitives
$changed[0].primitive_id = 'prim-001'
Reject { Get-UiStreamMapping -Primitives $changed -Templates $templates } 'primitive ID' 'case-sensitive primitive identity'
Reject { Get-UiEvidenceScopes -Mapping $mapping -TemplateId 'TPL-UNKNOWN' } 'Unknown template' 'unknown evidence scope'
$changed = Copy-Rows $primitives
($changed | Where-Object primitive_id -CEQ 'PRIM-057').stream_presence = 'S-SEMANTIC'
Reject { Get-UiStreamMapping -Primitives $changed -Templates $templates } 'No compatible stream' 'incompatible required content fails closed'

$batch = Import-Csv (Join-Path $root 'docs/phase-1-ui-reference-production/batch-production-plan.csv') | Where-Object batch_id -CEQ 'B08'
Check ($batch.stream_disposition -ceq 'S-HIGH=not_present;S-LOW=not_present;S-MEDIUM=not_present;S-SEMANTIC=not_present') 'staff batch has no public stream obligation'
Write-Output "RESULT=PASS CHECKS=$script:checks"
