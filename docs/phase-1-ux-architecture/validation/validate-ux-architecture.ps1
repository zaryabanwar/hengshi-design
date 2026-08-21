[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$script:PassCount = 0
$script:FailCount = 0
$script:Failures = [System.Collections.Generic.List[string]]::new()

function Add-Pass([string]$Message) {
    $script:PassCount++
    Write-Output "PASS: $Message"
}

function Add-Fail([string]$Message) {
    $script:FailCount++
    $script:Failures.Add($Message)
    Write-Output "FAIL: $Message"
}

function Assert-True([bool]$Condition, [string]$Message) {
    if ($Condition) { Add-Pass $Message } else { Add-Fail $Message }
}

$packageRoot = Split-Path -Parent $PSScriptRoot
$repoRoot = (Resolve-Path (Join-Path $packageRoot '..\..')).Path
$sourceRoutePath = Join-Path $repoRoot 'docs\phase-1-foundation\06-canonical-route-inventory.json'
$routeCsvPath = Join-Path $packageRoot 'route-room-parity.csv'
$exclusionCsvPath = Join-Path $packageRoot 'excluded-surfaces.csv'
$tracePath = Join-Path $packageRoot 'traceability.csv'
$wayfindingPath = Join-Path $packageRoot 'wayfinding-release-map.csv'

$requiredFiles = @(
    'README.md',
    'UX_ARCHITECTURE.md',
    'FLOWS.md',
    'STATES_AND_RECOVERY.md',
    'CONTENT_ANALYTICS_TESTS.md',
    'route-room-parity.csv',
    'excluded-surfaces.csv',
    'wayfinding-release-map.csv',
    'traceability.csv',
    'producer-inspection.md',
    'validation\validate-ux-architecture.ps1',
    'validation\validation-report.md'
)

foreach ($relative in $requiredFiles) {
    Assert-True (Test-Path -LiteralPath (Join-Path $packageRoot $relative) -PathType Leaf) "required artifact exists: $relative"
}

try {
    $source = Get-Content -Raw -LiteralPath $sourceRoutePath | ConvertFrom-Json
    Add-Pass 'source route inventory parses as JSON'
} catch {
    Add-Fail "source route inventory JSON parse failed: $($_.Exception.Message)"
    throw
}

try {
    $routes = @(Import-Csv -LiteralPath $routeCsvPath)
    $exclusions = @(Import-Csv -LiteralPath $exclusionCsvPath)
    $trace = @(Import-Csv -LiteralPath $tracePath)
    $wayfinding = @(Import-Csv -LiteralPath $wayfindingPath)
    Add-Pass 'package CSV artifacts parse'
} catch {
    Add-Fail "package CSV parse failed: $($_.Exception.Message)"
    throw
}

$sourceRoutes = @($source.routes)
$sourceExclusions = @($source.excludedSurfaces)
Assert-True ($sourceRoutes.Count -eq 33) 'source inventory contains exactly 33 routes'
Assert-True ($routes.Count -eq 33) 'UX parity contains exactly 33 route rows'
Assert-True ($sourceExclusions.Count -eq 9) 'source inventory contains exactly nine exclusions'
Assert-True ($exclusions.Count -eq 9) 'UX package contains exactly nine exclusion rows'

$sourceRouteIds = @($sourceRoutes.id | Sort-Object)
$uxRouteIds = @($routes.route_id | Sort-Object)
$missingRoutes = @($sourceRouteIds | Where-Object { $_ -notin $uxRouteIds })
$extraRoutes = @($uxRouteIds | Where-Object { $_ -notin $sourceRouteIds })
Assert-True ($missingRoutes.Count -eq 0 -and $extraRoutes.Count -eq 0) "route ID set matches source; missing=$($missingRoutes -join ';') extra=$($extraRoutes -join ';')"

$pathMismatches = foreach ($route in $routes) {
    $expected = $sourceRoutes | Where-Object id -eq $route.route_id
    if ($expected.path -ne $route.path) { "$($route.route_id):$($route.path)!=$($expected.path)" }
}
Assert-True (@($pathMismatches).Count -eq 0) "route paths match source: $($pathMismatches -join ';')"
Assert-True (@($routes.route_id | Group-Object | Where-Object Count -ne 1).Count -eq 0) 'route IDs are unique'
Assert-True (@($routes.path | Group-Object | Where-Object Count -ne 1).Count -eq 0) 'route paths are unique'

$incompleteRoutes = @($routes | Where-Object {
    [string]::IsNullOrWhiteSpace($_.semantic_quick_access) -or
    [string]::IsNullOrWhiteSpace($_.optional_immersive_representation) -or
    [string]::IsNullOrWhiteSpace($_.primary_next_actions) -or
    [string]::IsNullOrWhiteSpace($_.content_or_policy_gate)
})
Assert-True ($incompleteRoutes.Count -eq 0) "every route has semantic, immersive, action, and gate coverage: $($incompleteRoutes.route_id -join ';')"

$sourceExclusionIds = @($sourceExclusions.id | Sort-Object)
$uxExclusionIds = @($exclusions.exclusion_id | Sort-Object)
$missingExclusions = @($sourceExclusionIds | Where-Object { $_ -notin $uxExclusionIds })
$extraExclusions = @($uxExclusionIds | Where-Object { $_ -notin $sourceExclusionIds })
Assert-True ($missingExclusions.Count -eq 0 -and $extraExclusions.Count -eq 0) "exclusion ID set matches source; missing=$($missingExclusions -join ';') extra=$($extraExclusions -join ';')"
$incompleteExclusions = @($exclusions | Where-Object {
    [string]::IsNullOrWhiteSpace($_.ux_behavior) -or
    [string]::IsNullOrWhiteSpace($_.index_control) -or
    [string]::IsNullOrWhiteSpace($_.recovery_or_safe_destination)
})
Assert-True ($incompleteExclusions.Count -eq 0) "every exclusion has UX, indexing, and recovery coverage: $($incompleteExclusions.exclusion_id -join ';')"

$wingMap = @($wayfinding | Where-Object record_type -eq 'wing')
$serviceMap = @($wayfinding | Where-Object record_type -eq 'service')
Assert-True ($wayfinding.Count -eq 15 -and $wingMap.Count -eq 5 -and $serviceMap.Count -eq 10) 'wayfinding map contains exactly five wings and ten services'
Assert-True (@($wayfinding.concise_sign | Group-Object | Where-Object Count -ne 1).Count -eq 0) 'all 15 concise signs are unique'
Assert-True (@($wayfinding.room_id | Group-Object | Where-Object Count -ne 1).Count -eq 0) 'all 15 wayfinding room IDs are unique'
Assert-True (@($wayfinding.route_id | Group-Object | Where-Object Count -ne 1).Count -eq 0) 'all 15 wayfinding route IDs are unique'
$expectedWingTitles = @('AI, Data & Automation','Strategy & Transformation','Immersive & Creative','Digital Products & Growth','Cloud, Reliability & Trust') | Sort-Object
$expectedServiceTitles = @(
    'Strategy & Architecture','Platform & Product Engineering','Product Design & Experience Engineering',
    'Commerce, Content & Growth Platforms','AI Systems & Agentic Automation','Data Platforms & Analytics',
    'Spatial Computing & Immersive Platforms','Creative & Visual Design Services',
    'Cloud, DevOps & Platform Reliability','Security, Privacy & Trust Engineering'
) | Sort-Object
Assert-True ((@($wingMap.formal_title | Sort-Object) -join '|') -eq ($expectedWingTitles -join '|')) 'wayfinding contains the exact five approved wing titles'
Assert-True ((@($serviceMap.formal_title | Sort-Object) -join '|') -eq ($expectedServiceTitles -join '|')) 'wayfinding contains the exact ten approved service titles'
Assert-True (@($serviceMap | Where-Object { $_.formal_title -ne $_.accessible_semantic_title }).Count -eq 0) 'each service concise sign maps to its exact full accessible semantic title'
$wayfindingRouteMismatch = @($wayfinding | Where-Object {
    $sourceRoute = $sourceRoutes | Where-Object id -eq $_.route_id
    -not $sourceRoute -or $sourceRoute.path -ne $_.canonical_path
})
Assert-True ($wayfindingRouteMismatch.Count -eq 0) "wayfinding route IDs and paths match accepted source: $($wayfindingRouteMismatch.route_id -join ';')"
$expectedWingOrder = @('ai_data','strategy','immersive_creative','digital_products_growth','cloud_reliability_trust')
$actualWingOrder = @($wingMap | Sort-Object { [int]$_.release_ordinal } | ForEach-Object wing_key)
Assert-True (($actualWingOrder -join ',') -eq ($expectedWingOrder -join ',')) 'wing release order is AI/Data Strategy Immersive/Creative Digital/Growth Cloud/Trust'
Assert-True ((@($wingMap.release_ordinal | Sort-Object {[int]$_}) -join ',') -eq '1,2,3,4,5') 'wing release ordinals are unique and contiguous 1 through 5'
$incompleteWayfinding = @($wayfinding | Where-Object {
    [string]::IsNullOrWhiteSpace($_.formal_title) -or [string]::IsNullOrWhiteSpace($_.accessible_semantic_title) -or
    [string]::IsNullOrWhiteSpace($_.release_prerequisite) -or [string]::IsNullOrWhiteSpace($_.closed_behavior) -or
    [string]::IsNullOrWhiteSpace($_.held_content_behavior) -or [string]::IsNullOrWhiteSpace($_.opening_behavior) -or
    [string]::IsNullOrWhiteSpace($_.open_behavior)
})
Assert-True ($incompleteWayfinding.Count -eq 0) "every wayfinding entry has title prerequisite and four release states: $($incompleteWayfinding.room_id -join ';')"
Assert-True (@($wayfinding | Where-Object { $_.closed_behavior -notmatch 'canonical Quick Access page remains' -and $_.closed_behavior -notmatch 'canonical Quick Access remains' }).Count -eq 0) 'every closed wing/room preserves canonical Quick Access behavior'
Assert-True (@($wingMap | Where-Object { $_.opening_behavior -notmatch 'nonpublic|not publicly traversable' }).Count -eq 0) 'opening state never implies public-open wing activation'
Assert-True (@($wingMap | Where-Object { [int]$_.release_ordinal -gt 1 -and $_.open_behavior -notmatch 'only after' }).Count -eq 0) 'later wing open states require earlier ordinals'

$industries = @($routes | Where-Object route_id -eq 'ROUTE-INDUSTRIES')
Assert-True ($industries.Count -eq 1 -and $industries.path -eq '/industries') 'D-025 retained /industries is represented exactly once'
$readme = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'README.md')
Assert-True ($readme -match 'D-025' -and $readme -match 'supersedes' -and $readme -match 'founder_decision_pending') 'README explicitly reconciles stale /industries status through D-025'

