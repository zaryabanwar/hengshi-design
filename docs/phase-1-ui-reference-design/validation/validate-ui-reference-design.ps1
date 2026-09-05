[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:PassCount = 0
$script:Failures = [System.Collections.Generic.List[string]]::new()

function Add-Pass {
    param([string]$Name, [string]$Detail)
    $script:PassCount++
    Write-Output ("PASS [{0}] {1}" -f $Name, $Detail)
}

function Add-Fail {
    param([string]$Name, [string]$Detail)
    $script:Failures.Add(("FAIL [{0}] {1}" -f $Name, $Detail))
    Write-Output ("FAIL [{0}] {1}" -f $Name, $Detail)
}

function Assert-True {
    param([bool]$Condition, [string]$Name, [string]$PassDetail, [string]$FailDetail)
    if ($Condition) {
        Add-Pass $Name $PassDetail
    }
    else {
        Add-Fail $Name $FailDetail
    }
}

function Assert-ExactSet {
    param([object[]]$Expected, [object[]]$Actual, [string]$Name)
    $expectedSet = @($Expected | ForEach-Object { [string]$_ } | Sort-Object -Unique)
    $actualSet = @($Actual | ForEach-Object { [string]$_ } | Sort-Object -Unique)
    $difference = @()
    if ($expectedSet.Count -gt 0 -or $actualSet.Count -gt 0) {
        $difference = @(Compare-Object -ReferenceObject $expectedSet -DifferenceObject $actualSet -CaseSensitive)
    }
    if ($difference.Count -eq 0 -and $expectedSet.Count -eq $actualSet.Count) {
        Add-Pass $Name ("exact set count={0}" -f $actualSet.Count)
    }
    else {
        $missing = @($expectedSet | Where-Object { $_ -cnotin $actualSet })
        $unexpected = @($actualSet | Where-Object { $_ -cnotin $expectedSet })
        Add-Fail $Name ("missing={0}; unexpected={1}" -f ($missing -join ';'), ($unexpected -join ';'))
    }
}

function Assert-Unique {
    param([object[]]$Values, [string]$Name)
    $all = @($Values | ForEach-Object { [string]$_ })
    $unique = @($all | Sort-Object -Unique)
    Assert-True ($all.Count -eq $unique.Count) $Name ("unique count={0}" -f $all.Count) ("duplicates found; total={0}; unique={1}" -f $all.Count, $unique.Count)
}

function Split-List {
    param([AllowEmptyString()][string]$Value)
    if ([string]::IsNullOrWhiteSpace($Value)) { return @() }
    return @($Value -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
}

function Assert-RequiredColumns {
    param([object[]]$Rows, [string[]]$Columns, [string]$Name)
    if ($Rows.Count -eq 0) {
        Add-Fail $Name 'CSV has no data rows'
        return
    }
    $actual = @($Rows[0].PSObject.Properties.Name)
    $missing = @($Columns | Where-Object { $_ -cnotin $actual })
    Assert-True ($missing.Count -eq 0) $Name ("parsed rows={0}; required columns={1}" -f $Rows.Count, $Columns.Count) ("missing columns={0}" -f ($missing -join ';'))
}

function Assert-NonEmptyFields {
    param([object[]]$Rows, [string[]]$Fields, [string]$Name)
    $bad = [System.Collections.Generic.List[string]]::new()
    foreach ($row in $Rows) {
        $recordId = if ($row.PSObject.Properties['route_id']) { $row.route_id } elseif ($row.PSObject.Properties['coverage_id']) { $row.coverage_id } elseif ($row.PSObject.Properties['template_id']) { $row.template_id } elseif ($row.PSObject.Properties['profile_id']) { $row.profile_id } elseif ($row.PSObject.Properties['batch_id']) { $row.batch_id } elseif ($row.PSObject.Properties['trace_id']) { $row.trace_id } elseif ($row.PSObject.Properties['primitive_id']) { $row.primitive_id } else { '<row>' }
        foreach ($field in $Fields) {
            if (-not $row.PSObject.Properties[$field] -or [string]::IsNullOrWhiteSpace([string]$row.$field)) {
                $bad.Add(("{0}:{1}" -f $recordId, $field))
            }
        }
    }
    Assert-True ($bad.Count -eq 0) $Name ("all required fields populated across {0} rows" -f $Rows.Count) ("blank fields={0}" -f ($bad -join ';'))
}

$packageRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $packageRoot '..\..')).Path

Write-Output 'UI_REFERENCE_DESIGN_VALIDATION'
Write-Output 'EVIDENCE_DATE=2026-09-03'
Write-Output ("PACKAGE_ROOT={0}" -f $packageRoot)

$requiredFiles = @(
    'README.md',
    'UI_REFERENCE_DESIGN_CONTRACT.md',
    'foundation-route-coverage.csv',
    'foundation-flow-coverage.csv',
    'reference-template-inventory.csv',
    'responsive-state-mode-matrix.csv',
    'design-batch-plan.csv',
    'DESIGN_SYSTEM_IMPLICATIONS.md',
    'component-primitives.csv',
    'traceability.csv',
    'validation/validate-ui-reference-design.ps1',
    'validation/validation-report.md',
    'producer-inspection.md'
)
$missingFiles = @($requiredFiles | Where-Object { -not (Test-Path -LiteralPath (Join-Path $packageRoot $_) -PathType Leaf) })
Assert-True ($missingFiles.Count -eq 0) 'package-files' ("required files present={0}" -f $requiredFiles.Count) ("missing={0}" -f ($missingFiles -join ';'))
if ($missingFiles.Count -gt 0) {
    Write-Output ("RESULT=FAIL PASS_COUNT={0} FAIL_COUNT={1}" -f $script:PassCount, $script:Failures.Count)
    exit 1
}

$allowedExtensions = @('.md', '.csv', '.ps1')
$packageFiles = @(Get-ChildItem -LiteralPath $packageRoot -Recurse -File)
$badExtensions = @($packageFiles | Where-Object { $_.Extension.ToLowerInvariant() -cnotin $allowedExtensions } | ForEach-Object FullName)
Assert-True ($badExtensions.Count -eq 0) 'package-file-types' 'only Markdown CSV and PowerShell files present' ("prohibited files={0}" -f ($badExtensions -join ';'))

$packageCsvFiles = @(Get-ChildItem -LiteralPath $packageRoot -Recurse -File -Filter '*.csv' | Sort-Object FullName)
$packageJsonFiles = @(Get-ChildItem -LiteralPath $packageRoot -Recurse -File -Filter '*.json' | Sort-Object FullName)
$parsedCsv = @{}
foreach ($file in $packageCsvFiles) {
    try {
        $parsedCsv[$file.Name] = @(Import-Csv -LiteralPath $file.FullName)
        Add-Pass ("csv-parse-{0}" -f $file.Name) ("rows={0}" -f $parsedCsv[$file.Name].Count)
    }
    catch {
        Add-Fail ("csv-parse-{0}" -f $file.Name) $_.Exception.Message
    }
}
foreach ($file in $packageJsonFiles) {
    try {
        $null = Get-Content -Raw -LiteralPath $file.FullName | ConvertFrom-Json
        Add-Pass ("json-parse-{0}" -f $file.Name) 'parsed'
    }
    catch {
        Add-Fail ("json-parse-{0}" -f $file.Name) $_.Exception.Message
    }
}
Assert-True ($packageJsonFiles.Count -eq 0) 'package-json-scope' 'no package JSON files are present' ("unexpected package JSON files={0}" -f $packageJsonFiles.Count)

$sourceCsvRelative = @(
    'docs/phase-1-foundation/07-decision-requirement-traceability.csv',
    'docs/phase-1-brand-strategy/07-traceability.csv',
    'docs/phase-1-brand-identity/traceability.csv',
    'docs/phase-1-ux-architecture/route-room-parity.csv',
    'docs/phase-1-ux-architecture/excluded-surfaces.csv',
    'docs/phase-1-ux-architecture/wayfinding-release-map.csv',
    'docs/phase-1-ux-architecture/traceability.csv'
)
$sourceCsv = @{}
foreach ($relative in $sourceCsvRelative) {
    $path = Join-Path $repoRoot $relative
    try {
        $sourceCsv[$relative] = @(Import-Csv -LiteralPath $path)
        Add-Pass ("source-csv-{0}" -f ([IO.Path]::GetFileName($relative))) ("rows={0}" -f $sourceCsv[$relative].Count)
    }
    catch {
        Add-Fail ("source-csv-{0}" -f ([IO.Path]::GetFileName($relative))) $_.Exception.Message
    }
}

$sourceRoutePath = Join-Path $repoRoot 'docs/phase-1-foundation/06-canonical-route-inventory.json'
try {
    $sourceRouteJson = Get-Content -Raw -LiteralPath $sourceRoutePath | ConvertFrom-Json
    Add-Pass 'source-route-json' ("routes={0}; exclusions={1}" -f $sourceRouteJson.routes.Count, $sourceRouteJson.excludedSurfaces.Count)
}
catch {
    Add-Fail 'source-route-json' $_.Exception.Message
    Write-Output ("RESULT=FAIL PASS_COUNT={0} FAIL_COUNT={1}" -f $script:PassCount, $script:Failures.Count)
    exit 1
}

$routes = @($parsedCsv['foundation-route-coverage.csv'])
$flows = @($parsedCsv['foundation-flow-coverage.csv'])
$templates = @($parsedCsv['reference-template-inventory.csv'])
$matrix = @($parsedCsv['responsive-state-mode-matrix.csv'])
$batches = @($parsedCsv['design-batch-plan.csv'])
$trace = @($parsedCsv['traceability.csv'])
$primitives = @($parsedCsv['component-primitives.csv'])

