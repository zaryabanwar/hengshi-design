[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$validationDir = Split-Path -Parent $PSCommandPath
$strategyDir = Split-Path -Parent $validationDir
$repositoryRoot = (Resolve-Path (Join-Path $strategyDir '..\..')).Path
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

function Assert-ContainsAll {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string[]]$Values,
        [Parameter(Mandatory)][string]$Label
    )
    $missing = @($Values | Where-Object { $Text -notmatch [regex]::Escape($_) })
    Assert-True -Condition ($missing.Count -eq 0) `
        -PassMessage "$Label coverage is complete." `
        -FailureMessage "$Label coverage is missing: $($missing -join ', ')"
}

$requiredRelativeFiles = @(
    'README.md',
    '01-audience-and-buying-context.md',
    '02-strategic-directions.md',
    '03-BRAND_STRATEGY.md',
    '04-messaging-architecture.md',
    '05-naming-claims-and-terminology.md',
    '06-reference-accessibility-and-implementation.md',
    '07-traceability.csv',
    'producer-inspection.md',
    'validation/validation-report.md',
    'validation/validate-brand-strategy.ps1'
)

foreach ($relativePath in $requiredRelativeFiles) {
    Assert-True -Condition (Test-Path -LiteralPath (Join-Path $strategyDir $relativePath) -PathType Leaf) `
        -PassMessage "Required artifact exists: $relativePath" `
        -FailureMessage "Missing required artifact: $relativePath"
}

$readme = Get-Content -Raw -LiteralPath (Join-Path $strategyDir 'README.md')
$audience = Get-Content -Raw -LiteralPath (Join-Path $strategyDir '01-audience-and-buying-context.md')
$directions = Get-Content -Raw -LiteralPath (Join-Path $strategyDir '02-strategic-directions.md')
$brand = Get-Content -Raw -LiteralPath (Join-Path $strategyDir '03-BRAND_STRATEGY.md')
$messages = Get-Content -Raw -LiteralPath (Join-Path $strategyDir '04-messaging-architecture.md')
$claims = Get-Content -Raw -LiteralPath (Join-Path $strategyDir '05-naming-claims-and-terminology.md')
$implementation = Get-Content -Raw -LiteralPath (Join-Path $strategyDir '06-reference-accessibility-and-implementation.md')

Assert-ContainsAll -Text $readme -Label 'README section' -Values @(
    '## Scope and authority',
    '## Artifact map',
    '## Fixed strategic inputs',
    '## Acceptance boundary',
    '## Compact founder decision presentation'
)

Assert-ContainsAll -Text $audience -Label 'Audience artifact' -Values @(
    '## Evidence boundary',
    '## Approved primary audience',
    '## Decision context',
    '## Buying-context hypotheses',
    '## Sector context',
    '## Research and validation backlog'
)

Assert-ContainsAll -Text $directions -Label 'Strategic direction' -Values @(
    '## Category frame',
    '## Direction A — Evidence in Motion (recommended)',
    '## Direction B — Assurance Architecture',
    '## Direction C — Immersive Catalyst',
    '## Decision matrix',
    '## Recommendation rationale',
    '## Founder gate'
)

Assert-ContainsAll -Text $brand -Label 'Brand strategy section' -Values @(
    '## Purpose',
    '## Audience',
    '## Positioning',
    '## Brand promise',
    '## Strategic differentiation',
    '## Brand pillars',
    '## Promise-to-proof architecture',
    '## Personality',
    '## Voice',
    '## Messaging hierarchy',
    '## Decision rationale',
    '## Approval and departure boundary'
)

$routeFamilies = @(
    '| Home |',
    '| Services |',
    '| Industries |',
    '| Agriculture |',
    '| Mining |',
    '| Work |',
    '| Demos |',
    '| Insights |',
    '| Experts |',
    '| Trust |',
    '| About |',
    '| Contact |',
    '| Book |'
)
Assert-ContainsAll -Text $messages -Values $routeFamilies -Label 'Route-family message'