$requiredRequirementIds = @(
    (1..12 | ForEach-Object { 'BR-{0:D3}' -f $_ }),
    (1..19 | ForEach-Object { 'FR-{0:D3}' -f $_ }),
    (1..13 | ForEach-Object { 'SEO-{0:D3}' -f $_ }),
    (1..7 | ForEach-Object { 'PUB-{0:D3}' -f $_ }),
    (1..11 | ForEach-Object { 'UX-{0:D3}' -f $_ }),
    (1..9 | ForEach-Object { 'AI-{0:D3}' -f $_ }),
    (1..10 | ForEach-Object { 'DATA-{0:D3}' -f $_ }),
    (1..10 | ForEach-Object { 'SEC-{0:D3}' -f $_ }),
    (1..8 | ForEach-Object { 'NFR-{0:D3}' -f $_ })
) | ForEach-Object { $_ }
$traceIds = @($trace.source_id)
$missingRequirementTrace = @($requiredRequirementIds | Where-Object { $_ -notin $traceIds })
Assert-True ($missingRequirementTrace.Count -eq 0) "all required foundation IDs have direct trace rows: $($missingRequirementTrace -join ';')"

$requiredDecisionIds = @('D-025','D-026','D-035')
Assert-True (@($requiredDecisionIds | Where-Object { $_ -notin $traceIds }).Count -eq 0) 'D-025 D-026 and D-035 have direct trace rows'

