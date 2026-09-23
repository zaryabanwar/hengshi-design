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
Write-Output 'EVIDENCE_DATE=2026-09-06'
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
    'producer-inspection.md',
    '../../scripts/validation/ui-stream-mapping.ps1'
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

Assert-RequiredColumns $routes @('route_id','path','route_family','route_instance_id','template_id','baseline_frame_name','state_profile','viewport_profile','mode_profile','instance_evidence','semantic_quick_access','immersive_stream_representation','primary_next_actions','content_or_policy_gate','activation_status','browser_profile','time_limit_branch') 'route-columns'
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
Assert-True ($sourceRoutes.Count -eq 34) 'source-route-count' 'source canonical routes=34' ("actual={0}" -f $sourceRoutes.Count)
Assert-True ($routes.Count -eq 34) 'route-coverage-count' 'covered routes=34' ("actual={0}" -f $routes.Count)
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
$expectedTests = @(1..46 | ForEach-Object { 'UXTEST-{0:D3}' -f $_ })
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
    'FLOW-WORLD-HUD-STREAM',
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
# D-042 2026-09-06: four DS-S-* stream profiles added. Was 32 at D-037.
# D-043 2026-09-06: a guarded stream-invariance profile was added. Was 36 at D-042.
# D-045 2026-09-06: that profile is DELETED, not amended. It had zero members, and a
# zero-member guarded category is where an unexamined record hides. Invariance survives
# only as assertion A-06, which cannot be selected into. Back to 36.
$streamProfiles = @($matrix | Where-Object { $_.dimension -ceq 'stream' })
Assert-True ($matrix.Count -eq 36) 'profile-count' 'viewport mode state stream browser and time-limit profiles=36' ("actual={0}" -f $matrix.Count)
Assert-ExactSet @('DS-S-HIGH','DS-S-MEDIUM','DS-S-LOW','DS-S-SEMANTIC') $streamProfiles.profile_id 'delivery-stream-profile-set'

# D-043: a stream profile row must be homogeneous in its own dimension. Before this the
# DS-S-* rows carried STATE-*/MODE-*/VP-* tokens in required_values, which made the
# evidence set uncountable. required_values now holds stream tokens only.
$legalStreamTokens = @('S-HIGH','S-MEDIUM','S-LOW','S-SEMANTIC')
$streamTokenErrors = [System.Collections.Generic.List[string]]::new()
foreach ($row in $streamProfiles) {
    foreach ($token in @(Split-List $row.required_values)) {
        if ($token -cnotin $legalStreamTokens) { $streamTokenErrors.Add(("{0}:{1}" -f $row.profile_id, $token)) }
    }
}
Assert-True ($streamTokenErrors.Count -eq 0) 'delivery-stream-token-legality' 'every stream profile required value is a stream token' ("illegal={0}" -f ($streamTokenErrors -join ';'))
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
# D-045: the stream clause is removed from here because records no longer select a
# stream profile. Stream legality is resolved at the primitive by A-02 and folded to the
# template by A-03; there is nothing on a record to resolve.
Assert-True ($profileRefGaps.Count -eq 0) 'profile-reference-resolution' 'all route flow and template state viewport and mode profile references resolve' ("gaps={0}" -f ($profileRefGaps -join ';'))

# =====================================================================
# D-045 2026-09-06 - delivery-stream evidence model, assertions A-01..A-11.
#
# What was deleted here and why. Two D-043 assertions stood in this place:
#   * 'delivery-stream-assignment' enforced state_profile as a proxy for stream
#     presence and forbade the correct answer.
#   * 'delivery-stream-record-coverage' had the pass condition Count -eq 44.
# Both are deleted, not amended. An assertion whose pass condition is a row count
# proves a column exists; it cannot prove the column carries a judgement. That
# defect has now survived three independent FAIL rounds against 183, 184 and 185
# passing assertions, and its fourth spelling passed 189. No assertion below has a
# bare count in its pass condition.
#
# The model: stream obligations are DECLARED at the primitive (stream_presence),
# COMPUTED from alternative hosts constrained by required content dependencies, and
# INHERITED unstored at route and flow. No record carries a stream column, so
# there is nothing on a record for a future producer to populate as a total
# function of an existing column.
# =====================================================================

$legalStreams = @('S-HIGH','S-LOW','S-MEDIUM','S-SEMANTIC')
$streamExcluded = 'STREAM-SCOPE-EXCLUDED'

# --- A-01 stream-column-absence --------------------------------------------
# Deletion guard. Without it the concept returns under a new spelling, which is
# exactly how it arrived: D-042 added inert DS-S-* profiles, D-043 derived
# stream_profile from state_profile, and each passed every assertion of its day.
# Carve-out, stated rather than silent: immersive_stream_representation contains
# the substring 'stream' and is REQUIRED by N-02. It is authored prose that A-05
# resolves against the computed fold, so it is a checked claim, not a free column.
$prohibitedStreamColumn = -join ('stream','_','profile')
$invariantToken = -join ('DS-STREAM','-','INVARIANT')
$a01 = [System.Collections.Generic.List[string]]::new()
foreach ($name in @('foundation-route-coverage.csv','foundation-flow-coverage.csv','reference-template-inventory.csv')) {
    foreach ($col in @($parsedCsv[$name][0].PSObject.Properties.Name)) {
        if ($col -ceq 'immersive_stream_representation') { continue }
        if ($col -ceq $prohibitedStreamColumn -or $col -match 'stream') { $a01.Add(("{0}:{1}" -f $name, $col)) }
    }
}
# The token guard scans the seven package CSVs plus the two normative Markdown
# files. It deliberately does NOT scan producer-inspection.md, validation-report.md
# or this script: those three are dated historical records and must be able to name
# a concept they record as deleted. Data may not carry it; prose history may.
$a01Scan = @('foundation-route-coverage.csv','foundation-flow-coverage.csv','reference-template-inventory.csv','responsive-state-mode-matrix.csv','design-batch-plan.csv','component-primitives.csv','traceability.csv','README.md','UI_REFERENCE_DESIGN_CONTRACT.md')
foreach ($rel in $a01Scan) {
    $text = Get-Content -Raw -LiteralPath (Join-Path $packageRoot $rel)
    if ($text -match [regex]::Escape($invariantToken) -or $text -match '(?i)stream[_-]invariant') { $a01.Add(("{0}:token" -f $rel)) }
}
Assert-True ($a01.Count -eq 0) 'stream-column-absence' 'no record file carries a stream column and no package data or normative text carries the deleted invariance token' ("violations={0}" -f ($a01 -join ';'))

