#Requires -Version 7.0
<#
.SYNOPSIS
    Deterministic validator for the Phase 1 MA-025 external UI reference-production
    contract package.

.DESCRIPTION
    Documentation-only validation. This script performs no external provider
    operation, no network call, and no repository mutation. It emits one line per
    assertion and a final RESULT line.

.NOTES
    Run from the repository root:
        pwsh -NoProfile -File docs/phase-1-ui-reference-production/validation/validate-ui-reference-production.ps1
#>

[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:PassCount = 0
$script:FailCount = 0

function Assert-That {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][bool]$Condition,
        [string]$Detail = ''
    )
    if ($Condition) {
        $script:PassCount++
        Write-Output ("PASS  {0}" -f $Name)
    }
    else {
        $script:FailCount++
        if ([string]::IsNullOrWhiteSpace($Detail)) {
            Write-Output ("FAIL  {0}" -f $Name)
        }
        else {
            Write-Output ("FAIL  {0} :: {1}" -f $Name, $Detail)
        }
    }
}

# ---------------------------------------------------------------------------
# Roots
# ---------------------------------------------------------------------------

$validationRoot = Split-Path -Parent $PSCommandPath
$packageRoot    = Split-Path -Parent $validationRoot
$repoRoot       = Split-Path -Parent (Split-Path -Parent $packageRoot)
$acceptedRoot   = Join-Path $repoRoot 'docs/phase-1-ui-reference-design'

Write-Output ("VALIDATOR  validate-ui-reference-production")
Write-Output ("PACKAGE    {0}" -f $packageRoot)
Write-Output ("ACCEPTED   {0}" -f $acceptedRoot)

# ---------------------------------------------------------------------------
# Gate lifecycle state
# ---------------------------------------------------------------------------
# R-024 lesson: never assert that an authorized mutable input remains immutable.
# Several boundary assertions below are true only before MA-025 is approved.
# Rather than delete them once approval lands, scope them to an explicit
# lifecycle state derived from the durable ledger.

$manualActionsPath = Join-Path $repoRoot 'MANUAL_ACTIONS.md'
$ma025Status = 'unknown'
if (Test-Path -LiteralPath $manualActionsPath) {
    $maLines = @(Get-Content -LiteralPath $manualActionsPath)
    for ($i = 0; $i -lt $maLines.Count; $i++) {
        if ($maLines[$i] -match '^\*\*ID:\*\*\s*MA-025\s*$') {
            $upper = [Math]::Min($i + 6, $maLines.Count - 1)
            for ($j = $i + 1; $j -le $upper; $j++) {
                if ($maLines[$j] -match '^\*\*Status:\*\*\s*(.+)$') {
                    $ma025Status = $Matches[1].Trim()
                    break
                }
            }
            break
        }
    }
}

$gateState = if ($ma025Status -like 'accepted*') { 'POST_APPROVAL' } else { 'PRE_APPROVAL' }

Write-Output ("MA-025     {0}" -f $ma025Status)
Write-Output ("GATE_STATE {0}" -f $gateState)
Write-Output ''

# ---------------------------------------------------------------------------
# 1. Required package files
# ---------------------------------------------------------------------------

[string[]]$requiredFiles = @(
    'README.md',
    'UI_REFERENCE_PRODUCTION_CONTRACT.md',
    'batch-production-plan.csv',
    'evidence-capture-plan.csv',
    'external-write-scope.csv',
    'producer-inspection.md',
    'provider-evaluation.csv',
    'stop-conditions.csv',
    'traceability.csv',
    '../../scripts/validation/ui-stream-mapping.ps1'
)

foreach ($rel in $requiredFiles) {
    $full = Join-Path $packageRoot $rel
    Assert-That -Name ("required-file:{0}" -f $rel) -Condition (Test-Path -LiteralPath $full -PathType Leaf)
}

# ---------------------------------------------------------------------------
# 2. Accepted upstream inputs must exist and remain readable
# ---------------------------------------------------------------------------

[string[]]$acceptedInputs = @(
    'UI_REFERENCE_DESIGN_CONTRACT.md',
    'design-batch-plan.csv',
    'reference-template-inventory.csv',
    'responsive-state-mode-matrix.csv',
    'component-primitives.csv',
    'foundation-route-coverage.csv'
)

foreach ($rel in $acceptedInputs) {
    $full = Join-Path $acceptedRoot $rel
    Assert-That -Name ("accepted-input:{0}" -f $rel) -Condition (Test-Path -LiteralPath $full -PathType Leaf)
}

# ---------------------------------------------------------------------------
# 3. CSV parsing and identifier sets
# ---------------------------------------------------------------------------

function Import-PackageCsv {
    param([string]$RelativePath)
    $full = Join-Path $packageRoot $RelativePath
    return @(Import-Csv -LiteralPath $full)
}

$batchRows    = Import-PackageCsv 'batch-production-plan.csv'
$writeRows    = Import-PackageCsv 'external-write-scope.csv'
$stopRows     = Import-PackageCsv 'stop-conditions.csv'
$evidenceRows = Import-PackageCsv 'evidence-capture-plan.csv'
$providerRows = Import-PackageCsv 'provider-evaluation.csv'
$traceRows    = Import-PackageCsv 'traceability.csv'

Assert-That -Name 'csv-parse:batch-production-plan' -Condition ($batchRows.Count -eq 9) -Detail ("rows={0}" -f $batchRows.Count)
Assert-That -Name 'csv-parse:stop-conditions'       -Condition ($stopRows.Count -eq 12) -Detail ("rows={0}" -f $stopRows.Count)
# D-045 2026-09-06: EC-31 (per-stream coverage), EC-32 (exactly one stream per manifest
# row) and EC-33 (stream deferral recorded, never silent) added. Was 30.
Assert-That -Name 'csv-parse:evidence-capture-plan' -Condition ($evidenceRows.Count -eq 33) -Detail ("rows={0}" -f $evidenceRows.Count)
Assert-That -Name 'csv-parse:provider-evaluation'   -Condition ($providerRows.Count -eq 12) -Detail ("rows={0}" -f $providerRows.Count)
Assert-That -Name 'csv-parse:traceability'          -Condition ($traceRows.Count -eq 40) -Detail ("rows={0}" -f $traceRows.Count)