$allTextFiles = @(Get-ChildItem -LiteralPath $packageRoot -Recurse -File | Where-Object {
    $_.Extension -in @('.md','.csv','.ps1') -and
    $_.FullName -notmatch '[\\/](reviews|accessibility)[\\/]'
})
$allText = ($allTextFiles | ForEach-Object { Get-Content -Raw -LiteralPath $_.FullName }) -join "`n"
foreach ($gate in @('MA-002','MA-003','MA-004','MA-005','MA-006','MA-007','MA-008','MA-009','MA-010','MA-011','MA-013')) {
    Assert-True ($allText -match [regex]::Escape($gate)) "unresolved/manual gate remains visible: $gate"
}

foreach ($label in @('[APPROVED]','[PROPOSED UX]','[HYPOTHESIS]','[UNRESOLVED GATE]')) {
    Assert-True ($allText -match [regex]::Escape($label)) "status label is used: $label"
}

$actions = @(Import-Csv -LiteralPath $tracePath | Where-Object source_type -eq 'requirement')
Assert-True ($actions.Count -ge 90) 'traceability provides broad direct requirement coverage'

$stateText = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'STATES_AND_RECOVERY.md')
$actionRows = [regex]::Matches($stateText, '(?m)^\| ACT-(\d{2}) [^\r\n]+\|[^\r\n]+\|[^\r\n]+\|[^\r\n]+\|$')
Assert-True ($actionRows.Count -eq 53) 'action matrix contains exactly 53 actions with success error/pending and recovery columns'
$actionNumbers = @($actionRows | ForEach-Object { [int]$_.Groups[1].Value } | Sort-Object)
Assert-True (($actionNumbers -join ',') -eq ((1..53) -join ',')) 'action IDs ACT-01 through ACT-53 are contiguous'