$wingNames = @(
    'Strategy & Transformation',
    'Digital Products & Growth',
    'AI, Data & Automation',
    'Immersive & Creative',
    'Cloud, Reliability & Trust'
)
$serviceNames = @(
    'Strategy & Architecture',
    'Platform & Product Engineering',
    'Product Design & Experience Engineering',
    'Commerce, Content & Growth Platforms',
    'AI Systems & Agentic Automation',
    'Data Platforms & Analytics',
    'Spatial Computing & Immersive Platforms',
    'Creative & Visual Design Services',
    'Cloud, DevOps & Platform Reliability',
    'Security, Privacy & Trust Engineering'
)
Assert-ContainsAll -Text $claims -Values $wingNames -Label 'Exact wing name'
Assert-ContainsAll -Text $claims -Values $serviceNames -Label 'Exact formal service name'
Assert-ContainsAll -Text $claims -Values @(
    'Agriculture',
    'Mining',
    'Defense',
    'Industries'
) -Label 'Sector and parent name'

Assert-ContainsAll -Text $claims -Label 'Collection distinction' -Values @(
    '**Work** / **Verified Work**',
    '**Demos** / **Hengshi-owned capability demonstrations**',
    '**Insights**',
    '**Experts**',
    '**Trust** / **Trust Center**'
)

Assert-ContainsAll -Text $claims -Label 'Prohibited-claim safeguard' -Values @(
    'Novelty or superiority',
    'Client and social proof',
    'Outcomes and performance',
    'Geographic/operating footprint',
    'Trust and assurance',
    'AI operation',
    'Sector history',
    'Pricing and commitments',
    'Legal/entity facts',
    'Defense'
)

Assert-ContainsAll -Text $claims -Label 'Critical prohibited term' -Values @(
    'world-first',
    'best',
    'leading',
    'Atlanta HQ',
    'guaranteed ROI',
    'fixed package',
    '99.9% SLA achieved'
)

Assert-ContainsAll -Text $implementation -Label 'Reference synthesis' -Values @(
    'ScienceSoft',
    'Lusion',
    'Bruno Simon',
    'Active Theory',
    'Do not copy or infer'
)

Assert-ContainsAll -Text $implementation -Label 'Accessibility and cultural risk' -Values @(
    '## Accessibility implications for later identity',
    '## SEO and entity implications for later identity',
    '## Cultural and sector risks',
    '## Implementability for downstream teams',
    'WCAG 2.2 AA',
    'reduced-motion',
    'non-WebGL',
    'architectural mineral-neutral'
)

Assert-True -Condition (
    ($brand -match 'Evidence-led innovation delivery partner') -and
    ($brand -match 'From complex ambition to accountable delivery') -and
    ($messages -match '\*\*Primary CTA:\*\* Book a 30-minute discovery conversation\.') -and
    ($messages -match '\*\*Internal outcome:\*\* A verified, consented, confirmed 30-minute qualified\s+discovery booking') -and
    ($messages -match 'Email\s+ownership is verified before slot selection, and the booking is confirmed only\s+after durable provider reconciliation')
) -PassMessage 'Recommended category, promise, qualified-booking outcome, visitor CTA, and booking states are aligned.' `
  -FailureMessage 'Category, promise, qualified-booking outcome, visitor CTA, or booking-state wording is missing.'

Assert-True -Condition (
    ($readme -match 'Brand identity remains blocked') -and
    ($directions -match 'Brand identity remains blocked') -and
    ($brand -match 'Founder approval is required') -and
    ($directions -match 'After a clean independent review, approve the fully elaborated\s+\*\*Evidence in Motion\*\* strategy') -and
    ($directions -match 'no unresolved CRITICAL, HIGH, or\s+MEDIUM finding')
) -PassMessage 'Founder approval and identity-blocked boundaries are explicit.' `
  -FailureMessage 'Founder approval or identity-blocked boundary is incomplete.'