function Test-ExactIdSet {
    param(
        [string]$Name,
        [string[]]$Actual,
        [string[]]$Expected
    )
    $a = @($Actual | Sort-Object -Unique)
    $e = @($Expected | Sort-Object -Unique)
    $missing = @($e | Where-Object { $a -notcontains $_ })
    $extra   = @($a | Where-Object { $e -notcontains $_ })
    $detail  = ("missing=[{0}] extra=[{1}]" -f ($missing -join ';'), ($extra -join ';'))
    Assert-That -Name $Name -Condition (($missing.Count -eq 0) -and ($extra.Count -eq 0)) -Detail $detail
}

Test-ExactIdSet -Name 'id-set:stop-conditions' `
    -Actual @($stopRows.stop_id) `
    -Expected @(1..12 | ForEach-Object { 'SC-{0:D2}' -f $_ })

Test-ExactIdSet -Name 'id-set:evidence-capture' `
    -Actual @($evidenceRows.rule_id) `
    -Expected @(1..33 | ForEach-Object { 'EC-{0:D2}' -f $_ })

Test-ExactIdSet -Name 'id-set:provider-evaluation' `
    -Actual @($providerRows.criterion_id) `
    -Expected @(1..12 | ForEach-Object { 'PE-{0:D2}' -f $_ })

Test-ExactIdSet -Name 'id-set:traceability' `
    -Actual @($traceRows.trace_id) `
    -Expected @(1..40 | ForEach-Object { 'TR-{0:D3}' -f $_ })

Test-ExactIdSet -Name 'id-set:external-write-permitted' `
    -Actual @($writeRows | Where-Object { $_.mode -eq 'permitted' } | ForEach-Object { $_.scope_id }) `
    -Expected @(1..8 | ForEach-Object { 'WS-P-{0:D2}' -f $_ })

Test-ExactIdSet -Name 'id-set:external-write-prohibited' `
    -Actual @($writeRows | Where-Object { $_.mode -eq 'prohibited' } | ForEach-Object { $_.scope_id }) `
    -Expected @(1..11 | ForEach-Object { 'WS-X-{0:D2}' -f $_ })

# ---------------------------------------------------------------------------
# 4. Cross-artifact fidelity against the accepted D-037 batch plan
# ---------------------------------------------------------------------------

$acceptedBatches = @(Import-Csv -LiteralPath (Join-Path $acceptedRoot 'design-batch-plan.csv'))

Test-ExactIdSet -Name 'cross-artifact:batch-id-set-matches-accepted-plan' `
    -Actual @($batchRows.batch_id) `
    -Expected @($acceptedBatches.batch_id)

foreach ($accepted in $acceptedBatches) {
    $mine = @($batchRows | Where-Object { $_.batch_id -eq $accepted.batch_id })
    if ($mine.Count -ne 1) {
        Assert-That -Name ("cross-artifact:{0}:single-row" -f $accepted.batch_id) -Condition $false -Detail ("rows={0}" -f $mine.Count)
        continue
    }
    $row = $mine[0]

    Assert-That -Name ("cross-artifact:{0}:prerequisites-verbatim" -f $accepted.batch_id) `
        -Condition ($row.hard_prerequisite_batch_ids -eq $accepted.hard_prerequisite_batch_ids) `
        -Detail ("accepted='{0}' package='{1}'" -f $accepted.hard_prerequisite_batch_ids, $row.hard_prerequisite_batch_ids)

    Assert-That -Name ("cross-artifact:{0}:time-limit-branch-verbatim" -f $accepted.batch_id) `
        -Condition ($row.time_limit_branch_ids -eq $accepted.time_limit_branch_ids) `
        -Detail ("accepted='{0}' package='{1}'" -f $accepted.time_limit_branch_ids, $row.time_limit_branch_ids)

    Assert-That -Name ("cross-artifact:{0}:browser-profile-verbatim" -f $accepted.batch_id) `
        -Condition ($row.browser_profile_id -eq $accepted.browser_profile_id) `
        -Detail ("accepted='{0}' package='{1}'" -f $accepted.browser_profile_id, $row.browser_profile_id)

    Assert-That -Name ("cross-artifact:{0}:accepted-status-still-unauthorized" -f $accepted.batch_id) `
        -Condition ($accepted.status -eq 'future_not_authorized') `
        -Detail ("accepted status='{0}'" -f $accepted.status)
}

# ---------------------------------------------------------------------------
# 5. Authorization split
# ---------------------------------------------------------------------------

$authorized = @($batchRows | Where-Object { $_.ma_025_disposition -like 'authorized*' })
$deferred   = @($batchRows | Where-Object { $_.ma_025_disposition -eq 'deferred_not_authorizable' })

# D-045 2026-09-06, founder gate G-4. B01's disposition was 'authorized_pilot'. It is now
# 'future_not_authorized', because that is the state actually decided: B01 is held pending a
# clean independent review, and CB-06 requires per-call founder approval regardless. The six
# 'authorized_released_by_pilot' rows are unchanged and are correct as they stand: they are a
# CONDITIONAL disposition, released BY the pilot, and the pilot has not run. Nothing is
# authorized to execute today, and the assertions below say so instead of implying otherwise.
$b01 = @($batchRows | Where-Object { $_.batch_id -eq 'B01' })[0]
$conditional = @($batchRows | Where-Object { $_.ma_025_disposition -eq 'authorized_released_by_pilot' })
$sequenced = @($batchRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.execution_order) })

Assert-That -Name 'authorization:nothing-is-authorized-to-execute' `
    -Condition (@($batchRows | Where-Object { $_.ma_025_disposition -eq 'authorized_pilot' }).Count -eq 0) `
    -Detail 'no batch carries an unconditional execution authorization'
Assert-That -Name 'authorization:B01-is-held' -Condition ($b01.ma_025_disposition -eq 'future_not_authorized')
Assert-That -Name 'authorization:six-batches-conditional' -Condition ($conditional.Count -eq 6) -Detail ("count={0}" -f $conditional.Count)
Assert-That -Name 'authorization:two-batches-deferred'    -Condition ($deferred.Count -eq 2)    -Detail ("count={0}" -f $deferred.Count)