$testText = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'CONTENT_ANALYTICS_TESTS.md')
$testIds = @([regex]::Matches($testText, 'UXTEST-(\d{3})') | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique)
Assert-True ($testIds.Count -eq 45) 'UX acceptance inventory contains exactly 45 unique test IDs'
Assert-True (($testIds -join ',') -eq ((1..45 | ForEach-Object { '{0:D3}' -f $_ }) -join ',')) 'UXTEST-001 through UXTEST-045 are contiguous'

$flowText = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'FLOWS.md')
$requiredStaffFlowIds = 1..13 | ForEach-Object { 'SOF-01{0}' -f [char](64 + $_) }
Assert-True (@($requiredStaffFlowIds | Where-Object { $flowText -notmatch [regex]::Escape($_) }).Count -eq 0) 'staff operation flows SOF-01A through SOF-01M are present'
foreach ($staffTerm in @('Availability on','Availability off','Queue triage','Accept governed text conversation','Decline governed text conversation','End governed text conversation','Alert failure recovery','Assignment/reassignment','Booking reconciliation','Booking exception handling','Evidence/SEO review','Knowledge release review','Audit inspection')) {
    Assert-True ($flowText -match [regex]::Escape($staffTerm)) "staff operation is explicitly defined: $staffTerm"
}

$findingIds = @('UX-DR-I1-001','UX-DR-I1-002','UX-DR-I1-003','UX-DR-I1-004','A11Y-I1-01','A11Y-I1-02','A11Y-I1-03','A11Y-I1-04','A11Y-I1-05')
Assert-True (@($findingIds | Where-Object { $_ -notin $traceIds }).Count -eq 0) 'all nine iteration-1 findings have direct traceability dispositions'

$architectureText = Get-Content -Raw -LiteralPath (Join-Path $packageRoot 'UX_ARCHITECTURE.md')
$producerDocsText = (@('README.md','UX_ARCHITECTURE.md','FLOWS.md','STATES_AND_RECOVERY.md','CONTENT_ANALYTICS_TESTS.md','traceability.csv','producer-inspection.md') |
    ForEach-Object { Get-Content -Raw -LiteralPath (Join-Path $packageRoot $_) }) -join "`n"
$noJsOverclaimPatterns = @(
    '(?i)complete (a )?(verified )?(qualified )?booking[^\r\n]{0,80}without JavaScript',
    '(?i)end[- ]to[- ]end no[- ]JavaScript (booking|transaction)',
    '(?i)no[- ]JavaScript (booking|transaction) completion (is|remains) (approved|required)'
)
$noJsOverclaimHits = @($noJsOverclaimPatterns | Where-Object { $producerDocsText -match $_ })
Assert-True ($noJsOverclaimHits.Count -eq 0) 'producer package does not overclaim end-to-end no-JavaScript booking completion'
$normalizedArchitectureText = $architectureText -replace '\s+', ' '
Assert-True ($normalizedArchitectureText -match 'complete initial semantic HTML before JavaScript' -and $normalizedArchitectureText -match 'equivalent accessible non-WebGL flow' -and $normalizedArchitectureText -match 'End-to-end transaction completion without JavaScript is not an approved requirement') 'no-JavaScript authority boundary is explicit and aligned'
Assert-True ($stateText -match 'If required script\s+fails, no lineage/challenge/write/pending/confirmation is inferred') 'script failure preserves truthful non-completion state'

