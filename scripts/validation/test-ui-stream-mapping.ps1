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
$profiles = @(Import-Csv (Join-Path $design 'responsive-state-mode-matrix.csv'))
$frames = @(Get-UiFrameObligations -Mapping $mapping -Templates $templates -Profiles $profiles)
$keys = @($frames | ForEach-Object { "$($_.template_id)|$($_.state_id)|$($_.stream_id)" })
Check (@($keys | Sort-Object -Unique -CaseSensitive).Count -eq $keys.Count) 'baseline and critical state duplicates collapse to one obligation'
foreach ($t in $templates) {
    if ($t.template_id -cin $staff) {
        $owned = @($frames | Where-Object template_id -CEQ $t.template_id)
        Check ($owned.Count -eq 1 -and $owned[0].stream_id -ceq 'STREAM-SCOPE-EXCLUDED') ("staff baseline evidence: " + $t.template_id)
        continue
    }
    foreach ($state in @('STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED')) {
        foreach ($stream in $mapping.TemplatePresence[$t.template_id]) {
            Check ("$($t.template_id)|$state|$stream" -cin $keys) ("required state frame: $($t.template_id) $state $stream")
        }
    }
}
Check (@($frames | Where-Object template_id -CEQ 'TPL-BOOKING-QUALIFICATION').Count -eq 12) 'booking has baseline plus two critical states in all four streams'
foreach ($state in @('STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED')) {
    $changed = Copy-Rows $profiles
    $booking = $changed | Where-Object profile_id -CEQ 'SP-BOOKING'
    $booking.critical_distinct_frame_values = @($booking.critical_distinct_frame_values.Split(';') | Where-Object { $_ -cne $state }) -join ';'
    Reject { Get-UiFrameObligations -Mapping $mapping -Templates $templates -Profiles $changed } 'Missing critical stream state' "required-only $state must fail"
    $booking.required_values = @($booking.required_values.Split(';') | Where-Object { $_ -cne $state }) -join ';'
    Reject { Get-UiFrameObligations -Mapping $mapping -Templates $templates -Profiles $changed } 'Missing required stream state' "removed $state must fail"
}
$changed = @($profiles | Where-Object profile_id -CNE 'DS-S-MEDIUM')
Reject { Get-UiFrameObligations -Mapping $mapping -Templates $templates -Profiles $changed } 'Missing stream profile' 'stream evidence definitions cannot disappear'
$changed = Copy-Rows $profiles
($changed | Where-Object profile_id -CEQ 'SP-BOOKING').critical_distinct_frame_values += ';STATE-INVENTED'
Reject { Get-UiFrameObligations -Mapping $mapping -Templates $templates -Profiles $changed } 'Critical state is not required' 'unknown critical state cannot produce evidence'
# Guard the named anatomy, current/pending distinction, and visible-before-Apply advisement.
# Mutations run through the shared entry point used by both package validators.
foreach ($hostId in @('PRIM-001', 'PRIM-042', 'PRIM-043', 'PRIM-044')) {
    foreach ($column in @('required_anatomy', 'transactional_or_content_states', 'responsive_and_mode_obligations', 'implementation_evidence_expectations')) {
        $row = $primitives | Where-Object primitive_id -CEQ $hostId
        $tokens = @($row.$column.Split(';') | Where-Object { $_ -cmatch '^(delivery stream control$|stream (?!change announced)|four native stream |separate always-present Apply |persistent visible stream |stream-in-force$|stream-pending$|checked stream |above-ceiling stream |Apply accessible |Stream control review |Stream advisement review )' })
        Check ($tokens.Count -gt 0) "$hostId has explicit $column contract"
        foreach ($token in $tokens) {
            $changed = Copy-Rows $primitives
            $target = $changed | Where-Object primitive_id -CEQ $hostId
            $target.$column = @($target.$column.Split(';') | Where-Object { $_ -cne $token }) -join ';'
            Reject { Get-UiStreamMapping -Primitives $changed -Templates $templates } 'Stream control contract missing' "reject missing ${hostId}:${column}:$token"
        }
    }
    $changed = Copy-Rows $primitives
    ($changed | Where-Object primitive_id -CEQ $hostId).transactional_or_content_states += ';stream-selected'
    Reject { Get-UiStreamMapping -Primitives $changed -Templates $templates } 'Ambiguous stream-selected state' "reject ambiguous selected state on $hostId"
    Reject { Assert-UiStreamControlContract -Primitives @($primitives | Where-Object primitive_id -CNE $hostId) } 'Missing or duplicate stream control host' "required control host $hostId cannot disappear"
}
$styleGuide = Get-Content -Raw (Join-Path $root 'docs/active/3D_Mega_Menu_Style_Guide_v2.md')
Assert-UiStreamStyleGuideContract -Text $styleGuide
Check $true 'style-guide stream-control contract'
foreach ($phrase in @('four native radio inputs', 'always-present Apply', 'in-force stream', 'pending selection', 'checked state', 'blur, arrow movement or timeout', 'native Enter submission', 'inside the fieldset', 'DOM reading order', 'both the group and the Apply button', 'hover-only', 'same wording in every stream')) {
    $changedText = $styleGuide.Replace($phrase, 'REMOVED-CONTRACT')
    Reject { Assert-UiStreamStyleGuideContract -Text $changedText } 'Stream style-guide contract missing' "style guide rejects removed $phrase"
}
Reject { Assert-UiStreamStyleGuideContract -Text ($styleGuide.Replace('#### 8.2.4 ', '#### 8.2.9 ')) } 'Missing stream control style-guide section' 'control contract cannot be supplied by another section'
foreach ($level in 1..4) {
    $relocated = $styleGuide.Replace('**Control model — normative', (('#' * $level) + " Unrelated contract`n`n**Control model — normative"))
    Reject { Assert-UiStreamStyleGuideContract -Text $relocated } 'Stream style-guide contract missing' "contract moved outside section by heading level $level"
}
$srs = Get-Content -Raw (Join-Path $root 'docs/active/Hengshi_Design_SRS_v3.md')
Assert-UiStreamRequirementsContract -Text $srs
Check $true 'SRS stream requirements match approved control behavior'
foreach ($phrase in @('present and keyboard operable in every stream', 'four native radio inputs', 'always-present Apply', 'change only the checked state', 'without applying a stream', 'applies only after explicit Apply activation', 'never applies on focus', 'disabled with a textual reason', 'reports the in-force stream', 'checked radio reports the pending selection', 'in-force value remains unchanged', 'Apply has a distinct accessible name', 'persistent visible text inside the fieldset', 'both DOM reading order and visual order', 'associated with both the group and the Apply button', 'not tooltip, title', 'same wording in every stream', 'while preserving the current location')) {
    Reject { Assert-UiStreamRequirementsContract -Text ($srs.Replace($phrase, 'REMOVED-CONTRACT')) } 'Stream requirement contract missing' "SRS rejects missing $phrase"
}
foreach ($id in @('FR-3D-014', 'NFR-A11Y-004')) {
    $row = [regex]::Match($srs, ('(?m)^\| ' + $id + ' \|[^\r\n]+')).Value
    Reject { Assert-UiStreamRequirementsContract -Text ($srs.Replace($row, '')) } 'Missing or duplicate stream requirement' "SRS rejects missing $id"
    Reject { Assert-UiStreamRequirementsContract -Text ($srs + "`n" + $row) } 'Missing or duplicate stream requirement' "SRS rejects duplicate $id"
    $moved = $srs.Replace($row, ($row.Replace("| $id |", "| $id | Description removed |")))
    Reject { Assert-UiStreamRequirementsContract -Text $moved } 'Stream requirement contract missing' "SRS ignores contract relocated to status cell for $id"
}
$uxStates = Get-Content -Raw (Join-Path $root 'docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md')
Assert-UiStreamActionContract -Text $uxStates
Check $true 'ACT-09 distinguishes pending selection from successful Apply'
$actionRow = [regex]::Match($uxStates, '(?m)^\| ACT-09 [^\r\n]+').Value
foreach ($phrase in @('only after explicit Apply activation', 'reports the new in-force stream', 'location preserved', 'native radio anatomy and advance advisement', 'checked radio reports the pending selection', 'still reports the in-force stream', 'change only checked state', 'no stream application, reload, transition', 'never apply on focus', 'requested stream above the WebGL ceiling', 'remain on the prior stream and say why', 'the ceiling is stated, not silently substituted', 'the choice still applies for the session', 'no content loss in any stream')) {
    $changed = $uxStates.Replace($actionRow, $actionRow.Replace($phrase, 'REMOVED-CONTRACT'))
    Reject { Assert-UiStreamActionContract -Text $changed } 'Stream action contract missing' "ACT-09 rejects omitted $phrase"
}
Reject { Assert-UiStreamActionContract -Text ($uxStates.Replace($actionRow, '')) } 'Missing or duplicate stream action' 'ACT-09 cannot disappear'
Reject { Assert-UiStreamActionContract -Text ($uxStates + "`n" + $actionRow) } 'Missing or duplicate stream action' 'ACT-09 cannot be duplicated'
$actionCells = $actionRow.Split('|')
foreach ($pair in @(@(2,3), @(2,4), @(3,4))) {
    $cells = $actionCells.Clone()
    $cells[$pair[0]], $cells[$pair[1]] = $cells[$pair[1]], $cells[$pair[0]]
    Reject { Assert-UiStreamActionContract -Text ($uxStates.Replace($actionRow, ($cells -join '|'))) } 'Stream action contract missing' "ACT-09 rejects swapped cells $pair"
}
$uxTests = Get-Content -Raw (Join-Path $root 'docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md')
Assert-UiStreamAcceptanceContract -Text $uxTests
Check $true 'UXTEST-046 specifies approved controls and preserves existing journeys'
$acceptanceRow = [regex]::Match($uxTests, '(?m)^\| UXTEST-046 \|[^\r\n]+').Value
foreach ($phrase in @('four native radio inputs', 'always-present Apply', 'reports the in-force stream', 'checked radio reports the pending selection', 'Apply has a distinct accessible name', 'change only the checked state', 'no stream application, reload, transition', 'only explicit Apply activation', 'Fail if focus, selection, blur', 'persistent visible text inside the fieldset', 'both DOM reading order and visual order', 'associated with both the group and the Apply button', 'not tooltip, title', 'same wording in every stream', 'applying the pending selection re-enters', 'screen-magnifier users at 400% zoom', 'Streams above the capability ceiling', 'reachable and operable in all four streams', 'preserves scroll, open panel, and route', 'outgoing shell leaves the accessibility tree', 'a held slot, a verified email', 'change is refused and explained', 'any automatic canvas entry')) {
    $changed = $uxTests.Replace($acceptanceRow, $acceptanceRow.Replace($phrase, 'REMOVED-CONTRACT'))
    Reject { Assert-UiStreamAcceptanceContract -Text $changed } 'Stream acceptance contract missing' "UXTEST-046 rejects omitted $phrase"
}
Reject { Assert-UiStreamAcceptanceContract -Text ($uxTests.Replace($acceptanceRow, '')) } 'Missing or duplicate stream acceptance test' 'UXTEST-046 cannot disappear'
Reject { Assert-UiStreamAcceptanceContract -Text ($uxTests + "`n" + $acceptanceRow) } 'Missing or duplicate stream acceptance test' 'UXTEST-046 cannot be duplicated'
$acceptanceCells = $acceptanceRow.Split('|')
$acceptanceCells[2], $acceptanceCells[3] = $acceptanceCells[3], $acceptanceCells[2]
Reject { Assert-UiStreamAcceptanceContract -Text ($uxTests.Replace($acceptanceRow, ($acceptanceCells -join '|'))) } 'Stream acceptance contract missing' 'UXTEST-046 criteria cannot be supplied by its title'
$flows = @(Import-Csv (Join-Path $design 'foundation-flow-coverage.csv'))
Assert-UiStreamCoverageContract -Flows $flows
Check $true 'COV-ACT-09 matches explicit Apply and truthful recovery'
$coverageMutations = @{
    success_or_expected_state = @('only after explicit Apply', 'new in-force stream', 'only after a successful preference write', 'announced politely without interrupting', 'within a shell', 'across the semantic boundary', 'scroll, open panel and route preserved', 'control anatomy and advance advisement')
    error_empty_pending_state = @('checked radio reports the pending selection', 'still reports the in-force stream', 'selection changes only checked state', 'no accessibility-tree change beyond checked state', 'never apply on focus', 'change failure; preference write failure')
    recovery = @('never silently substituted', 'retain the prior stream', 'choice applies for the current session', 'explained without blocking', 'no destination and no content is lost')
}
foreach ($column in $coverageMutations.Keys) {
    foreach ($phrase in $coverageMutations[$column]) {
        $changed = Copy-Rows $flows
        $target = $changed | Where-Object coverage_id -CEQ 'COV-ACT-09'
        $target.$column = $target.$column.Replace($phrase, 'REMOVED-CONTRACT')
        Reject { Assert-UiStreamCoverageContract -Flows $changed } 'Stream coverage contract missing' "COV-ACT-09 rejects omitted $phrase"
    }
}
$coverage = $flows | Where-Object coverage_id -CEQ 'COV-ACT-09'
Reject { Assert-UiStreamCoverageContract -Flows @($flows | Where-Object coverage_id -CNE 'COV-ACT-09') } 'Missing or duplicate stream coverage' 'COV-ACT-09 cannot disappear'
Reject { Assert-UiStreamCoverageContract -Flows ($flows + $coverage) } 'Missing or duplicate stream coverage' 'COV-ACT-09 cannot be duplicated'
$changed = Copy-Rows $flows
$target = $changed | Where-Object coverage_id -CEQ 'COV-ACT-09'
$target.success_or_expected_state, $target.error_empty_pending_state = $target.error_empty_pending_state, $target.success_or_expected_state
Reject { Assert-UiStreamCoverageContract -Flows $changed } 'Stream coverage contract missing' 'COV-ACT-09 cannot swap success and pending'
Write-Output "RESULT=PASS CHECKS=$script:checks FRAME_OBLIGATIONS=$($frames.Count)"