Assert-RequiredColumns $routes @('route_id','path','route_family','route_instance_id','template_id','baseline_frame_name','state_profile','viewport_profile','mode_profile','instance_evidence','semantic_quick_access','optional_immersive_representation','primary_next_actions','content_or_policy_gate','activation_status','browser_profile','time_limit_branch') 'route-columns'
Assert-RequiredColumns $flows @('coverage_id','coverage_kind','source_id','flow_family','action_name','template_ids','state_profile','viewport_profile','mode_profile','success_or_expected_state','error_empty_pending_state','recovery','linked_tests','gate','browser_profile','time_limit_branch') 'flow-columns'
Assert-RequiredColumns $templates @('template_id','template_name','surface_kind','reuse_scope','representative_instance','state_profile','viewport_profile','mode_profile','baseline_frame_name','minimum_reference_evidence','interaction_focus_notes','content_stress_case','primitive_dependencies','gated_inputs','browser_profile','time_limit_branch') 'template-columns'
Assert-RequiredColumns $matrix @('profile_id','dimension','applies_to','required_values','minimum_evidence','critical_distinct_frame_values','annotation_requirements','exception_rule','browser_profile','time_limit_branch') 'matrix-columns'
Assert-RequiredColumns $batches @('batch_id','sequence','batch_name','objective','primary_template_ids','supporting_template_ids','primary_source_ids','supporting_or_final_evidence_ids','hard_prerequisite_batch_ids','prerequisites_and_held_inputs','required_visual_evidence','validation_and_review','stop_condition','status','browser_profile_id','time_limit_branch_ids') 'batch-columns'
Assert-RequiredColumns $trace @('trace_id','source_id','source_type','source_artifact','contract_artifacts','contract_records','required_future_evidence','status_or_gate') 'trace-columns'
Assert-RequiredColumns $primitives @('primitive_id','primitive_name','primitive_category','interaction_class','required_anatomy','required_variants','pseudo_states','transactional_or_content_states','state_redundancy','responsive_and_mode_obligations','reference_templates_or_flows','source_decisions','source_requirements','source_ux_tests','source_actions','implementation_evidence_expectations','gated_facts') 'primitive-columns'

Assert-NonEmptyFields $routes @('route_id','path','route_instance_id','template_id','baseline_frame_name','state_profile','viewport_profile','mode_profile','instance_evidence','content_or_policy_gate','activation_status','browser_profile','time_limit_branch') 'route-required-fields'
Assert-NonEmptyFields $flows @('coverage_id','coverage_kind','source_id','flow_family','action_name','template_ids','state_profile','viewport_profile','mode_profile','success_or_expected_state','error_empty_pending_state','recovery','linked_tests','gate','browser_profile','time_limit_branch') 'flow-required-fields'
Assert-NonEmptyFields $templates @('template_id','template_name','surface_kind','reuse_scope','representative_instance','state_profile','viewport_profile','mode_profile','baseline_frame_name','minimum_reference_evidence','interaction_focus_notes','content_stress_case','primitive_dependencies','gated_inputs','browser_profile','time_limit_branch') 'template-required-fields'
Assert-NonEmptyFields $matrix @('profile_id','dimension','applies_to','required_values','minimum_evidence','critical_distinct_frame_values','annotation_requirements','exception_rule','browser_profile','time_limit_branch') 'matrix-required-fields'
Assert-NonEmptyFields $batches @('batch_id','sequence','batch_name','objective','prerequisites_and_held_inputs','required_visual_evidence','validation_and_review','stop_condition','status','browser_profile_id','time_limit_branch_ids') 'batch-required-fields'
Assert-NonEmptyFields $trace @('trace_id','source_id','source_type','source_artifact','contract_artifacts','contract_records','required_future_evidence','status_or_gate') 'trace-required-fields'
Assert-NonEmptyFields $primitives @('primitive_id','primitive_name','primitive_category','required_anatomy','responsive_and_mode_obligations','implementation_evidence_expectations','gated_facts') 'primitive-required-fields'

$sourceRoutes = @($sourceRouteJson.routes)
$sourceRouteRoom = @($sourceCsv['docs/phase-1-ux-architecture/route-room-parity.csv'])
Assert-True ($sourceRoutes.Count -eq 33) 'source-route-count' 'source canonical routes=33' ("actual={0}" -f $sourceRoutes.Count)
Assert-True ($routes.Count -eq 33) 'route-coverage-count' 'covered routes=33' ("actual={0}" -f $routes.Count)
Assert-Unique $routes.route_id 'route-id-uniqueness'
Assert-Unique $routes.path 'route-path-uniqueness'
Assert-Unique $routes.route_instance_id 'route-instance-uniqueness'
Assert-ExactSet ($sourceRoutes | ForEach-Object { $_.id }) $routes.route_id 'route-id-parity-json'
Assert-ExactSet ($sourceRoutes | ForEach-Object { "{0}|{1}" -f $_.id, $_.path }) ($routes | ForEach-Object { "{0}|{1}" -f $_.route_id, $_.path }) 'route-id-path-parity-json'
Assert-ExactSet ($sourceRouteRoom | ForEach-Object { "{0}|{1}" -f $_.route_id, $_.path }) ($routes | ForEach-Object { "{0}|{1}" -f $_.route_id, $_.path }) 'route-id-path-parity-ux'
$industries = @($routes | Where-Object { $_.route_id -ceq 'ROUTE-INDUSTRIES' -and $_.path -ceq '/industries' })
Assert-True ($industries.Count -eq 1) 'd025-industries-retained' 'ROUTE-INDUSTRIES=/industries appears exactly once' 'D-025 retained route is absent or duplicated'
$allowedRouteStatuses = @('planned_inactive_not_published','planned_pattern_inactive_not_published')
$badRouteStatus = @($routes | Where-Object { $_.activation_status -cnotin $allowedRouteStatuses })
Assert-True ($badRouteStatus.Count -eq 0) 'route-inactive-status' 'all concrete and pattern route references are inactive and not published' ("unexpected statuses on {0} rows" -f $badRouteStatus.Count)

$sourceExclusions = @($sourceCsv['docs/phase-1-ux-architecture/excluded-surfaces.csv'])
$sourceJsonExclusions = @($sourceRouteJson.excludedSurfaces)
$flowExclusions = @($flows | Where-Object { $_.coverage_kind -ceq 'exclusion' })
Assert-True ($sourceExclusions.Count -eq 9 -and $flowExclusions.Count -eq 9) 'exclusion-count' 'source and contract exclusions=9' ("source={0}; contract={1}" -f $sourceExclusions.Count, $flowExclusions.Count)
Assert-ExactSet $sourceExclusions.exclusion_id $flowExclusions.source_id 'exclusion-id-parity'
Assert-ExactSet ($sourceJsonExclusions | ForEach-Object id) $sourceExclusions.exclusion_id 'exclusion-json-csv-id-parity'
$blankExclusionPatterns = @($sourceJsonExclusions | Where-Object { [string]::IsNullOrWhiteSpace([string]$_.pattern) }) + @($sourceExclusions | Where-Object { [string]::IsNullOrWhiteSpace([string]$_.pattern) })
Assert-True ($blankExclusionPatterns.Count -eq 0) 'exclusion-pattern-presence' 'JSON and UX exclusion authorities retain explicit patterns' ("blank pattern rows={0}" -f $blankExclusionPatterns.Count)

$sourceWayfinding = @($sourceCsv['docs/phase-1-ux-architecture/wayfinding-release-map.csv'])
$flowWayfinding = @($flows | Where-Object { $_.coverage_kind -ceq 'wayfinding' })
Assert-True ($sourceWayfinding.Count -eq 15 -and $flowWayfinding.Count -eq 15) 'wayfinding-count' 'source and contract wayfinding records=15' ("source={0}; contract={1}" -f $sourceWayfinding.Count, $flowWayfinding.Count)
Assert-Unique $sourceWayfinding.room_id 'wayfinding-source-id-uniqueness'
Assert-ExactSet $sourceWayfinding.room_id $flowWayfinding.source_id 'wayfinding-id-parity'
$wayfindingRouteGaps = @($sourceWayfinding | Where-Object { $_.route_id -cnotin $routes.route_id -or $_.canonical_path -cnotin $routes.path })
Assert-True ($wayfindingRouteGaps.Count -eq 0) 'wayfinding-route-resolution' 'all wayfinding route IDs and canonical paths resolve' ("unresolved rows={0}" -f $wayfindingRouteGaps.Count)

$actionSourceText = Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md')
$sourceActions = @([regex]::Matches($actionSourceText, '\bACT-\d{2}\b') | ForEach-Object Value | Sort-Object -Unique)
$expectedActions = @(1..53 | ForEach-Object { 'ACT-{0:D2}' -f $_ })
$flowActions = @($flows | Where-Object { $_.coverage_kind -ceq 'action' })
Assert-ExactSet $expectedActions $sourceActions 'source-action-set'
Assert-ExactSet $expectedActions $flowActions.source_id 'action-coverage-set'
Assert-Unique $flowActions.source_id 'action-id-uniqueness'

$testSourceText = Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md')
$sourceTests = @([regex]::Matches($testSourceText, '\bUXTEST-\d{3}\b') | ForEach-Object Value | Sort-Object -Unique)
$expectedTests = @(1..45 | ForEach-Object { 'UXTEST-{0:D3}' -f $_ })
$traceTests = @($trace | Where-Object { $_.source_type -ceq 'ux_test' })
$linkedTests = @($flows | ForEach-Object { Split-List $_.linked_tests } | Sort-Object -Unique)
Assert-ExactSet $expectedTests $sourceTests 'source-ux-test-set'
Assert-ExactSet $expectedTests $traceTests.source_id 'trace-ux-test-set'
Assert-ExactSet $expectedTests $linkedTests 'flow-linked-ux-test-set'

