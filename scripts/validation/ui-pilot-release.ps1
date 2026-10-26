# Read-only verification of D-059 approval records. No record is generated here.
Set-StrictMode -Version Latest
. (Join-Path $PSScriptRoot 'ui-stream-mapping.ps1')
. (Join-Path $PSScriptRoot 'ui-exit-coverage.ps1')

function Get-UiApprovalMetadata {
    param([string]$Text, [string]$Name)
    $matches = [regex]::Matches($Text, ('(?m)^' + [regex]::Escape($Name) + ':[ \t]+([^\r\n]+)\r?$'))
    if ($matches.Count -ne 1) { throw "Missing or duplicate approval metadata: $Name" }
    $value = $matches[0].Groups[1].Value.Trim()
    if ([string]::IsNullOrWhiteSpace($value)) { throw 'Approval metadata value is empty' }
    return $value
}

function Resolve-UiEvidenceFilePath {
    param([string]$RepoRoot, [string]$RelativePath)
    if ([string]::IsNullOrWhiteSpace($RelativePath) -or $RelativePath -match '[:\\]' -or $RelativePath.StartsWith('/') -or @($RelativePath.Split('/') | Where-Object { $_ -in @('', '.', '..') }).Count -gt 0) { throw 'Unsafe evidence path' }
    $root = [IO.Path]::GetFullPath($RepoRoot).TrimEnd([IO.Path]::DirectorySeparatorChar)
    $path = [IO.Path]::GetFullPath((Join-Path $root $RelativePath))
    if (-not $path.StartsWith($root + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Evidence path escapes repository' }
    $cursor = $root
    foreach ($part in $RelativePath.Split('/')) {
        $cursor = Join-Path $cursor $part
        $item = Get-Item -LiteralPath $cursor -Force -ErrorAction Stop
        if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw 'Evidence references may not traverse links' }
    }
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw 'Evidence reference is not a file' }
    return $path
}

function Resolve-UiPinnedEvidenceFile {
    param([string]$RepoRoot, [string]$RelativePath, [string]$Hash)
    if ($Hash -cnotmatch '^[A-F0-9]{64}$') { throw 'Invalid evidence hash' }
    $path = Resolve-UiEvidenceFilePath $RepoRoot $RelativePath
    if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash -cne $Hash) { throw 'Evidence hash disagrees with frozen reference' }
    return $path
}