$qualificationBlock = [regex]::Match($flowText, '(?is)Fields are exactly:.*?fixed-price branch').Value
$qualificationNames = @('email','organization','role','desired outcome','matched wing','desired timing')
Assert-True ($qualificationBlock -match 'exactly six required data fields' -and $qualificationBlock -match 'seven required elements total') 'qualification declares six data fields plus consent as seven total elements'
Assert-True (@($qualificationNames | Where-Object { $qualificationBlock -notmatch [regex]::Escape($_) }).Count -eq 0) 'qualification contains the exact six required data-field names'
Assert-True ($qualificationBlock -match 'Budget is\s+optional' -and $qualificationBlock -match 'name/phone/upload/account requirement') 'budget remains optional and forbidden extra requirements remain absent'
Assert-True ($producerDocsText -notmatch '(?i)seven (approved )?required fields\s*\+\s*consent') 'contradictory seven-fields-plus-consent wording is absent'

$mediaNormativeText = (@('UX_ARCHITECTURE.md','FLOWS.md','STATES_AND_RECOVERY.md','CONTENT_ANALYTICS_TESTS.md') |
    ForEach-Object { Get-Content -Raw -LiteralPath (Join-Path $packageRoot $_) }) -join "`n"
$normalizedMediaText = $mediaNormativeText -replace '\s+', ' '
$staleMediaDisjunction = '(?i)audio description\s*(or|/)\s*(a\s+)?(complete\s+)?(media|visual) alternative'
Assert-True ($mediaNormativeText -notmatch $staleMediaDisjunction) 'SC 1.2.5 audio description is never replaced by a disjunctive complete media alternative'
Assert-True ($normalizedMediaText -match 'SC 1\.2\.5 at the AA target requires audio description for every applicable item containing prerecorded video content in synchronized media') 'SC 1.2.5 AA audio-description obligation is explicit'
Assert-True ($normalizedMediaText -match 'SC 1\.2\.3.{0,120}(audio-description/media-alternative|description/media-alternative)' -and $normalizedMediaText -match 'not a substitute for SC 1\.2\.5') 'SC 1.2.3 media-alternative handling is separate and cannot substitute for SC 1.2.5'
Assert-True ($normalizedMediaText -match 'Fail when an applicable item has only a complete media alternative but lacks required SC 1\.2\.5 audio description') 'UXTEST-041 rejects complete-media-alternative-only substitution'
Assert-True ($normalizedMediaText -match 'standards-supported applicability evidence' -and $normalizedMediaText -match 'hold(s)? media activation') 'media non-applicability evidence and held-media recovery are explicit'

foreach ($obligation in @(
    'moving away before release does not trigger an action','accessible name contains the visible label text','Every dragging operation has a single-pointer non-drag alternative','24 by 24 CSS px',
    'pause, stop, or hide','three flashes','20 seconds','at least ten times',
    'audio description','live captions','programmatic input purpose','autocomplete',
    'redundant-entry exception','password managers','unaided cognitive-function test'
)) {
    Assert-True (($producerDocsText -replace '\s+', ' ') -match [regex]::Escape($obligation)) "accessibility obligation is explicit: $obligation"
}