$unsafeAlternativeApproval = [regex]::Matches(
    $directions,
    '(?im)^-\s.*\*\*[BC]\*\*.*\bApprove\b'
)
Assert-True -Condition (
    ($unsafeAlternativeApproval.Count -eq 0) -and
    ($directions -match '\*\*B\*\* — Prefer \*\*Assurance Architecture\*\*') -and
    ($directions -match '\*\*C\*\* — Prefer \*\*Immersive Catalyst\*\*') -and
    ($directions -match 'directional preference,\s+not strategy approval') -and
    ($readme -match 'bounded\s+reconciliation of the A-specific strategy, messaging, and implementation') -and
    ($messages -match 'B or C preference requires bounded reconciliation') -and
    ($implementation -match 'C preference requires bounded reconciliation') -and
    ($brand -match 'deterministic revalidation, and a new\s+independent review before approval')
) -PassMessage 'B/C are preference-only choices with reconciliation, revalidation, re-review, and identity-block safeguards.' `
  -FailureMessage 'B/C preference semantics or required reconciliation/re-review safeguards are incomplete.'

$semanticProducerFiles = @(
    Get-ChildItem -LiteralPath $strategyDir -Recurse -File |
        Where-Object {
            ($_.Extension -in @('.md', '.csv')) -and
            ($_.FullName -notmatch '[\\/]reviews[\\/]')
        }
)
$semanticProducerText = ($semanticProducerFiles | ForEach-Object {
    Get-Content -Raw -LiteralPath $_.FullName
}) -join [Environment]::NewLine
$verifiedConversationMisuse = [regex]::Matches(
    $semanticProducerText,
    '(?i)\bverified\s+(?:30-minute\s+)?discovery\s+conversation\b'
)
Assert-True -Condition ($verifiedConversationMisuse.Count -eq 0) `
    -PassMessage 'No producer artifact calls the discovery conversation verified.' `
    -FailureMessage 'A producer artifact incorrectly calls the discovery conversation verified.'

$matrixRows = [regex]::Matches(
    $directions,
    '(?m)^\|\s*(?!Criterion|---|Weighted total)(?<criterion>[^|]+?)\s*\|\s*(?<weight>\d+)\s*\|\s*(?<a>\d+)\s*\|\s*(?<b>\d+)\s*\|\s*(?<c>\d+)\s*\|\s*$'
)
$totalRow = [regex]::Match(
    $directions,
    '(?m)^\|\s*Weighted total, maximum (?<max>\d+)\s*\|\s*—\s*\|\s*\*\*(?<a>\d+)\*\*\s*\|\s*\*\*(?<b>\d+)\*\*\s*\|\s*\*\*(?<c>\d+)\*\*\s*\|\s*$'
)
$computedA = 0
$computedB = 0
$computedC = 0
$computedMaximum = 0
foreach ($matrixRow in $matrixRows) {
    $weight = [int]$matrixRow.Groups['weight'].Value
    $computedA += $weight * [int]$matrixRow.Groups['a'].Value
    $computedB += $weight * [int]$matrixRow.Groups['b'].Value
    $computedC += $weight * [int]$matrixRow.Groups['c'].Value
    $computedMaximum += $weight * 5
}
$matrixArithmeticValid =
    ($matrixRows.Count -eq 8) -and
    $totalRow.Success -and
    ($computedA -eq [int]$totalRow.Groups['a'].Value) -and
    ($computedB -eq [int]$totalRow.Groups['b'].Value) -and
    ($computedC -eq [int]$totalRow.Groups['c'].Value) -and
    ($computedMaximum -eq [int]$totalRow.Groups['max'].Value) -and
    ($computedA -eq 161) -and
    ($computedB -eq 144) -and
    ($computedC -eq 112) -and
    ($computedMaximum -eq 165)
Assert-True -Condition $matrixArithmeticValid `
    -PassMessage 'Direction-matrix weighted totals are arithmetically correct: A 161, B 144, C 112, maximum 165.' `
    -FailureMessage "Direction-matrix arithmetic mismatch: rows=$($matrixRows.Count), A=$computedA, B=$computedB, C=$computedC, maximum=$computedMaximum."

$traceabilityPath = Join-Path $strategyDir '07-traceability.csv'
try {
    $traceability = @(Import-Csv -LiteralPath $traceabilityPath)
    Add-Pass 'Brand traceability parses as CSV.'
} catch {
    Add-Failure "Brand traceability CSV parse failed: $($_.Exception.Message)"
    $traceability = @()
}

$expectedDecisions = 1..25 | ForEach-Object { 'D-{0:D3}' -f $_ }
$actualDecisions = @($traceability | ForEach-Object { [string]$_.decision_id })
Assert-True -Condition ($traceability.Count -eq 25) `
    -PassMessage 'Traceability contains 25 decision rows.' `
    -FailureMessage "Expected 25 traceability rows; found $($traceability.Count)."
Assert-True -Condition (@($actualDecisions | Sort-Object -Unique).Count -eq $actualDecisions.Count) `
    -PassMessage 'Traceability decision IDs are unique.' `
    -FailureMessage 'Duplicate decision IDs were found in brand traceability.'
$missingDecisions = @($expectedDecisions | Where-Object { $_ -notin $actualDecisions })
$unexpectedDecisions = @($actualDecisions | Where-Object { $_ -notin $expectedDecisions })
Assert-True -Condition (($missingDecisions.Count -eq 0) -and ($unexpectedDecisions.Count -eq 0)) `
    -PassMessage 'Traceability covers exactly D-001 through D-025.' `
    -FailureMessage "Decision traceability mismatch. Missing: $($missingDecisions -join ', '); unexpected: $($unexpectedDecisions -join ', ')."

$emptyTraceFields = @(
    $traceability | Where-Object {
        [string]::IsNullOrWhiteSpace([string]$_.decision_id) -or
        [string]::IsNullOrWhiteSpace([string]$_.decision_summary) -or
        [string]::IsNullOrWhiteSpace([string]$_.brand_artifacts) -or
        [string]::IsNullOrWhiteSpace([string]$_.strategy_effect) -or
        [string]::IsNullOrWhiteSpace([string]$_.open_gate)
    }
)
Assert-True -Condition ($emptyTraceFields.Count -eq 0) `
    -PassMessage 'Every traceability row names its effect, artifacts, and open gate.' `
    -FailureMessage "Traceability rows have missing required fields: $(($emptyTraceFields | ForEach-Object { [string]$_.decision_id }) -join ', ')"

$foundationRequirementsText = Get-Content -Raw -LiteralPath (Join-Path $repositoryRoot 'docs/phase-1-foundation/01-product-requirements.md')
$foundationRequirementIds = @(
    [regex]::Matches(
        $foundationRequirementsText,
        '(?m)^\|\s*((?:BR|FR|SEO|PUB|UX|AI|DATA|SEC|NFR|OPS)-\d{3})\s*\|'
    ) | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique
)
$traceRequirementIds = @(
    $traceability | ForEach-Object {
        ([string]$_.requirement_ids -split ';') | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    } | Sort-Object -Unique
)
$unknownRequirementIds = @($traceRequirementIds | Where-Object { $_ -notin $foundationRequirementIds })
Assert-True -Condition ($unknownRequirementIds.Count -eq 0) `
    -PassMessage 'All traced requirement IDs exist in the accepted foundation.' `
    -FailureMessage "Unknown traced requirement IDs: $($unknownRequirementIds -join ', ')"

$foundationClaims = Get-Content -Raw -LiteralPath (Join-Path $repositoryRoot 'docs/phase-1-foundation/05-evidence-and-claims-ledger.json') | ConvertFrom-Json
$foundationClaimIds = @($foundationClaims.entries | ForEach-Object { [string]$_.id })
$traceClaimIds = @(
    $traceability | ForEach-Object {
        ([string]$_.claim_ledger_ids -split ';') | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    } | Sort-Object -Unique
)
$unknownClaimIds = @($traceClaimIds | Where-Object { $_ -notin $foundationClaimIds })
Assert-True -Condition ($unknownClaimIds.Count -eq 0) `
    -PassMessage 'All traced claim-ledger IDs exist in the accepted foundation.' `
    -FailureMessage "Unknown traced claim-ledger IDs: $($unknownClaimIds -join ', ')"

Assert-True -Condition (
    (@($traceability | Where-Object { $_.decision_id -eq 'D-025' }).Count -eq 1) -and
    ([string](@($traceability | Where-Object { $_.decision_id -eq 'D-025' })[0].strategy_effect) -match '/industries is no longer treated as founder-pending')
) -PassMessage 'D-025 acceptance and retained industries hub are explicitly reflected.' `
  -FailureMessage 'D-025 or retained industries-hub strategy effect is missing.'

