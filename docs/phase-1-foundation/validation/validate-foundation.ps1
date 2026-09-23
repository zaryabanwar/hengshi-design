[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$validationDir = Split-Path -Parent $PSCommandPath
$foundationDir = Split-Path -Parent $validationDir
$repositoryRoot = (Resolve-Path (Join-Path $foundationDir '..\..')).Path
$errors = [System.Collections.Generic.List[string]]::new()
$passes = [System.Collections.Generic.List[string]]::new()

function Add-Failure {
    param([Parameter(Mandatory)][string]$Message)
    $errors.Add($Message)
}

function Add-Pass {
    param([Parameter(Mandatory)][string]$Message)
    $passes.Add($Message)
}

function Assert-True {
    param(
        [Parameter(Mandatory)][bool]$Condition,
        [Parameter(Mandatory)][string]$PassMessage,
        [Parameter(Mandatory)][string]$FailureMessage
    )

    if ($Condition) {
        Add-Pass $PassMessage
    } else {
        Add-Failure $FailureMessage
    }
}

$requiredRelativeFiles = @(
    'README.md',
    '01-product-requirements.md',
    '02-market-competitor-seo-evidence.md',
    '03-seo-entity-route-editorial-strategy.md',
    '04-conversion-measurement-model.md',
    '05-evidence-and-claims-ledger.json',
    '06-canonical-route-inventory.json',
    '07-decision-requirement-traceability.csv',
    'evidence/libreoffice-capability-2026-07-19.md'
)

foreach ($relativePath in $requiredRelativeFiles) {
    $absolutePath = Join-Path $foundationDir $relativePath
    Assert-True -Condition (Test-Path -LiteralPath $absolutePath -PathType Leaf) `
        -PassMessage "Required artifact exists: $relativePath" `
        -FailureMessage "Missing required artifact: $relativePath"
}

$requiredReviewChains = @(
    @(
        'reviews/requirements-review-iteration-1.md',
        'reviews/requirements-review-iteration-2.md'
    ),
    @(
        'reviews/seo-evidence-review-iteration-1.md',
        'reviews/seo-evidence-review-iteration-2.md'
    )
)

foreach ($reviewChain in $requiredReviewChains) {
    $missingReviewFiles = @(
        $reviewChain | Where-Object {
            -not (Test-Path -LiteralPath (Join-Path $foundationDir $_) -PathType Leaf)
        }
    )
    Assert-True -Condition ($missingReviewFiles.Count -eq 0) `
        -PassMessage "Complete independent review chain exists: $($reviewChain -join ', ')" `
        -FailureMessage "Incomplete independent review chain; missing: $($missingReviewFiles -join ', ')"
}

$requirementsPath = Join-Path $foundationDir '01-product-requirements.md'
$claimsPath = Join-Path $foundationDir '05-evidence-and-claims-ledger.json'
$routesPath = Join-Path $foundationDir '06-canonical-route-inventory.json'
$traceabilityPath = Join-Path $foundationDir '07-decision-requirement-traceability.csv'

try {
    $claims = Get-Content -Raw -LiteralPath $claimsPath | ConvertFrom-Json
    Add-Pass 'Claims ledger parses as JSON.'
} catch {
    Add-Failure "Claims ledger JSON parse failed: $($_.Exception.Message)"
    $claims = $null
}

try {
    $routes = Get-Content -Raw -LiteralPath $routesPath | ConvertFrom-Json
    Add-Pass 'Route inventory parses as JSON.'
} catch {
    Add-Failure "Route inventory JSON parse failed: $($_.Exception.Message)"
    $routes = $null
}

try {
    $traceability = @(Import-Csv -LiteralPath $traceabilityPath)
    Add-Pass 'Decision traceability parses as CSV.'
} catch {
    Add-Failure "Decision traceability CSV parse failed: $($_.Exception.Message)"
    $traceability = @()
}

$requirementsText = Get-Content -Raw -LiteralPath $requirementsPath
$requirementMatches = [regex]::Matches(
    $requirementsText,
    '(?m)^\|\s*((?:BR|FR|SEO|PUB|UX|AI|DATA|SEC|NFR|OPS)-\d{3})\s*\|'
)
$requirementIds = @($requirementMatches | ForEach-Object { $_.Groups[1].Value })
$uniqueRequirementIds = @($requirementIds | Sort-Object -Unique)
Assert-True -Condition ($requirementIds.Count -eq 114) `
    -PassMessage 'Product requirements contain 114 atomic requirement rows after review revision.' `
    -FailureMessage "Expected 114 atomic requirement rows; found $($requirementIds.Count)."
Assert-True -Condition ($uniqueRequirementIds.Count -eq $requirementIds.Count) `
    -PassMessage 'All requirement IDs are unique.' `
    -FailureMessage 'Duplicate requirement IDs were found.'

if ($null -ne $claims) {
    $claimEntries = @($claims.entries)
    $claimIds = @($claimEntries | ForEach-Object { [string]$_.id })
    $uniqueClaimIds = @($claimIds | Sort-Object -Unique)
    Assert-True -Condition ($claimEntries.Count -eq 33) `
        -PassMessage 'Claims ledger contains 33 evidence entries.' `
        -FailureMessage "Expected 33 claims entries; found $($claimEntries.Count)."
    Assert-True -Condition ($uniqueClaimIds.Count -eq $claimIds.Count) `
        -PassMessage 'All claims-ledger IDs are unique.' `
        -FailureMessage 'Duplicate claims-ledger IDs were found.'

    $allowedDispositions = @(
        'eligible_after_phase_1_and_publication_approval',
        'hold_until_verified',
        'internal_only',
        'quarantine',
        'reference_only'
    )
    $invalidDispositions = @($claimEntries | Where-Object { [string]$_.publicDisposition -notin $allowedDispositions })
    Assert-True -Condition ($invalidDispositions.Count -eq 0) `
        -PassMessage 'Every claims-ledger entry uses an allowed fail-closed disposition.' `
        -FailureMessage "Invalid claims dispositions: $(($invalidDispositions | ForEach-Object { [string]$_.id }) -join ', ')"

    $unverifiedStatusPattern = '(?i)(unverified|missing|placeholder|unsupported|not_cleared|none_verified|none_assigned|filename_and_label_only|reference_only)'
    $unsafeUnverified = @(
        $claimEntries | Where-Object {
            ([string]$_.evidenceStatus -match $unverifiedStatusPattern) -and
            ([string]$_.publicDisposition -eq 'eligible_after_phase_1_and_publication_approval')
        }
    )
    Assert-True -Condition ($unsafeUnverified.Count -eq 0) `
        -PassMessage 'Unverified, missing, unsupported, placeholder, and reference-only evidence is not marked publication-eligible.' `
        -FailureMessage "Unsafe publication eligibility for evidence entries: $(($unsafeUnverified | ForEach-Object { [string]$_.id }) -join ', ')"

    $seedSubjects = @('Atlas', 'Vertex', 'Signal', 'Drift', 'Lumen', 'Aegis')
    $seedEntryText = @(
        $claimEntries |
            Where-Object { [string]$_.evidenceStatus -eq 'prototype_seed_unverified' } |
            ForEach-Object { [string]$_.subject }
    ) -join ' '
    $missingSeeds = @($seedSubjects | Where-Object { $seedEntryText -notmatch [regex]::Escape($_) })
    Assert-True -Condition ($missingSeeds.Count -eq 0) `
        -PassMessage 'All six prototype seeds are explicitly represented in the quarantine ledger.' `
        -FailureMessage "Prototype seeds missing from the quarantine ledger: $($missingSeeds -join ', ')"
}

if ($null -ne $routes) {
    $routeEntries = @($routes.routes)
    $excludedSurfaces = @($routes.excludedSurfaces)
    $routeIds = @($routeEntries | ForEach-Object { [string]$_.id })
    $routePaths = @($routeEntries | ForEach-Object { [string]$_.path })
    Assert-True -Condition ([int]$routes.schemaVersion -eq 2) `
        -PassMessage 'Route inventory uses the reviewed state-separated schema version 2.' `
        -FailureMessage "Expected route inventory schemaVersion 2; found $($routes.schemaVersion)."
    Assert-True -Condition ([string]$routes.canonicalHost -eq 'https://hengshidesign.com') `
        -PassMessage 'Canonical host matches the approved proposal.' `
        -FailureMessage "Unexpected canonical host: $($routes.canonicalHost)"
    Assert-True -Condition ($routeEntries.Count -eq 34) `
        -PassMessage 'Route inventory contains 34 unique routes and patterns.' `
        -FailureMessage "Expected 34 routes and patterns; found $($routeEntries.Count)."
    Assert-True -Condition (@($routeIds | Sort-Object -Unique).Count -eq $routeIds.Count) `
        -PassMessage 'All route IDs are unique.' `
        -FailureMessage 'Duplicate route IDs were found.'
    Assert-True -Condition (@($routePaths | Sort-Object -Unique).Count -eq $routePaths.Count) `
        -PassMessage 'All route paths are unique.' `
        -FailureMessage 'Duplicate route paths were found.'

    $requiredRouteStateFields = @(
        'plannedCanonicalStatus',
        'contentApprovalStatus',
        'releaseActivationStatus',
        'indexabilityPolicy',
        'activeSitemap',
        'futureSitemapRule'
    )
    $routesMissingState = @(
        foreach ($route in $routeEntries) {
            $propertyNames = @($route.PSObject.Properties.Name)
            $missingFields = @(
                $requiredRouteStateFields | Where-Object {
                    ($_ -notin $propertyNames) -or
                    (($_ -ne 'activeSitemap') -and [string]::IsNullOrWhiteSpace([string]$route.$_))
                }
            )
            if ($missingFields.Count -gt 0) {
                [pscustomobject]@{ id = [string]$route.id; fields = ($missingFields -join ',') }
            }
        }
    )
    Assert-True -Condition ($routesMissingState.Count -eq 0) `
        -PassMessage 'Every planned route separates canonical, content, release, indexability, and active-sitemap state.' `
        -FailureMessage "Routes missing state fields: $(($routesMissingState | ForEach-Object { "$($_.id):$($_.fields)" }) -join '; ')"

    $legacyRouteStateProperties = @(
        $routeEntries | Where-Object {
            $names = @($_.PSObject.Properties.Name)
            ('approvalStatus' -in $names) -or ('indexability' -in $names) -or ('sitemap' -in $names)
        }
    )
    Assert-True -Condition ($legacyRouteStateProperties.Count -eq 0) `
        -PassMessage 'No route retains the ambiguous legacy approvalStatus/indexability/sitemap fields.' `
        -FailureMessage "Routes retain legacy state fields: $(($legacyRouteStateProperties | ForEach-Object { [string]$_.id }) -join ', ')"

    $activePlanningRoutes = @(
        $routeEntries | Where-Object {
            ([bool]$_.activeSitemap) -or
            ([string]$_.releaseActivationStatus -ne 'inactive_no_approved_release')
        }
    )
    Assert-True -Condition ($activePlanningRoutes.Count -eq 0) `
        -PassMessage 'No planned route is serialized as release-active or in the active sitemap.' `
        -FailureMessage "Planning routes incorrectly active: $(($activePlanningRoutes | ForEach-Object { [string]$_.id }) -join ', ')"

    $activationSnapshotValid =
        ($null -eq $routes.activationSnapshot.approvedPublicationChecksum) -and
        (@($routes.activationSnapshot.contentApprovedRouteIds).Count -eq 0) -and
        (@($routes.activationSnapshot.releaseActiveRouteIds).Count -eq 0) -and
        (@($routes.activationSnapshot.activeSitemapRouteIds).Count -eq 0)
    Assert-True -Condition $activationSnapshotValid `
        -PassMessage 'The planning snapshot has no approved checksum, content-approved route, active route, or active-sitemap member.' `
        -FailureMessage 'The planning snapshot incorrectly claims current content/release/sitemap activation.'

    $invalidPathShape = @(
        $routeEntries | Where-Object {
            $path = [string]$_.path
            ($path -cne $path.ToLowerInvariant()) -or
            (($path -ne '/') -and $path.EndsWith('/')) -or
            (-not $path.StartsWith('/'))
        }
    )
    Assert-True -Condition ($invalidPathShape.Count -eq 0) `
        -PassMessage 'All route paths are lowercase, root-relative, and have no trailing slash except root.' `
        -FailureMessage "Invalid route path shape: $(($invalidPathShape | ForEach-Object { [string]$_.path }) -join ', ')"

    $allowedSchemaTypes = @($routes.allowedStructuredDataTypes | ForEach-Object { [string]$_ })
    $invalidSchemas = @(
        $routeEntries | ForEach-Object {
            $route = $_
            @($route.schemaTypes) | Where-Object { [string]$_ -notin $allowedSchemaTypes } | ForEach-Object {
                [pscustomobject]@{ id = $route.id; schema = [string]$_ }
            }
        }
    )
    Assert-True -Condition ($invalidSchemas.Count -eq 0) `
        -PassMessage 'All route schema types are within the approved truthful schema allowlist.' `
        -FailureMessage "Disallowed route schema types: $(($invalidSchemas | ForEach-Object { "$($_.id):$($_.schema)" }) -join ', ')"

    $industriesHub = @($routeEntries | Where-Object { [string]$_.path -eq '/industries' })
    Assert-True -Condition (
        ($industriesHub.Count -eq 1) -and
        ([string]$industriesHub[0].plannedCanonicalStatus -eq 'founder_decision_pending') -and
        ([string]$industriesHub[0].contentApprovalStatus -eq 'blocked_by_founder_route_decision_and_content_approval') -and
        (-not [bool]$industriesHub[0].activeSitemap)
    ) `
        -PassMessage 'The derived /industries hub remains explicitly gated for founder review.' `
        -FailureMessage 'The /industries route is absent, duplicated, or no longer marked as a founder-review proposal.'

    $excludedSurfaceCount = $excludedSurfaces.Count
    $excludedIds = @($excludedSurfaces | ForEach-Object { [string]$_.id })
    Assert-True -Condition ($excludedSurfaceCount -eq 9) `
        -PassMessage 'Route inventory records nine deterministic excluded-surface classes.' `
        -FailureMessage "Expected nine excluded-surface classes; found $excludedSurfaceCount."
    Assert-True -Condition (@($excludedIds | Sort-Object -Unique).Count -eq $excludedIds.Count) `
        -PassMessage 'All excluded-surface IDs are unique.' `
        -FailureMessage 'Duplicate excluded-surface IDs were found.'

    $ambiguousIndexability = @(
        @($routeEntries) + @($excludedSurfaces) | Where-Object {
            [string]$_.indexabilityPolicy -match '(?i)(?:^|_)or(?:_|$)'
        }
    )
    Assert-True -Condition ($ambiguousIndexability.Count -eq 0) `
        -PassMessage 'No route or exclusion uses an ambiguous *_or_* indexability policy.' `
        -FailureMessage "Ambiguous indexability policies: $(($ambiguousIndexability | ForEach-Object { [string]$_.id }) -join ', ')"

    $queryClassIds = @(
        'EXCL-INTERNAL-SEARCH',
        'EXCL-TRACKING-PARAMETERS',
        'EXCL-FILTER-SORT-VARIANTS'
    )
    $queryClasses = @($excludedSurfaces | Where-Object { [string]$_.id -in $queryClassIds })
    $missingQueryClassIds = @($queryClassIds | Where-Object { $_ -notin @($queryClasses.id) })
    $queryClassesMissingRules = @(
        foreach ($queryClass in $queryClasses) {
            $propertyNames = @($queryClass.PSObject.Properties.Name)
            $requiredFields = @(
                'statusPolicy',
                'canonicalMode',
                'canonicalPolicy',
                'internalLinkPolicy',
                'parameterAllowlist',
                'parameterRule',
                'activeSitemap'
            )
            $missingFields = @($requiredFields | Where-Object { $_ -notin $propertyNames })
            if ($missingFields.Count -gt 0) {
                [pscustomobject]@{ id = [string]$queryClass.id; fields = ($missingFields -join ',') }
            }
        }
    )
    Assert-True -Condition (($missingQueryClassIds.Count -eq 0) -and ($queryClassesMissingRules.Count -eq 0)) `
        -PassMessage 'Internal-search, tracking, and filter/sort classes each define status, canonical, link, parameter, and sitemap rules.' `
        -FailureMessage "Query-class rule gaps. Missing classes: $($missingQueryClassIds -join ', '); missing fields: $(($queryClassesMissingRules | ForEach-Object { "$($_.id):$($_.fields)" }) -join '; ')"

    $conflictingNoindexCanonicals = @(
        $queryClasses | Where-Object {
            ([string]$_.indexabilityPolicy -match '(?i)noindex') -and
            ([string]$_.canonicalMode -eq 'clean_document')
        }
    )
    Assert-True -Condition ($conflictingNoindexCanonicals.Count -eq 0) `
        -PassMessage 'No query class combines noindex with a clean-document canonical mode.' `
        -FailureMessage "Undocumented noindex/canonical conflicts: $(($conflictingNoindexCanonicals | ForEach-Object { [string]$_.id }) -join ', ')"

    $trackingClass = @($queryClasses | Where-Object { [string]$_.id -eq 'EXCL-TRACKING-PARAMETERS' })
    $expectedTrackingParameters = @('utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'msclkid')
    $trackingAllowlistValid =
        ($trackingClass.Count -eq 1) -and
        (@(Compare-Object -ReferenceObject $expectedTrackingParameters -DifferenceObject @($trackingClass[0].parameterAllowlist)).Count -eq 0)
    Assert-True -Condition $trackingAllowlistValid `
        -PassMessage 'The recognized tracking-parameter allowlist is explicit and exact.' `
        -FailureMessage 'The tracking-parameter allowlist is absent or differs from the reviewed inventory.'
}

$expectedDecisions = 1..24 | ForEach-Object { 'D-{0:D3}' -f $_ }
$actualDecisions = @($traceability | ForEach-Object { [string]$_.decision_id })
Assert-True -Condition ($traceability.Count -eq 24) `
    -PassMessage 'Traceability matrix contains 24 decision rows.' `
    -FailureMessage "Expected 24 traceability rows; found $($traceability.Count)."
Assert-True -Condition (@($actualDecisions | Sort-Object -Unique).Count -eq $actualDecisions.Count) `
    -PassMessage 'All traceability decision IDs are unique.' `
    -FailureMessage 'Duplicate decision IDs were found in traceability.'
$missingDecisions = @($expectedDecisions | Where-Object { $_ -notin $actualDecisions })
$unexpectedDecisions = @($actualDecisions | Where-Object { $_ -notin $expectedDecisions })
Assert-True -Condition (($missingDecisions.Count -eq 0) -and ($unexpectedDecisions.Count -eq 0)) `
    -PassMessage 'Traceability covers exactly D-001 through D-024.' `
    -FailureMessage "Traceability decision mismatch. Missing: $($missingDecisions -join ', '); unexpected: $($unexpectedDecisions -join ', ')."

$traceRequirementIds = @(
    $traceability | ForEach-Object {
        ([string]$_.requirement_ids -split ';') | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    } | Sort-Object -Unique
)
$unknownTraceRequirementIds = @($traceRequirementIds | Where-Object { $_ -notin $uniqueRequirementIds })
Assert-True -Condition ($unknownTraceRequirementIds.Count -eq 0) `
    -PassMessage 'Every requirement referenced by decision traceability exists in the product requirements.' `
    -FailureMessage "Unknown requirement IDs in traceability: $($unknownTraceRequirementIds -join ', ')"

$emptyTraceFields = @(
    $traceability | Where-Object {
        [string]::IsNullOrWhiteSpace([string]$_.decision_id) -or
        [string]::IsNullOrWhiteSpace([string]$_.requirement_ids) -or
        [string]::IsNullOrWhiteSpace([string]$_.foundation_artifacts) -or
        [string]::IsNullOrWhiteSpace([string]$_.acceptance_evidence) -or
        [string]::IsNullOrWhiteSpace([string]$_.coverage_status) -or
        [string]::IsNullOrWhiteSpace([string]$_.open_gate_or_next_slice)
    }
)
Assert-True -Condition ($emptyTraceFields.Count -eq 0) `
    -PassMessage 'Every traceability row names requirements, artifacts, evidence, status, and an open gate or next slice.' `
    -FailureMessage "Traceability rows with missing fields: $(($emptyTraceFields | ForEach-Object { [string]$_.decision_id }) -join ', ')"

$markdownFiles = @(Get-ChildItem -LiteralPath $foundationDir -Recurse -File -Filter '*.md')
$brokenLocalLinks = [System.Collections.Generic.List[string]]::new()
foreach ($markdownFile in $markdownFiles) {
    $markdown = Get-Content -Raw -LiteralPath $markdownFile.FullName
    foreach ($match in [regex]::Matches($markdown, '\]\((?<target>[^)]+)\)')) {
        $target = $match.Groups['target'].Value.Trim()
        if (
            $target -match '^(?i:https?://|mailto:|tel:)' -or
            $target.StartsWith('#') -or
            $target.StartsWith('<http')
        ) {
            continue
        }

        $pathOnly = ($target -split '#', 2)[0]
        if ([string]::IsNullOrWhiteSpace($pathOnly)) {
            continue
        }
        $decodedPath = [uri]::UnescapeDataString($pathOnly.Trim('<', '>'))
        $resolvedTarget = Join-Path $markdownFile.DirectoryName $decodedPath
        if (-not (Test-Path -LiteralPath $resolvedTarget)) {
            $brokenLocalLinks.Add("$($markdownFile.FullName): $target")
        }
    }
}
Assert-True -Condition ($brokenLocalLinks.Count -eq 0) `
    -PassMessage 'All local Markdown links resolve.' `
    -FailureMessage "Broken local Markdown links: $($brokenLocalLinks -join '; ')"

$draftMarkers = @(
    Get-ChildItem -LiteralPath $foundationDir -Recurse -File |
        Where-Object { $_.Extension -in @('.md', '.json', '.csv') } |
        Select-String -Pattern '\b(TODO|TBD|FIXME)\b|changeme' -CaseSensitive:$false
)
Assert-True -Condition ($draftMarkers.Count -eq 0) `
    -PassMessage 'No unresolved TODO, TBD, FIXME, or changeme markers were found.' `
    -FailureMessage "Unresolved drafting markers: $(($draftMarkers | ForEach-Object { "$($_.Path):$($_.LineNumber)" }) -join ', ')"

$secretPatterns = [ordered]@{
    private_key_material = ('-----BEGIN ' + '(?:(?:RSA|EC|OPENSSH) )?PRIVATE KEY-----')
    aws_access_key = '\bAKIA[0-9A-Z]{16}\b'
    github_token = '\b(?:(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,})\b'
    openai_token = '\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b'
    slack_token = '\bxox[baprs]-[A-Za-z0-9-]{20,}\b'
    azure_storage_connection_string = '(?i)DefaultEndpointsProtocol=https?;[^\r\n]{0,500}\bAccountKey='
    credentialed_database_url = '(?i)\b(?:postgres(?:ql)?|mysql|mariadb|mongodb(?:\+srv)?)://[^\s:/@]+:[^\s/@]{8,}@'
    secret_assignment = '(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password|connection[_-]?string)\b\s*[:=]\s*["'']?[A-Za-z0-9+/=_.-]{16,}'
}
$secretFindings = [System.Collections.Generic.List[object]]::new()
$secretScanFiles = @(
    Get-ChildItem -LiteralPath $foundationDir -Recurse -File |
        Where-Object { $_.Extension -in @('.md', '.json', '.csv', '.ps1', '.yaml', '.yml', '.toml') }
)
foreach ($secretScanFile in $secretScanFiles) {
    $lineNumber = 0
    foreach ($line in Get-Content -LiteralPath $secretScanFile.FullName) {
        $lineNumber++
        foreach ($secretPattern in $secretPatterns.GetEnumerator()) {
            if ($line -match $secretPattern.Value) {
                $secretFindings.Add([pscustomobject]@{
                    kind = $secretPattern.Key
                    path = $secretScanFile.FullName
                    line = $lineNumber
                })
            }
        }
    }
}
$secretLocations = @(
    $secretFindings | ForEach-Object { "$($_.kind) at $($_.path):$($_.line)" }
)
Assert-True -Condition ($secretFindings.Count -eq 0) `
    -PassMessage 'No common secret-shaped value patterns were detected.' `
    -FailureMessage "Potential secret-shaped values detected; values suppressed. Stop and inspect securely: $($secretLocations -join '; ')"

$trailingWhitespace = @(
    $validationFiles = @(
        Get-ChildItem -LiteralPath $foundationDir -Recurse -File |
            Where-Object { $_.Extension -in @('.md', '.json', '.csv', '.ps1') }
    )
    foreach ($validationFile in $validationFiles) {
        if ($validationFile.Extension -eq '.md') {
            # Exactly two trailing spaces are a valid CommonMark hard break.
            Select-String -LiteralPath $validationFile.FullName -Pattern '(?<! ) $| {3,}$|\t+[ ]*$'
        } else {
            Select-String -LiteralPath $validationFile.FullName -Pattern '[ \t]+$'
        }
    }
)
Assert-True -Condition ($trailingWhitespace.Count -eq 0) `
    -PassMessage 'No invalid trailing whitespace was found; CommonMark two-space hard breaks are allowed.' `
    -FailureMessage "Invalid trailing whitespace found at: $(($trailingWhitespace | ForEach-Object { "$($_.Path):$($_.LineNumber)" }) -join ', ')"

# Discard git's stderr rather than merging it into the error stream. This repo
# stores CRLF blobs with core.autocrlf=true, so git emits a benign
# "LF will be replaced by CRLF" warning for any modified file here; merged with
# 2>&1 that warning surfaces as a terminating NativeCommandError and aborts the
# run before any RESULT line is written. The exit code still carries the real
# whitespace verdict, which is what this assertion is about.
$previousErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
$gitDiffCheckOutput = @(& git -C $repositoryRoot diff --check -- 'docs/phase-1-foundation' 2>$null)
$gitDiffCheckExit = $LASTEXITCODE
$ErrorActionPreference = $previousErrorActionPreference
Assert-True -Condition ($gitDiffCheckExit -eq 0) `
    -PassMessage 'git diff --check reports no whitespace errors in tracked foundation changes.' `
    -FailureMessage "git diff --check failed: $($gitDiffCheckOutput -join [Environment]::NewLine)"

Write-Output 'Hengshi Design Phase 1 foundation validation'
Write-Output "Foundation: $foundationDir"
Write-Output "Passes: $($passes.Count)"
foreach ($message in $passes) {
    Write-Output "PASS: $message"
}

if ($errors.Count -gt 0) {
    Write-Output "Failures: $($errors.Count)"
    foreach ($message in $errors) {
        Write-Error "FAIL: $message"
    }
    exit 1
}

Write-Output 'RESULT: PASS'
exit 0