Test-ExactIdSet -Name 'authorization:deferred-set-is-B07-and-B09' `
    -Actual @($deferred.batch_id) -Expected @('B07', 'B09')

Test-ExactIdSet -Name 'authorization:conditional-set' `
    -Actual @($conditional.batch_id) -Expected @('B02', 'B03', 'B04', 'B05', 'B06', 'B08')

$orders = @($sequenced | ForEach-Object { [int]$_.execution_order })
Assert-That -Name 'sequence:execution-order-is-1-to-7-unique' `
    -Condition (((@($orders | Sort-Object -Unique)) -join ',') -eq '1,2,3,4,5,6,7') `
    -Detail ("orders={0}" -f (($orders | Sort-Object) -join ','))

Assert-That -Name 'sequence:B01-runs-first' -Condition ([int]$b01.execution_order -eq 1)

foreach ($row in $deferred) {
    Assert-That -Name ("sequence:{0}:no-execution-order" -f $row.batch_id) `
        -Condition ([string]::IsNullOrWhiteSpace($row.execution_order))
}

# Every sequenced batch must have all its hard prerequisites also sequenced. Held and
# conditional batches are both sequenced; a prerequisite that is not in the sequence at all
# would be an unreachable dependency, which is what this checks.
foreach ($row in $sequenced) {
    $prereqs = @($row.hard_prerequisite_batch_ids -split ';' | Where-Object { $_ -ne '' })
    $unmet = @($prereqs | Where-Object { @($sequenced.batch_id) -notcontains $_ })
    Assert-That -Name ("sequence:{0}:prerequisites-are-authorized" -f $row.batch_id) `
        -Condition ($unmet.Count -eq 0) -Detail ("unmet=[{0}]" -f ($unmet -join ';'))

    foreach ($p in $prereqs) {
        $prow = @($sequenced | Where-Object { $_.batch_id -eq $p })[0]
        Assert-That -Name ("sequence:{0}:runs-after-{1}" -f $row.batch_id, $p) `
            -Condition ([int]$row.execution_order -gt [int]$prow.execution_order)
    }
}

# The deferral reasons must be the real ones, not invented.
$b07 = @($batchRows | Where-Object { $_.batch_id -eq 'B07' })[0]
$b09 = @($batchRows | Where-Object { $_.batch_id -eq 'B09' })[0]
Assert-That -Name 'authorization:B07-cites-MA-004-and-storyboard' `
    -Condition (($b07.external_gate_dependency -match 'MA-004') -and ($b07.external_gate_dependency -match 'three_d_storyboard'))
Assert-That -Name 'authorization:B09-cites-B07-dependency' `
    -Condition ($b09.external_gate_dependency -match 'B07')
Assert-That -Name 'authorization:B09-accepted-plan-really-requires-B07' `
    -Condition ((@($acceptedBatches | Where-Object { $_.batch_id -eq 'B09' })[0].hard_prerequisite_batch_ids) -match 'B07')

# ---------------------------------------------------------------------------
# 6. Contract section coverage — the eleven contracted areas
# ---------------------------------------------------------------------------

$contractPath = Join-Path $packageRoot 'UI_REFERENCE_PRODUCTION_CONTRACT.md'
$contractText = Get-Content -LiteralPath $contractPath -Raw

# Heading patterns are regular expressions so that typographic dashes in the
# contract cannot silently break a literal comparison.
[string[]]$requiredHeadingPatterns = @(
    '^## 1\. Provider selection and rationale$',
    '^## 2\. Exact B01.B09 production scope and sequence$',
    '^## 3\. External write scope$',
    '^## 4\. Visual deliverables$',
    '^## 5\. Evidence and screenshot capture$',
    '^## 6\. Design and accessibility review sequence$',
    '^## 7\. Provider and cost boundary$',
    '^## 8\. Stop conditions$',
    '^## 9\. Rollback and export strategy$',
    '^## 10\. Credential-handling boundary$',
    '^## 11\. Acceptance criteria$'
)

foreach ($pattern in $requiredHeadingPatterns) {
    $label = ($pattern -replace '^\^## ', '' -replace '\$$', '' -replace '\\', '')
    Assert-That -Name ("contract-section:{0}" -f $label) `
        -Condition ($contractText -match ('(?m)' + $pattern))
}

# ---------------------------------------------------------------------------
# 7. Gate and boundary assertions
# ---------------------------------------------------------------------------

Assert-That -Name 'boundary:no-TL-EXCEPTION-selected' `
    -Condition (-not ($batchRows.time_limit_branch_ids -join ';').Contains('TL-EXCEPTION'))

Assert-That -Name 'boundary:TEST_CAPTURE-excluded-from-scope' `
    -Condition (@($evidenceRows | Where-Object { $_.rule_id -eq 'EC-07' })[0].requirement -match 'Do not produce TEST_CAPTURE')

Assert-That -Name 'boundary:stitch-operations-prohibited' `
    -Condition (@($writeRows | Where-Object { $_.scope_id -eq 'WS-X-08' })[0].operation -match 'Stitch')

Assert-That -Name 'boundary:billing-actions-prohibited' `
    -Condition (@($writeRows | Where-Object { $_.scope_id -eq 'WS-X-05' })[0].operation -match 'billing')

Assert-That -Name 'boundary:UI_SPEC-not-written-under-MA-025' `
    -Condition ((@($writeRows | Where-Object { $_.scope_id -eq 'WS-R-05' })).Count -eq 1) `
    -Detail 'WS-R-05 must prohibit writing docs/ui/UI_SPEC.md'

Assert-That -Name 'boundary:UI_SPEC-absent-from-repository' `
    -Condition (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'docs/ui/UI_SPEC.md')))

Assert-That -Name 'boundary:git-operations-gated' `
    -Condition ((@($writeRows | Where-Object { $_.mode -eq 'git_prohibited' })).Count -eq 1)

$capabilityEvidencePath = Join-Path $validationRoot 'capability-evidence.md'
$callBudgetPath         = Join-Path $validationRoot 'mcp-call-budget.csv'
$callLedgerPath         = Join-Path $validationRoot 'mcp-call-ledger.csv'

if ($gateState -eq 'PRE_APPROVAL') {
    Assert-That -Name 'boundary:no-external-write-performed' `
        -Condition (-not (Test-Path -LiteralPath (Join-Path $packageRoot 'evidence'))) `
        -Detail 'An evidence directory must not exist before MA-025 is approved'

    Assert-That -Name 'boundary:capability-evidence-not-yet-claimed' `
        -Condition (-not (Test-Path -LiteralPath $capabilityEvidencePath)) `
        -Detail 'Capability evidence is recorded only after MA-025 approval'
}
else {
    # MA-025 is accepted. Capability evidence and the rationing instruments are
    # now REQUIRED rather than forbidden, because the verified 20-calls-per-month
    # allowance makes an uncounted budget the primary programme risk.

    Assert-That -Name 'gate:capability-evidence-recorded' `
        -Condition (Test-Path -LiteralPath $capabilityEvidencePath) `
        -Detail 'MA-025 is accepted so section 3.5 capability evidence must exist'

    Assert-That -Name 'gate:call-budget-recorded' `
        -Condition (Test-Path -LiteralPath $callBudgetPath) `
        -Detail 'A written call budget is required under the verified allowance'

    Assert-That -Name 'gate:call-ledger-recorded' `
        -Condition (Test-Path -LiteralPath $callLedgerPath) `
        -Detail 'Every Figma MCP call must be counted in a durable ledger'

    $capabilityText = if (Test-Path -LiteralPath $capabilityEvidencePath) {
        Get-Content -LiteralPath $capabilityEvidencePath -Raw
    } else { '' }

    $budgetText = if (Test-Path -LiteralPath $callBudgetPath) {
        Get-Content -LiteralPath $callBudgetPath -Raw
    } else { '' }

    Assert-That -Name 'gate:verified-allowance-recorded' `
        -Condition ($capabilityText -match '20 tool calls per month') `
        -Detail 'The verified Starter allowance must be stated, not implied'

    Assert-That -Name 'gate:SC-05-shortfall-recorded' `
        -Condition ($capabilityText.Contains('SC-05') -and $capabilityText.Contains('21')) `
        -Detail 'The stop condition and the exact numeric shortfall must both be recorded'

    Assert-That -Name 'gate:exemption-not-asserted' `
        -Condition ($capabilityText.Contains('NOT ASSERTED') -and $budgetText.Contains('CB-02')) `
        -Detail 'Write-tool rate-limit exemption is undocumented and must not be assumed'

    Assert-That -Name 'gate:no-purchase-workaround-authorized' `
        -Condition ($budgetText.Contains('CB-12')) `
        -Detail 'The budget must forbid restoring allowance by purchase'

    Assert-That -Name 'boundary:no-external-write-performed-yet' `
        -Condition (-not (Test-Path -LiteralPath (Join-Path $packageRoot 'evidence'))) `
        -Detail 'B01 has not started; an evidence directory would indicate an unrecorded write'
}

Assert-That -Name 'gate:D-037-freeze-hash-cited' `
    -Condition ($contractText.Contains('97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F'))

Assert-That -Name 'gate:MA-004-block-recorded' -Condition ($contractText.Contains('MA-004'))
Assert-That -Name 'gate:MA-010-cost-routing-recorded' -Condition ($contractText.Contains('MA-010'))
Assert-That -Name 'gate:MA-026-deferral-recorded' -Condition ($contractText.Contains('MA-026'))
Assert-That -Name 'gate:MA-013-recorded-as-separate' -Condition ($contractText.Contains('MA-013'))

Assert-That -Name 'gate:host-mcp-exposure-gap-recorded' `
    -Condition ($contractText.Contains('%APPDATA%\Code\User\mcp.json') -and $contractText.Contains('does not exist'))

Assert-That -Name 'gate:unverified-pricing-items-recorded' `
    -Condition ($contractText.Contains('[MUST VERIFY AT GATE]'))

# ---------------------------------------------------------------------------
# 8. Unsupported-claim scan
# ---------------------------------------------------------------------------

[string[]]$markdownFiles = @(
    Get-ChildItem -LiteralPath $packageRoot -Recurse -Filter '*.md' -File |
        ForEach-Object { $_.FullName }
)

[string[]]$forbiddenClaims = @(
    'is WCAG 2.2 AA conformant',
    'is fully accessible',
    'conformance achieved',
    'certified accessible',
    'production ready',
    'has been deployed',
    'is live',
    'we created the Figma file',
    'the Figma file has been created'
)

foreach ($claim in $forbiddenClaims) {
    $hits = @($markdownFiles | Where-Object {
        (Get-Content -LiteralPath $_ -Raw) -match [regex]::Escape($claim)
    })
    Assert-That -Name ("claim-scan:{0}" -f $claim) -Condition ($hits.Count -eq 0) `
        -Detail ("hits=[{0}]" -f (($hits | ForEach-Object { Split-Path -Leaf $_ }) -join ';'))
}

# ---------------------------------------------------------------------------
# 9. Secret scan
# ---------------------------------------------------------------------------

[string[]]$secretPatterns = @(
    'figd_[A-Za-z0-9_\-]{20,}',
    'figu_[A-Za-z0-9_\-]{20,}',
    'ghp_[A-Za-z0-9]{20,}',
    '-----BEGIN [A-Z ]*PRIVATE KEY-----',
    '(?i)\b(password|passwd|client_secret|api[_-]?key|access[_-]?token)\s*[:=]\s*["'']?[A-Za-z0-9_\-]{12,}'
)

[string[]]$allPackageFiles = @(
    Get-ChildItem -LiteralPath $packageRoot -Recurse -File |
        ForEach-Object { $_.FullName }
)

foreach ($pattern in $secretPatterns) {
    $hits = @($allPackageFiles | Where-Object {
        (Get-Content -LiteralPath $_ -Raw) -match $pattern
    })
    Assert-That -Name ("secret-scan:{0}" -f $pattern) -Condition ($hits.Count -eq 0) `
        -Detail ("hits=[{0}]" -f (($hits | ForEach-Object { Split-Path -Leaf $_ }) -join ';'))
}

# ---------------------------------------------------------------------------
# 10. Local reference validation
# ---------------------------------------------------------------------------

$linkPattern = '\]\((?<target>[^)#:]+\.(?:md|csv|ps1|json|svg))(?:#[^)]*)?\)'
foreach ($md in $markdownFiles) {
    $text = Get-Content -LiteralPath $md -Raw
    $dir  = Split-Path -Parent $md
    foreach ($m in [regex]::Matches($text, $linkPattern)) {
        $target = $m.Groups['target'].Value
        if ($target -match '^[a-z]+://') { continue }
        $resolved = Join-Path $dir $target
        Assert-That -Name ("local-reference:{0} -> {1}" -f (Split-Path -Leaf $md), $target) `
            -Condition (Test-Path -LiteralPath $resolved)
    }
}

# ---------------------------------------------------------------------------
# 11. Traceability integrity
# ---------------------------------------------------------------------------

$unresolvedTrace = @($traceRows | Where-Object { [string]::IsNullOrWhiteSpace($_.upstream_authority) -or [string]::IsNullOrWhiteSpace($_.downstream_gate) })
Assert-That -Name 'traceability:every-row-has-authority-and-gate' `
    -Condition ($unresolvedTrace.Count -eq 0) `
    -Detail ("rows=[{0}]" -f (($unresolvedTrace | ForEach-Object { $_.trace_id }) -join ';'))

$badStatus = @($traceRows | Where-Object { @('proposed', 'deferred', 'unresolved_gate', 'must_verify_at_gate', 'unchanged') -notcontains $_.status })
Assert-That -Name 'traceability:status-vocabulary' `
    -Condition ($badStatus.Count -eq 0) `
    -Detail ("rows=[{0}]" -f (($badStatus | ForEach-Object { $_.trace_id }) -join ';'))

Assert-That -Name 'traceability:records-the-host-mcp-gap' `
    -Condition ((@($traceRows | Where-Object { $_.trace_id -eq 'TR-004' })[0].status) -eq 'unresolved_gate')

Assert-That -Name 'traceability:records-the-unverified-pricing-items' `
    -Condition ((@($traceRows | Where-Object { $_.trace_id -eq 'TR-030' })[0].status) -eq 'must_verify_at_gate')

# ---------------------------------------------------------------------------
# 12. Repository write-scope check
#
# Deliberately broader than the D-037 validator's package-only assertion, which
# could not re-run clean once durable root records were updated in the same
# change. Durable root records are an expected part of this slice.
# ---------------------------------------------------------------------------

Push-Location $repoRoot
try {
    $porcelain = @(git status --porcelain=v1 --untracked-files=all 2>$null)
}
finally {
    Pop-Location
}

# The allowed set is deliberately the whole documentation tree plus the
# enumerated durable root records, not this package alone. A worktree legitimately
# carries other concurrently authorized documentation slices; a validator that
# assumes it is the only work in flight repeats the D-037 defect one level up and
# fails for a reason that has nothing to do with what it exists to prove.
# The load-bearing safety assertion is the separate application/dependency/
# migration check below, which is evaluated over EVERY changed path rather than
# only the paths this check already rejected.
[string[]]$allowedPrefixes = @(
    'docs/',
    'specs/',
    'PROJECT.md',
    'PROJECT_STATE.yaml',
    'TASKS.md',
    'DECISIONS.md',
    'RISKS.md',
    'MANUAL_ACTIONS.md',
    'CHANGELOG.md',
    'AGENTS.md'
)

$changedPaths = @()
foreach ($line in $porcelain) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    $path = ($line.Substring(3)).Trim('"')
    if ($path -match ' -> ') { $path = ($path -split ' -> ')[-1] }
    $changedPaths += $path
}

$outOfScope = @()
foreach ($path in $changedPaths) {
    $ok = $path -cin @('scripts/validation/ui-stream-mapping.ps1', 'scripts/validation/test-ui-stream-mapping.ps1')
    foreach ($prefix in $allowedPrefixes) {
        if ($path.StartsWith($prefix)) { $ok = $true; break }
    }
    if (-not $ok) { $outOfScope += $path }
}

Assert-That -Name 'git-write-scope:documentation-only' `
    -Condition ($outOfScope.Count -eq 0) `
    -Detail ("out-of-scope=[{0}]" -f ($outOfScope -join ';'))

$appChanges = @($changedPaths | Where-Object {
    $_ -like 'apps/*' -or $_ -like '*lock*' -or $_ -like '*/migrations/*' -or $_ -like '*.glb'
})
Assert-That -Name 'git-write-scope:no-application-dependency-or-migration-change' `
    -Condition ($appChanges.Count -eq 0) `
    -Detail ("changes=[{0}]" -f ($appChanges -join ';'))

# ---------------------------------------------------------------------------
# 13. Reproducible package freeze
# ---------------------------------------------------------------------------

[string[]]$freezeRelativePaths = @($requiredFiles)
[Array]::Sort($freezeRelativePaths, [StringComparer]::Ordinal)

$freezeHashLines = @($freezeRelativePaths | ForEach-Object {
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $packageRoot $_)).Hash.ToUpperInvariant()
    "{0}  {1}" -f $hash, $_.Replace('\', '/')
})
$freezePayload = [string]::Join("`n", $freezeHashLines)

$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $bytes = (New-Object System.Text.UTF8Encoding($false)).GetBytes($freezePayload)
    $packageHash = ([System.BitConverter]::ToString($sha.ComputeHash($bytes))).Replace('-', '')
}
finally {
    $sha.Dispose()
}

Assert-That -Name 'freeze:package-hash-computed' -Condition ($packageHash.Length -eq 64)

Write-Output ''
Write-Output ("FREEZE_FILE_COUNT={0}" -f $freezeRelativePaths.Count)
Write-Output ("FREEZE_SHA256={0}" -f $packageHash)
Write-Output ''

# ---------------------------------------------------------------------------
# Result
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# D-045 2026-09-06 - delivery-stream assertions A-12..A-16.
#
# The production package had NO stream axis at all. Not a weak one: absent. Every
# rule here therefore has to be able to fail while the evidence manifest is still
# empty, because an empty manifest is exactly the state in which "nothing is wrong"
# is indistinguishable from "nothing is checked". A-12 and A-14 are exercised
# against the negative fixtures the accepted specification names, so they are
# load-bearing today rather than load-bearing once evidence exists.
#
# Every literal that these rules would otherwise match in their own source is
# assembled at run time. This is not cosmetic. The guards below scan validator
# sources as well as data and prose, and a guard that has to be excused from
# reading itself is a guard with a hole in exactly the place a producer would
# hide something. Constructing the literals keeps the scan total.
# ---------------------------------------------------------------------------

$streamVocab       = @('S-HIGH', 'S-LOW', 'S-MEDIUM', 'S-SEMANTIC')
$streamSegments    = @('STREAM_HIGH', 'STREAM_MEDIUM', 'STREAM_LOW', 'STREAM_SEMANTIC')
$evidenceIdPattern = '^HSD_UIR_(B\d{2})_(.+?)_STATE_(.+?)_VP_(.+?)_MODE_(.+?)_(?:STREAM_(HIGH|MEDIUM|LOW|SEMANTIC)|SCOPE_(EXCLUDED))_V(\d{2})$'

# --- A-12 evidence-id-grammar-resolution -----------------------------------
function Test-EvidenceId {
    param([string]$EvidenceId, [string]$StreamId)
    $m = [regex]::Match($EvidenceId, $evidenceIdPattern)
    if (-not $m.Success) { return $false }
    if ($m.Groups[7].Success) { return $StreamId -ceq 'STREAM-SCOPE-EXCLUDED' }
    if ($StreamId -cnotin $streamVocab) { return $false }
    return (('S-' + $m.Groups[6].Value) -ceq $StreamId)
}
$fxStem = 'HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_REST_VP_DESKTOP_MODE_STANDARD'
$fx = @(
    @{ n = 'no-stream-segment';    id = ($fxStem + '_V01');                           s = 'S-HIGH' },
    @{ n = 'illegal-stream-token'; id = ($fxStem + '_STREAM_' + 'FALLBACK' + '_V01'); s = 'S-HIGH' },
    @{ n = 'aggregate-stream';     id = ($fxStem + '_STREAM_' + 'ALL' + '_V01');      s = 'S-HIGH' },
    @{ n = 'stream-id-disagrees';  id = ($fxStem + '_STREAM_HIGH_V01');               s = 'S-SEMANTIC' }
)
$fxLeaks = @($fx | Where-Object { Test-EvidenceId -EvidenceId $_.id -StreamId $_.s } | ForEach-Object { $_.n })
Assert-That -Name 'A-12:evidence-id-grammar-rejects-every-negative-fixture' -Condition ($fxLeaks.Count -eq 0) `
    -Detail ("fixtures={0}; leaked=[{1}]" -f $fx.Count, ($fxLeaks -join ';'))
Assert-That -Name 'A-12:evidence-id-grammar-accepts-a-well-formed-id' `
    -Condition (Test-EvidenceId -EvidenceId ($fxStem + '_STREAM_SEMANTIC_V01') -StreamId 'S-SEMANTIC')

# --- A-13 batch-stream-disposition-resolution ------------------------------
# Live against current data. Every key resolves against the closed vocabulary,
# every deferral target resolves against a batch that is itself deferred, and
# every not_present claim is checked against the presence set computed from the
# ACCEPTED DESIGN PACKAGE - not against anything this package says about itself.
$designPrimitives = @(Import-Csv -LiteralPath (Join-Path $acceptedRoot 'component-primitives.csv'))
$designTemplates  = @(Import-Csv -LiteralPath (Join-Path $acceptedRoot 'reference-template-inventory.csv'))
$designBatches    = @(Import-Csv -LiteralPath (Join-Path $acceptedRoot 'design-batch-plan.csv'))
. (Join-Path $repoRoot 'scripts/validation/ui-stream-mapping.ps1')
try {
    $streamMapping = Get-UiStreamMapping -Primitives $designPrimitives -Templates $designTemplates
}
catch {
    Assert-That -Name 'A-13:template-stream-mapping' -Condition $false -Detail $_.Exception.Message
    Write-Output ("RESULT=FAIL PASS_COUNT={0} FAIL_COUNT={1}" -f $script:PassCount, $script:FailCount)
    exit 1
}
$presenceByTemplate = $streamMapping.TemplatePresence
$designBatchById = @{}
foreach ($b in $designBatches) { $designBatchById[$b.batch_id] = $b }
function Get-BatchTemplateIds {
    param([object]$DesignBatch)
    $ids = @($DesignBatch.primary_template_ids -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
    if ($ids.Count -eq 0) {
        $ids = @($DesignBatch.supporting_template_ids -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
    }
    return @($ids)
}
$deferredIds = @($deferred.batch_id)
$a13 = [System.Collections.Generic.List[string]]::new()
foreach ($row in $batchRows) {
    if (-not $row.PSObject.Properties['stream_disposition']) { $a13.Add(("{0}:column-missing" -f $row.batch_id)); continue }
    $pairs = @($row.stream_disposition -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
    $keys  = @($pairs | ForEach-Object { ($_ -split '=')[0] })
    foreach ($k in $streamVocab) { if ($k -cnotin $keys) { $a13.Add(("{0}:missing-key={1}" -f $row.batch_id, $k)) } }
    if (($keys -join ',') -cne (@($keys | Sort-Object -CaseSensitive) -join ',')) { $a13.Add(("{0}:keys-unsorted" -f $row.batch_id)) }
    $union = [System.Collections.Generic.List[string]]::new()
    foreach ($t in (Get-BatchTemplateIds -DesignBatch $designBatchById[$row.batch_id])) {
        foreach ($s in $presenceByTemplate[$t]) { if ($s -cnotin $union) { $union.Add($s) } }
    }
    foreach ($pair in $pairs) {
        $k, $v = ($pair -split '=', 2)
        if ($k -cnotin $streamVocab) { $a13.Add(("{0}:illegal-key={1}" -f $row.batch_id, $k)); continue }
        if ($v -ceq 'in_scope') {
            if ($k -cnotin $union) { $a13.Add(("{0}:{1}-claimed-present-but-absent" -f $row.batch_id, $k)) }
        }
        elseif ($v -ceq 'not_present') {
            if ($k -cin $union) { $a13.Add(("{0}:{1}-claimed-absent-but-present-in-fold" -f $row.batch_id, $k)) }
        }
        elseif ($v -cmatch '^deferred_(B\d{2})$') {
            $target = $Matches[1]
            if ($target -cnotin @($batchRows.batch_id)) { $a13.Add(("{0}:{1}-deferred-to-unknown-batch={2}" -f $row.batch_id, $k, $target)) }
            elseif ($target -cnotin $deferredIds) { $a13.Add(("{0}:{1}-deferred-to-non-deferred-batch={2}" -f $row.batch_id, $k, $target)) }
        }
        else { $a13.Add(("{0}:{1}-illegal-value={2}" -f $row.batch_id, $k, $v)) }
    }
}
Assert-That -Name 'A-13:batch-stream-disposition-resolution' -Condition ($a13.Count -eq 0) `
    -Detail ("errors=[{0}]" -f ($a13 -join ';'))

# PRODUCER OBSERVATION, reported and not failed, because failing it would be the
# producer overruling the accepted specification rather than implementing it.
# stream_disposition is CONSTANT across all nine rows on the current data: N-01
# places the semantic host shell in almost every template's dependencies, so every
# batch folds to all four streams. A constant column encodes no per-batch judgement
# and cannot be wrong - the same shape as the defect D-045 was decided to end,
# appearing inside the accepted remedy for it. The column is implemented exactly as
# specified because it is the hook A-13 resolves against, but no later producer
# should read the current uniform value as a template to copy. Recorded in
# producer-inspection.md and in RISKS.md.
$dispositionValues = @($batchRows | ForEach-Object { $_.stream_disposition } | Sort-Object -Unique)
Write-Output ("INERT-REPORT batch-production-plan.csv:stream_disposition distinct-values={0} rows={1}" -f $dispositionValues.Count, $batchRows.Count)

# --- A-14 per-stream-frame-coverage-resolution -----------------------------
# There is no evidence manifest yet, and that is the point. The obligation set is
# computed non-empty from the design fold, so this rule reports an outstanding
# obligation rather than passing vacuously on an absent file.
$obligedList = [System.Collections.Generic.List[string]]::new()
foreach ($row in $batchRows) {
    foreach ($t in (Get-BatchTemplateIds -DesignBatch $designBatchById[$row.batch_id])) {
        foreach ($s in @(Get-UiEvidenceScopes -Mapping $streamMapping -TemplateId $t)) { $obligedList.Add(("{0}|{1}|{2}" -f $row.batch_id, $t, $s)) }
    }
}
$obliged = @($obligedList | Sort-Object -Unique)
Assert-That -Name 'A-14:per-stream-obligation-set-is-non-empty' -Condition ($obliged.Count -gt 0) `
    -Detail ("obliged (batch|template|stream) triples={0}" -f $obliged.Count)
$manifestPath = Join-Path $packageRoot 'evidence-manifest.csv'
$manifestRows = @()
if (Test-Path -LiteralPath $manifestPath -PathType Leaf) { $manifestRows = @(Import-Csv -LiteralPath $manifestPath) }
$invalidScopeRows = @($manifestRows | Where-Object {
    -not $presenceByTemplate.ContainsKey($_.template_id) -or
    -not (Test-EvidenceId -EvidenceId $_.evidence_id -StreamId $_.stream_id) -or
    $_.stream_id -cnotin @(Get-UiEvidenceScopes -Mapping $streamMapping -TemplateId $_.template_id)
})
Assert-That -Name 'A-14:manifest-evidence-scope-resolution' -Condition ($invalidScopeRows.Count -eq 0) `
    -Detail ("invalid evidence scopes={0}" -f $invalidScopeRows.Count)
$satisfied = @($manifestRows | ForEach-Object { "{0}|{1}|{2}" -f $_.batch_id, $_.template_id, $_.stream_id })
$unmet = @($obliged | Where-Object { $_ -cnotin $satisfied })
$executable = @($batchRows | Where-Object { $_.ma_025_disposition -eq 'authorized_pilot' })
Assert-That -Name 'A-14:unmet-per-stream-obligations-are-explained-by-held-authorization' `
    -Condition ($unmet.Count -eq 0 -or $executable.Count -eq 0) `
    -Detail ("unmet={0}; manifest-rows={1}; batches-authorized-to-execute={2}; no batch may execute today, so an empty manifest is the expected state and is not a discharge" -f $unmet.Count, $manifestRows.Count, $executable.Count)

# --- A-15 stream-token-vocabulary-guard ------------------------------------
# Scans the design, production and UX packages. Hyphen and underscore spellings are
# normalised before comparison, because the surviving R-034 instance evaded the
# design guard for precisely that reason: the alternation matched hyphens and the
# defect was spelled with underscores inside an identifier.
$streamScanRoots = @(
    (Join-Path $repoRoot 'docs/phase-1-ui-reference-design'),
    (Join-Path $repoRoot 'docs/phase-1-ui-reference-production'),
    (Join-Path $repoRoot 'docs/phase-1-ux-architecture')
)
$presentRoots = @($streamScanRoots | Where-Object { Test-Path -LiteralPath $_ })
Assert-That -Name 'A-15:all-three-packages-are-in-scope' -Condition ($presentRoots.Count -eq 3) `
    -Detail ("roots resolved={0} of {1}" -f $presentRoots.Count, $streamScanRoots.Count)
$streamScanFiles = @($presentRoots | ForEach-Object { Get-ChildItem -LiteralPath $_ -Recurse -File -Include '*.md', '*.csv', '*.ps1' })
$legalStreamTokens = $streamSegments + @('STREAM_SCOPE')
# SCOPE NOTE, written here because the first implementation of this rule was wrong
# and a reviewer should be able to see how. Matching every `STREAM[_-][A-Z0-9]+`
# occurrence returns 32 hits across the three packages, and none of them is the
# defect this rule exists to catch: `STATE-STREAM-CHANGED` is a state value,
# `NFR-STREAM-01`..`07` are requirement identifiers, `DS-STREAM-INVARIANT` is the
# profile A-01 already guards by name, and `DELIVERY_STREAM_EVIDENCE_MODEL` is a
# filename. `STREAM` is a word three separate vocabularies legitimately use. What
# EC-08 actually governs is the frame-name SEGMENT, and that is what is matched:
# the token sitting between `_STREAM_` and the `_V<NN>` version suffix. A guard
# that fails on correct records teaches producers to widen exemptions, which is how
# the design package's peer-framing guard acquired the hole R-034 hid in.
$illegalStreamTokens = [System.Collections.Generic.List[string]]::new()
foreach ($file in $streamScanFiles) {
    $text = Get-Content -Raw -LiteralPath $file.FullName
    foreach ($hit in [regex]::Matches($text, '_(STREAM[_-][A-Z0-9]+)[_-]V\d{2}')) {
        $normalised = $hit.Groups[1].Value -creplace '-', '_'
        if ($normalised -cnotin $legalStreamTokens) {
            $illegalStreamTokens.Add(("{0}:{1}" -f $file.Name, $hit.Groups[1].Value))
        }
    }
}
Assert-That -Name 'A-15:stream-token-vocabulary-guard' -Condition ($illegalStreamTokens.Count -eq 0) `
    -Detail ("files scanned={0}; illegal=[{1}]" -f $streamScanFiles.Count, ((@($illegalStreamTokens | Sort-Object -Unique)) -join ';'))
# The rule must be able to fail. The three abolished spellings the accepted
# specification names are fed through the same matcher, in the same segment
# position, and are required to be rejected.
$vocabFixtures = @(('STREAM_' + 'FALLBACK'), ('STREAM_' + 'NONWEBGL'), ('STREAM_' + 'ALL'))
$vocabLeaks = @($vocabFixtures | Where-Object {
    $m = [regex]::Match(('_' + $_ + '_V01'), '_(STREAM[_-][A-Z0-9]+)[_-]V\d{2}')
    $m.Success -and (($m.Groups[1].Value -creplace '-', '_') -cin $legalStreamTokens)
})
Assert-That -Name 'A-15:stream-token-vocabulary-guard-rejects-abolished-spellings' -Condition ($vocabLeaks.Count -eq 0) `
    -Detail ("fixtures={0}; leaked=[{1}]" -f $vocabFixtures.Count, ($vocabLeaks -join ';'))

# --- A-16 framing-guard-scope ----------------------------------------------
# The design package's peer-framing guard is scoped to thirteen freeze files, and
# both surviving R-034 instances lived where it was not looking. Here the scope is
# the union of three whole packages, computed rather than listed, and the scope
# itself is asserted: if a package stops contributing files, this fails before the
# framing check has a chance to pass for the wrong reason.
# EVERY element is parenthesised, and it has to be. In PowerShell the comma
# operator binds tighter than `+`, so an array literal written as
# @('a' + 'b', 'c' + 'd') does not build two elements - it parses as
# 'a' + ('b','c') + 'd' and collapses to ONE string joined by $OFS. The first
# version of this list was written that way. `-join '|'` then had nothing to join,
# the alternation became a single space-separated literal, and this guard reported
# zero hits across 56 files while UX_ARCHITECTURE.md still carried the abolished
# elective-World phrasing three times. A guard that cannot fail is the exact defect D-045 was decided to
# end, and it was reintroduced here by an unparenthesised comma. No warning was
# emitted. The count is asserted below so the same silence cannot happen twice.
$framingParts = @(
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
Assert-That -Name 'A-16:framing-pattern-is-nine-alternatives' -Condition ($framingParts.Count -eq 9) `
    -Detail ("alternatives={0}; expected 9 - a count of 1 means the array literal collapsed and the guard is inert" -f $framingParts.Count)
$framingPattern = '(?i)(' + ($framingParts -join '|') + ')'
# Same principle as the design validator, stated as a rule rather than a name list:
# a dated evidence record must be able to name the defect it records as removed, and
# the two accepted specifications must be able to quote the vocabulary they abolish.
# A record that cannot name what it records is not a record.
#
# The exempt class is therefore CLOSED and structural, not discretionary: dated
# review and audit records live under a `reviews/` or `accessibility/` directory, the
# two per-package dated reports are named, and the two accepted specifications are
# named. A producer cannot quietly add a normative file to this class, because a
# normative file is not in one of those directories and does not have one of those
# names. The exemption is counted and asserted below rather than assumed, and the
# exempt set is required to be a strict subset - if it ever grows to swallow the
# scan, this fails instead of passing on an empty scan.
$framingExemptNames = @(
    'validation-report.md',
    'producer-inspection.md',
    'DELIVERY_STREAM_EVIDENCE_MODEL.md',
    'DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md'
)
$framingExemptDirs = @('reviews', 'accessibility')
function Test-FramingExempt {
    param([System.IO.FileInfo]$File)
    if ($File.Name -cin $framingExemptNames) { return $true }
    return ((Split-Path -Leaf $File.DirectoryName) -cin $framingExemptDirs)
}
$framingExempt = @($streamScanFiles | Where-Object { Test-FramingExempt -File $_ })
$framingScope  = @($streamScanFiles | Where-Object { -not (Test-FramingExempt -File $_) })
Assert-That -Name 'A-16:framing-guard-scope-is-the-three-package-union' `
    -Condition ($streamScanFiles.Count -gt 13 -and ($framingScope.Count + $framingExempt.Count) -eq $streamScanFiles.Count -and $framingScope.Count -gt $framingExempt.Count) `
    -Detail ("union={0}; scanned={1}; exempt={2}; the design package guard scopes to 13 freeze files, and the scanned set must remain larger than the exempt set" -f $streamScanFiles.Count, $framingScope.Count, $framingExempt.Count)
$framingHits = [System.Collections.Generic.List[string]]::new()
foreach ($file in $framingScope) {
    $text = Get-Content -Raw -LiteralPath $file.FullName
    foreach ($hit in [regex]::Matches($text, $framingPattern)) { $framingHits.Add(("{0}:{1}" -f $file.Name, $hit.Value)) }
}
Assert-That -Name 'A-16:no-degradation-framing-across-design-ux-and-production' -Condition ($framingHits.Count -eq 0) `
    -Detail ("hits={0}; distinct=[{1}]" -f $framingHits.Count, ((@($framingHits | Sort-Object -Unique)) -join ';'))

$result = if ($script:FailCount -eq 0) { 'PASS' } else { 'FAIL' }
Write-Output ("RESULT={0} PASS_COUNT={1} FAIL_COUNT={2}" -f $result, $script:PassCount, $script:FailCount)

if ($script:FailCount -ne 0) { exit 1 }
exit 0