$markdownFiles = @(Get-ChildItem -LiteralPath $strategyDir -Recurse -File -Filter '*.md')
$brokenLocalLinks = [System.Collections.Generic.List[string]]::new()
foreach ($markdownFile in $markdownFiles) {
    $markdown = Get-Content -Raw -LiteralPath $markdownFile.FullName
    foreach ($match in [regex]::Matches($markdown, '\]\((?<target>[^)]+)\)')) {
        $target = $match.Groups['target'].Value.Trim()
        if ($target -match '^(?i:https?://|mailto:|tel:)' -or $target.StartsWith('#')) {
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

$contentFiles = @(
    Get-ChildItem -LiteralPath $strategyDir -Recurse -File |
        Where-Object { $_.Extension -in @('.md', '.csv') }
)
$draftMarkers = @(
    $contentFiles | Select-String -Pattern '\b(TODO|TBD|FIXME)\b|changeme' -CaseSensitive:$false
)
Assert-True -Condition ($draftMarkers.Count -eq 0) `
    -PassMessage 'No unresolved TODO, TBD, FIXME, or changeme marker was found.' `
    -FailureMessage "Unresolved drafting markers: $(($draftMarkers | ForEach-Object { "$($_.Path):$($_.LineNumber)" }) -join ', ')"

$secretPatterns = [ordered]@{
    private_key_material = ('-----BEGIN ' + '(?:(?:RSA|EC|OPENSSH) )?PRIVATE KEY-----')
    aws_access_key = '\bAKIA[0-9A-Z]{16}\b'
    github_token = '\b(?:(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,})\b'
    openai_token = '\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b'
    slack_token = '\bxox[baprs]-[A-Za-z0-9-]{20,}\b'
    credentialed_database_url = '(?i)\b(?:postgres(?:ql)?|mysql|mariadb|mongodb(?:\+srv)?)://[^\s:/@]+:[^\s/@]{8,}@'
    secret_assignment = '(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password|connection[_-]?string)\b\s*[:=]\s*["'']?[A-Za-z0-9+/=_.-]{16,}'
}
$secretFindings = [System.Collections.Generic.List[object]]::new()
foreach ($contentFile in $contentFiles) {
    $lineNumber = 0
    foreach ($line in Get-Content -LiteralPath $contentFile.FullName) {
        $lineNumber++
        foreach ($secretPattern in $secretPatterns.GetEnumerator()) {
            if ($line -match $secretPattern.Value) {
                $secretFindings.Add([pscustomobject]@{
                    kind = $secretPattern.Key
                    path = $contentFile.FullName
                    line = $lineNumber
                })
            }
        }
    }
}
Assert-True -Condition ($secretFindings.Count -eq 0) `
    -PassMessage 'No common secret-shaped value pattern was detected.' `
    -FailureMessage "Potential secret-shaped values detected; values suppressed: $(($secretFindings | ForEach-Object { "$($_.kind) at $($_.path):$($_.line)" }) -join '; ')"

$validationFiles = @(
    Get-ChildItem -LiteralPath $strategyDir -Recurse -File |
        Where-Object { $_.Extension -in @('.md', '.csv', '.ps1') }
)
$trailingWhitespace = @(
    foreach ($validationFile in $validationFiles) {
        if ($validationFile.Extension -eq '.md') {
            Select-String -LiteralPath $validationFile.FullName -Pattern '(?<! ) $| {3,}$|\t+[ ]*$'
        } else {
            Select-String -LiteralPath $validationFile.FullName -Pattern '[ \t]+$'
        }
    }
)
Assert-True -Condition ($trailingWhitespace.Count -eq 0) `
    -PassMessage 'No invalid trailing whitespace was found.' `
    -FailureMessage "Invalid trailing whitespace: $(($trailingWhitespace | ForEach-Object { "$($_.Path):$($_.LineNumber)" }) -join ', ')"

$missingFinalNewline = @()
foreach ($validationFile in $validationFiles) {
    $bytes = [System.IO.File]::ReadAllBytes($validationFile.FullName)
    if (($bytes.Count -eq 0) -or ($bytes[-1] -ne 10)) {
        $missingFinalNewline += $validationFile.FullName
    }
}
Assert-True -Condition ($missingFinalNewline.Count -eq 0) `
    -PassMessage 'Every strategy text artifact ends with a newline.' `
    -FailureMessage "Files missing final newline: $($missingFinalNewline -join ', ')"

$gitDiffCheckOutput = & git -C $repositoryRoot diff --check -- 'docs/phase-1-brand-strategy' 2>&1
$gitDiffCheckExit = $LASTEXITCODE
Assert-True -Condition ($gitDiffCheckExit -eq 0) `
    -PassMessage 'Scoped git diff --check reports no tracked whitespace error.' `
    -FailureMessage "Scoped git diff --check failed: $($gitDiffCheckOutput -join [Environment]::NewLine)"

Write-Output 'Hengshi Design Phase 1 brand-strategy validation'
Write-Output "Strategy: $strategyDir"
Write-Output "Passes: $($passes.Count)"
foreach ($message in $passes) {
    Write-Output "PASS: $message"
}

Write-Output "Failures: $($errors.Count)"
if ($errors.Count -gt 0) {
    foreach ($message in $errors) {
        Write-Error "FAIL: $message"
    }
    Write-Output 'RESULT: FAIL'
    exit 1
}

Write-Output 'RESULT: PASS'
exit 0