$uxArchitectureText = Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/phase-1-ux-architecture/UX_ARCHITECTURE.md')
$sourceFlowText = Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/phase-1-ux-architecture/FLOWS.md')
$expectedJourneyIds = @('J-01','J-02','J-03','J-04','J-05','FV-01','RV-01')
$expectedFlowAndSubflowIds = @(
    'AF-01','AF-02',
    'BF-01','BF-01A','BF-01B','BF-01C','BF-01D','BF-01E',
    'CF-01','DF-01','PF-01',
    'SOF-01','SOF-01A','SOF-01B','SOF-01C','SOF-01D','SOF-01E','SOF-01F',
    'SOF-01G','SOF-01H','SOF-01I','SOF-01J','SOF-01K','SOF-01L','SOF-01M'
)
$sourceJourneyIds = @([regex]::Matches($uxArchitectureText, '\b(?:J-\d{2}|FV-\d{2}|RV-\d{2})\b') | ForEach-Object Value | Sort-Object -Unique)
$sourceFlowAndSubflowIds = @([regex]::Matches($sourceFlowText, '\b(?:AF-\d{2}|BF-\d{2}[A-Z]?|CF-\d{2}|DF-\d{2}|PF-\d{2}|SOF-\d{2}[A-Z]?)\b') | ForEach-Object Value | Sort-Object -Unique)
$acceptedExperienceIds = @($sourceJourneyIds + $sourceFlowAndSubflowIds | Sort-Object -Unique)
Assert-ExactSet $expectedJourneyIds $sourceJourneyIds 'source-journey-id-set'
Assert-ExactSet $expectedFlowAndSubflowIds $sourceFlowAndSubflowIds 'source-flow-subflow-id-set'
Assert-True ($acceptedExperienceIds.Count -eq 32) 'source-experience-id-count' 'accepted journey/flow/subflow IDs=32' ("actual={0}" -f $acceptedExperienceIds.Count)

$requiredFlowFamilies = @(
    'FLOW-NAVIGATION-SEARCH',
    'FLOW-FIRST-VISIT',
    'FLOW-RETURN-VISIT',
    'FLOW-WORLD-HUD-FALLBACK',
    'FLOW-AI',
    'FLOW-HUMAN-HANDOFF',
    'FLOW-MEDIA-OPT-IN',
    'FLOW-BOOKING-LINEAGE',
    'FLOW-CONTACT',
    'FLOW-STAFF-PUBLICATION-OPERATIONS',
    'FLOW-AUTH-SESSION-PERMISSION',
    'FLOW-ERROR-OFFLINE-RECOVERY'
)
$flowFamilies = @($flows | Where-Object { $_.coverage_kind -ceq 'flow_family' })
Assert-ExactSet $requiredFlowFamilies $flowFamilies.source_id 'required-flow-family-set'
Assert-True ($flows.Count -eq 89) 'flow-coverage-row-count' 'flow coverage rows=89' ("actual={0}" -f $flows.Count)
Assert-Unique $flows.coverage_id 'flow-coverage-id-uniqueness'

Assert-True ($templates.Count -eq 40) 'template-count' 'reusable templates=40' ("actual={0}" -f $templates.Count)
Assert-Unique $templates.template_id 'template-id-uniqueness'
Assert-Unique $matrix.profile_id 'profile-id-uniqueness'
Assert-True ($matrix.Count -eq 32) 'profile-count' 'viewport mode state browser and time-limit profiles=32' ("actual={0}" -f $matrix.Count)
$templateIds = @($templates.template_id)
$profileIds = @($matrix.profile_id)
$routeTemplateRefs = @($routes.template_id | Sort-Object -Unique)
$flowTemplateRefs = @($flows | ForEach-Object { Split-List $_.template_ids } | Sort-Object -Unique)
Assert-True ($routeTemplateRefs.Count -eq 19) 'route-template-ref-count' 'unique route template references=19' ("actual={0}" -f $routeTemplateRefs.Count)
Assert-True ($flowTemplateRefs.Count -eq 29) 'flow-template-ref-count' 'unique flow template references=29' ("actual={0}" -f $flowTemplateRefs.Count)
Assert-True (@($routeTemplateRefs | Where-Object { $_ -cnotin $templateIds }).Count -eq 0) 'route-template-resolution' 'all route template references resolve' 'one or more route template references are missing'
Assert-True (@($flowTemplateRefs | Where-Object { $_ -cnotin $templateIds }).Count -eq 0) 'flow-template-resolution' 'all flow template references resolve' 'one or more flow template references are missing'
Assert-ExactSet $templateIds (@($routeTemplateRefs + $flowTemplateRefs)) 'template-reference-completeness'

$profileRefGaps = [System.Collections.Generic.List[string]]::new()
foreach ($row in @($routes + $flows + $templates)) {
    foreach ($field in @('state_profile','viewport_profile','mode_profile')) {
        if ($row.$field -cnotin $profileIds) {
            $id = if ($row.PSObject.Properties['route_id']) { $row.route_id } elseif ($row.PSObject.Properties['coverage_id']) { $row.coverage_id } else { $row.template_id }
            $profileRefGaps.Add(("{0}:{1}={2}" -f $id, $field, $row.$field))
        }
    }
}
Assert-True ($profileRefGaps.Count -eq 0) 'profile-reference-resolution' 'all route flow and template profile references resolve' ("gaps={0}" -f ($profileRefGaps -join ';'))

$requiredViewports = @('VP-320','VP-NARROW','VP-LANDSCAPE','VP-TABLET','VP-DESKTOP','VP-WIDE','VP-ZOOM-400')
$viewportProfiles = @($matrix | Where-Object { $_.profile_id -like 'VP-*' })
$viewportFailures = @($viewportProfiles | Where-Object { $values = @(Split-List $_.required_values); @($requiredViewports | Where-Object { $_ -cnotin $values }).Count -gt 0 })
Assert-True ($viewportProfiles.Count -eq 4 -and $viewportFailures.Count -eq 0) 'required-viewports' 'all four viewport profiles include 320 narrow landscape tablet desktop wide and 400-percent reflow' ("profiles={0}; incomplete={1}" -f $viewportProfiles.Count, $viewportFailures.Count)

$requiredModes = @('MODE-STANDARD','MODE-REDUCED-MOTION','MODE-LOW-POWER','MODE-NON-WEBGL-QUICK-ACCESS','MODE-FORCED-COLORS','MODE-GRAYSCALE','MODE-UNAVAILABLE-FONT','MODE-UNAVAILABLE-IMAGE-ASSET','MODE-PRINT','MODE-KEYBOARD','MODE-SCREEN-READER')
$allModes = @($matrix | Where-Object { $_.profile_id -like 'MP-*' } | ForEach-Object { Split-List $_.required_values } | Sort-Object -Unique)
$publicModes = @($matrix | Where-Object { $_.profile_id -ceq 'MP-PUBLIC' } | ForEach-Object { Split-List $_.required_values })
Assert-ExactSet $requiredModes $allModes 'required-mode-union'
Assert-ExactSet $requiredModes $publicModes 'public-mode-completeness'

$requiredStateClasses = @('STATE-REST','STATE-LOADING','STATE-EMPTY','STATE-PENDING','STATE-SUCCESS','STATE-UNAVAILABLE','STATE-OFFLINE','STATE-ERROR','STATE-PERMISSION-DENIED','STATE-SESSION-EXPIRED','STATE-ASSET-FAILURE','STATE-CHECKSUM-MISMATCH','STATE-FOCUS')
$allStates = @($matrix | Where-Object { $_.profile_id -like 'SP-*' } | ForEach-Object { Split-List $_.required_values } | Sort-Object -Unique)
$missingStateClasses = @($requiredStateClasses | Where-Object { $_ -cnotin $allStates })
Assert-True ($missingStateClasses.Count -eq 0) 'required-state-classes' 'normal loading empty pending success degraded authorization recovery and focus classes are represented' ("missing={0}" -f ($missingStateClasses -join ';'))

$expectedBrowserProfile = 'BP-NFR-006'
$browserProfileRows = @($matrix | Where-Object { $_.dimension -ceq 'browser' })
Assert-True ($browserProfileRows.Count -eq 1 -and $browserProfileRows[0].profile_id -ceq $expectedBrowserProfile) 'nfr006-browser-profile-definition' 'one normative BP-NFR-006 browser profile is defined' ("browser rows={0}; ids={1}" -f $browserProfileRows.Count, (($browserProfileRows.profile_id | Sort-Object) -join ';'))
$browserMappingErrors = [System.Collections.Generic.List[string]]::new()
foreach ($row in @($routes + $flows + $templates + $matrix)) {
    $id = if ($row.PSObject.Properties['route_id']) { $row.route_id } elseif ($row.PSObject.Properties['coverage_id']) { $row.coverage_id } elseif ($row.PSObject.Properties['template_id']) { $row.template_id } else { $row.profile_id }
    if ($row.browser_profile -cne $expectedBrowserProfile) { $browserMappingErrors.Add(("{0}:{1}" -f $id, $row.browser_profile)) }
}
foreach ($batch in $batches) {
    if ($batch.browser_profile_id -cne $expectedBrowserProfile) { $browserMappingErrors.Add(("{0}:{1}" -f $batch.batch_id, $batch.browser_profile_id)) }
}
Assert-True ($browserMappingErrors.Count -eq 0) 'nfr006-browser-profile-mapping' 'all routes flows templates profiles and B01-B09 map directly to BP-NFR-006' ("mapping errors={0}" -f ($browserMappingErrors -join ';'))
$browserProfileText = (($browserProfileRows | ForEach-Object { $_.required_values + ' ' + $_.minimum_evidence + ' ' + $_.annotation_requirements + ' ' + $_.exception_rule }) -join ' ' -replace '\s+', ' ')
$browserContractComplete = (
    $browserProfileText -match '(?i)latest two stable release families' -and
    $browserProfileText -match '(?i)Chrome Edge Firefox and Safari' -and
    $browserProfileText -match '(?i)Safari on iOS 16\.4.*minimum legacy floor' -and
    $browserProfileText -match '(?i)dated later QA.*exact current stable versions|exact current stable versions.*dated later QA' -and
    $browserProfileText -match '(?i)mobile layout input virtual-keyboard and safe-area' -and
    $browserProfileText -match '(?i)below-floor and otherwise-unsupported recovery.*semantic Quick Access|semantic Quick Access.*below that floor or otherwise unsupported'
)
Assert-True $browserContractComplete 'nfr006-browser-profile-content' 'browser profile fixes current-two-stable families, Safari/iOS 16.4 floor, deferred dated versions, mobile evidence, and unsupported Quick Access' 'BP-NFR-006 content is incomplete'