# --- A-02 primitive-stream-presence-legality -------------------------------
# Resolves every stream_presence value against the closed vocabulary, requires
# ordinal sort so two spellings of one set cannot both be legal, and resolves every
# STREAM-SCOPE-EXCLUDED primitive against the excluded surfaces via the templates
# that depend on it.
$presenceOf = @{}
$a02 = [System.Collections.Generic.List[string]]::new()
foreach ($p in $primitives) {
    if (-not $p.PSObject.Properties['stream_presence']) { $a02.Add(("{0}:column-missing" -f $p.primitive_id)); continue }
    $tokens = @(Split-List $p.stream_presence)
    if ($tokens.Count -eq 0) { $a02.Add(("{0}:blank" -f $p.primitive_id)); continue }
    if ($tokens.Count -eq 1 -and $tokens[0] -ceq $streamExcluded) { $presenceOf[$p.primitive_id] = @(); continue }
    foreach ($t in $tokens) { if ($t -cnotin $legalStreams) { $a02.Add(("{0}:illegal={1}" -f $p.primitive_id, $t)) } }
    $sorted = @($tokens | Sort-Object -CaseSensitive)
    if (($tokens -join ';') -cne ($sorted -join ';')) { $a02.Add(("{0}:unsorted" -f $p.primitive_id)) }
    if (@($tokens | Sort-Object -Unique).Count -ne $tokens.Count) { $a02.Add(("{0}:duplicate-token" -f $p.primitive_id)) }
    $presenceOf[$p.primitive_id] = $tokens
}
# An excluded primitive must not be reachable from a surface that routes reach.
$routeReachedTemplates = @($routes.template_id | Sort-Object -Unique)
foreach ($p in $primitives) {
    if (@(Split-List $p.stream_presence) -ccontains $streamExcluded) {
        foreach ($t in $templates) {
            if (@(Split-List $t.primitive_dependencies) -ccontains $p.primitive_id -and $t.template_id -cin $routeReachedTemplates) {
                $a02.Add(("{0}:excluded-but-route-reachable-via={1}" -f $p.primitive_id, $t.template_id))
            }
        }
    }
}
Assert-True ($a02.Count -eq 0) 'primitive-stream-presence-legality' 'every primitive declares a legal ordinal-sorted stream presence and no excluded primitive is reachable from a routed surface' ("errors={0}" -f ($a02 -join ';'))