function Assert-UiBatchExitArtifacts {
    param([string]$RepoRoot, [string]$BatchId, [object]$record, [string]$ManifestPrefix, [object]$EvidenceContext, [string[]]$Obliged)
    if ($record.($ManifestPrefix + '_path') -cne ("docs/phase-1-ui-reference-production/evidence/{0}/manifest.csv" -f $BatchId)) { throw 'Proof must pin the immutable target batch manifest' }
    $paths = @{}
    foreach ($role in @($ManifestPrefix,'design_review','accessibility_review','pre_archive','exit_archive')) {
        $paths[$role] = Resolve-UiPinnedEvidenceFile $RepoRoot $record.($role + '_path') $record.($role + '_sha256')
    }
    $manifest = @(Import-Csv -LiteralPath $paths[$ManifestPrefix])
    if ($manifest.Count -eq 0 -or @($manifest | Where-Object batch_id -CNE $BatchId).Count -gt 0) { throw 'Pilot manifest is empty or contains another batch' }
    if (@($manifest.evidence_id | Sort-Object -Unique -CaseSensitive).Count -ne $manifest.Count) { throw 'Duplicate evidence identities in frozen manifest' }
    if ($paths.design_review -ceq $paths.accessibility_review -or $record.design_review_sha256 -ceq $record.accessibility_review_sha256) { throw 'Two independent reviews are required' }
    $reviewers = @()
    $producers = @()
    foreach ($role in @('design_review','accessibility_review')) {
        $review = Get-Content -LiteralPath $paths[$role] -Raw
        foreach ($pair in @(@('batch_id',$BatchId),@('manifest_sha256',$record.($ManifestPrefix + '_sha256')),@('result','PASS'),@('open_critical','0'),@('open_high','0'),@('open_medium','0'))) {
            if ((Get-UiApprovalMetadata $review $pair[0]) -cne $pair[1]) { throw 'Review does not qualify this pilot exit' }
        }
        $reviewer = Get-UiApprovalMetadata $review 'reviewer_id'
        if ($reviewer -ceq (Get-UiApprovalMetadata $review 'producer_id')) { throw 'Producer cannot approve their own output' }
        $reviewers += $reviewer
        $producers += Get-UiApprovalMetadata $review 'producer_id'
    }
    if ($producers[0] -cne $producers[1]) { throw 'Reviews disagree about the batch producer' }
    if ($reviewers[0] -ceq $reviewers[1]) { throw 'Reviewers must be independent of each other' }
    Assert-UiAcceptedExitCoverage $manifest $BatchId $EvidenceContext $Obliged
    $batchRoot = Split-Path -Parent $paths[$ManifestPrefix]
    $columns = @('evidence_id','batch_id','evidence_type','template_id','instance_id','state_id','viewport_id','mode_id','stream_id','profile_ids','prim_ids','time_limit_branch','file_relpath','sha256','export_scale','exported_on','figma_node_id','revision')
    $actualColumns = @($manifest[0].PSObject.Properties.Name)
    if ($actualColumns.Count -ne $columns.Count -or @($actualColumns | Where-Object { $_ -cnotin $columns }).Count) { throw 'Batch manifest schema mismatch' }
    $exportPaths = [string[]]@($manifest.file_relpath)
    if (@($exportPaths | Sort-Object -Unique).Count -ne $exportPaths.Count) { throw 'Duplicate export paths in batch manifest' }
    foreach ($role in @('pre_archive','exit_archive')) {
        $archiveRelative = [IO.Path]::GetRelativePath($batchRoot, $paths[$role]).Replace('\','/')
        $archive = @($manifest | Where-Object { $_.file_relpath -ceq $archiveRelative -and $_.sha256 -ceq $record.($role + '_sha256') })
        if ($archive.Count -ne 1) { throw 'Checkpoint archive is not bound in the frozen pilot manifest' }
    }
    foreach ($row in $manifest) {
        [void](Resolve-UiPinnedEvidenceFile $batchRoot $row.file_relpath $row.sha256)
    }
    [Array]::Sort($exportPaths, [StringComparer]::Ordinal)
    $digestLines = @($exportPaths | ForEach-Object {
        $exportPath = $_
        $exportRow = @($manifest | Where-Object file_relpath -CEQ $exportPath)[0]
        $exportRow.sha256 + '  ' + $exportPath
    })
    $digest = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.UTF8Encoding]::new($false).GetBytes($digestLines -join "`n")))
    if ('BoundaryAllocations' -cin @($EvidenceContext.PSObject.Properties.Name)) {
        $annotations = @{}
        foreach ($row in @($manifest | Where-Object { $_.state_id -cmatch '^STATE-(BOUNDARY|ANCESTOR)-TO-' -and $_.evidence_type -ceq 'ANNOTATION' })) {
            $annotations[$row.evidence_id] = Get-Content -LiteralPath (Resolve-UiEvidenceFilePath $batchRoot $row.file_relpath) -Raw | ConvertFrom-Json
        }
        $boundaryGaps = @(Get-UiBoundaryCoverageGaps $BatchId $manifest $EvidenceContext $annotations)
        if ($boundaryGaps.Count) { throw ('Boundary evidence incomplete: ' + ($boundaryGaps -join ';')) }
    }
    $digestPath = Resolve-UiEvidenceFilePath $batchRoot 'manifest.sha256'
    if ((Get-Content -LiteralPath $digestPath -Raw).Trim() -cne $digest) { throw 'Export inventory digest mismatch' }
    foreach ($role in @('pre_archive','exit_archive')) {
        $checkpoint = if ($role -ceq 'pre_archive') { 'PRE' } else { 'EXIT' }
        if ([IO.Path]::GetFileNameWithoutExtension($paths[$role]) -cne ("HSD_UIR_{0}_{1}" -f $BatchId,$checkpoint)) { throw 'Checkpoint role/name mismatch' }
    }
}