$expectedTimeBranches = @('TL-REMOVABLE-ADJUSTABLE','TL-WARN-EXTEND','TL-EXCEPTION','TL-NOT-APPLICABLE')
$timeProfileRows = @($matrix | Where-Object { $_.dimension -ceq 'time_limit' })
Assert-ExactSet $expectedTimeBranches $timeProfileRows.profile_id 'wcag221-time-limit-profile-set'
$timeReferenceErrors = [System.Collections.Generic.List[string]]::new()
foreach ($row in @($routes + $flows + $templates + $matrix)) {
    $id = if ($row.PSObject.Properties['route_id']) { $row.route_id } elseif ($row.PSObject.Properties['coverage_id']) { $row.coverage_id } elseif ($row.PSObject.Properties['template_id']) { $row.template_id } else { $row.profile_id }
    if ($row.time_limit_branch -cnotin $expectedTimeBranches) { $timeReferenceErrors.Add(("{0}:{1}" -f $id, $row.time_limit_branch)) }
}
foreach ($batch in $batches) {
    foreach ($branch in @(Split-List $batch.time_limit_branch_ids)) {
        if ($branch -cnotin $expectedTimeBranches) { $timeReferenceErrors.Add(("{0}:{1}" -f $batch.batch_id, $branch)) }
    }
}
Assert-True ($timeReferenceErrors.Count -eq 0) 'wcag221-time-limit-reference-resolution' 'every route flow template profile and batch time-limit branch resolves' ("unresolved={0}" -f ($timeReferenceErrors -join ';'))

function Get-ExpectedTimeBranchForState {
    param([string]$StateProfile)
    if ($StateProfile -cin @('SP-FIRST-VISIT','SP-WORLD')) { return 'TL-REMOVABLE-ADJUSTABLE' }
    if ($StateProfile -cin @('SP-AI','SP-HANDOFF-MEDIA','SP-BOOKING','SP-AUTH','SP-STAFF-QUEUE','SP-STAFF-WORK','SP-PUBLICATION','SP-AUDIT','SP-SYSTEM-RECOVERY')) { return 'TL-WARN-EXTEND' }
    return 'TL-NOT-APPLICABLE'
}
$timeMappingErrors = [System.Collections.Generic.List[string]]::new()
foreach ($row in @($routes + $flows + $templates)) {
    $id = if ($row.PSObject.Properties['route_id']) { $row.route_id } elseif ($row.PSObject.Properties['coverage_id']) { $row.coverage_id } else { $row.template_id }
    $expected = Get-ExpectedTimeBranchForState $row.state_profile
    if ($row.time_limit_branch -cne $expected) { $timeMappingErrors.Add(("{0}:expected={1}:actual={2}" -f $id, $expected, $row.time_limit_branch)) }
}
Assert-True ($timeMappingErrors.Count -eq 0) 'wcag221-time-limit-record-mapping' 'all route flow and template branches match their accepted state profile' ("mapping errors={0}" -f ($timeMappingErrors -join ';'))

$expectedBatchTimeBranches = @{
    B01 = @('TL-WARN-EXTEND'); B02 = @('TL-NOT-APPLICABLE'); B03 = @('TL-NOT-APPLICABLE')
    B04 = @('TL-NOT-APPLICABLE'); B05 = @('TL-WARN-EXTEND'); B06 = @('TL-WARN-EXTEND')
    B07 = @('TL-REMOVABLE-ADJUSTABLE'); B08 = @('TL-WARN-EXTEND')
    B09 = @('TL-REMOVABLE-ADJUSTABLE','TL-WARN-EXTEND')
}
foreach ($batchId in @(1..9 | ForEach-Object { 'B{0:D2}' -f $_ })) {
    Assert-ExactSet $expectedBatchTimeBranches[$batchId] @(Split-List ($batches | Where-Object batch_id -ceq $batchId).time_limit_branch_ids) ("wcag221-batch-branch-{0}" -f $batchId)
}
$timeDefinitionText = (($timeProfileRows | ForEach-Object { $_.profile_id + ' ' + $_.required_values + ' ' + $_.minimum_evidence + ' ' + $_.annotation_requirements + ' ' + $_.exception_rule }) -join ' ' -replace '\s+', ' ')
$timeContractComplete = (
    $timeDefinitionText -match '(?i)turn off.*before.*adjust.*before start' -and
    $timeDefinitionText -match '(?i)at least 20 seconds before expiry' -and
    $timeDefinitionText -match '(?i)(at least 10x|at least ten times)' -and
    $timeDefinitionText -match '(?i)criterion-supported exception' -and
    $timeDefinitionText -match '(?i)permitted data and (the )?last authoritative state' -and
    $timeDefinitionText -match '(?i)accessible reauthentication' -and
    $timeDefinitionText -match '(?i)exact product duration remains gated'
)
Assert-True $timeContractComplete 'wcag221-time-limit-definition-content' 'all SC 2.2.1 alternatives, thresholds, preservation, reauthentication, and duration gate are explicit' 'time-limit profile language is incomplete'
$selectedExceptionRows = @($routes + $flows + $templates | Where-Object { $_.time_limit_branch -ceq 'TL-EXCEPTION' })
$selectedExceptionBatches = @($batches | Where-Object { 'TL-EXCEPTION' -cin @(Split-List $_.time_limit_branch_ids) })
Assert-True ($selectedExceptionRows.Count -eq 0 -and $selectedExceptionBatches.Count -eq 0) 'wcag221-no-undocumented-exception-selection' 'no current route flow template or batch selects TL-EXCEPTION' ("record selections={0}; batch selections={1}" -f $selectedExceptionRows.Count, $selectedExceptionBatches.Count)
$sourceTimingText = (($uxArchitectureText + "`n" + $actionSourceText) -replace '\s+', ' ')
Assert-True ($sourceTimingText -match '(?i)at least 20 seconds' -and $sourceTimingText -match '(?i)at least ten times' -and $sourceTimingText -match '(?i)accessible reauthentication') 'wcag221-accepted-source-parity' 'accepted UX source retains 20-second, ten-times, and accessible-reauthentication authority' 'accepted UX timing authority is incomplete'

$browserNegativeFixture = 'latest browsers; fallback if needed'
Assert-True (-not ($browserNegativeFixture -match '(?i)latest two stable release families' -and $browserNegativeFixture -match '(?i)Safari.*16\.4' -and $browserNegativeFixture -match '(?i)semantic Quick Access')) 'nfr006-negative-fixture' 'vague browser-support fixture is rejected' 'browser negative fixture unexpectedly satisfies the profile'
$timingNegativeFixture = 'TL-WARN-EXTEND warns before expiry and lets the user continue'
Assert-True (-not ($timingNegativeFixture -match '(?i)at least 20 seconds' -and $timingNegativeFixture -match '(?i)(at least 10x|at least ten times)')) 'wcag221-negative-fixture' 'threshold-free timeout fixture is rejected' 'timing negative fixture unexpectedly satisfies SC 2.2.1 thresholds'

Assert-Unique $routes.baseline_frame_name 'route-frame-name-uniqueness'
Assert-Unique $templates.baseline_frame_name 'template-frame-name-uniqueness'
$allFrameNames = @($routes.baseline_frame_name + $templates.baseline_frame_name)
Assert-Unique $allFrameNames 'all-frame-name-uniqueness'
$badFrameNames = @($allFrameNames | Where-Object { $_ -cnotmatch '^HSD_UIR_B\d{2}_[A-Z0-9_]+_V\d{2}$' })
Assert-True ($badFrameNames.Count -eq 0) 'frame-name-grammar' 'all baseline frame names follow the tool-neutral grammar' ("invalid={0}" -f ($badFrameNames -join ';'))
$badRouteFrames = @($routes | Where-Object { $_.baseline_frame_name -cnotmatch '_INST_' })
$badTemplateFrames = @($templates | Where-Object { $_.baseline_frame_name -cnotmatch '_REF_' })
Assert-True ($badRouteFrames.Count -eq 0 -and $badTemplateFrames.Count -eq 0) 'template-instance-frame-distinction' 'route instance frames use INST and reusable representatives use REF' ("route errors={0}; template errors={1}" -f $badRouteFrames.Count, $badTemplateFrames.Count)

Assert-Unique $primitives.primitive_id 'primitive-id-uniqueness'
$expectedPrimitives = @(1..$primitives.Count | ForEach-Object { 'PRIM-{0:D3}' -f $_ })
Assert-ExactSet $expectedPrimitives $primitives.primitive_id 'primitive-id-sequence'
$templatePrimitiveRefs = @($templates | ForEach-Object { Split-List $_.primitive_dependencies } | Sort-Object -Unique)
Assert-ExactSet $primitives.primitive_id $templatePrimitiveRefs 'primitive-template-reference-completeness'
$primitiveTemplateRefs = @($primitives | ForEach-Object { Split-List $_.reference_templates_or_flows })
$badPrimitiveTemplateRefs = @($primitiveTemplateRefs | Where-Object { $_ -like 'TPL-*' -and $_ -cnotin $templateIds })
Assert-True ($badPrimitiveTemplateRefs.Count -eq 0) 'primitive-template-reference-resolution' 'all explicit PRIM-to-TPL references resolve' ("missing={0}" -f (($badPrimitiveTemplateRefs | Sort-Object -Unique) -join ';'))

