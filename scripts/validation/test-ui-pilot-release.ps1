#Requires -Version 7.0
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'ui-pilot-release.ps1')
. (Join-Path $PSScriptRoot 'ui-stream-mapping.ps1')
. (Join-Path $PSScriptRoot 'test-ui-exit-coverage.ps1') -FunctionsOnly
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$design = Join-Path $repo 'docs/phase-1-ui-reference-design'
$templates = @(Import-Csv (Join-Path $design 'reference-template-inventory.csv'))
$context = [pscustomobject]@{
    Templates=$templates; Batches=@(Import-Csv (Join-Path $design 'design-batch-plan.csv'))
    Profiles=@(Import-Csv (Join-Path $design 'responsive-state-mode-matrix.csv'))
    Mapping=(Get-UiStreamMapping @(Import-Csv (Join-Path $design 'component-primitives.csv')) $templates)
    Routes=@(Import-Csv (Join-Path $design 'foundation-route-coverage.csv'))
    Flows=@(Import-Csv (Join-Path $design 'foundation-flow-coverage.csv'))
}
$fixtureObliged = @('B01|TPL-GLOBAL-NAVIGATION|STATE-OPEN|S-SEMANTIC')
$script:checks = 0
function Check([string]$Name, [scriptblock]$Action, [bool]$Throws = $false) {
    $failed = $false
    try { & $Action } catch { $failed = $true; if (-not $Throws) { throw } }
    if ($Throws -and -not $failed) { throw "Expected rejection: $Name" }
    $script:checks++
    Write-Output "PASS $Name"
}
$tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$fixture = Join-Path $tempBase ('hsd-pilot-test-' + [guid]::NewGuid().ToString('N'))
[void](New-Item -ItemType Directory -Path $fixture)
$artifactPrefix = 'docs/phase-1-ui-reference-production/evidence/B01/'
$artifactRoot = Join-Path $fixture $artifactPrefix
[void](New-Item -ItemType Directory -Path $artifactRoot -Force)
function FixturePath([string]$Path) { if ($Path -in @('DECISIONS.md','pilot-release.json')) { Join-Path $fixture $Path } else { Join-Path $artifactRoot $Path } }
function Put([string]$Path, [string]$Text) { [IO.File]::WriteAllText((FixturePath $Path), $Text, [Text.UTF8Encoding]::new($false)) }
function Hash([string]$Path) { (Get-FileHash -LiteralPath (FixturePath $Path)).Hash }
function SaveRecord { Put 'pilot-release.json' ($script:record | ConvertTo-Json -Depth 5) }
try {
    Put 'HSD_UIR_B01_PRE.zip' 'synthetic pre archive'
    Put 'HSD_UIR_B01_EXIT.zip' 'synthetic exit archive'
    Put 'frame.png' 'synthetic frame'
    $proofRows = @(New-UiExitCoverageFixture B01 $context)
    $exportIndex = 0
    foreach ($row in $proofRows) {
        $exportName = "synthetic-$exportIndex.txt"; $exportIndex++
        Put $exportName 'synthetic reference fixture only'
        foreach ($pair in @(@('file_relpath',$exportName),@('sha256',(Hash $exportName)),@('export_scale','1'),@('exported_on','2026-10-03'),@('figma_node_id','synthetic'))) { $row | Add-Member -NotePropertyName $pair[0] -NotePropertyValue $pair[1] }
    }
    foreach ($name in @('HSD_UIR_B01_PRE.zip','HSD_UIR_B01_EXIT.zip')) {
        $archive = $proofRows[0].PSObject.Copy()
        $archive.evidence_id=$name; $archive.evidence_type='ARCHIVE'; $archive.file_relpath=$name; $archive.sha256=Hash $name
        $proofRows += $archive
    }
    $proofRows | Export-Csv -LiteralPath (FixturePath 'manifest.csv') -NoTypeInformation
    $inventory = @(Import-Csv -LiteralPath (FixturePath 'manifest.csv'))
    $sortedPaths = [string[]]@($inventory.file_relpath)
    [Array]::Sort($sortedPaths, [StringComparer]::Ordinal)
    $lines = @($sortedPaths | ForEach-Object { (Hash $_) + '  ' + $_ })
    Put 'manifest.sha256' ([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.UTF8Encoding]::new($false).GetBytes($lines -join "`n"))))
    $manifestHash = Hash 'manifest.csv'
    foreach ($role in @('design','accessibility')) {
        Put "$role.md" "batch_id: B01`nmanifest_sha256: $manifestHash`nresult: PASS`nopen_critical: 0`nopen_high: 0`nopen_medium: 0`nreviewer_id: $role-reviewer`nproducer_id: synthetic-producer`n"
    }
    $script:record = [ordered]@{ schema_version=1; pilot_batch='B01'; acceptance_decision='D-999'; released_batches=@('B02','B03','B04','B05','B06','B08'); pilot_manifest_path=($artifactPrefix + 'manifest.csv'); pilot_manifest_sha256=$manifestHash; design_review_path=($artifactPrefix + 'design.md'); design_review_sha256=(Hash 'design.md'); accessibility_review_path=($artifactPrefix + 'accessibility.md'); accessibility_review_sha256=(Hash 'accessibility.md'); pre_archive_path=($artifactPrefix + 'HSD_UIR_B01_PRE.zip'); pre_archive_sha256=(Hash 'HSD_UIR_B01_PRE.zip'); exit_archive_path=($artifactPrefix + 'HSD_UIR_B01_EXIT.zip'); exit_archive_sha256=(Hash 'HSD_UIR_B01_EXIT.zip') }
    $decision = "## D-999 Synthetic fixture only`n`n**Status:** Approved`npilot_batch: B01`npilot_manifest_path: ${artifactPrefix}manifest.csv`npilot_manifest_sha256: $manifestHash`nreleased_batches: B02;B03;B04;B05;B06;B08`n"
    Put 'DECISIONS.md' $decision
    $recordPath = Join-Path $fixture 'pilot-release.json'
    Check 'missing record stays held' { if ($null -ne (Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged)) { throw 'Unexpected release' } }
    SaveRecord
    Check 'explicit synthetic acceptance resolves' { $script:accepted = Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged; if ($null -eq $script:accepted) { throw 'Missing acceptance' } }
    Check 'generic decision cannot authorize pilot' { Assert-UiPilotAuthorization $fixture } $true
    Put 'DECISIONS.md' ($decision + "`npilot_authorization: B01`npilot_contract_reference: ${artifactPrefix}design.md`npilot_entry_conditions_reference: ${artifactPrefix}accessibility.md`n")
    Check 'explicit pilot authorization resolves' { Assert-UiPilotAuthorization $fixture }
    Put 'DECISIONS.md' $decision
    $inventoryDigest = Get-Content -LiteralPath (FixturePath 'manifest.sha256') -Raw
    Put 'manifest.sha256' ('A' * 64)
    Check 'export inventory digest mismatch rejected' { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
    Put 'manifest.sha256' $inventoryDigest
    Check 'missing approved coverage context rejected' { Get-UiPilotAcceptance $fixture $recordPath $null $fixtureObliged | Out-Null } $true
    Check 'additional required frame cannot be waived' { Get-UiPilotAcceptance $fixture $recordPath $context ($fixtureObliged + 'B01|TPL-GLOBAL-NAVIGATION|STATE-MISSING|S-SEMANTIC') | Out-Null } $true
    $badRow = [pscustomobject]@{ evidence_type='FRAME'; evidence_id='synthetic'; batch_id='B01'; template_id='TPL-GLOBAL-NAVIGATION'; stream_id='S-SEMANTIC' }
    Check 'unresolved accepted evidence rejected' { Assert-UiAcceptedExitCoverage @($badRow) B01 $context $fixtureObliged } $true
    Check 'CRLF metadata parses without changing content' { if ((Get-UiApprovalMetadata "result: PASS`r`n" 'result') -cne 'PASS') { throw 'CRLF metadata failed' } }
    Check 'conflicting decision statuses rejected' { if (Test-UiAcceptedDecisionStatus "**Status:** Approved`n**Status:** Rejected`n") { throw 'Ambiguous status accepted' } }
    $prerequisiteDecision = "## D-998 Synthetic prerequisite fixture`n**Status:** Approved`nbatch_exit: B01`n"
    foreach ($field in @('pilot_manifest_path','pilot_manifest_sha256','design_review_path','design_review_sha256','accessibility_review_path','accessibility_review_sha256','pre_archive_path','pre_archive_sha256','exit_archive_path','exit_archive_sha256')) {
        $metadataName = $field.Replace('pilot_manifest','batch_manifest')
        $prerequisiteDecision += "${metadataName}: $($script:record[$field])`n"
    }
    Put 'DECISIONS.md' ($decision + "`n" + $prerequisiteDecision)
    Check 'recorded prerequisite resolves the same frozen artifacts' { if (@(Get-UiAcceptedPrerequisiteExits $fixture @('B01') $null $context $fixtureObliged) -cnotcontains 'B01') { throw 'Missing prerequisite' } }
    Check 'prerequisite acceptance cannot waive missing coverage' { Get-UiAcceptedPrerequisiteExits $fixture @('B01') $null $context ($fixtureObliged + 'B01|TPL-GLOBAL-NAVIGATION|STATE-MISSING|S-SEMANTIC') | Out-Null } $true
    Put 'DECISIONS.md' $decision
    $manifestText = Get-Content -LiteralPath (FixturePath 'manifest.csv') -Raw
    $duplicateRows = @(Import-Csv -LiteralPath (FixturePath 'manifest.csv'))
    $duplicateRows[1].evidence_id = $duplicateRows[0].evidence_id
    $duplicateRows | Export-Csv -LiteralPath (FixturePath 'manifest.csv') -NoTypeInformation
    $duplicateHash = Hash 'manifest.csv'
    $duplicateProof = [pscustomobject]$script:record
    $duplicateProof.pilot_manifest_sha256 = $duplicateHash
    Check 'duplicate evidence identities rejected before artifact acceptance' { Assert-UiBatchExitArtifacts $fixture B01 $duplicateProof 'pilot_manifest' $context $fixtureObliged } $true
    Put 'manifest.csv' $manifestText
    $script:record.pilot_manifest_sha256 = $manifestHash
    SaveRecord
    $originalJson = Get-Content -LiteralPath $recordPath -Raw
    foreach ($field in @('pilot_manifest_sha256','design_review_sha256','accessibility_review_sha256','pre_archive_sha256','exit_archive_sha256')) {
        $old = $script:record[$field]; $script:record[$field] = 'A' * 64; SaveRecord
        Check "stale $field rejected" { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
        $script:record[$field] = $old; SaveRecord
    }
    Put 'DECISIONS.md' "## D-999 Unrelated approval`n**Status:** Approved`n"
    Check 'unrelated approval rejected' { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
    Put 'DECISIONS.md' $decision
    Put 'pilot-release.json' ($originalJson.Replace('"schema_version": 1','"schema_version": true'))
    Check 'boolean schema rejected' { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
    Put 'pilot-release.json' ($originalJson.Replace('"schema_version": 1','"schema_version": 1, "schema_version": 1'))
    Check 'duplicate fields rejected' { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
    SaveRecord
    $script:record.released_batches = @('B02','B03','B04','B05','B06','B07'); SaveRecord
    Check 'deferred batch cannot be released' { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
    $script:record.released_batches = @('B02','B03','B04','B05','B06','B08'); SaveRecord
    foreach ($path in @('../outside.txt','C:/outside.txt','/outside.txt','a//b','./frame.png')) {
        Check "unsafe path $path rejected" { Resolve-UiEvidenceFilePath $fixture $path | Out-Null } $true
    }
    Check 'missing artifact rejected' { Resolve-UiPinnedEvidenceFile $fixture 'missing.zip' ('A' * 64) | Out-Null } $true
    $review = Get-Content -LiteralPath (FixturePath 'design.md') -Raw
    Put 'design.md' ($review.Replace('open_high: 0','open_high: 1'))
    $script:record.design_review_sha256 = Hash 'design.md'; SaveRecord
    Check 'open HIGH finding rejected' { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
    Put 'design.md' ($review.Replace('reviewer_id: design-reviewer','reviewer_id: synthetic-producer'))
    $script:record.design_review_sha256 = Hash 'design.md'; SaveRecord
    Check 'self review rejected' { Get-UiPilotAcceptance $fixture $recordPath $context $fixtureObliged | Out-Null } $true
    Put 'design.md' $review; $script:record.design_review_sha256 = Hash 'design.md'; SaveRecord
    $batches = @(
        [pscustomobject]@{batch_id='B01'; ma_025_disposition='future_not_authorized'; hard_prerequisite_batch_ids=''},
        [pscustomobject]@{batch_id='B02'; ma_025_disposition='authorized_released_by_pilot'; hard_prerequisite_batch_ids='B01'},
        [pscustomobject]@{batch_id='B03'; ma_025_disposition='authorized_released_by_pilot'; hard_prerequisite_batch_ids='B01'},
        [pscustomobject]@{batch_id='B07'; ma_025_disposition='deferred_not_authorizable'; hard_prerequisite_batch_ids=''}
    )
    $obliged = @('B01|one','B02|two','B03|three','B07|seven')
    Check 'held pilot rejects exit' { Get-UiTargetBatchUnmetEvidence B01 $batches $obliged @() $null @() | Out-Null } $true
    $batches[0].ma_025_disposition = 'authorized_pilot'
    Check 'pilot checks only its own evidence' { $missing = @(Get-UiTargetBatchUnmetEvidence B01 $batches $obliged @('B01|one') $null @()); if ($missing.Count) { throw 'Unrelated evidence required' } }
    Check 'complete pilot evidence alone cannot release B02' { Get-UiTargetBatchUnmetEvidence B02 $batches $obliged $obliged $null @('B01') | Out-Null } $true
    Check 'conditional own evidence is required' { $missing = @(Get-UiTargetBatchUnmetEvidence B02 $batches $obliged @() $script:accepted @('B01')); if ($missing.Count -ne 1 -or $missing[0] -cne 'B02|two') { throw 'Wrong target obligations' } }
    Check 'unstarted and deferred batches do not block B02' { if (@(Get-UiTargetBatchUnmetEvidence B02 $batches $obliged @('B02|two') $script:accepted @('B01')).Count) { throw 'Wrong global coverage' } }
    Check 'missing prerequisite rejects exit' { Get-UiTargetBatchUnmetEvidence B02 $batches $obliged $obliged $script:accepted @() | Out-Null } $true
    foreach ($target in @('B07','B09','B99')) { Check "ineligible target $target rejected" { Get-UiTargetBatchUnmetEvidence $target $batches $obliged $obliged $script:accepted @('B01') | Out-Null } $true }
    Check 'held plans agree without founder authorization' { if (-not (Test-UiPilotPlanState 'future_not_authorized' 'future_not_authorized' $false)) { throw 'Held plans disagree' } }
    Check 'authorized plans require explicit founder decision' { if (Test-UiPilotPlanState 'authorized_pilot' 'authorized_pilot' $false) { throw 'Implicit authorization' } }
    Check 'authorized plans agree only after explicit decision' { if (-not (Test-UiPilotPlanState 'authorized_pilot' 'authorized_pilot' $true)) { throw 'Authorized plans disagree' } }
    Check 'contradictory held design blocks authorized production' { if (Test-UiPilotPlanState 'future_not_authorized' 'authorized_pilot' $true) { throw 'Contradictory authorization' } }
    Write-Output "RESULT=PASS CHECKS=$script:checks"
} finally {
    $resolvedFixture = [IO.Path]::GetFullPath($fixture)
    if (-not $resolvedFixture.StartsWith($tempBase.TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase) -or [IO.Path]::GetFileName($resolvedFixture) -notlike 'hsd-pilot-test-*') { throw 'Unsafe fixture cleanup path' }
    Remove-Item -LiteralPath $resolvedFixture -Recurse -Force
}