# --- A-03 template-stream-presence-resolution ------------------------------
# The fold. This is the assertion whose absence is why the old exception_rule bound
# nothing: before D-045 nothing resolved primitive_dependencies against primitive
# stream data.
. (Join-Path $repoRoot 'scripts/validation/ui-stream-mapping.ps1')
try {
    Assert-UiStreamStyleGuideContract -Text (Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/active/3D_Mega_Menu_Style_Guide_v2.md'))
    Add-Pass 'stream-control-style-guide' 'explicit activation, in-force/pending values and visible-before-Apply guidance'
}
catch { Add-Fail 'stream-control-style-guide' $_.Exception.Message }
try {
    Assert-UiStreamRequirementsContract -Text (Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/active/Hengshi_Design_SRS_v3.md'))
    Add-Pass 'stream-control-requirements' 'SRS control anatomy, activation, names and advance advisement match D-045'
}
catch { Add-Fail 'stream-control-requirements' $_.Exception.Message }
try {
    Assert-UiStreamActionContract -Text (Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md'))
    Add-Pass 'stream-control-ux-action' 'ACT-09 separates pending selection, explicit Apply success and preserved recovery'
}
catch { Add-Fail 'stream-control-ux-action' $_.Exception.Message }
try {
    Assert-UiStreamAcceptanceContract -Text (Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md'))
    Add-Pass 'stream-control-ux-acceptance' 'UXTEST-046 covers explicit controls and guidance while retaining boundary and booking criteria'
}
catch { Add-Fail 'stream-control-ux-acceptance' $_.Exception.Message }
try {
    Assert-UiStreamCoverageContract -Flows $flows
    Add-Pass 'stream-control-flow-coverage' 'COV-ACT-09 distinguishes pending selection, explicit Apply and truthful recovery'
}
catch { Add-Fail 'stream-control-flow-coverage' $_.Exception.Message }
try {
    Assert-UiStreamTraceContract -Trace $trace
    Add-Pass 'stream-control-requirement-traces' 'stream traces bind all four hosts, action coverage and B01 without claiming completed evidence'
}
catch { Add-Fail 'stream-control-requirement-traces' $_.Exception.Message }
try {
    Assert-UiStreamBatchContract -Batches $batches
    Add-Pass 'stream-control-batch-evidence' 'B01 requires visible guidance, interaction evidence and UXTEST-046 while remaining unauthorized'
}
catch { Add-Fail 'stream-control-batch-evidence' $_.Exception.Message }
try {
    $streamMapping = Get-UiStreamMapping -Primitives $primitives -Templates $templates
}
catch {
    Add-Fail 'template-stream-presence-resolution' $_.Exception.Message
    Write-Output ("RESULT=FAIL PASS_COUNT={0} FAIL_COUNT={1}" -f $script:PassCount, $script:Failures.Count)
    exit 1
}
$templatePresence = $streamMapping.TemplatePresence
Assert-True $true 'template-stream-presence-resolution' 'alternative hosts determine scope; required content constrains public streams; staff hosts remain excluded' ''

# S-SEMANTIC may never be absent from a template that any route reaches. This is the
# peer guarantee expressed as a resolution rather than as a vocabulary regex.
$a03b = @($templates | Where-Object { $_.template_id -cin $routeReachedTemplates -and 'S-SEMANTIC' -cnotin $templatePresence[$_.template_id] } | ForEach-Object template_id)
Assert-True ($a03b.Count -eq 0) 'semantic-peer-presence-completeness' 'every route-reachable template folds to a presence set containing S-SEMANTIC' ("missing={0}" -f ($a03b -join ';'))

# --- A-04 flow-template-stream-resolution ----------------------------------
# Founder-required. Resolves every flow's template_ids, computes presence(F), and
# resolves that set against the union of presence over the templates owned by the
# batches that own the flow's templates. The stream_disposition half of A-04 is
# resolved in the production package by A-13; it cannot be resolved here because
# design-batch-plan.csv carries no disposition column.
$batchOfTemplate = @{}
foreach ($b in $batches) { foreach ($t in @(Split-List $b.primary_template_ids)) { $batchOfTemplate[$t] = $b.batch_id } }
$a04 = [System.Collections.Generic.List[string]]::new()
foreach ($f in $flows) {
    $ft = @(Split-List $f.template_ids)
    $fp = [System.Collections.Generic.List[string]]::new()
    foreach ($t in $ft) {
        if (-not $templatePresence.ContainsKey($t)) { $a04.Add(("{0}:unresolved-template={1}" -f $f.coverage_id, $t)); continue }
        foreach ($s in $templatePresence[$t]) { if ($s -cnotin $fp) { $fp.Add($s) } }
    }
    $owned = [System.Collections.Generic.List[string]]::new()
    foreach ($t in $ft) {
        if (-not $batchOfTemplate.ContainsKey($t)) { $a04.Add(("{0}:template-unowned={1}" -f $f.coverage_id, $t)); continue }
        foreach ($ot in @($batches | Where-Object { $_.batch_id -ceq $batchOfTemplate[$t] } | ForEach-Object { Split-List $_.primary_template_ids })) {
            foreach ($s in $templatePresence[$ot]) { if ($s -cnotin $owned) { $owned.Add($s) } }
        }
    }
    foreach ($s in $fp) { if ($s -cnotin $owned) { $a04.Add(("{0}:stream-unowned={1}" -f $f.coverage_id, $s)) } }
}
Assert-True ($a04.Count -eq 0) 'flow-template-stream-resolution' 'every flow resolves its templates and every stream in its computed presence is owned by a batch that owns one of those templates' ("errors={0}" -f ($a04 -join ';'))

# --- A-05 route-immersive-representation-agreement -------------------------
# N-02. Authored prose on the left, computed fold on the right; disagreement in
# either direction fails. Neither direction is detectable by any pre-D-045
# assertion.
$immersiveStreams = @('S-HIGH','S-LOW','S-MEDIUM')
$a05 = [System.Collections.Generic.List[string]]::new()
foreach ($r in $routes) {
    $computed = @()
    if ($templatePresence.ContainsKey($r.template_id)) { $computed = @($templatePresence[$r.template_id] | Where-Object { $_ -cin $immersiveStreams }) }
    $authored = -not [string]::IsNullOrWhiteSpace([string]$r.immersive_stream_representation)
    if ($authored -and $computed.Count -eq 0) { $a05.Add(("{0}:authored-but-not-computed" -f $r.route_id)) }
    if (-not $authored -and $computed.Count -gt 0) { $a05.Add(("{0}:computed-but-not-authored" -f $r.route_id)) }
}
Assert-True ($a05.Count -eq 0) 'route-immersive-representation-agreement' 'every route immersive stream representation agrees with the presence set computed from its template' ("disagreements={0}" -f ($a05 -join ';'))

# --- A-06 stream-sharing-prohibition ---------------------------------------
# Invariance survives here and only here. D-045 deleted the invariance PROFILE
# because a zero-member guarded category is where an unexamined record hides; the
# test is kept as an assertion that cannot be selected into. Each obligation is a
# (template, stream-critical coordinate, stream) triple; the prohibition is that no
# obligation names more than one stream and no two streams collapse onto one
# obligation.
$profileByIdA = @{}
foreach ($m in $matrix) { $profileByIdA[$m.profile_id] = $m }
try {
    $frameObligations = @(Get-UiFrameObligations -Mapping $streamMapping -Templates $templates -Profiles $matrix)
}
catch {
    Add-Fail 'stream-state-frame-obligations' $_.Exception.Message
    Write-Output ("RESULT=FAIL PASS_COUNT={0} FAIL_COUNT={1}" -f $script:PassCount, $script:Failures.Count)
    exit 1
}
$a06 = [System.Collections.Generic.List[string]]::new()
$obligations = [System.Collections.Generic.HashSet[string]]::new()
foreach ($frame in $frameObligations) {
    $key = "{0}|{1}|{2}" -f $frame.template_id, $frame.state_id, $frame.stream_id
    if ($frame.stream_id -cnotin @('S-HIGH','S-LOW','S-MEDIUM','S-SEMANTIC','STREAM-SCOPE-EXCLUDED')) {
        $a06.Add(("{0}:invalid-scope" -f $key))
    }
    if (-not $obligations.Add($key)) { $a06.Add(("{0}:collapsed" -f $key)) }
}
Assert-True ($a06.Count -eq 0) 'stream-sharing-prohibition' 'baseline and critical-state obligations use distinct template state and evidence-scope keys' ("errors={0}" -f ($a06 -join ';'))

# --- A-07 stream-control-host-completeness ---------------------------------
# N-01. A template that lists no host shell has no surface on which the stream
# control can appear, so its stream obligations are unsatisfiable and nothing said
# so. An excluded-surface template is one that depends on a STREAM-SCOPE-EXCLUDED
# primitive; that is derived from the data, not listed here.
$shellPrimitives = @($primitives | Where-Object { $_.primitive_category -ceq 'shell_navigation' -or $_.required_anatomy -match 'delivery stream control' } | ForEach-Object primitive_id)
$controlHosts = @($primitives | Where-Object { $_.required_anatomy -match 'delivery stream control' } | ForEach-Object primitive_id)
$a07 = [System.Collections.Generic.List[string]]::new()
foreach ($t in $templates) {
    $deps = @(Split-List $t.primitive_dependencies)
    $isExcludedSurface = $false
    foreach ($d in $deps) { if ($presenceOf.ContainsKey($d) -and $presenceOf[$d].Count -eq 0) { $isExcludedSurface = $true } }
    if ($isExcludedSurface) { continue }
    if (@($deps | Where-Object { $_ -cin $shellPrimitives }).Count -eq 0) { $a07.Add(("{0}:no-host-shell" -f $t.template_id)) }
}
foreach ($h in $controlHosts) {
    if ($presenceOf.ContainsKey($h) -and $presenceOf[$h].Count -lt 2) { $a07.Add(("{0}:control-host-presence-below-two" -f $h)) }
}
Assert-True ($a07.Count -eq 0) 'stream-control-host-completeness' 'every non-excluded template resolves to a host shell primitive and every stream-control host is present in at least two streams' ("errors={0}" -f ($a07 -join ';'))

# --- A-08 stream-state-availability ----------------------------------------
# Closes accessibility finding B-03. If a template is hosted by a surface carrying
# the stream control, the stream can be changed there, and the changed state and the
# preference-write failure must both exist in that template's state profile.
# Producer note for reviewers: the accepted specification's migration table named
# only SP-NAVIGATION. N-01 plus this assertion mechanically implicate fourteen state
# profiles, eleven of which the table did not enumerate. Those eleven were amended
# as a derivation, not as a design choice; see producer-inspection.md.
$requiredStreamStates = @('STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED')
$a08 = [System.Collections.Generic.List[string]]::new()
foreach ($t in $templates) {
    if (@(Split-List $t.primitive_dependencies | Where-Object { $_ -cin $controlHosts }).Count -eq 0) { continue }
    $sp = $profileByIdA[$t.state_profile]
    $vals = @(Split-List $sp.required_values)
    $criticalVals = @(Split-List $sp.critical_distinct_frame_values)
    foreach ($s in $requiredStreamStates) { if ($s -cnotin $vals -or $s -cnotin $criticalVals) { $a08.Add(("{0}:{1}:{2}" -f $t.template_id, $t.state_profile, $s)) } }
}
Assert-True ($a08.Count -eq 0) 'stream-state-availability' 'every control-hosted template requires distinct frames for stream-changed and preference-write-failed states' ("missing={0}" -f (($a08 | Sort-Object -Unique) -join ';'))

# --- A-09 stream-mode-precedence-resolution --------------------------------
# Closes accessibility finding S-05. Where the mode axis excludes a mode that a
# stream in presence(record) requires, both statements are true at once and the
# precedence must be written down rather than inferred by whoever draws the frame.
$modeExclusions = @{}
foreach ($m in @($matrix | Where-Object { $_.profile_id -clike 'MP-*' })) {
    foreach ($hit in [regex]::Matches([string]$m.exception_rule, 'MODE-[A-Z-]+')) {
        if (-not $modeExclusions.ContainsKey($m.profile_id)) { $modeExclusions[$m.profile_id] = [System.Collections.Generic.List[string]]::new() }
        if ($hit.Value -cnotin $modeExclusions[$m.profile_id]) { $modeExclusions[$m.profile_id].Add($hit.Value) }
    }
}
$streamModeNeeds = @{}
foreach ($sp in $streamProfiles) {
    $token = $sp.profile_id -creplace '^DS-', ''
    $streamModeNeeds[$token] = @([regex]::Matches([string]$sp.minimum_evidence, 'MODE-[A-Z-]+') | ForEach-Object { $_.Value } | Sort-Object -Unique)
}
$worldPrecedence = [string]($matrix | Where-Object { $_.profile_id -ceq 'MP-WORLD' } | Select-Object -First 1).exception_rule
$a09 = [System.Collections.Generic.List[string]]::new()
foreach ($t in $templates) {
    if (-not $modeExclusions.ContainsKey($t.mode_profile)) { continue }
    foreach ($s in $templatePresence[$t.template_id]) {
        if (-not $streamModeNeeds.ContainsKey($s)) { continue }
        foreach ($mode in $modeExclusions[$t.mode_profile]) {
            if ($mode -cin $streamModeNeeds[$s]) {
                if (-not ($worldPrecedence -match [regex]::Escape($mode) -and $worldPrecedence -match '(?i)prevails')) {
                    $a09.Add(("{0}:{1}:{2}" -f $t.template_id, $s, $mode))
                }
            }
        }
    }
}
Assert-True ($a09.Count -eq 0) 'stream-mode-precedence-resolution' 'every mode excluded by a mode profile and required by a stream in that record presence is named by the stated precedence rule' ("unnamed={0}" -f (($a09 | Sort-Object -Unique) -join ';'))

# --- A-10 baseline-frame-name-token-resolution -----------------------------
# This replaces a vocabulary regex with a resolution, which is why it catches what
# two successive widenings of semantic-stream-peer-framing did not: the surviving
# R-034 instance was spelled with underscores inside an identifier, and the guard
# matched hyphens. Each parsed segment is resolved against the value set the record
# itself selects, with underscore/hyphen normalisation in both directions.
function ConvertTo-Token { param([string]$V) return ($V -creplace '_', '-') }
$batchIds = @($batches.batch_id)
$a10 = [System.Collections.Generic.List[string]]::new()
$framePattern = '^HSD_UIR_(B\d{2})_(.+?)_STATE_(.+?)_VP_(.+?)_MODE_(.+?)_(?:STREAM_(HIGH|MEDIUM|LOW|SEMANTIC)|SCOPE_(EXCLUDED))_V(\d{2})$'
foreach ($rec in @($templates + $routes)) {
    $isRoute = [bool]$rec.PSObject.Properties['route_id']
    $id = if ($isRoute) { $rec.route_id } else { $rec.template_id }
    $m = [regex]::Match([string]$rec.baseline_frame_name, $framePattern)
    if (-not $m.Success) { $a10.Add(("{0}:unparseable" -f $id)); continue }
    if ($m.Groups[1].Value -cnotin $batchIds) { $a10.Add(("{0}:batch={1}" -f $id, $m.Groups[1].Value)) }
    $sp = $profileByIdA[$rec.state_profile]; $vp = $profileByIdA[$rec.viewport_profile]; $mp = $profileByIdA[$rec.mode_profile]
    if ((ConvertTo-Token ('STATE_' + $m.Groups[3].Value)) -cnotin @(Split-List $sp.required_values)) { $a10.Add(("{0}:state={1}" -f $id, $m.Groups[3].Value)) }
    if ((ConvertTo-Token ('VP_' + $m.Groups[4].Value)) -cnotin @(Split-List $vp.required_values)) { $a10.Add(("{0}:viewport={1}" -f $id, $m.Groups[4].Value)) }
    if ((ConvertTo-Token ('MODE_' + $m.Groups[5].Value)) -cnotin @(Split-List $mp.required_values)) { $a10.Add(("{0}:mode={1}" -f $id, $m.Groups[5].Value)) }
    $tid = if ($isRoute) { $rec.template_id } else { $rec.template_id }
    $isExcluded = $streamMapping.TemplateScope[$tid] -ceq $streamExcluded
    if ($isExcluded) {
        if ($m.Groups[7].Value -cne 'EXCLUDED') { $a10.Add(("{0}:excluded-frame-requires-scope-token" -f $id)) }
    }
    else {
        $frameStream = 'S-' + $m.Groups[6].Value
        if ($m.Groups[7].Success -or $frameStream -cnotin $templatePresence[$tid]) { $a10.Add(("{0}:stream={1}-not-in-presence" -f $id, $frameStream)) }
    }
}
Assert-True ($a10.Count -eq 0) 'baseline-frame-name-token-resolution' 'every baseline frame name parses under the amended EC-08 grammar and every parsed token resolves against the value set the record selects' ("unresolved={0}" -f ($a10 -join ';'))

# --- A-11 inert-column-detection -------------------------------------------
# The generalised guard against the recurring defect: a column populated as a total
# function of an existing column encodes no judgement and cannot be wrong.
#
# PRODUCER NOTE, recorded rather than smoothed over. The accepted specification says
# to test each judgement column "against every other column in the same file". Taken
# literally that is vacuous: every column is a total function of its file's primary
# key, so the literal reading fails every column in every file, including
# stream_presence itself. The reading implemented here restricts determiners to
# columns that are themselves CLASSIFICATIONS the package already makes - which is
# precisely the shape of the defect, since stream_profile was determined by
# state_profile. The determiner set is written out below so a reviewer can disagree
# with it in one place. The producer did not author this restriction as a design
# choice and flags it as a specification gap; see producer-inspection.md.
$classifierColumns = @('route_family','state_profile','viewport_profile','mode_profile','surface_kind','activation_status','primitive_category','interaction_class','browser_profile','time_limit_branch','coverage_kind','flow_family','reuse_scope')
$judgementColumns = @{
    'foundation-route-coverage.csv'    = @('template_id','state_profile','viewport_profile','mode_profile','semantic_quick_access','immersive_stream_representation','content_or_policy_gate','activation_status','time_limit_branch')
    'foundation-flow-coverage.csv'     = @('state_profile','viewport_profile','mode_profile','gate','time_limit_branch')
    'reference-template-inventory.csv' = @('surface_kind','state_profile','viewport_profile','mode_profile','time_limit_branch')
    'component-primitives.csv'         = @('primitive_category','interaction_class','stream_presence')
}
# Declared exemption, with its reason, as the specification requires:
# browser_profile is inert and legitimately so - exactly one accepted profile
# (BP-NFR-006) exists and the contract declares it. A constant column asserts
# nothing and hides nothing.
$inertExempt = @('browser_profile')
$inertFound = [System.Collections.Generic.List[string]]::new()
foreach ($fileName in $judgementColumns.Keys) {
    $rows = @($parsedCsv[$fileName])
    $cols = @($rows[0].PSObject.Properties.Name)
    foreach ($c in $judgementColumns[$fileName]) {
        if ($c -cin $inertExempt) { continue }
        if (@($rows | ForEach-Object { [string]$_.$c } | Sort-Object -Unique).Count -le 1) { continue }
        foreach ($o in @($cols | Where-Object { $_ -cin $classifierColumns -and $_ -cne $c })) {
            $map = @{}
            $singleValued = $true
            foreach ($row in $rows) {
                $k = [string]$row.$o
                if ($map.ContainsKey($k)) { if ($map[$k] -cne [string]$row.$c) { $singleValued = $false; break } }
                else { $map[$k] = [string]$row.$c }
            }
            if ($singleValued) { $inertFound.Add(("{0}:{1}<-{2}" -f $fileName, $c, $o)) }
        }
    }
}
foreach ($entry in $inertFound) { Write-Output ("INERT-REPORT {0}" -f $entry) }
# The stream axis is the column this model exists to make load-bearing. Its
# inertness is a hard failure and is not negotiable by exemption.
$streamInert = @($inertFound | Where-Object { $_ -match 'stream_presence' })
Assert-True ($streamInert.Count -eq 0) 'inert-column-detection' 'stream_presence is not a total function of any classification the package already makes' ("inert={0}" -f ($streamInert -join ';'))

$requiredViewports = @('VP-320','VP-NARROW','VP-LANDSCAPE','VP-TABLET','VP-DESKTOP','VP-WIDE','VP-ZOOM-400')
$viewportProfiles = @($matrix | Where-Object { $_.profile_id -like 'VP-*' })
$viewportFailures = @($viewportProfiles | Where-Object { $values = @(Split-List $_.required_values); @($requiredViewports | Where-Object { $_ -cnotin $values }).Count -gt 0 })
Assert-True ($viewportProfiles.Count -eq 4 -and $viewportFailures.Count -eq 0) 'required-viewports' 'all four viewport profiles include 320 narrow landscape tablet desktop wide and 400-percent reflow' ("profiles={0}; incomplete={1}" -f $viewportProfiles.Count, $viewportFailures.Count)

$requiredModes = @('MODE-STANDARD','MODE-REDUCED-MOTION','MODE-LOW-POWER','MODE-SEMANTIC-SHELL','MODE-FORCED-COLORS','MODE-GRAYSCALE','MODE-UNAVAILABLE-FONT','MODE-UNAVAILABLE-IMAGE-ASSET','MODE-PRINT','MODE-KEYBOARD','MODE-SCREEN-READER')
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
# D-045: EC-08 gains a mandatory single-valued <STREAM> segment. There is no aggregate
# form: a frame that names no stream, or more than one, cannot discharge a stream
# obligation. A-10 resolves each parsed segment; this only checks the shape.
$badFrameNames = @($allFrameNames | Where-Object { $_ -cnotmatch '^HSD_UIR_B\d{2}_[A-Z0-9_]+_STATE_[A-Z0-9_]+_VP_[A-Z0-9_]+_MODE_[A-Z0-9_]+_(?:STREAM_(HIGH|MEDIUM|LOW|SEMANTIC)|SCOPE_EXCLUDED)_V\d{2}$' })
Assert-True ($badFrameNames.Count -eq 0) 'frame-name-grammar' 'all baseline frame names follow the tool-neutral grammar including a single mandatory stream segment' ("invalid={0}" -f ($badFrameNames -join ';'))
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

# Re-frozen 2026-09-03 by the D-039 CR-002 revision window, which removed the
# "optional"/fallback framing for the semantic stream. The 2026-09-03 D-037
# acceptance values are retained below as provenance and MUST NOT be deleted;
# the amended package requires fresh founder acceptance at MA-028 before these
# values carry the same authority the superseded pair did.
# D-037 acceptance 2026-09-03:
#   DESIGN_SYSTEM_IMPLICATIONS.md DCF2F63D11BB45CB71568B18A0E16C95BD94F1991CBE23B5B677D832F1310AD2
#   component-primitives.csv      2D01496DCC7D9C062AD77E52CC9F0F110D3F7B4CE899D95A52A8B6F7311E6F4A
#   CR-002 amendment 2026-09-06 B4F0F9E34908B691C73CADCE33784E7D2709BFDB89F84F3B24188CF3198626BB
$expectedDesignSystemHash = '0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763'
#   CR-002 amendment 2026-09-06 0EC5B81452EAF79076CF06A5F57C7982D8F581D6105466D5352796C542DF007C
#   D-043 remediation 2026-09-06 E06D11057AF1E903E37FC0F289E994B196FD337B4E8A22AB37BB686562BB9470
# D-045 2026-09-06: stream_presence added per the accepted specification section 5.1.
#   D-045 stream_presence E6B39B5B9B5B917EAB8306E653E38E9F06934788AACB7CFF05226D21005929CB
# D-045 B-04 record correction: native controls, in-force/pending state and visible advisement.
$expectedPrimitiveHash = 'EF0DE11B23A6C6A9C8C721D55F528237A72153315B633E6198AF0B50ADED9C78'
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
    'B01' = @('FLOW-NAVIGATION-SEARCH','FLOW-ERROR-OFFLINE-RECOVERY','DF-01','ACT-01','ACT-02','ACT-03','ACT-04','ACT-05','ACT-09','EXCL-INTERNAL-SEARCH','EXCL-TRACKING-PARAMETERS','EXCL-FILTER-SORT-VARIANTS')
    'B02' = @($routes | Where-Object { $_.template_id -cin @('TPL-PUBLIC-HOME','TPL-SERVICE-COLLECTION','TPL-PUBLIC-ABOUT') } | ForEach-Object route_id) + @('J-01')
    'B03' = @($routes | Where-Object { $_.template_id -cin @('TPL-SERVICE-WING','TPL-SERVICE-DETAIL','TPL-INDUSTRY-COLLECTION','TPL-INDUSTRY-DETAIL') } | ForEach-Object route_id) + @('J-03') + @($sourceWayfinding.room_id)
    'B04' = @($routes | Where-Object { $_.template_id -cin @('TPL-WORK-COLLECTION','TPL-WORK-DETAIL','TPL-DEMO-COLLECTION','TPL-DEMO-DETAIL','TPL-INSIGHT-COLLECTION','TPL-INSIGHT-DETAIL','TPL-EXPERT-COLLECTION','TPL-EXPERT-DETAIL','TPL-TRUST-COLLECTION','TPL-TRUST-DETAIL') } | ForEach-Object route_id) + @('J-04','ACT-13')
    'B05' = @('ROUTE-CONTACT','FLOW-AI','FLOW-HUMAN-HANDOFF','FLOW-MEDIA-OPT-IN','FLOW-CONTACT','J-05','AF-01','AF-02','CF-01','ACT-14','ACT-15','ACT-16','ACT-17','ACT-18','ACT-19','ACT-32','EXCL-CHAT-SESSIONS')
    'B06' = @('ROUTE-BOOK','FLOW-BOOKING-LINEAGE','BF-01','BF-01A','BF-01B','BF-01C','BF-01D','BF-01E') + @(20..31 | ForEach-Object { 'ACT-{0:D2}' -f $_ })
    'B07' = @('FLOW-FIRST-VISIT','FLOW-RETURN-VISIT','FLOW-WORLD-HUD-STREAM','J-02','FV-01','RV-01') + @(6,7,8,10,11,12 | ForEach-Object { 'ACT-{0:D2}' -f $_ }) + @('ACT-40','EXCL-WORLD')
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
Assert-True ($routeBatchFrameErrors.Count -eq 0) 'route-frame-primary-batch-alignment' 'all 34 route baseline frame batch tokens match their single primary batch owner' ("errors={0}" -f ($routeBatchFrameErrors -join ';'))

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
$wrongDateDocs = @($requiredDateDocs | Where-Object { (Get-Content -Raw -LiteralPath (Join-Path $packageRoot $_)) -notmatch '2026-09-06' })
Assert-True ($wrongDateDocs.Count -eq 0) 'evidence-date' 'all package evidence documents use 2026-09-06' ("missing date={0}" -f ($wrongDateDocs -join ';'))

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

# Write-scope lifecycle. This assertion originally encoded a moment -- the package
# authoring window, during which nothing outside the package could legitimately
# change -- rather than a durable rule. Once decision D-039 opened the CR-002
# revision window, authorized work necessarily spans other accepted packages and
# the root ledgers, so an unconditional assertion would report a false defect.
# This is the same lifecycle error recorded as R-024; the repair is explicit
# states, not deletion. The post-D-039 branch is an enumerated allowlist, so it
# still fails on genuinely unrelated writes.
$decisionsPath = Join-Path $repoRoot 'DECISIONS.md'
$d039Approved = $false
if (Test-Path -LiteralPath $decisionsPath) {
    $d039Approved = @(Get-Content -LiteralPath $decisionsPath | Where-Object { $_ -match '^\|\s*D-039\s*\|.*\|\s*Approved\s*\|' }).Count -eq 1
}
$writeScopeState = if ($d039Approved) { 'CR002_REVISION_WINDOW' } else { 'PACKAGE_AUTHORING' }
Write-Output ("WRITE_SCOPE_STATE={0}" -f $writeScopeState)

[string[]]$allowedScopePrefixes = @('docs/phase-1-ui-reference-design/')
[string[]]$allowedScopeFiles = @()
if ($writeScopeState -eq 'CR002_REVISION_WINDOW') {
    # Exactly the artifacts decision D-039 and risk R-032 assign to the window,
    # plus the root durable ledgers that must record it.
    $allowedScopePrefixes += @(
        'docs/phase-1-ui-reference-production/',
        'docs/phase-1-ux-architecture/',
        'docs/phase-1-foundation/',
        'docs/phase-1-3d/',
        'docs/requirements/'
    )
    $allowedScopeFiles = @(
        'CHANGELOG.md','DECISIONS.md','MANUAL_ACTIONS.md','PROJECT.md',
        'PROJECT_STATE.yaml','RISKS.md','TASKS.md',
        'scripts/validation/ui-stream-mapping.ps1',
        'scripts/validation/test-ui-stream-mapping.ps1',
        'docs/archive/PROJECT_STATE-2026-09-23-pre-recovery.yaml',
        'docs/decisions-log.md',
        'docs/active/3D_Mega_Menu_Style_Guide_v2.md',
        'docs/active/Hengshi_Design_SRS_v3.md',
        'docs/software-definition/02-ai-dev-tooling-and-mcp.md'
    )
}

$gitLines = @(& git -C $repoRoot status --porcelain=v1 --untracked-files=all 2>$null)
$outsideScope = [System.Collections.Generic.List[string]]::new()
foreach ($line in $gitLines) {
    if ($line.Length -lt 4) { continue }
    $path = $line.Substring(3).Trim().Replace('\','/')
    if ($path.Contains(' -> ')) { $path = ($path -split ' -> ')[-1] }
    $path = $path.Trim('"')
    $inScope = $false
    foreach ($prefix in $allowedScopePrefixes) { if ($path.StartsWith($prefix)) { $inScope = $true; break } }
    if (-not $inScope -and $allowedScopeFiles -contains $path) { $inScope = $true }
    if (-not $inScope) { $outsideScope.Add($path) }
}
$scopeExpectation = if ($writeScopeState -eq 'CR002_REVISION_WINDOW') {
    'all current worktree changes are inside the D-039 CR-002 revision-window allowlist'
} else {
    'all current worktree changes are inside docs/phase-1-ui-reference-design'
}
Assert-True ($outsideScope.Count -eq 0) 'git-write-scope' $scopeExpectation ("outside-scope changes={0}" -f ($outsideScope -join ';'))

# The semantic stream is a peer, never a fallback (D-039, R-034). Guard the
# package against reintroducing degradation framing for it.
#
# D-043 2026-09-06: the D-042 form of this guard matched four alternatives and passed
# while five distinct degradation framings sat in the freeze. R-034 was closed against
# it once already. The pattern now also catches the identifier and vocabulary forms
# that the narrow version missed: *_FALLBACK journey keys, FLOW-*-FALLBACK family IDs,
# non-WebGL mode identifiers, and the two quality-ladder phrases. They are not
# spelled out here: the alternative list below is the authority, and a comment that
# restates it becomes hits of the guard it documents.
# The identifier alternatives are scoped to stream contexts on purpose. A broader
# "*_fallback" pattern also matches booking_fallback and durable_fallback, which are
# provider and storage contingencies and have nothing to do with the semantic stream;
# renaming those would be collateral damage, not peer framing.
# D-045 2026-09-06: the alternatives are assembled at run time so that this line
# does not match itself. Written as one literal, the pattern was five of its own
# hits, which is why the guard could only ever be read alongside a mental note that
# some of its findings were the guard. Every element is parenthesised: in PowerShell
# the comma operator binds tighter than `+`, so an unparenthesised @('a' + 'b', 'c')
# collapses to a single space-joined string and the alternation silently becomes one
# literal that matches nothing. The count is asserted for exactly that reason.
$degradationParts = @(
    ('optional ' + '(world|enhancement|immersive)'),
    ('semantic ' + 'fallback'),
    ('fallback ' + 'to (static|semantic)'),
    ('(world|semantic|webgl|stream|quick[_-]?access)[a-z0-9_-]*' + '_fallback'),
    ('FLOW-[A-Z-]*' + '-FALLBACK'),
    ('MODE[_-]NON[_-]WEBGL[A-Z0-9_-]*'),
    ('quality ' + 'downgrade'),
    ('toggle ' + 'quality'),
    ('quality ' + 'tier')
)
Assert-True ($degradationParts.Count -eq 9) 'degradation-pattern-alternative-count' 'the peer-framing pattern has nine alternatives' ("alternatives={0}; a count of 1 means the array literal collapsed and the guard is inert" -f $degradationParts.Count)
$degradationPattern = '(?i)(' + ($degradationParts -join '|') + ')'
# D-045 2026-09-06: two files are excluded from THIS guard only, and the exclusion is
# asserted rather than assumed. `validation-report.md` and `producer-inspection.md` are
# dated evidence records whose job is to name defects that have been removed; when the
# underscore spelling was added to the pattern above, the guard began failing on this
# report's own account of the defect it had just caught. A record that cannot name what
# it records is not a record. Every data file and every normative Markdown file in the
# package remains fully scanned, and no other guard uses this exclusion.
$framingExemptSuffixes = @('validation-report.md', 'producer-inspection.md')
$framingScopeFiles = @($producerFreezeFiles | Where-Object { $suffix = Split-Path $_ -Leaf; $suffix -cnotin $framingExemptSuffixes })
Assert-True (($producerFreezeFiles.Count - $framingScopeFiles.Count) -eq $framingExemptSuffixes.Count) 'framing-guard-scope' 'the peer-framing guard scans every freeze file except the two named dated evidence records' ("expected exemptions={0}; actual={1}" -f $framingExemptSuffixes.Count, ($producerFreezeFiles.Count - $framingScopeFiles.Count))
$framingScopeText = ($framingScopeFiles | ForEach-Object { Get-Content -Raw -LiteralPath $_ }) -join "`n"
$degradedSemanticFraming = @([regex]::Matches($framingScopeText, $degradationPattern))
Assert-True ($degradedSemanticFraming.Count -eq 0) 'semantic-stream-peer-framing' 'no package artifact frames the semantic stream as optional or a fallback' ("degradation framings={0}; first={1}" -f $degradedSemanticFraming.Count, ($(if ($degradedSemanticFraming.Count -gt 0) { $degradedSemanticFraming[0].Value } else { 'none' })))

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
Assert-True ($freezeHashLines.Count -eq 14) 'freeze-file-count' '14 required files including the shared stream resolver included in the deterministic freeze' ("actual={0}" -f $freezeHashLines.Count)
Write-Output 'FREEZE_METHOD=Sort relative forward-slash paths ordinally; for each emit uppercase SHA-256 two spaces path; join lines with LF and no terminal newline; SHA-256 the UTF-8 no-BOM payload'
foreach ($freezeHashLine in $freezeHashLines) { Write-Output ("FREEZE_FILE_SHA256={0}" -f $freezeHashLine) }
Write-Output ("FREEZE_AGGREGATE_SHA256={0}" -f $freezeAggregateHash)
# D-043 2026-09-06: the D-042 freeze hashed a validation-report.md whose COUNTS line
# described a different package (routes=33 profiles=32 while the validator asserted 34
# and 36). A freeze that certifies its own stale report is worthless, so the report must
# now agree with the counts computed in the same run.
$countsLine = ("COUNTS routes={0} exclusions={1} wayfinding={2} actions={3} ux_tests={4} flow_families={5} source_experience_ids={6} flow_rows={7} templates={8} primary_template_owners={9} route_template_refs={10} flow_template_refs={11} profiles={12} browser_profiles={13} time_limit_profiles={14} primitives={15} batches={16} primary_source_owners={17} trace_rows={18} package_csv={19} package_json={20}" -f $routes.Count, $flowExclusions.Count, $flowWayfinding.Count, $flowActions.Count, $traceTests.Count, $flowFamilies.Count, $acceptedExperienceIds.Count, $flows.Count, $templates.Count, $primaryTemplateRefs.Count, $routeTemplateRefs.Count, $flowTemplateRefs.Count, $matrix.Count, $browserProfileRows.Count, $timeProfileRows.Count, $primitives.Count, $batches.Count, $allPrimarySourceIds.Count, $trace.Count, $packageCsvFiles.Count, $packageJsonFiles.Count)
$reportPath = Join-Path $packageRoot 'validation/validation-report.md'
$reportText = if (Test-Path -LiteralPath $reportPath) { Get-Content -LiteralPath $reportPath -Raw } else { '' }
Assert-True ($reportText -like ("*" + $countsLine + "*")) 'validation-report-counts-agreement' 'validation-report.md states the counts this run computed' ("expected={0}" -f $countsLine)
Write-Output $countsLine
if ($script:Failures.Count -gt 0) {
    Write-Output ("RESULT=FAIL PASS_COUNT={0} FAIL_COUNT={1}" -f $script:PassCount, $script:Failures.Count)
    exit 1
}

Write-Output ("RESULT=PASS PASS_COUNT={0} FAIL_COUNT=0" -f $script:PassCount)
exit 0