$expectedDesignSystemHash = 'DCF2F63D11BB45CB71568B18A0E16C95BD94F1991CBE23B5B677D832F1310AD2'
$expectedPrimitiveHash = '2D01496DCC7D9C062AD77E52CC9F0F110D3F7B4CE899D95A52A8B6F7311E6F4A'
$actualDesignSystemHash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $packageRoot 'DESIGN_SYSTEM_IMPLICATIONS.md')).Hash.ToUpperInvariant()
$actualPrimitiveHash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $packageRoot 'component-primitives.csv')).Hash.ToUpperInvariant()
Assert-True ($actualDesignSystemHash -ceq $expectedDesignSystemHash) 'design-system-freeze-hash' $actualDesignSystemHash ("expected={0}; actual={1}" -f $expectedDesignSystemHash, $actualDesignSystemHash)
Assert-True ($actualPrimitiveHash -ceq $expectedPrimitiveHash) 'component-primitives-freeze-hash' $actualPrimitiveHash ("expected={0}; actual={1}" -f $expectedPrimitiveHash, $actualPrimitiveHash)

$expectedBatches = @(1..9 | ForEach-Object { 'B{0:D2}' -f $_ })
Assert-ExactSet $expectedBatches $batches.batch_id 'design-batch-set'
Assert-Unique $batches.sequence 'design-batch-sequence-uniqueness'
$badBatchStatus = @($batches | Where-Object { $_.status -cne 'future_not_authorized' })
Assert-True ($badBatchStatus.Count -eq 0) 'design-batch-authorization' 'all visual batches are future_not_authorized' ("unexpected status rows={0}" -f $badBatchStatus.Count)

$batchById = @{}
foreach ($batch in $batches) { $batchById[$batch.batch_id] = $batch }

$primaryTemplateRefs = @($batches | ForEach-Object { Split-List $_.primary_template_ids })
$supportingTemplateRefs = @($batches | ForEach-Object { Split-List $_.supporting_template_ids })
Assert-Unique $primaryTemplateRefs 'design-batch-primary-template-ownership'
Assert-ExactSet $templateIds $primaryTemplateRefs 'design-batch-primary-template-completeness'
Assert-True (@($supportingTemplateRefs | Where-Object { $_ -cnotin $templateIds }).Count -eq 0) 'design-batch-supporting-template-resolution' 'all supporting template references resolve' 'one or more supporting template references are missing'
Assert-ExactSet $templateIds @(Split-List $batchById['B09'].supporting_template_ids) 'design-batch-final-template-evidence-set'

$hardPrerequisiteErrors = [System.Collections.Generic.List[string]]::new()
foreach ($batch in $batches) {
    $prerequisites = @(Split-List $batch.hard_prerequisite_batch_ids)
    foreach ($prerequisite in $prerequisites) {
        if ($prerequisite -cnotin $expectedBatches) {
            $hardPrerequisiteErrors.Add(("{0}:unknown:{1}" -f $batch.batch_id, $prerequisite))
        }
        elseif ($prerequisite -ceq $batch.batch_id) {
            $hardPrerequisiteErrors.Add(("{0}:self" -f $batch.batch_id))
        }
        elseif ([int]$batchById[$prerequisite].sequence -ge [int]$batch.sequence) {
            $hardPrerequisiteErrors.Add(("{0}:not-earlier:{1}" -f $batch.batch_id, $prerequisite))
        }
    }
}
Assert-True ($hardPrerequisiteErrors.Count -eq 0) 'design-batch-hard-prerequisite-resolution' 'all hard prerequisite IDs resolve to earlier batches without self-dependency' ("errors={0}" -f ($hardPrerequisiteErrors -join ';'))

$expectedPrimaryByBatch = @{
    'B01' = @('FLOW-NAVIGATION-SEARCH','FLOW-ERROR-OFFLINE-RECOVERY','DF-01','ACT-01','ACT-02','ACT-03','ACT-04','ACT-05','EXCL-INTERNAL-SEARCH','EXCL-TRACKING-PARAMETERS','EXCL-FILTER-SORT-VARIANTS')
    'B02' = @($routes | Where-Object { $_.template_id -cin @('TPL-PUBLIC-HOME','TPL-SERVICE-COLLECTION','TPL-PUBLIC-ABOUT') } | ForEach-Object route_id) + @('J-01')
    'B03' = @($routes | Where-Object { $_.template_id -cin @('TPL-SERVICE-WING','TPL-SERVICE-DETAIL','TPL-INDUSTRY-COLLECTION','TPL-INDUSTRY-DETAIL') } | ForEach-Object route_id) + @('J-03') + @($sourceWayfinding.room_id)
    'B04' = @($routes | Where-Object { $_.template_id -cin @('TPL-WORK-COLLECTION','TPL-WORK-DETAIL','TPL-DEMO-COLLECTION','TPL-DEMO-DETAIL','TPL-INSIGHT-COLLECTION','TPL-INSIGHT-DETAIL','TPL-EXPERT-COLLECTION','TPL-EXPERT-DETAIL','TPL-TRUST-COLLECTION','TPL-TRUST-DETAIL') } | ForEach-Object route_id) + @('J-04','ACT-13')
    'B05' = @('ROUTE-CONTACT','FLOW-AI','FLOW-HUMAN-HANDOFF','FLOW-MEDIA-OPT-IN','FLOW-CONTACT','J-05','AF-01','AF-02','CF-01','ACT-14','ACT-15','ACT-16','ACT-17','ACT-18','ACT-19','ACT-32','EXCL-CHAT-SESSIONS')
    'B06' = @('ROUTE-BOOK','FLOW-BOOKING-LINEAGE','BF-01','BF-01A','BF-01B','BF-01C','BF-01D','BF-01E') + @(20..31 | ForEach-Object { 'ACT-{0:D2}' -f $_ })
    'B07' = @('FLOW-FIRST-VISIT','FLOW-RETURN-VISIT','FLOW-WORLD-HUD-FALLBACK','J-02','FV-01','RV-01') + @(6..12 | ForEach-Object { 'ACT-{0:D2}' -f $_ }) + @('ACT-40','EXCL-WORLD')
    'B08' = @('FLOW-STAFF-PUBLICATION-OPERATIONS','FLOW-AUTH-SESSION-PERMISSION','PF-01') + @($expectedFlowAndSubflowIds | Where-Object { $_ -like 'SOF-*' }) + @(33..39 | ForEach-Object { 'ACT-{0:D2}' -f $_ }) + @(41..53 | ForEach-Object { 'ACT-{0:D2}' -f $_ }) + @('EXCL-ADMIN','EXCL-NONPUBLIC-PUBLICATION','EXCL-STAGING','EXCL-DEFENSE')
    'B09' = @()
}
foreach ($batchId in $expectedBatches) {
    Assert-ExactSet $expectedPrimaryByBatch[$batchId] @(Split-List $batchById[$batchId].primary_source_ids) ("design-batch-primary-map-{0}" -f $batchId)
}

$knownPrimarySourceIds = @($routes.route_id + $requiredFlowFamilies + $acceptedExperienceIds + $expectedActions + $sourceExclusions.exclusion_id + $sourceWayfinding.room_id | Sort-Object -Unique)
$allPrimarySourceIds = @($batches | ForEach-Object { Split-List $_.primary_source_ids })
$allSupportingSourceIds = @($batches | ForEach-Object { Split-List $_.supporting_or_final_evidence_ids })
$knownSupportingSourceIds = @($knownPrimarySourceIds + $expectedTests | Sort-Object -Unique)
$unknownPrimaryIds = @($allPrimarySourceIds | Where-Object { $_ -cnotin $knownPrimarySourceIds })
$unknownSupportingIds = @($allSupportingSourceIds | Where-Object { $_ -cnotin $knownSupportingSourceIds })
Assert-True ($unknownPrimaryIds.Count -eq 0) 'design-batch-primary-reference-resolution' 'every primary source ID resolves to an accepted source set' ("unknown={0}" -f (($unknownPrimaryIds | Sort-Object -Unique) -join ';'))
Assert-True ($unknownSupportingIds.Count -eq 0) 'design-batch-supporting-reference-resolution' 'every supporting/final-evidence ID resolves to an accepted source or UX test' ("unknown={0}" -f (($unknownSupportingIds | Sort-Object -Unique) -join ';'))
Assert-Unique $allPrimarySourceIds 'design-batch-primary-source-ownership'
Assert-ExactSet $knownPrimarySourceIds $allPrimarySourceIds 'design-batch-primary-source-completeness'
Assert-ExactSet $routes.route_id @($allPrimarySourceIds | Where-Object { $_ -like 'ROUTE-*' }) 'design-batch-primary-route-set'
Assert-ExactSet $requiredFlowFamilies @($allPrimarySourceIds | Where-Object { $_ -like 'FLOW-*' }) 'design-batch-primary-package-flow-set'
Assert-ExactSet $acceptedExperienceIds @($allPrimarySourceIds | Where-Object { $_ -cin $acceptedExperienceIds }) 'design-batch-primary-experience-set'
Assert-ExactSet $expectedActions @($allPrimarySourceIds | Where-Object { $_ -like 'ACT-*' }) 'design-batch-primary-action-set'
Assert-ExactSet $sourceExclusions.exclusion_id @($allPrimarySourceIds | Where-Object { $_ -like 'EXCL-*' }) 'design-batch-primary-exclusion-set'
Assert-ExactSet $sourceWayfinding.room_id @($allPrimarySourceIds | Where-Object { $_ -like 'WING-*' -or $_ -like 'ROOM-*' }) 'design-batch-primary-wayfinding-set'
Assert-ExactSet $expectedTests @(Split-List $batchById['B09'].supporting_or_final_evidence_ids) 'design-batch-final-ux-test-set'