$reviewPath = Join-Path $packageRoot 'reviews\design-review-iteration-1.md'
$auditPath = Join-Path $packageRoot 'accessibility\accessibility-audit-iteration-1.md'
$review2Path = Join-Path $packageRoot 'reviews\design-review-iteration-2.md'
$audit2Path = Join-Path $packageRoot 'accessibility\accessibility-audit-iteration-2.md'
Assert-True ((Get-FileHash -Algorithm SHA256 -LiteralPath $reviewPath).Hash -eq '6D9939DB9FAF065857EB95FBF51CF804FF851C1497069A389E7332460567EFDF') 'iteration-1 design review is unchanged'
Assert-True ((Get-FileHash -Algorithm SHA256 -LiteralPath $auditPath).Hash -eq 'DCF4F36F8A9C1F9FAD4E6F7E2E65B4EF09C30CBAA2267A64FDD28624C01F2D34') 'iteration-1 accessibility audit is unchanged'
Assert-True ((Get-FileHash -Algorithm SHA256 -LiteralPath $review2Path).Hash -eq '7AB29D4EDEC5FEF3614E0A2801686C7BDE74701B907DB0BDC961BB608C26E5C7') 'iteration-2 design review is unchanged'
Assert-True ((Get-FileHash -Algorithm SHA256 -LiteralPath $audit2Path).Hash -eq 'ED633A821C2E13F06E726E979E283E2C8FE49289FE197ACDCCA4070E1FB66F41') 'iteration-2 accessibility audit is unchanged'

$markdownFiles = @(Get-ChildItem -LiteralPath $packageRoot -Recurse -File -Filter '*.md')
$brokenLinks = [System.Collections.Generic.List[string]]::new()
foreach ($file in $markdownFiles) {
    $content = Get-Content -Raw -LiteralPath $file.FullName
    foreach ($match in [regex]::Matches($content, '\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)')) {
        $target = $match.Groups[1].Value
        if ($target -match '^(https?:|mailto:|#)') { continue }
        $decoded = [uri]::UnescapeDataString($target)
        $resolved = Join-Path $file.DirectoryName $decoded
        if (-not (Test-Path -LiteralPath $resolved)) { $brokenLinks.Add("$($file.Name) -> $target") }
    }
}
Assert-True ($brokenLinks.Count -eq 0) "all relative Markdown links resolve: $($brokenLinks -join ';')"

$secretPatterns = @(
    '(?i)\bsk-[A-Za-z0-9_-]{16,}\b',
    '(?i)\bgh[pousr]_[A-Za-z0-9]{20,}\b',
    '\bAKIA[0-9A-Z]{16}\b',
    '(?i)\bBearer\s+[A-Za-z0-9._~+/-]{20,}=*',
    '(?i)\b(password|client_secret|api[_-]?key)\s*[:=]\s*["''][^"'']{8,}["'']'
)
$secretHits = [System.Collections.Generic.List[string]]::new()
foreach ($file in $allTextFiles) {
    $content = Get-Content -Raw -LiteralPath $file.FullName
    foreach ($pattern in $secretPatterns) {
        if ($content -match $pattern) { $secretHits.Add("$($file.Name):$pattern") }
    }
}
Assert-True ($secretHits.Count -eq 0) "no secret-like values detected: $($secretHits -join ';')"

$unsupportedAssertionPattern = '(?im)\b(Hengshi Design|we)\s+(is|are)\s+(the\s+)?(world[- ]first|best|leading|unique|unrivalled|most advanced)\b'
$unsupportedHits = [System.Collections.Generic.List[string]]::new()
foreach ($file in $allTextFiles) {
    if ((Get-Content -Raw -LiteralPath $file.FullName) -match $unsupportedAssertionPattern) { $unsupportedHits.Add($file.Name) }
}
Assert-True ($unsupportedHits.Count -eq 0) "no unsupported superiority assertion detected: $($unsupportedHits -join ';')"

$forbiddenFiles = @(Get-ChildItem -LiteralPath $packageRoot -Recurse -File | Where-Object Extension -in @('.tsx','.ts','.jsx','.js','.py','.json','.svg','.png','.glb','.blend'))
Assert-True ($forbiddenFiles.Count -eq 0) "package contains no implementation/design/asset files: $($forbiddenFiles.Name -join ';')"

$status = if ($script:FailCount -eq 0) { 'PASS' } else { 'FAIL' }
Write-Output "SUMMARY: $status; pass=$($script:PassCount); fail=$($script:FailCount); routes=$($routes.Count); exclusions=$($exclusions.Count); wayfinding=$($wayfinding.Count); actions=$($actionRows.Count); tests=$($testIds.Count); traceRows=$($trace.Count)"
if ($script:Failures.Count -gt 0) {
    Write-Output 'FAILURES:'
    $script:Failures | ForEach-Object { Write-Output "- $_" }
    exit 1
}
exit 0
