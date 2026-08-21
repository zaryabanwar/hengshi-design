#requires -Version 7.0

[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$CompatibilityRoot = $PSScriptRoot
$RepositoryRoot = (Resolve-Path -LiteralPath (Join-Path $CompatibilityRoot "../..")).Path
$BaselinePath = Join-Path $CompatibilityRoot "baseline-inventory.json"
$GraphPath = Join-Path $CompatibilityRoot "compatibility-graph.json"
$ControlsPath = Join-Path $CompatibilityRoot "compatibility-controls.json"
$ReferenceIndexPath = Join-Path $CompatibilityRoot "reference-index.json"
$EvidencePath = Join-Path $CompatibilityRoot "evidence-log-2026-07-19.md"
$BlockersPath = Join-Path $CompatibilityRoot "blockers-and-obligations.md"
$ReadmePath = Join-Path $CompatibilityRoot "README.md"
$ReviewIteration1Path = Join-Path $CompatibilityRoot "reviews/architecture-supply-chain-review-iteration-1.md"
$ReviewIteration2Path = Join-Path $CompatibilityRoot "reviews/architecture-supply-chain-review-iteration-2.md"
$Failures = [System.Collections.Generic.List[string]]::new()
$Passes = [System.Collections.Generic.List[string]]::new()
$PlaceholderPattern = '(?im)\b(?:TO' + 'DO|T' + 'BD|FIX' + 'ME|X' + 'XX)\b'

function Add-Failure {
    param([Parameter(Mandatory)][string]$Message)
    $Failures.Add($Message)
}

function Add-Pass {
    param([Parameter(Mandatory)][string]$Message)
    $Passes.Add($Message)
}

function Test-HasProperty {
    param(
        [Parameter(Mandatory)]$Object,
        [Parameter(Mandatory)][string]$Name
    )
    return $null -ne $Object -and $Object.PSObject.Properties.Name -contains $Name
}

function Test-NonEmptyArray {
    param($Value)
    return $null -ne $Value -and @($Value).Count -gt 0 -and
        @($Value | Where-Object { $null -eq $_ -or [string]::IsNullOrWhiteSpace([string]$_) }).Count -eq 0
}

function Get-ById {
    param(
        [Parameter(Mandatory)]$Collection,
        [Parameter(Mandatory)][string]$Id
    )
    return @($Collection | Where-Object { $_.id -eq $Id })[0]
}

function Assert-GraphRecord {
    param(
        [Parameter(Mandatory)]$Record,
        [Parameter(Mandatory)][string]$Kind
    )

    $Required = @(
        "id", "current", "targetCandidate", "status", "stability", "evidence",
        "constraints", "rollback", "requiredTests", "lockSelectionState"
    )
    foreach ($Name in $Required) {
        if (-not (Test-HasProperty -Object $Record -Name $Name)) {
            Add-Failure "$Kind '$($Record.id)' is missing required property '$Name'."
        }
    }

    if ([string]::IsNullOrWhiteSpace([string]$Record.id)) {
        Add-Failure "$Kind has an empty id."
    }
    if ($null -eq $Record.current) {
        Add-Failure "$Kind '$($Record.id)' has no current-state object."
    }
    if ($null -eq $Record.targetCandidate) {
        if (-not (Test-HasProperty -Object $Record -Name "targetCandidateReason") -or
            [string]::IsNullOrWhiteSpace([string]$Record.targetCandidateReason)) {
            Add-Failure "$Kind '$($Record.id)' defers a candidate without a reason."
        }
    }
    if ([string]::IsNullOrWhiteSpace([string]$Record.status)) {
        Add-Failure "$Kind '$($Record.id)' has an empty status."
    }
    if ([string]::IsNullOrWhiteSpace([string]$Record.stability)) {
        Add-Failure "$Kind '$($Record.id)' has an empty stability value."
    }
    if ($Record.lockSelectionState -ne "deferred") {
        Add-Failure "$Kind '$($Record.id)' claims lockSelectionState '$($Record.lockSelectionState)' instead of 'deferred'."
    }
    if ($null -eq $Record.evidence -or $Record.evidence.date -notmatch '^\d{4}-\d{2}-\d{2}$' -or
        -not (Test-NonEmptyArray $Record.evidence.refs)) {
        Add-Failure "$Kind '$($Record.id)' lacks dated, nonempty evidence references."
    }
    if (-not (Test-NonEmptyArray $Record.constraints)) {
        Add-Failure "$Kind '$($Record.id)' has no compatibility constraints."
    }
    if (-not (Test-NonEmptyArray $Record.requiredTests)) {
        Add-Failure "$Kind '$($Record.id)' has no required tests."
    }
    if ($null -eq $Record.rollback -or
        [string]::IsNullOrWhiteSpace([string]$Record.rollback.trigger) -or
        [string]::IsNullOrWhiteSpace([string]$Record.rollback.strategy) -or
        -not (Test-NonEmptyArray $Record.rollback.evidenceRequired)) {
        Add-Failure "$Kind '$($Record.id)' lacks a concrete rollback trigger, strategy, or evidence requirement."
    }
}

function Add-NestedReferenceUses {
    param(
        $Value,
        [Parameter(Mandatory)][string]$Artifact,
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)]$Collector
    )

    if ($null -eq $Value) {
        return
    }
    if ($Value -is [pscustomobject]) {
        foreach ($Property in $Value.PSObject.Properties) {
            $PropertyPath = if ([string]::IsNullOrWhiteSpace($Path)) {
                $Property.Name
            }
            else {
                "$Path.$($Property.Name)"
            }
            if ($Property.Name -match '(?i)(?:Ref|Refs)$') {
                $FieldValues = @(
                    @($Property.Value) |
                        Where-Object { $null -ne $_ -and -not [string]::IsNullOrWhiteSpace([string]$_) } |
                        ForEach-Object { [string]$_ }
                )
                $DuplicateValues = @($FieldValues | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
                if ($DuplicateValues.Count -gt 0) {
                    Add-Failure "Duplicate references in ${Artifact}:${PropertyPath}: $($DuplicateValues -join ', ')."
                }
                foreach ($Reference in $FieldValues) {
                    $Collector.Add([pscustomobject]@{
                        Artifact = $Artifact
                        Path = $PropertyPath
                        Reference = $Reference
                    })
                }
            }
            Add-NestedReferenceUses -Value $Property.Value -Artifact $Artifact -Path $PropertyPath -Collector $Collector
        }
        return
    }
    if ($Value -is [System.Collections.IEnumerable] -and $Value -isnot [string]) {
        $Index = 0
        foreach ($Item in $Value) {
            Add-NestedReferenceUses -Value $Item -Artifact $Artifact -Path "$Path[$Index]" -Collector $Collector
            $Index++
        }
    }
}

foreach ($RequiredFile in @(
    $BaselinePath,
    $GraphPath,
    $ControlsPath,
    $ReferenceIndexPath,
    $EvidencePath,
    $BlockersPath,
    $ReadmePath,
    $ReviewIteration1Path,
    $ReviewIteration2Path
)) {
    if (-not (Test-Path -LiteralPath $RequiredFile -PathType Leaf)) {
        Add-Failure "Required artifact is missing: $([System.IO.Path]::GetFileName($RequiredFile))."
    }
}