$opaqueBatchReferences = @($batches | Where-Object { ($_.primary_source_ids + ';' + $_.supporting_or_final_evidence_ids) -match '(?i)\bthrough\b|\brelated\b|\bcount-only\b|\.\.|\*' })
Assert-True ($opaqueBatchReferences.Count -eq 0) 'design-batch-no-opaque-references' 'batch executable reference fields contain only exact semicolon-delimited IDs' ("opaque rows={0}" -f (($opaqueBatchReferences | ForEach-Object batch_id) -join ';'))
$priorInvalidIds = @('AI-01','HF-01','MF-01','BF-02','BF-03','BF-04','BF-05','BF-06','BF-07','EXCL-ADMIN-WILDCARD','EXCL-LOGIN','EXCL-API','EXCL-PREVIEW','EXCL-PREVIEW-WILDCARD')
$priorInvalidAccepted = @($priorInvalidIds | Where-Object { $_ -cin $knownSupportingSourceIds })
$priorInvalidPresent = @($priorInvalidIds | Where-Object { $_ -cin $allPrimarySourceIds -or $_ -cin $allSupportingSourceIds })
Assert-True ($priorInvalidAccepted.Count -eq 0 -and $priorInvalidPresent.Count -eq 0) 'design-batch-prior-invalid-reference-negative-fixture' 'prior synthetic IDs are rejected by the accepted-source resolver and absent from the plan' ("accepted={0}; present={1}" -f ($priorInvalidAccepted -join ';'), ($priorInvalidPresent -join ';'))

$b06Prerequisites = @(Split-List $batchById['B06'].hard_prerequisite_batch_ids)
$b06PrimaryActions = @(Split-List $batchById['B06'].primary_source_ids | Where-Object { $_ -like 'ACT-*' })
$b06AllReferences = @((Split-List $batchById['B06'].primary_source_ids) + (Split-List $batchById['B06'].supporting_or_final_evidence_ids))
$b06ForbiddenReferences = @('FLOW-AI','FLOW-HUMAN-HANDOFF','FLOW-MEDIA-OPT-IN','J-02','J-05','AF-01','AF-02','EXCL-WORLD')
Assert-ExactSet @('B01') $b06Prerequisites 'booking-hard-prerequisite-independence'
Assert-ExactSet @(20..31 | ForEach-Object { 'ACT-{0:D2}' -f $_ }) $b06PrimaryActions 'booking-primary-action-ownership'
Assert-True (@($b06AllReferences | Where-Object { $_ -cin $b06ForbiddenReferences }).Count -eq 0) 'booking-optional-flow-reference-independence' 'B06 has no AI handoff media or World source dependency' 'B06 contains an optional-flow source dependency'
$b06PrerequisiteText = ($batchById['B06'].prerequisites_and_held_inputs -replace '\s+', ' ')
Assert-True ($b06PrerequisiteText -match '(?i)no prior AI human handoff media World account audio or upload dependency' -and $b06PrerequisiteText -match '(?i)B05 consistency review is non-blocking') 'booking-independence-language' 'B06 explicitly has no prior optional-help/account/media dependency and treats B05 consistency as non-blocking' 'B06 independence/non-blocking wording is incomplete'

$batchReviewGaps = @($batches | Where-Object { $_.validation_and_review -notmatch '(?i)independent design review' -or $_.validation_and_review -notmatch '(?i)independent accessibility review' })
Assert-True ($batchReviewGaps.Count -eq 0) 'design-batch-independent-review-obligations' 'every B01-B09 row requires independent design and independent accessibility review' ("missing rows={0}" -f (($batchReviewGaps | ForEach-Object batch_id) -join ';'))
$batchWcagGaps = @($batches | Where-Object {
    $_.validation_and_review -notmatch '(?i)normative WCAG 2\.2 Level AA target' -or
    $_.validation_and_review -notmatch '(?i)every applicable full page and complete process' -or
    $_.validation_and_review -notmatch '(?i)represented third-party steps' -or
    $_.validation_and_review -notmatch '(?i)does not claim current conformance'
})
Assert-True ($batchWcagGaps.Count -eq 0) 'design-batch-wcag-target-review' 'every B01-B09 gate reviews the normative WCAG 2.2 AA complete-process target without claiming current conformance' ("missing rows={0}" -f (($batchWcagGaps | ForEach-Object batch_id) -join ';'))
$batchBrowserEvidenceGaps = @($batches | Where-Object {
    $_.required_visual_evidence -notmatch 'BP-NFR-006' -or
    $_.required_visual_evidence -notmatch '(?i)Safari/iOS 16\.4' -or
    $_.required_visual_evidence -notmatch '(?i)mobile layout input virtual-keyboard and safe-area' -or
    $_.required_visual_evidence -notmatch '(?i)semantic Quick Access recovery'
})
Assert-True ($batchBrowserEvidenceGaps.Count -eq 0) 'design-batch-browser-evidence' 'every B01-B09 batch requires browser-floor, mobile Safari, and unsupported Quick Access evidence' ("missing rows={0}" -f (($batchBrowserEvidenceGaps | ForEach-Object batch_id) -join ';'))
$batchTimingEvidenceGaps = [System.Collections.Generic.List[string]]::new()
foreach ($batch in $batches) {
    $branches = @(Split-List $batch.time_limit_branch_ids)
    $evidence = $batch.required_visual_evidence
    if ($branches -contains 'TL-REMOVABLE-ADJUSTABLE' -and ($evidence -notmatch 'TL-REMOVABLE-ADJUSTABLE' -or $evidence -notmatch '(?i)before start')) { $batchTimingEvidenceGaps.Add(("{0}:removable" -f $batch.batch_id)) }
    if ($branches -contains 'TL-WARN-EXTEND' -and ($evidence -notmatch 'TL-WARN-EXTEND' -or $evidence -notmatch '(?i)at least 20 seconds' -or $evidence -notmatch '(?i)at least 10x')) { $batchTimingEvidenceGaps.Add(("{0}:warn" -f $batch.batch_id)) }
    if ($branches -contains 'TL-NOT-APPLICABLE' -and $evidence -notmatch 'TL-NOT-APPLICABLE') { $batchTimingEvidenceGaps.Add(("{0}:not-applicable" -f $batch.batch_id)) }
    if ($branches -notcontains 'TL-NOT-APPLICABLE' -and ($evidence -notmatch '(?i)preserve permitted data and (the )?last authoritative state' -or $evidence -notmatch '(?i)accessible reauthentication')) { $batchTimingEvidenceGaps.Add(("{0}:preservation-reauth" -f $batch.batch_id)) }
    if ($branches -notcontains 'TL-NOT-APPLICABLE' -and $evidence -notmatch '(?i)exact durations remain gated') { $batchTimingEvidenceGaps.Add(("{0}:duration-gate" -f $batch.batch_id)) }
}
Assert-True ($batchTimingEvidenceGaps.Count -eq 0) 'design-batch-time-limit-evidence' 'every B01-B09 batch proves its assigned time-limit branch and duration gate' ("gaps={0}" -f ($batchTimingEvidenceGaps -join ';'))

$templatePrimaryOwner = @{}
foreach ($batch in $batches) {
    foreach ($templateId in @(Split-List $batch.primary_template_ids)) {
        $templatePrimaryOwner[$templateId] = $batch.batch_id
    }
}
$templateBatchFrameErrors = [System.Collections.Generic.List[string]]::new()
foreach ($template in $templates) {
    $frameBatchMatch = [regex]::Match($template.baseline_frame_name, '^HSD_UIR_(B\d{2})_')
    $frameBatch = if ($frameBatchMatch.Success) { $frameBatchMatch.Groups[1].Value } else { '<missing>' }
    if ($templatePrimaryOwner[$template.template_id] -cne $frameBatch) {
        $templateBatchFrameErrors.Add(("{0}:owner={1}:frame={2}" -f $template.template_id, $templatePrimaryOwner[$template.template_id], $frameBatch))
    }
}
Assert-True ($templateBatchFrameErrors.Count -eq 0) 'template-frame-primary-batch-alignment' 'all 40 template baseline frame batch tokens match their single primary batch owner' ("errors={0}" -f ($templateBatchFrameErrors -join ';'))

$routePrimaryOwner = @{}
foreach ($batch in $batches) {
    foreach ($routeId in @(Split-List $batch.primary_source_ids | Where-Object { $_ -like 'ROUTE-*' })) {
        $routePrimaryOwner[$routeId] = $batch.batch_id
    }
}
$routeBatchFrameErrors = [System.Collections.Generic.List[string]]::new()
foreach ($route in $routes) {
    $frameBatchMatch = [regex]::Match($route.baseline_frame_name, '^HSD_UIR_(B\d{2})_')
    $frameBatch = if ($frameBatchMatch.Success) { $frameBatchMatch.Groups[1].Value } else { '<missing>' }
    if ($routePrimaryOwner[$route.route_id] -cne $frameBatch) {
        $routeBatchFrameErrors.Add(("{0}:owner={1}:frame={2}" -f $route.route_id, $routePrimaryOwner[$route.route_id], $frameBatch))
    }
}
Assert-True ($routeBatchFrameErrors.Count -eq 0) 'route-frame-primary-batch-alignment' 'all 33 route baseline frame batch tokens match their single primary batch owner' ("errors={0}" -f ($routeBatchFrameErrors -join ';'))