function Get-UiPilotAcceptance {
    param([string]$RepoRoot, [string]$RecordPath, [object]$EvidenceContext, [string[]]$Obliged)
    if (-not (Test-Path -LiteralPath $RecordPath)) { return $null }
    $relative = [IO.Path]::GetRelativePath([IO.Path]::GetFullPath($RepoRoot), [IO.Path]::GetFullPath($RecordPath)).Replace('\','/')
    $safeRecordPath = Resolve-UiEvidenceFilePath $RepoRoot $relative
    $jsonText = Get-Content -LiteralPath $safeRecordPath -Raw
    $document = [System.Text.Json.JsonDocument]::Parse($jsonText)
    try {
        if ($document.RootElement.ValueKind -ne [System.Text.Json.JsonValueKind]::Object) { throw 'Pilot approval record must be an object' }
        $names = @($document.RootElement.EnumerateObject() | ForEach-Object { $_.Name })
        if (@($names | Sort-Object -Unique -CaseSensitive).Count -ne $names.Count) { throw 'Duplicate pilot approval record fields' }
        if ($document.RootElement.GetProperty('schema_version').GetRawText() -cne '1') { throw 'Invalid pilot approval schema version' }
    } finally { $document.Dispose() }
    $record = $jsonText | ConvertFrom-Json
    $fields = @('schema_version','pilot_batch','acceptance_decision','released_batches','pilot_manifest_path','pilot_manifest_sha256','design_review_path','design_review_sha256','accessibility_review_path','accessibility_review_sha256','pre_archive_path','pre_archive_sha256','exit_archive_path','exit_archive_sha256')
    $actual = @($record.PSObject.Properties.Name)
    if ($actual.Count -ne $fields.Count -or @($actual | Where-Object { $_ -cnotin $fields }).Count -gt 0) { throw 'Pilot approval record schema mismatch' }
    if ($record.schema_version -ne 1 -or $record.pilot_batch -cne 'B01' -or $record.acceptance_decision -cnotmatch '^D-\d{3}$') { throw 'Pilot approval identity mismatch' }
    $released = @($record.released_batches)
    $expected = @('B02','B03','B04','B05','B06','B08')
    if ($released.Count -ne 6 -or (($released | Sort-Object -CaseSensitive) -join ';') -cne ($expected -join ';')) { throw 'Pilot approval release set mismatch' }
    $decisions = Get-Content -LiteralPath (Join-Path $RepoRoot 'DECISIONS.md') -Raw
    $sections = [regex]::Matches($decisions, ('(?ms)^## ' + [regex]::Escape($record.acceptance_decision) + ' [^\r\n]+\r?\n(?<body>.*?)(?=^## |\z)'))
    if ($sections.Count -ne 1) { throw 'Pilot approval decision does not resolve uniquely' }
    $decision = $sections[0].Groups['body'].Value
    if (-not (Test-UiAcceptedDecisionStatus $decision)) { throw 'Pilot approval decision is not accepted' }
    foreach ($name in @('pilot_batch','pilot_manifest_path','pilot_manifest_sha256')) {
        if ((Get-UiApprovalMetadata $decision $name) -cne $record.$name) { throw 'Decision does not explicitly accept the frozen pilot exit' }
    }
    if ((Get-UiApprovalMetadata $decision 'released_batches') -cne ($expected -join ';')) { throw 'Decision does not explicitly release the conditional batches' }
    Assert-UiBatchExitArtifacts -RepoRoot $RepoRoot -BatchId 'B01' -record $record -ManifestPrefix 'pilot_manifest' -EvidenceContext $EvidenceContext -Obliged $Obliged
    return $record
}

function Get-UiTargetBatchUnmetEvidence {
    param([string]$BatchId, [object[]]$Batches, [string[]]$Obliged, [string[]]$Satisfied, [object]$PilotAcceptance, [string[]]$AcceptedPrerequisiteExits)
    $target = @($Batches | Where-Object batch_id -CEQ $BatchId)
    if ($target.Count -ne 1 -or $BatchId -cin @('B07','B09')) { throw 'Unknown or ineligible batch-exit target' }
    $row = $target[0]
    if ($BatchId -ceq 'B01') {
        if ($row.ma_025_disposition -cne 'authorized_pilot') { throw 'B01 remains held' }
    }
    elseif ($row.ma_025_disposition -cne 'authorized_released_by_pilot' -or $null -eq $PilotAcceptance -or $BatchId -cnotin @($PilotAcceptance.released_batches)) { throw 'Conditional batch has no recorded founder pilot release' }
    foreach ($prerequisite in @($row.hard_prerequisite_batch_ids.Split(';') | Where-Object { $_ })) {
        if ($prerequisite -cnotin $AcceptedPrerequisiteExits) { throw 'Hard-prerequisite exit has not been accepted' }
    }
    # Deferrals cannot waive a target's own primary-template exit obligations.
    foreach ($coordinate in $Obliged) {
        if ($coordinate.Split('|')[0] -ceq $BatchId -and $coordinate -cnotin $Satisfied) { $coordinate }
    }
}

function Get-UiAcceptedPrerequisiteExits {
    param([string]$RepoRoot, [string[]]$Required, [object]$PilotAcceptance, [object]$EvidenceContext, [string[]]$Obliged)
    $decisions = Get-Content -LiteralPath (Join-Path $RepoRoot 'DECISIONS.md') -Raw
    $sections = @([regex]::Matches($decisions, '(?ms)^## D-\d{3} [^\r\n]+\r?\n(?<body>.*?)(?=^## |\z)'))
    foreach ($batch in $Required) {
        if ($batch -ceq 'B01' -and $null -ne $PilotAcceptance) { 'B01'; continue }
        $candidates = @($sections | Where-Object { $_.Groups['body'].Value -cmatch ('(?m)^batch_exit: ' + [regex]::Escape($batch) + '\s*$') })
        if ($candidates.Count -eq 0) { continue }
        if ($candidates.Count -ne 1) { throw 'Prerequisite exit decision is ambiguous' }
        $body = $candidates[0].Groups['body'].Value
        if (-not (Test-UiAcceptedDecisionStatus $body)) { throw 'Prerequisite exit decision is not accepted' }
        $proof = [ordered]@{}
        foreach ($name in @('batch_manifest_path','batch_manifest_sha256','design_review_path','design_review_sha256','accessibility_review_path','accessibility_review_sha256','pre_archive_path','pre_archive_sha256','exit_archive_path','exit_archive_sha256')) {
            $proof[$name] = Get-UiApprovalMetadata $body $name
        }
        Assert-UiBatchExitArtifacts -RepoRoot $RepoRoot -BatchId $batch -record ([pscustomobject]$proof) -ManifestPrefix 'batch_manifest' -EvidenceContext $EvidenceContext -Obliged $Obliged
        $batch
    }
}

function Assert-UiPilotAuthorization {
    param([string]$RepoRoot)
    $decisions = Get-Content -LiteralPath (Join-Path $RepoRoot 'DECISIONS.md') -Raw
    $sections = @([regex]::Matches($decisions, '(?ms)^## D-\d{3} [^\r\n]+\r?\n(?<body>.*?)(?=^## |\z)'))
    $candidates = @($sections | Where-Object { $_.Groups['body'].Value -cmatch '(?m)^pilot_authorization: B01[ \t]*\r?$' })
    if ($candidates.Count -ne 1) { throw 'No unique explicit founder B01 authorization' }
    $body = $candidates[0].Groups['body'].Value
    if (-not (Test-UiAcceptedDecisionStatus $body)) { throw 'Pilot authorization decision is not approved' }
    foreach ($name in @('pilot_contract_reference','pilot_entry_conditions_reference')) {
        [void](Resolve-UiEvidenceFilePath $RepoRoot (Get-UiApprovalMetadata $body $name))
    }
}

function Assert-UiAcceptedExitCoverage {
    param([object[]]$Manifest, [string]$BatchId, [object]$EvidenceContext, [string[]]$Obliged)
    if ($null -eq $EvidenceContext) { throw 'Accepted exit requires the approved evidence context' }
    $coverageGaps = @(Get-UiExitCoverageGaps $BatchId @($Manifest | Where-Object evidence_type -CNE 'ARCHIVE') $EvidenceContext)
    if ($coverageGaps.Count) { throw ('Accepted exit has contracted coverage gaps: ' + ($coverageGaps -join ';')) }
    $required = @($Obliged | Where-Object { $_.Split('|')[0] -ceq $BatchId })
    if ($required.Count -eq 0) { throw 'Accepted exit has no target coverage obligations' }
    $satisfied = @()
    foreach ($row in $Manifest) {
        if ($row.evidence_type -ceq 'ARCHIVE') { continue }
        $resolved = Get-UiResolvedManifestRow $row $EvidenceContext
        if ($null -eq $resolved) { throw 'Accepted exit contains unresolved evidence identity' }
        if ($row.evidence_type -cin @('FRAME','FOCUSED_FRAME','VARIANT')) {
            $satisfied += '{0}|{1}|{2}|{3}' -f $resolved.BatchId,$resolved.TemplateId,$resolved.StateId,$resolved.StreamId
        }
    }
    if (@($required | Where-Object { $_ -cnotin $satisfied }).Count) { throw 'Accepted exit has incomplete target frame coverage' }
}

function Test-UiAcceptedDecisionStatus {
    param([string]$Text)
    $statuses = [regex]::Matches($Text, '(?m)^\*\*Status:\*\*[ \t]+([^\r\n]+)\r?$')
    return $statuses.Count -eq 1 -and $statuses[0].Groups[1].Value.Trim() -cin @('Approved','accepted')
}

function Test-UiPilotPlanState {
    param([string]$DesignStatus, [string]$ProductionDisposition, [bool]$FounderAuthorized)
    if ($ProductionDisposition -ceq 'future_not_authorized') { return $DesignStatus -ceq 'future_not_authorized' }
    return $ProductionDisposition -ceq 'authorized_pilot' -and $DesignStatus -ceq 'authorized_pilot' -and $FounderAuthorized
}