if ($Failures.Count -gt 0) {
    $Failures | ForEach-Object { Write-Error $_ }
    exit 1
}

try {
    $Baseline = Get-Content -LiteralPath $BaselinePath -Raw | ConvertFrom-Json -Depth 100
    $Graph = Get-Content -LiteralPath $GraphPath -Raw | ConvertFrom-Json -Depth 100
    $Controls = Get-Content -LiteralPath $ControlsPath -Raw | ConvertFrom-Json -Depth 100
    $ReferenceIndex = Get-Content -LiteralPath $ReferenceIndexPath -Raw | ConvertFrom-Json -Depth 100
    Add-Pass "JSON syntax: baseline, graph, controls, and reference index parsed."
}
catch {
    Add-Failure "JSON parsing failed: $($_.Exception.Message)"
}

if ($null -ne $Baseline -and $null -ne $Graph -and $null -ne $Controls -and $null -ne $ReferenceIndex) {
    if ($Baseline.lockSelectionState -ne "deferred" -or $Graph.lockSelectionState -ne "deferred" -or
        $Controls.lockSelectionState -ne "deferred") {
        Add-Failure "Top-level lock selection is not deferred in all machine decision artifacts."
    }
    else {
        Add-Pass "Decision boundary: all top-level lock selection remains deferred."
    }

    $BaselineIds = @($Baseline.items.id)
    $CapabilityIds = @($Baseline.capabilities.id)
    $ComponentIds = @($Graph.components.id)
    $EdgeIds = @($Graph.edges.id)
    $DeferredFamilyIds = @($Graph.deferredFamilies.id)
    $GateIds = @($Controls.humanGates.id)

    foreach ($Pair in @(
        @{ Name = "baseline item"; Values = $BaselineIds },
        @{ Name = "capability"; Values = $CapabilityIds },
        @{ Name = "graph component"; Values = $ComponentIds },
        @{ Name = "graph edge"; Values = $EdgeIds },
        @{ Name = "deferred family"; Values = $DeferredFamilyIds },
        @{ Name = "human gate"; Values = $GateIds },
        @{ Name = "wave"; Values = @($Controls.waves.id) },
        @{ Name = "checkpoint"; Values = @($Controls.checkpoints.id) },
        @{ Name = "candidate path"; Values = @($Controls.candidatePaths.id) },
        @{ Name = "supply-chain obligation"; Values = @($Controls.supplyChainObligations.id) },
        @{ Name = "reference index entry"; Values = @($ReferenceIndex.entries.id) }
    )) {
        $Duplicates = @($Pair.Values | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
        if ($Duplicates.Count -gt 0) {
            Add-Failure "Duplicate $($Pair.Name) ids: $($Duplicates -join ', ')."
        }
    }

    $ReferenceFailureCountBefore = $Failures.Count
    $AllowedNamespaces = @($ReferenceIndex.allowedNamespaces)
    $NamespaceNameDuplicates = @($AllowedNamespaces.name | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
    $NamespacePatternDuplicates = @($AllowedNamespaces.pattern | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
    if ($NamespaceNameDuplicates.Count -gt 0 -or $NamespacePatternDuplicates.Count -gt 0) {
        Add-Failure "Reference index has duplicate namespace names or patterns."
    }
    foreach ($Namespace in $AllowedNamespaces) {
        if ([string]::IsNullOrWhiteSpace([string]$Namespace.name) -or
            [string]::IsNullOrWhiteSpace([string]$Namespace.pattern)) {
            Add-Failure "Reference index contains an incomplete namespace."
            continue
        }
        try {
            [void][regex]::new([string]$Namespace.pattern)
        }
        catch {
            Add-Failure "Reference namespace '$($Namespace.name)' has an invalid pattern."
        }
    }

    $ReferenceEntriesById = @{}
    foreach ($Entry in $ReferenceIndex.entries) {
        if ([string]::IsNullOrWhiteSpace([string]$Entry.id) -or
            [string]::IsNullOrWhiteSpace([string]$Entry.namespace) -or
            [string]::IsNullOrWhiteSpace([string]$Entry.kind) -or
            $null -eq $Entry.target -or
            [string]::IsNullOrWhiteSpace([string]$Entry.target.path)) {
            Add-Failure "Reference index contains an incomplete entry."
            continue
        }
        if (-not $ReferenceEntriesById.ContainsKey([string]$Entry.id)) {
            $ReferenceEntriesById[[string]$Entry.id] = $Entry
        }
        $NamespaceMatches = @($AllowedNamespaces | Where-Object { [string]$Entry.id -match [string]$_.pattern })
        if ($NamespaceMatches.Count -ne 1) {
            Add-Failure "Reference '$($Entry.id)' has ambiguous or missing namespace resolution."
        }
        elseif ($NamespaceMatches[0].name -ne $Entry.namespace) {
            Add-Failure "Reference '$($Entry.id)' declares namespace '$($Entry.namespace)' but resolves to '$($NamespaceMatches[0].name)'."
        }

        if ([System.IO.Path]::IsPathRooted([string]$Entry.target.path)) {
            Add-Failure "Reference '$($Entry.id)' uses an absolute local target."
            continue
        }
        $ResolvedTarget = [System.IO.Path]::GetFullPath((Join-Path $RepositoryRoot ([string]$Entry.target.path)))
        $RepositoryPrefix = $RepositoryRoot.TrimEnd([System.IO.Path]::DirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
        if (-not $ResolvedTarget.StartsWith($RepositoryPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            Add-Failure "Reference '$($Entry.id)' resolves outside the repository."
            continue
        }
        if (-not (Test-Path -LiteralPath $ResolvedTarget)) {
            Add-Failure "Reference '$($Entry.id)' has an unresolved local target."
            continue
        }
        if ($Entry.kind -eq 'record') {
            if ([string]::IsNullOrWhiteSpace([string]$Entry.target.recordId) -or
                -not (Test-Path -LiteralPath $ResolvedTarget -PathType Leaf)) {
                Add-Failure "Record reference '$($Entry.id)' lacks a resolvable file and record locator."
                continue
            }
            $TargetText = [System.IO.File]::ReadAllText($ResolvedTarget)
            $RecordPattern = '(?<![A-Za-z0-9_-])' + [regex]::Escape([string]$Entry.target.recordId) + '(?![A-Za-z0-9_-])'
            if ($TargetText -notmatch $RecordPattern) {
                Add-Failure "Record reference '$($Entry.id)' locator is unresolved in its target."
            }
        }
        elseif ($Entry.kind -ne 'path') {
            Add-Failure "Reference '$($Entry.id)' has unsupported kind '$($Entry.kind)'."
        }
    }

    $ReferenceUses = [System.Collections.Generic.List[object]]::new()
    Add-NestedReferenceUses -Value $Baseline -Artifact 'baseline-inventory.json' -Path '$' -Collector $ReferenceUses
    Add-NestedReferenceUses -Value $Graph -Artifact 'compatibility-graph.json' -Path '$' -Collector $ReferenceUses
    Add-NestedReferenceUses -Value $Controls -Artifact 'compatibility-controls.json' -Path '$' -Collector $ReferenceUses
    $ReferenceUseCount = $ReferenceUses.Count
    $UniqueReferenceCount = @($ReferenceUses.Reference | Sort-Object -Unique).Count
    foreach ($Use in $ReferenceUses) {
        if (-not $ReferenceEntriesById.ContainsKey([string]$Use.Reference)) {
            Add-Failure "Unknown reference '$($Use.Reference)' at $($Use.Artifact):$($Use.Path)."
        }
    }
    if ($Failures.Count -eq $ReferenceFailureCountBefore) {
        Add-Pass "Reference resolution: checked $ReferenceUseCount uses across $UniqueReferenceCount unique ids; zero unknown, duplicate, ambiguous, or unresolved references."
    }

    $MissingComponents = @($BaselineIds | Where-Object { $_ -notin $ComponentIds })
    $ExtraComponents = @($ComponentIds | Where-Object { $_ -notin $BaselineIds })
    if ($MissingComponents.Count -gt 0 -or $ExtraComponents.Count -gt 0) {
        Add-Failure "Baseline/graph component mismatch. Missing: $($MissingComponents -join ', '); extra: $($ExtraComponents -join ', ')."
    }
    else {
        Add-Pass "Coverage: every baseline item has exactly one graph component."
    }

    foreach ($Component in $Graph.components) {
        Assert-GraphRecord -Record $Component -Kind "Component"
    }
    foreach ($Edge in $Graph.edges) {
        Assert-GraphRecord -Record $Edge -Kind "Edge"
        if ($Edge.from -notin $ComponentIds -or $Edge.to -notin $ComponentIds) {
            Add-Failure "Edge '$($Edge.id)' references an unknown component ('$($Edge.from)' -> '$($Edge.to)')."
        }
        if ($Edge.from -eq $Edge.to) {
            Add-Failure "Edge '$($Edge.id)' is a self-edge."
        }
    }
    $RequiredDeferredFamilyIds = @(
        'deferred-redis', 'deferred-azure-ai-search-sdks', 'deferred-microsoft-graph-sdks',
        'deferred-observability-sdks', 'deferred-nvidia-clients', 'deferred-blender-gltf-tooling',
        'deferred-ci-actions', 'deferred-container-images', 'deferred-bicep-api-versions'
    )
    foreach ($Family in $Graph.deferredFamilies) {
        Assert-GraphRecord -Record $Family -Kind "Deferred family"
        if ($Family.status -ne 'not_present_architecture_selection_deferred') {
            Add-Failure "Deferred family '$($Family.id)' has unexpected status '$($Family.status)'."
        }
        if (-not (Test-NonEmptyArray $Family.selectionEvidenceRequired) -or
            [string]::IsNullOrWhiteSpace([string]$Family.couplingOwner) -or
            [string]::IsNullOrWhiteSpace([string]$Family.laterPhase1Dependency)) {
            Add-Failure "Deferred family '$($Family.id)' lacks selection evidence, coupling owner, or later Phase 1 dependency."
        }
        if ($Family.targetCandidate -ne $null -or $Family.humanApprovalRequired -ne $true) {
            Add-Failure "Deferred family '$($Family.id)' must remain unselected and human-gated."
        }
    }
    $MissingDeferredFamilies = @($RequiredDeferredFamilyIds | Where-Object { $_ -notin $DeferredFamilyIds })
    if ($MissingDeferredFamilies.Count -gt 0) {
        Add-Failure "Required deferred matrix families are missing: $($MissingDeferredFamilies -join ', ')."
    }
    if ($Failures.Count -eq 0) {
        Add-Pass "Graph structure: components, edges, and required absent families include evidence, constraints, rollback, tests, ownership, and deferred-lock state."
    }

    $CandidateChannelPattern = '(?i)(?:^|[^a-z0-9])(?:alpha|beta|canary|experimental|nightly|preview|release[-_ ]?candidate|rc(?:[._-]?\d+)?)(?:$|[^a-z0-9])'
    foreach ($Record in @($Graph.components) + @($Graph.edges) + @($Graph.deferredFamilies)) {
        if ($null -ne $Record.targetCandidate) {
            $CandidateText = $Record.targetCandidate | ConvertTo-Json -Depth 30 -Compress
            if ($CandidateText -match $CandidateChannelPattern) {
                Add-Failure "Candidate '$($Record.id)' contains a disallowed production release channel."
            }
        }
    }
    if (-not ($Failures | Where-Object { $_ -like "Candidate '*" })) {
        Add-Pass "Candidate channels: no pre-stable production target appears in targetCandidate data."
    }

    $WaveIds = @($Controls.waves.id)
    $CheckpointIds = @($Controls.checkpoints.id)
    $RequiredWaveIds = 0..13 | ForEach-Object { 'WAVE-{0:d2}' -f $_ }
    $RequiredCheckpointIds = 0..13 | ForEach-Object { 'CP-{0:d2}' -f $_ }
    $MissingWaves = @($RequiredWaveIds | Where-Object { $_ -notin $WaveIds })
    $ExtraWaves = @($WaveIds | Where-Object { $_ -notin $RequiredWaveIds })
    $MissingCheckpoints = @($RequiredCheckpointIds | Where-Object { $_ -notin $CheckpointIds })
    $ExtraCheckpoints = @($CheckpointIds | Where-Object { $_ -notin $RequiredCheckpointIds })
    if ($MissingWaves.Count -gt 0 -or $ExtraWaves.Count -gt 0 -or
        $MissingCheckpoints.Count -gt 0 -or $ExtraCheckpoints.Count -gt 0) {
        Add-Failure "Wave/checkpoint id set is incomplete or contains unplanned records."
    }
    foreach ($Wave in $Controls.waves) {
        if ([string]::IsNullOrWhiteSpace([string]$Wave.name) -or
            $Wave.state -ne 'not_authorized' -or
            [string]::IsNullOrWhiteSpace([string]$Wave.scope) -or
            $Wave.outputCheckpointId -notin $CheckpointIds -or
            -not (Test-NonEmptyArray $Wave.gateIds) -or
            -not (Test-NonEmptyArray $Wave.requiredTests) -or
            [string]::IsNullOrWhiteSpace([string]$Wave.rollback)) {
            Add-Failure "Wave '$($Wave.id)' is incomplete or claims authorization."
        }
        if ($null -ne $Wave.entryCheckpointId -and $Wave.entryCheckpointId -notin $CheckpointIds) {
            Add-Failure "Wave '$($Wave.id)' has an unknown entry checkpoint."
        }
        $UnknownWaveGates = @($Wave.gateIds | Where-Object { $_ -notin $GateIds })
        if ($UnknownWaveGates.Count -gt 0) {
            Add-Failure "Wave '$($Wave.id)' references unknown human gates."
        }
    }
    foreach ($Checkpoint in $Controls.checkpoints) {
        if ($Checkpoint.afterWaveId -notin $WaveIds -or
            $Checkpoint.state -ne 'unaccepted' -or
            [string]::IsNullOrWhiteSpace([string]$Checkpoint.compatibilityRule) -or
            -not (Test-NonEmptyArray $Checkpoint.acceptanceEvidence) -or
            [string]::IsNullOrWhiteSpace([string]$Checkpoint.rollback)) {
            Add-Failure "Checkpoint '$($Checkpoint.id)' is incomplete or claims acceptance."
        }
        $OwningWave = Get-ById -Collection $Controls.waves -Id $Checkpoint.afterWaveId
        if ($null -eq $OwningWave -or $OwningWave.outputCheckpointId -ne $Checkpoint.id) {
            Add-Failure "Checkpoint '$($Checkpoint.id)' is not the declared output of its wave."
        }
    }

    $AssignmentEdgeIds = @($Controls.edgeAssignments.edgeId)
    $DuplicateAssignedEdges = @($AssignmentEdgeIds | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
    $MissingAssignedEdges = @($EdgeIds | Where-Object { $_ -notin $AssignmentEdgeIds })
    $UnknownAssignedEdges = @($AssignmentEdgeIds | Where-Object { $_ -notin $EdgeIds })
    if ($DuplicateAssignedEdges.Count -gt 0 -or $MissingAssignedEdges.Count -gt 0 -or $UnknownAssignedEdges.Count -gt 0) {
        Add-Failure "Every graph edge must have exactly one wave/checkpoint assignment."
    }
    foreach ($Assignment in $Controls.edgeAssignments) {
        if ($Assignment.waveId -notin $WaveIds -or $Assignment.outputCheckpointId -notin $CheckpointIds) {
            Add-Failure "Edge assignment '$($Assignment.edgeId)' references an unknown wave or checkpoint."
            continue
        }
        $AssignedWave = Get-ById -Collection $Controls.waves -Id $Assignment.waveId
        if ($AssignedWave.outputCheckpointId -ne $Assignment.outputCheckpointId) {
            Add-Failure "Edge assignment '$($Assignment.edgeId)' does not use its wave's output checkpoint."
        }
    }

    $AtomicReactWave = Get-ById -Collection $Controls.waves -Id 'WAVE-04'
    $RequiredAtomicReactComponents = @(
        'frontend-react', 'frontend-react-dom', 'frontend-types-react',
        'frontend-types-react-dom', 'three-r3f', 'three-drei'
    )
    $MissingAtomicReactComponents = @($RequiredAtomicReactComponents | Where-Object { $_ -notin @($AtomicReactWave.atomicComponentIds) })
    if ($MissingAtomicReactComponents.Count -gt 0) {
        Add-Failure "WAVE-04 does not transition the complete React/R3F/Drei peer set atomically."
    }
    foreach ($EdgeId in @('edge-react-dom', 'edge-react-types', 'edge-react-dom-types', 'edge-react-r3f', 'edge-r3f-drei')) {
        $Assignment = Get-ById -Collection $Controls.edgeAssignments -Id $EdgeId
        if ($null -eq $Assignment) {
            $Assignment = @($Controls.edgeAssignments | Where-Object edgeId -eq $EdgeId)[0]
        }
        if ($null -eq $Assignment -or $Assignment.waveId -ne 'WAVE-04' -or $Assignment.outputCheckpointId -ne 'CP-04') {
            Add-Failure "React peer edge '$EdgeId' is not closed atomically at CP-04."
        }
    }
    $ReactCheckpoint = Get-ById -Collection $Controls.checkpoints -Id 'CP-04'
    if ($null -eq $ReactCheckpoint -or
        @($ReactCheckpoint.forbiddenCombinations).Count -lt 3 -or
        $ReactCheckpoint.compatibilityRule -notmatch 'React 19' -or
        $ReactCheckpoint.compatibilityRule -notmatch 'R3F 9' -or
        $ReactCheckpoint.compatibilityRule -notmatch 'Drei 10' -or
        $ReactCheckpoint.compatibilityRule -notmatch 'Three 0\.160\.1') {
        Add-Failure "CP-04 does not explicitly prohibit incompatible React/R3F/Drei checkpoints and prove retained Three peer satisfaction."
    }
    $RouterAssignment = @($Controls.edgeAssignments | Where-Object edgeId -eq 'edge-react-router')[0]
    $ThreeAssignment = @($Controls.edgeAssignments | Where-Object edgeId -eq 'edge-three-r3f')[0]
    $ZustandPath = @($Controls.candidatePaths | Where-Object componentId -eq 'frontend-zustand')[0]
    $GsapPath = @($Controls.candidatePaths | Where-Object componentId -eq 'frontend-gsap')[0]
    if ($RouterAssignment.waveId -ne 'WAVE-05' -or $ThreeAssignment.waveId -ne 'WAVE-06' -or
        $ZustandPath.waveId -ne 'WAVE-07' -or $GsapPath.waveId -ne 'WAVE-08') {
        Add-Failure "Router, Three, Zustand, and GSAP are not isolated in the smallest declared reversible subwaves."
    }
    if (-not ($Failures | Where-Object { $_ -match 'Wave|Checkpoint|checkpoint|Edge assignment|graph edge|React peer|Router, Three' })) {
        Add-Pass "Wave/checkpoint model: 14 unaccepted checkpoints, all 27 edges assigned once, atomic React/R3F/Drei transition enforced, and Router/Three/Zustand/GSAP remain reversible."
    }

    $RequiredGateIds = 1..15 | ForEach-Object { 'HG-{0:d3}' -f $_ }
    $MissingGateIds = @($RequiredGateIds | Where-Object { $_ -notin $GateIds })
    $ExtraGateIds = @($GateIds | Where-Object { $_ -notin $RequiredGateIds })
    if ($MissingGateIds.Count -gt 0 -or $ExtraGateIds.Count -gt 0) {
        Add-Failure "Required human-gate set is incomplete or contains unplanned records."
    }
    foreach ($Gate in $Controls.humanGates) {
        if ([string]::IsNullOrWhiteSpace([string]$Gate.scope) -or
            [string]::IsNullOrWhiteSpace([string]$Gate.approver) -or
            -not (Test-NonEmptyArray $Gate.evidenceRequirements) -or
            -not (Test-NonEmptyArray $Gate.prohibitedBeforeApproval) -or
            -not (Test-NonEmptyArray $Gate.durableRefs) -or
            -not (Test-HasProperty -Object $Gate -Name 'founderApprovalEvidenceRefs')) {
            Add-Failure "Human gate '$($Gate.id)' is incomplete."
        }
        if ($Gate.state -notin @('unsatisfied', 'satisfied')) {
            Add-Failure "Human gate '$($Gate.id)' has an invalid state."
        }
        $FounderEvidence = @($Gate.founderApprovalEvidenceRefs)
        if ($Gate.state -eq 'satisfied') {
            if (-not (Test-NonEmptyArray $FounderEvidence)) {
                Add-Failure "Human gate '$($Gate.id)' is satisfied without durable founder evidence."
            }
            foreach ($FounderReference in $FounderEvidence) {
                $FounderEntry = $ReferenceEntriesById[[string]$FounderReference]
                if ($null -eq $FounderEntry -or $FounderEntry.target.path -notin @('DECISIONS.md', 'docs/decisions-log.md')) {
                    Add-Failure "Human gate '$($Gate.id)' has non-durable founder evidence."
                }
            }
        }
        elseif ($FounderEvidence.Count -gt 0) {
            Add-Failure "Unsatisfied human gate '$($Gate.id)' carries founder-approval evidence."
        }
    }

    $ExpectedHumanGateCoverage = @()
    $ExpectedHumanGateCoverage += @($Graph.components | Where-Object humanApprovalRequired -eq $true | ForEach-Object { "component|$($_.id)" })
    $ExpectedHumanGateCoverage += @($Graph.deferredFamilies | Where-Object humanApprovalRequired -eq $true | ForEach-Object { "deferredFamily|$($_.id)" })
    $ActualHumanGateCoverage = @($Controls.humanGateCoverage | ForEach-Object { "$($_.recordType)|$($_.recordId)" })
    $DuplicateHumanGateCoverage = @($ActualHumanGateCoverage | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
    $MissingHumanGateCoverage = @($ExpectedHumanGateCoverage | Where-Object { $_ -notin $ActualHumanGateCoverage })
    $OrphanHumanGateCoverage = @($ActualHumanGateCoverage | Where-Object { $_ -notin $ExpectedHumanGateCoverage })
    $HumanGateOrphanCount = $MissingHumanGateCoverage.Count + $OrphanHumanGateCoverage.Count + $DuplicateHumanGateCoverage.Count
    if ($HumanGateOrphanCount -gt 0) {
        Add-Failure "Human-gate coverage has missing, duplicate, or orphan component/family records."
    }
    foreach ($Coverage in $Controls.humanGateCoverage) {
        if (-not (Test-NonEmptyArray $Coverage.gateRefs) -or
            @($Coverage.gateRefs | Where-Object { $_ -notin $GateIds }).Count -gt 0) {
            Add-Failure "Human-gate coverage '$($Coverage.recordType)|$($Coverage.recordId)' has missing or unknown gateRefs."
        }
    }
    foreach ($Path in $Controls.candidatePaths) {
        if ($Path.humanApprovalRequired -ne $true -or -not (Test-NonEmptyArray $Path.gateRefs) -or
            @($Path.gateRefs | Where-Object { $_ -notin $GateIds }).Count -gt 0) {
            Add-Failure "Candidate path '$($Path.id)' lacks complete gateRefs."
        }
    }
    if (-not ($Failures | Where-Object { $_ -match 'human-gate|Human gate|Unsatisfied human gate|Candidate path.*gateRefs' })) {
        Add-Pass "Human gates: 15 explicit gates remain unsatisfied; all human-gated components, 44 candidate paths, and deferred families are covered with zero orphans."
    }

    $RequiredObligationIds = 1..7 | ForEach-Object { 'SCO-{0:d3}' -f $_ }
    $ObligationIds = @($Controls.supplyChainObligations.id)
    $MissingObligationIds = @($RequiredObligationIds | Where-Object { $_ -notin $ObligationIds })
    $ExtraObligationIds = @($ObligationIds | Where-Object { $_ -notin $RequiredObligationIds })
    if ($MissingObligationIds.Count -gt 0 -or $ExtraObligationIds.Count -gt 0) {
        Add-Failure "Required supply-chain obligation set is incomplete or contains unplanned records."
    }
    foreach ($Obligation in $Controls.supplyChainObligations) {
        if ([string]::IsNullOrWhiteSpace([string]$Obligation.type) -or
            [string]::IsNullOrWhiteSpace([string]$Obligation.scope) -or
            [string]::IsNullOrWhiteSpace([string]$Obligation.owner) -or
            $Obligation.status -notmatch '^blocking_' -or
            -not (Test-NonEmptyArray $Obligation.evidenceRefs) -or
            -not (Test-NonEmptyArray $Obligation.beforeGateRefs) -or
            -not (Test-NonEmptyArray $Obligation.beforeWaveRefs) -or
            [string]::IsNullOrWhiteSpace([string]$Obligation.failureHandling) -or
            $null -eq $Obligation.exceptionHandling) {
            Add-Failure "Supply-chain obligation '$($Obligation.id)' is incomplete or non-blocking."
            continue
        }
        foreach ($PropertyName in @('state', 'adrId', 'approver', 'reason', 'expiresAt', 'recheckDueAt', 'rollback')) {
            if (-not (Test-HasProperty -Object $Obligation.exceptionHandling -Name $PropertyName)) {
                Add-Failure "Supply-chain obligation '$($Obligation.id)' lacks exception field '$PropertyName'."
            }
        }
        if ($Obligation.exceptionHandling.state -ne 'unapproved' -or
            $null -ne $Obligation.exceptionHandling.adrId -or
            [string]::IsNullOrWhiteSpace([string]$Obligation.exceptionHandling.approver) -or
            [string]::IsNullOrWhiteSpace([string]$Obligation.exceptionHandling.rollback)) {
            Add-Failure "Supply-chain obligation '$($Obligation.id)' fabricates or incompletely models exception approval."
        }
    }
    $AdvisoryObligation = Get-ById -Collection $Controls.supplyChainObligations -Id 'SCO-001'
    if ($AdvisoryObligation.status -ne 'blocking_timed_out_or_missing' -or 'LOC-010' -notin @($AdvisoryObligation.evidenceRefs)) {
        Add-Failure "Timed-out or missing advisory evidence is not explicitly blocking."
    }

    $ExpectedCandidatePathKeys = [System.Collections.Generic.List[string]]::new()
    foreach ($Component in $Graph.components | Where-Object { $null -ne $_.targetCandidate }) {
        if (Test-HasProperty -Object $Component.targetCandidate -Name 'options') {
            foreach ($Option in $Component.targetCandidate.options) {
                $ExpectedCandidatePathKeys.Add("$($Component.id)|$($Option.id)")
            }
        }
        else {
            $ExpectedCandidatePathKeys.Add("$($Component.id)|default")
        }
    }
    $ActualCandidatePathKeys = @($Controls.candidatePaths | ForEach-Object { "$($_.componentId)|$($_.optionId)" })
    $DuplicateCandidatePathKeys = @($ActualCandidatePathKeys | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
    $MissingCandidatePathKeys = @($ExpectedCandidatePathKeys | Where-Object { $_ -notin $ActualCandidatePathKeys })
    $ExtraCandidatePathKeys = @($ActualCandidatePathKeys | Where-Object { $_ -notin $ExpectedCandidatePathKeys })
    if ($DuplicateCandidatePathKeys.Count -gt 0 -or $MissingCandidatePathKeys.Count -gt 0 -or $ExtraCandidatePathKeys.Count -gt 0) {
        Add-Failure "Candidate-path records do not map one-to-one to every graph candidate option."
    }
    foreach ($Path in $Controls.candidatePaths) {
        if ($Path.waveId -notin $WaveIds -or $Path.status -notmatch 'blocked' -or
            -not (Test-NonEmptyArray $Path.obligationRefs) -or
            @($RequiredObligationIds | Where-Object { $_ -notin @($Path.obligationRefs) }).Count -gt 0 -or
            @($Path.obligationRefs | Where-Object { $_ -notin $RequiredObligationIds }).Count -gt 0 -or
            $null -eq $Path.exception) {
            Add-Failure "Candidate path '$($Path.id)' lacks complete blocking wave/obligation coverage."
            continue
        }
        foreach ($PropertyName in @('state', 'adrId', 'approver', 'reason', 'expiresAt', 'recheckDueAt', 'rollback')) {
            if (-not (Test-HasProperty -Object $Path.exception -Name $PropertyName)) {
                Add-Failure "Candidate path '$($Path.id)' lacks exception field '$PropertyName'."
            }
        }
        if ([string]::IsNullOrWhiteSpace([string]$Path.exception.approver) -or
            [string]::IsNullOrWhiteSpace([string]$Path.exception.rollback)) {
            Add-Failure "Candidate path '$($Path.id)' has incomplete exception authority or rollback."
        }
        if ($Path.exception.state -eq 'approved') {
            $ExceptionGate = Get-ById -Collection $Controls.humanGates -Id 'HG-002'
            if ([string]::IsNullOrWhiteSpace([string]$Path.exception.adrId) -or
                [string]::IsNullOrWhiteSpace([string]$Path.exception.reason) -or
                ([string]::IsNullOrWhiteSpace([string]$Path.exception.expiresAt) -and
                    [string]::IsNullOrWhiteSpace([string]$Path.exception.recheckDueAt)) -or
                $ExceptionGate.state -ne 'satisfied') {
                Add-Failure "Candidate path '$($Path.id)' claims an exception without approved ADR, reason, expiry/recheck, and founder gate."
            }
        }
        elseif ($null -ne $Path.exception.adrId) {
            Add-Failure "Candidate path '$($Path.id)' carries an ADR id without approved exception state."
        }
    }

    $FamilyCoverageIds = @($Controls.deferredFamilySupplyChainCoverage.familyId)
    $DuplicateFamilyCoverage = @($FamilyCoverageIds | Group-Object | Where-Object Count -gt 1 | Select-Object -ExpandProperty Name)
    $MissingFamilyCoverage = @($DeferredFamilyIds | Where-Object { $_ -notin $FamilyCoverageIds })
    $ExtraFamilyCoverage = @($FamilyCoverageIds | Where-Object { $_ -notin $DeferredFamilyIds })
    if ($DuplicateFamilyCoverage.Count -gt 0 -or $MissingFamilyCoverage.Count -gt 0 -or $ExtraFamilyCoverage.Count -gt 0) {
        Add-Failure "Deferred-family supply-chain coverage is missing, duplicated, or orphaned."
    }
    foreach ($Coverage in $Controls.deferredFamilySupplyChainCoverage) {
        if ($Coverage.status -notmatch '^blocking_' -or
            -not (Test-NonEmptyArray $Coverage.obligationRefs) -or
            @($RequiredObligationIds | Where-Object { $_ -notin @($Coverage.obligationRefs) }).Count -gt 0 -or
            @($Coverage.obligationRefs | Where-Object { $_ -notin $RequiredObligationIds }).Count -gt 0) {
            Add-Failure "Deferred family '$($Coverage.familyId)' lacks complete blocking supply-chain obligations."
        }
    }
    if (-not ($Failures | Where-Object { $_ -match 'supply-chain obligation|Supply-chain obligation|advisory evidence|Candidate-path|Candidate path.*obligation|Deferred-family supply-chain|Deferred family.*supply-chain' })) {
        Add-Pass "Supply chain: 7 blocking obligations cover all 44 candidate paths and all 9 deferred families; timed-out or missing scans remain blocking and no exception ADR is approved."
    }

    foreach ($Capability in $Baseline.capabilities) {
        if ($Capability.operationalClaimed -ne $false) {
            Add-Failure "Capability '$($Capability.id)' makes an operational claim."
        }
        if ($Capability.detail -match '(?i)timed out' -and $Capability.capabilityTested -ne $false) {
            Add-Failure "Capability '$($Capability.id)' treats a timeout as capability-tested."
        }
    }
    $PlaywrightCapability = Get-ById -Collection $Baseline.capabilities -Id "cap-playwright"
    if ($PlaywrightCapability.installed -ne $true -or $PlaywrightCapability.configured -ne $true -or
        $PlaywrightCapability.versionProbeTested -ne $true -or $PlaywrightCapability.capabilityTested -ne $false -or
        $PlaywrightCapability.operationalClaimed -ne $false) {
        Add-Failure "Playwright truthfulness state must be installed/configured with a successful version probe, but browser-flow capability and operational state must remain false."
    }
    $Context7Capability = Get-ById -Collection $Baseline.capabilities -Id "cap-context7"
    if ($Context7Capability.configured -ne $true -or $Context7Capability.authenticated -ne $false -or
        $Context7Capability.protocolTested -ne $true -or $Context7Capability.capabilityTested -ne $true -or
        $Context7Capability.operationalClaimed -ne $false) {
        Add-Failure "Context7 state does not preserve configured/auth/protocol/capability/operational distinctions."
    }
    foreach ($Id in @("cap-docker", "cap-compose")) {
        $Capability = Get-ById -Collection $Baseline.capabilities -Id $Id
        if ($Capability.capabilityTested -ne $false -or $Capability.operationalClaimed -ne $false) {
            Add-Failure "Capability '$Id' must remain capability-unverified and non-operational after timeout."
        }
    }
    if (-not ($Failures | Where-Object { $_ -match 'Capability|Playwright|Context7' })) {
        Add-Pass "Integration truthfulness: version, protocol, scoped capability, timeout, authentication, and operational states remain distinct."
    }
}

$ArtifactFiles = @(Get-ChildItem -LiteralPath $CompatibilityRoot -File)
foreach ($File in $ArtifactFiles) {
    $Text = [System.IO.File]::ReadAllText($File.FullName)
    $Lines = [System.IO.File]::ReadAllLines($File.FullName)
    for ($Index = 0; $Index -lt $Lines.Count; $Index++) {
        if ($Lines[$Index] -match '[ \t]+$') {
            Add-Failure "Trailing whitespace: $($File.Name):$($Index + 1)."
        }
        if ($Lines[$Index].Contains("`t")) {
            Add-Failure "Tab character: $($File.Name):$($Index + 1)."
        }
    }
    if ($Text.Length -gt 0 -and -not ($Text.EndsWith("`n"))) {
        Add-Failure "Missing final newline: $($File.Name)."
    }
    if ($Text -match $PlaceholderPattern) {
        Add-Failure "Unresolved placeholder marker: $($File.Name)."
    }
}
if (-not ($Failures | Where-Object { $_ -match 'whitespace|Tab character|final newline|placeholder' })) {
    Add-Pass "Text hygiene: no placeholders, tabs, trailing whitespace, or missing final newlines."
}

$MarkdownFiles = @(Get-ChildItem -LiteralPath $CompatibilityRoot -Filter "*.md" -File)
foreach ($File in $MarkdownFiles) {
    $Text = [System.IO.File]::ReadAllText($File.FullName)
    $LinkMatches = [regex]::Matches($Text, '\[[^\]]+\]\((?<target>[^)]+)\)')
    foreach ($LinkMatch in $LinkMatches) {
        $Target = $LinkMatch.Groups['target'].Value.Trim()
        if ($Target.StartsWith('<') -and $Target.EndsWith('>')) {
            $Target = $Target.Substring(1, $Target.Length - 2)
        }
        if ($Target -match '^(?i:https?|mailto):' -or $Target.StartsWith('#')) {
            continue
        }
        $PathPart = ($Target -split '#', 2)[0]
        if ([string]::IsNullOrWhiteSpace($PathPart)) {
            continue
        }
        $ResolvedTarget = Join-Path $File.DirectoryName ([uri]::UnescapeDataString($PathPart))
        if (-not (Test-Path -LiteralPath $ResolvedTarget)) {
            Add-Failure "Broken local Markdown link in $($File.Name): $PathPart."
        }
    }
}
if (-not ($Failures | Where-Object { $_ -like 'Broken local Markdown link*' })) {
    Add-Pass "Markdown links: every local target resolves."
}

$SecretPatterns = @(
    @{ Kind = "private key header"; Regex = '-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----' },
    @{ Kind = "AWS access key id"; Regex = '\bAKIA[0-9A-Z]{16}\b' },
    @{ Kind = "GitHub token"; Regex = '\bgh[pousr]_[A-Za-z0-9]{20,}\b' },
    @{ Kind = "JWT-shaped value"; Regex = '\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b' },
    @{ Kind = "Context7 key"; Regex = '\bctx7sk-[A-Za-z0-9_-]{10,}\b' },
    @{ Kind = "credential-bearing connection URL"; Regex = '(?i)\b(?:postgres(?:ql)?|mysql|redis|mongodb(?:\+srv)?):\/\/[^:\s\/]+:[^@\s\/]+@' },
    @{ Kind = "generic secret assignment"; Regex = '(?i)(?:api[_-]?key|password|private[_-]?key|access[_-]?token)\s*[:=]\s*["''][^"''\r\n]{8,}["'']' }
)
foreach ($File in $ArtifactFiles) {
    $Lines = [System.IO.File]::ReadAllLines($File.FullName)
    for ($Index = 0; $Index -lt $Lines.Count; $Index++) {
        foreach ($Pattern in $SecretPatterns) {
            if ($Lines[$Index] -match $Pattern.Regex) {
                Add-Failure "Secret-shaped finding ($($Pattern.Kind)): $($File.Name):$($Index + 1). Matched value intentionally withheld."
            }
        }
    }
}
if (-not ($Failures | Where-Object { $_ -like 'Secret-shaped finding*' })) {
    Add-Pass "Secret-shaped scan: zero findings; matched values would be withheld."
}

if ($null -ne $Baseline) {
    foreach ($SourceFile in $Baseline.sourceFiles) {
        $FullPath = Join-Path $RepositoryRoot $SourceFile.path
        if (-not (Test-Path -LiteralPath $FullPath -PathType Leaf)) {
            Add-Failure "Baseline source is missing: $($SourceFile.path)."
            continue
        }
        $ActualHash = (Get-FileHash -LiteralPath $FullPath -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($ActualHash -ne $SourceFile.sha256) {
            Add-Failure "Baseline source hash drift: $($SourceFile.path)."
        }
    }
    if (-not ($Failures | Where-Object { $_ -match 'Baseline source .*missing|Baseline source hash drift' })) {
        Add-Pass "Source reconciliation: all recorded source hashes match the working tree."
    }

    $BaselineById = @{}
    foreach ($Item in $Baseline.items) {
        $BaselineById[$Item.id] = $Item
    }

    try {
        $NodeVersion = ((& node --version 2>&1 | Out-String).Trim() -replace '^v', '')
        $NpmVersion = ((& npm --version 2>&1 | Out-String).Trim())
        if ($NodeVersion -ne $BaselineById['runtime-node'].currentVersion) {
            Add-Failure "Node runtime drift: recorded $($BaselineById['runtime-node'].currentVersion), observed $NodeVersion."
        }
        if ($NpmVersion -ne $BaselineById['runtime-npm'].currentVersion) {
            Add-Failure "npm runtime drift: recorded $($BaselineById['runtime-npm'].currentVersion), observed $NpmVersion."
        }
    }
    catch {
        Add-Failure "Node/npm reconciliation failed: $($_.Exception.Message)"
    }

    $ApiPython = Join-Path $RepositoryRoot "apps/api/.venv/Scripts/python.exe"
    if (-not (Test-Path -LiteralPath $ApiPython -PathType Leaf)) {
        Add-Failure "API venv Python executable is missing."
    }
    else {
        try {
            $PythonVersion = ((& $ApiPython --version 2>&1 | Out-String).Trim() -replace '^Python\s+', '')
            if ($PythonVersion -ne $BaselineById['runtime-python'].currentVersion) {
                Add-Failure "Python runtime drift: recorded $($BaselineById['runtime-python'].currentVersion), observed $PythonVersion."
            }

            $DistributionNames = @(
                'fastapi', 'starlette', 'pydantic', 'uvicorn', 'sqlalchemy', 'alembic',
                'psycopg', 'bcrypt', 'pyjwt', 'httpx', 'email-validator', 'python-dotenv',
                'pytest', 'pytest-asyncio', 'pip'
            )
            $DistributionListJson = $DistributionNames | ConvertTo-Json -Compress
            $MetadataCode = "import importlib.metadata as m,json; names=json.loads(r'''$DistributionListJson'''); print(json.dumps({n:(m.version(n) if any(d.metadata['Name'].lower()==n.lower() for d in m.distributions()) else None) for n in names}))"
            $Installed = (& $ApiPython -c $MetadataCode | Out-String).Trim() | ConvertFrom-Json -AsHashtable
            $PythonMap = @{
                'backend-fastapi' = 'fastapi'; 'backend-starlette' = 'starlette'; 'backend-pydantic' = 'pydantic'
                'backend-uvicorn' = 'uvicorn'; 'backend-sqlalchemy' = 'sqlalchemy'; 'backend-alembic' = 'alembic'
                'backend-psycopg' = 'psycopg'; 'backend-bcrypt' = 'bcrypt'; 'backend-pyjwt' = 'pyjwt'
                'backend-httpx' = 'httpx'; 'backend-email-validator' = 'email-validator'
                'backend-python-dotenv' = 'python-dotenv'; 'qa-pytest' = 'pytest'; 'tool-pip' = 'pip'
            }
            foreach ($Entry in $PythonMap.GetEnumerator()) {
                if ($Installed[$Entry.Value] -ne $BaselineById[$Entry.Key].currentVersion) {
                    Add-Failure "Python distribution drift for $($Entry.Value): recorded $($BaselineById[$Entry.Key].currentVersion), observed $($Installed[$Entry.Value])."
                }
            }
            if ($null -ne $Installed['pytest-asyncio']) {
                Add-Failure "pytest-asyncio is now installed; baseline declared/installed divergence must be refreshed."
            }

            $PipCheckOutput = (& $ApiPython -m pip check 2>&1 | Out-String).Trim()
            if ($LASTEXITCODE -ne 0) {
                Add-Failure "pip check failed; output intentionally omitted from this validator summary."
            }
            elseif ($PipCheckOutput -ne 'No broken requirements found.') {
                Add-Failure "pip check returned an unexpected success payload."
            }
        }
        catch {
            Add-Failure "Python environment reconciliation failed: $($_.Exception.Message)"
        }
    }

    try {
        $WebLock = Get-Content -LiteralPath (Join-Path $RepositoryRoot 'apps/web/package-lock.json') -Raw | ConvertFrom-Json -AsHashtable -Depth 100
        $RootLock = Get-Content -LiteralPath (Join-Path $RepositoryRoot 'package-lock.json') -Raw | ConvertFrom-Json -AsHashtable -Depth 100
        $NpmMap = @{
            'frontend-react' = @{ Lock = 'web'; Package = 'react' }
            'frontend-react-dom' = @{ Lock = 'web'; Package = 'react-dom' }
            'frontend-react-router-dom' = @{ Lock = 'web'; Package = 'react-router-dom' }
            'frontend-zustand' = @{ Lock = 'web'; Package = 'zustand' }
            'frontend-gsap' = @{ Lock = 'web'; Package = 'gsap' }
            'frontend-types-react' = @{ Lock = 'web'; Package = '@types/react' }
            'frontend-types-react-dom' = @{ Lock = 'web'; Package = '@types/react-dom' }
            'three-r3f' = @{ Lock = 'web'; Package = '@react-three/fiber' }
            'three-drei' = @{ Lock = 'web'; Package = '@react-three/drei' }
            'three-core' = @{ Lock = 'web'; Package = 'three' }
            'tool-typescript-web' = @{ Lock = 'web'; Package = 'typescript' }
            'tool-vite' = @{ Lock = 'web'; Package = 'vite' }
            'tool-vite-react' = @{ Lock = 'web'; Package = '@vitejs/plugin-react' }
            'tool-tailwind' = @{ Lock = 'web'; Package = 'tailwindcss' }
            'tool-postcss' = @{ Lock = 'web'; Package = 'postcss' }
            'tool-autoprefixer' = @{ Lock = 'web'; Package = 'autoprefixer' }
            'tool-eslint' = @{ Lock = 'web'; Package = 'eslint' }
            'tool-typescript-eslint-parser' = @{ Lock = 'web'; Package = '@typescript-eslint/parser' }
            'tool-typescript-eslint-plugin' = @{ Lock = 'web'; Package = '@typescript-eslint/eslint-plugin' }
            'tool-eslint-react-hooks' = @{ Lock = 'web'; Package = 'eslint-plugin-react-hooks' }
            'tool-eslint-react-refresh' = @{ Lock = 'web'; Package = 'eslint-plugin-react-refresh' }
            'qa-playwright' = @{ Lock = 'web'; Package = '@playwright/test' }
            'qa-axe-playwright' = @{ Lock = 'web'; Package = '@axe-core/playwright' }
            'qa-lighthouse-ci' = @{ Lock = 'root'; Package = '@lhci/cli' }
        }
        foreach ($Entry in $NpmMap.GetEnumerator()) {
            $Lock = if ($Entry.Value.Lock -eq 'web') { $WebLock } else { $RootLock }
            $PackageKey = "node_modules/$($Entry.Value.Package)"
            $ObservedVersion = $Lock['packages'][$PackageKey]['version']
            if ($ObservedVersion -ne $BaselineById[$Entry.Key].currentVersion) {
                Add-Failure "npm lock drift for $($Entry.Value.Package): recorded $($BaselineById[$Entry.Key].currentVersion), observed $ObservedVersion."
            }
        }
    }
    catch {
        Add-Failure "npm lock reconciliation failed: $($_.Exception.Message)"
    }

    $ComposeText = [System.IO.File]::ReadAllText((Join-Path $RepositoryRoot 'docker-compose.yml'))
    if ($ComposeText -notmatch '(?m)^\s*image:\s*postgres:16\s*$') {
        Add-Failure "Compose PostgreSQL declaration no longer matches the recorded floating postgres:16 major tag."
    }
    if (-not ($Failures | Where-Object { $_ -match 'runtime drift|distribution drift|npm lock drift|environment reconciliation|lock reconciliation|pip check|pytest-asyncio is now|Compose PostgreSQL' })) {
        Add-Pass "Observed state: runtimes, installed Python distributions, pip check, npm locks, declared plugin absence, and Compose tag reconcile."
    }
}

foreach ($Pass in $Passes) {
    Write-Host "PASS: $Pass"
}

if ($Failures.Count -gt 0) {
    foreach ($Failure in $Failures) {
        Write-Error $Failure
    }
    Write-Host "VALIDATION FAILED: $($Failures.Count) finding(s)."
    exit 1
}

$CandidateComponents = @($Graph.components | Where-Object { $null -ne $_.targetCandidate }).Count
$DeferredComponents = @($Graph.components | Where-Object { $null -eq $_.targetCandidate }).Count
$CandidatePaths = 0
foreach ($Component in $Graph.components) {
    if ($null -eq $Component.targetCandidate) {
        continue
    }
    if (Test-HasProperty -Object $Component.targetCandidate -Name 'options') {
        $CandidatePaths += @($Component.targetCandidate.options).Count
    }
    else {
        $CandidatePaths += 1
    }
}
Write-Host (
    "VALIDATION PASSED: baselineItems={0}; capabilities={1}; components={2}; edges={3}; deferredFamilies={4}; referenceIndexEntries={5}; referenceUses={6}; unresolvedRefs=0; waves={7}; checkpoints={8}; edgeAssignments={9}; humanGates={10}; humanGateOrphans={11}; supplyChainObligations={12}; deferredFamilyCoverage={13}; candidateComponents={14}; deferredComponents={15}; candidatePaths={16}." -f
    @($Baseline.items).Count, @($Baseline.capabilities).Count, @($Graph.components).Count,
    @($Graph.edges).Count, @($Graph.deferredFamilies).Count, @($ReferenceIndex.entries).Count,
    $ReferenceUseCount, @($Controls.waves).Count, @($Controls.checkpoints).Count,
    @($Controls.edgeAssignments).Count, @($Controls.humanGates).Count, $HumanGateOrphanCount,
    @($Controls.supplyChainObligations).Count, @($Controls.deferredFamilySupplyChainCoverage).Count,
    $CandidateComponents, $DeferredComponents, @($Controls.candidatePaths).Count
)
exit 0