Assert-Unique $trace.trace_id 'trace-id-uniqueness'
$sourceRequirements = @($sourceCsv['docs/phase-1-ux-architecture/traceability.csv'] | Where-Object { $_.source_type -ceq 'requirement' } | ForEach-Object source_id)
$traceRequirements = @($trace | Where-Object { $_.source_type -ceq 'requirement' } | ForEach-Object source_id)
Assert-ExactSet $sourceRequirements $traceRequirements 'requirement-trace-completeness'
Assert-ExactSet @('D-025','D-026','D-035','D-036') @($trace | Where-Object { $_.source_type -ceq 'decision' } | ForEach-Object source_id) 'decision-trace-set'
Assert-ExactSet $routes.route_id @($trace | Where-Object { $_.source_type -ceq 'route' } | ForEach-Object source_id) 'route-trace-set'
Assert-ExactSet $expectedActions @($trace | Where-Object { $_.source_type -ceq 'action' } | ForEach-Object source_id) 'action-trace-set'
Assert-ExactSet $sourceExclusions.exclusion_id @($trace | Where-Object { $_.source_type -ceq 'exclusion' } | ForEach-Object source_id) 'exclusion-trace-set'
Assert-ExactSet $sourceWayfinding.room_id @($trace | Where-Object { $_.source_type -ceq 'wayfinding' } | ForEach-Object source_id) 'wayfinding-trace-set'
$requiredGateIds = @('MA-002','MA-003','MA-004','MA-005','MA-006','MA-007','MA-008','MA-009','MA-010','MA-011','MA-013','MA-024','GATE-EXTERNAL-DESIGN-WRITE')
Assert-ExactSet $requiredGateIds @($trace | Where-Object { $_.source_type -ceq 'manual_gate' } | ForEach-Object source_id) 'manual-gate-trace-set'
$proposedPackageGates = @($trace | Where-Object { $_.source_id -cin @('MA-024','GATE-EXTERNAL-DESIGN-WRITE') })
$proposedGateProvenanceErrors = @($proposedPackageGates | Where-Object {
    $_.source_artifact -cne 'README.md;UI_REFERENCE_DESIGN_CONTRACT.md' -or
    $_.source_artifact -match 'MANUAL_ACTIONS\.md' -or
    $_.status_or_gate -cne 'proposed_at_2026-09-03_producer_freeze_root_integration_only_after_clean_independent_reviews' -or
    $_.contract_records -notmatch '(?i)package-only proposal at the 2026-09-03 producer freeze' -or
    $_.required_future_evidence -notmatch '(?i)root durable integration'
})
Assert-True ($proposedPackageGates.Count -eq 2 -and $proposedGateProvenanceErrors.Count -eq 0) 'proposed-gate-trace-provenance' 'MA-024 and external-write provenance is package-only and time-bounded to the 2026-09-03 producer freeze pending clean-review root integration' ("gate rows={0}; provenance errors={1}" -f $proposedPackageGates.Count, $proposedGateProvenanceErrors.Count)

$markdownFiles = @(Get-ChildItem -LiteralPath $packageRoot -Recurse -File -Filter '*.md')
$brokenLinks = [System.Collections.Generic.List[string]]::new()
foreach ($file in $markdownFiles) {
    $content = Get-Content -Raw -LiteralPath $file.FullName
    foreach ($match in [regex]::Matches($content, '\[[^\]]+\]\((?<target>[^)]+)\)')) {
        $target = $match.Groups['target'].Value.Trim().Trim('<','>')
        if ($target -match '^(?i)(https?:|mailto:)' -or $target.StartsWith('#')) { continue }
        $pathPart = ($target -split '#')[0]
        if ([string]::IsNullOrWhiteSpace($pathPart)) { continue }
        $candidate = Join-Path $file.DirectoryName $pathPart
        if (-not (Test-Path -LiteralPath $candidate)) {
            $brokenLinks.Add(("{0}->{1}" -f $file.FullName.Substring($repoRoot.Length + 1), $target))
        }
    }
}
Assert-True ($brokenLinks.Count -eq 0) 'local-markdown-references' 'all local Markdown links resolve' ("broken={0}" -f ($brokenLinks -join ';'))

$contentFiles = @($packageFiles | Where-Object { $_.Extension -in @('.md','.csv') })
$artifactText = ($contentFiles | ForEach-Object { Get-Content -Raw -LiteralPath $_.FullName }) -join "`n"
$urlPattern = ('h' + 'ttps?://')
$externalUrlMatches = @([regex]::Matches($artifactText, $urlPattern, [Text.RegularExpressions.RegexOptions]::IgnoreCase))
Assert-True ($externalUrlMatches.Count -eq 0) 'external-url-absence' 'no external URL appears in package content' ("external URL matches={0}" -f $externalUrlMatches.Count)
$privateKeyPattern = ('-----BEGIN ' + '(RSA |OPENSSH |EC )?' + 'PRIVATE KEY-----')
$secretAssignmentPattern = ('(?i)(api[_-]?key|client[_-]?secret|password|bearer[_-]?token)' + '\s*[:=]\s*["'']?[A-Za-z0-9_\-]{8,}')
$secretMatches = @([regex]::Matches($artifactText, $privateKeyPattern) + [regex]::Matches($artifactText, $secretAssignmentPattern))
Assert-True ($secretMatches.Count -eq 0) 'secret-pattern-absence' 'no credential/private-key assignment pattern appears in package content' ("secret-like matches={0}" -f $secretMatches.Count)

$requiredDateDocs = @('README.md','UI_REFERENCE_DESIGN_CONTRACT.md','DESIGN_SYSTEM_IMPLICATIONS.md','validation/validation-report.md','producer-inspection.md')
$wrongDateDocs = @($requiredDateDocs | Where-Object { (Get-Content -Raw -LiteralPath (Join-Path $packageRoot $_)) -notmatch '2026-09-03' })
Assert-True ($wrongDateDocs.Count -eq 0) 'evidence-date' 'all package evidence documents use 2026-09-03' ("missing date={0}" -f ($wrongDateDocs -join ';'))

$contractText = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'UI_REFERENCE_DESIGN_CONTRACT.md')
$readmeText = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'README.md')
$designSystemText = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'DESIGN_SYSTEM_IMPLICATIONS.md')
$normalizedAuthorityText = (($contractText + "`n" + $readmeText + "`n" + $designSystemText) -replace '\s+', ' ')
foreach ($decision in @('D-025','D-026','D-035','D-036')) {
    Assert-True ($normalizedAuthorityText -match [regex]::Escape($decision)) ("authority-{0}" -f $decision) ("{0} explicit" -f $decision) ("{0} missing" -f $decision)
}
$gateLabel = 'MA-024 — Phase 1 UI reference-design contract and foundation-surface coverage acceptance'
Assert-True ($normalizedAuthorityText.Contains($gateLabel)) 'ma024-exact-label' 'exact MA-024 label present' 'exact MA-024 label missing'
Assert-True ($contractText -match '(?im)^\*\*External Figma/Stitch write authority:\*\* false\s*$') 'external-write-false' 'external Figma/Stitch write authority explicitly false' 'external write false declaration missing'
Assert-True ($normalizedAuthorityText -match '(?i)separate explicit future manual gate') 'external-write-separate-gate' 'separate future external-write gate explicit' 'separate future external-write gate is not explicit'
Assert-True ($normalizedAuthorityText -match '(?i)reusable reference templates?' -and $normalizedAuthorityText -match '(?i)route-instance') 'template-instance-contract-language' 'reusable templates and route instances are explicitly distinct' 'template versus instance distinction missing'
Assert-True ($normalizedAuthorityText -match '(?i)does not create visual screens' -and $normalizedAuthorityText -match '(?i)producer cannot approve') 'nonapproval-boundary' 'no-screen and no-self-approval boundaries explicit' 'nonapproval boundary missing'
$normalizedReadmeText = ($readmeText -replace '\s+', ' ')
$normalizedContractText = ($contractText -replace '\s+', ' ')
$currentReviewPattern = '(?i)independent design and independent accessibility review before (?:founder decision at )?MA-024'
Assert-True ($normalizedReadmeText -match $currentReviewPattern -and $normalizedContractText -match $currentReviewPattern) 'current-design-accessibility-review-gate' 'README and contract require both current independent reviews before MA-024' 'README or contract does not require both current independent reviews before MA-024'

$wcagTargetPattern = '(?i)WCAG 2\.2 Level AA.*(?:all|every) applicable full page(?:s)? and complete process(?:es)?.*third-party steps'
$wcagDisclaimerPattern = '(?i)(?:not[^.]{0,160}current[^.]{0,160}conformance|does not[^.]{0,160}establish[^.]{0,80}conformance|neither[^.]{0,200}establishes[^.]{0,80}conformance|not a current conformance claim)'
Assert-True ($normalizedReadmeText -match $wcagTargetPattern -and $normalizedContractText -match $wcagTargetPattern -and ($designSystemText -replace '\s+',' ') -match $wcagTargetPattern) 'wcag22aa-normative-target' 'README contract and design-system guidance require WCAG 2.2 Level AA for applicable full pages and complete processes including third-party steps' 'normative WCAG target is missing from one or more controlling package documents'
Assert-True ($normalizedReadmeText -match $wcagDisclaimerPattern -and $normalizedContractText -match $wcagDisclaimerPattern -and ($designSystemText -replace '\s+',' ') -match $wcagDisclaimerPattern) 'wcag-no-current-conformance-disclaimer' 'README contract and design-system guidance explicitly reject a current conformance claim' 'no-current-conformance disclaimer is incomplete'

$ux001Trace = @($trace | Where-Object { $_.source_id -ceq 'UX-001' })
$ux005Trace = @($trace | Where-Object { $_.source_id -ceq 'UX-005' })
$nfr006Trace = @($trace | Where-Object { $_.source_id -ceq 'NFR-006' })
$uxTest040Trace = @($trace | Where-Object { $_.source_id -ceq 'UXTEST-040' })
Assert-True ($ux001Trace.Count -eq 1 -and (($ux001Trace.contract_records + ' ' + $ux001Trace.required_future_evidence) -replace '\s+',' ') -match $wcagTargetPattern -and ($ux001Trace.required_future_evidence -match '(?i)does not claim current conformance|before any conformance claim')) 'ux001-wcag-trace-contract' 'UX-001 trace carries the complete-process target and no-current-conformance gate' 'UX-001 trace is incomplete'
Assert-True ($ux005Trace.Count -eq 1 -and $ux005Trace.contract_records -match 'BP-NFR-006' -and $ux005Trace.required_future_evidence -match '(?i)Safari/iOS 16\.4.*safe-area.*unsupported-client semantic Quick Access') 'ux005-browser-recovery-trace' 'UX-005 trace carries Safari floor and unsupported semantic recovery evidence' 'UX-005 browser recovery trace is incomplete'
Assert-True ($nfr006Trace.Count -eq 1 -and (($nfr006Trace.contract_records + ' ' + $nfr006Trace.required_future_evidence) -replace '\s+',' ') -match '(?i)latest two stable Chrome Edge Firefox Safari release families.*Safari/iOS 16\.4 minimum legacy floor.*dated later QA.*exact then-current versions') 'nfr006-trace-contract' 'NFR-006 trace fixes the browser families and floor while deferring exact versions to dated QA' 'NFR-006 trace is incomplete'
Assert-True ($uxTest040Trace.Count -eq 1 -and $uxTest040Trace.contract_records -match 'TL-REMOVABLE-ADJUSTABLE' -and $uxTest040Trace.required_future_evidence -match '(?i)at least 20 seconds.*at least 10x.*criterion-supported exception.*last authoritative state.*accessible reauthentication.*exact durations remain gated') 'uxtest040-time-limit-trace' 'UXTEST-040 trace carries every allowed branch, threshold, preservation rule, reauthentication, and duration gate' 'UXTEST-040 timing trace is incomplete'

$normalizedBrowserDocs = (($normalizedReadmeText + ' ' + $normalizedContractText) -replace '\s+',' ')
Assert-True ($normalizedBrowserDocs -match '(?i)BP-NFR-006.*latest two stable release families of Chrome, Edge, Firefox, and Safari' -and $normalizedBrowserDocs -match '(?i)Safari on iOS 16\.4.*minimum legacy floor' -and $normalizedBrowserDocs -match '(?i)Exact then-current.*version.*deferred.*dated QA|exact then-current browser versions selected and recorded by dated QA' -and $normalizedBrowserDocs -match '(?i)mobile.*layout.*input.*virtual-keyboard.*safe-area' -and $normalizedBrowserDocs -match '(?i)below the floor or otherwise unsupported.*semantic Quick Access|semantic Quick Access.*below the floor or otherwise unsupported') 'nfr006-document-contract' 'README and contract state the complete browser profile, deferred version selection, mobile Safari evidence, and unsupported recovery' 'browser contract prose is incomplete'
$normalizedTimingDocs = (($normalizedReadmeText + ' ' + $normalizedContractText) -replace '\s+',' ')
Assert-True ($normalizedTimingDocs -match 'TL-REMOVABLE-ADJUSTABLE' -and $normalizedTimingDocs -match 'TL-WARN-EXTEND' -and $normalizedTimingDocs -match 'TL-EXCEPTION' -and $normalizedTimingDocs -match 'TL-NOT-APPLICABLE' -and $normalizedTimingDocs -match '(?i)at least 20 seconds' -and $normalizedTimingDocs -match '(?i)(at least 10 times|at least 10x)' -and $normalizedTimingDocs -match '(?i)permitted data and (the )?last authoritative state' -and $normalizedTimingDocs -match '(?i)accessible reauthentication' -and $normalizedTimingDocs -match '(?i)exact.*durations remain gated') 'wcag221-document-contract' 'README and contract state all time-limit branches, thresholds, preservation, reauthentication, and exact-duration gate' 'time-limit contract prose is incomplete'

$freezeProvenancePattern = '(?i)at the 2026-09-03 producer freeze.*package proposals?.*not yet recorded in root durable manual-action records.*only after clean independent design and accessibility reviews.*time-bounded freeze'
Assert-True ($normalizedReadmeText -match $freezeProvenancePattern -and $normalizedContractText -match '(?i)at the 2026-09-03 producer freeze.*package proposals?.*not yet recorded in root durable manual-action records.*only after clean independent design and accessibility reviews.*time-bounded freeze') 'ma024-time-bounded-provenance-language' 'README and contract time-bound package-only gate provenance and defer root integration until clean reviews' 'MA-024 time-bounded provenance wording is incomplete'

$wcagNegativeFixture = 'The mockups comply with WCAG 2.2 AA.'
Assert-True (-not ($wcagNegativeFixture -match $wcagTargetPattern -and $wcagNegativeFixture -match $wcagDisclaimerPattern)) 'wcag-target-negative-fixture' 'mockup-only compliance claim is rejected by the normative target/disclaimer contract' 'WCAG negative fixture unexpectedly satisfies the contract'
$producerFreezeFiles = @($requiredFiles | ForEach-Object { Join-Path $packageRoot $_ } | Where-Object { [IO.Path]::GetExtension($_) -in @('.md','.csv') })
$producerFreezeText = ($producerFreezeFiles | ForEach-Object { Get-Content -Raw -LiteralPath $_ }) -join "`n"
$unsupportedConformanceClaims = @([regex]::Matches($producerFreezeText, '(?i)\b(?:currently\s+)?(?:meets|achieves|certifies|is conformant with|is compliant with)\s+WCAG\s*2\.2'))
Assert-True ($unsupportedConformanceClaims.Count -eq 0) 'unsupported-conformance-claim-absence' 'no producer-freeze artifact claims current WCAG conformance' ("unsupported conformance claims={0}" -f $unsupportedConformanceClaims.Count)

$gitLines = @(& git -C $repoRoot status --porcelain=v1 2>$null)
$outsideScope = [System.Collections.Generic.List[string]]::new()
foreach ($line in $gitLines) {
    if ($line.Length -lt 4) { continue }
    $path = $line.Substring(3).Trim().Replace('\','/')
    if ($path.Contains(' -> ')) { $path = ($path -split ' -> ')[-1] }
    if (-not $path.StartsWith('docs/phase-1-ui-reference-design/')) {
        $outsideScope.Add($path)
    }
}
Assert-True ($outsideScope.Count -eq 0) 'git-write-scope' 'all current worktree changes are inside docs/phase-1-ui-reference-design' ("outside-scope changes={0}" -f ($outsideScope -join ';'))

[string[]]$freezeRelativePaths = @($requiredFiles)
[Array]::Sort($freezeRelativePaths, [StringComparer]::Ordinal)
$freezeHashLines = @($freezeRelativePaths | ForEach-Object {
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $packageRoot $_)).Hash.ToUpperInvariant()
    "{0}  {1}" -f $hash, $_.Replace('\','/')
})
$freezePayload = [string]::Join("`n", $freezeHashLines)
$sha256 = [Security.Cryptography.SHA256]::Create()
try {
    $freezeAggregateHash = [BitConverter]::ToString($sha256.ComputeHash([Text.UTF8Encoding]::new($false).GetBytes($freezePayload))).Replace('-','')
}
finally {
    $sha256.Dispose()
}
Assert-True ($freezeHashLines.Count -eq 13) 'freeze-file-count' '13 required package files included in the deterministic freeze' ("actual={0}" -f $freezeHashLines.Count)
Write-Output 'FREEZE_METHOD=Sort relative forward-slash paths ordinally; for each emit uppercase SHA-256 two spaces path; join lines with LF and no terminal newline; SHA-256 the UTF-8 no-BOM payload'
foreach ($freezeHashLine in $freezeHashLines) { Write-Output ("FREEZE_FILE_SHA256={0}" -f $freezeHashLine) }
Write-Output ("FREEZE_AGGREGATE_SHA256={0}" -f $freezeAggregateHash)
Write-Output ("COUNTS routes={0} exclusions={1} wayfinding={2} actions={3} ux_tests={4} flow_families={5} source_experience_ids={6} flow_rows={7} templates={8} primary_template_owners={9} route_template_refs={10} flow_template_refs={11} profiles={12} browser_profiles={13} time_limit_profiles={14} primitives={15} batches={16} primary_source_owners={17} trace_rows={18} package_csv={19} package_json={20}" -f $routes.Count, $flowExclusions.Count, $flowWayfinding.Count, $flowActions.Count, $traceTests.Count, $flowFamilies.Count, $acceptedExperienceIds.Count, $flows.Count, $templates.Count, $primaryTemplateRefs.Count, $routeTemplateRefs.Count, $flowTemplateRefs.Count, $matrix.Count, $browserProfileRows.Count, $timeProfileRows.Count, $primitives.Count, $batches.Count, $allPrimarySourceIds.Count, $trace.Count, $packageCsvFiles.Count, $packageJsonFiles.Count)
if ($script:Failures.Count -gt 0) {
    Write-Output ("RESULT=FAIL PASS_COUNT={0} FAIL_COUNT={1}" -f $script:PassCount, $script:Failures.Count)
    exit 1
}

Write-Output ("RESULT=PASS PASS_COUNT={0} FAIL_COUNT=0" -f $script:PassCount)
exit 0
