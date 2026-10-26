# D-060 allocation-only registry. No provider calls or repository writes.
function Get-UiBoundaryAllocations {
    param([object[]]$Rows, [object]$Context)
    $expected = @(
        'B07|TPL-GLOBAL-NAVIGATION|STATE-BOUNDARY-TO-SEMANTIC|S-SEMANTIC|S-HIGH;S-MEDIUM;S-LOW',
        'B07|TPL-GLOBAL-NAVIGATION|STATE-ANCESTOR-TO-SEMANTIC|S-SEMANTIC|S-HIGH;S-MEDIUM;S-LOW',
        'B07|TPL-WORLD-HUD|STATE-BOUNDARY-TO-WORLD|S-HIGH;S-MEDIUM;S-LOW|S-SEMANTIC',
        'B07|TPL-WORLD-HUD|STATE-ANCESTOR-TO-WORLD|S-HIGH;S-MEDIUM;S-LOW|S-SEMANTIC'
    )
    $actual = @($Rows | ForEach-Object { '{0}|{1}|{2}|{3}|{4}' -f $_.batch_id,$_.template_id,$_.state_id,$_.destination_streams,$_.origin_streams })
    if ($actual.Count -ne 4 -or @($actual | Sort-Object -Unique -CaseSensitive).Count -ne 4 -or @($actual | Where-Object { $_ -cnotin $expected }).Count) { throw 'Boundary allocation does not match D-060' }
    foreach ($row in $Rows) {
        $batch = @($Context.Batches | Where-Object batch_id -CEQ $row.batch_id)
        if ($batch.Count -ne 1 -or $row.template_id -cnotin ($batch[0].primary_template_ids + ';' + $batch[0].supporting_template_ids).Split(';')) { throw 'Boundary allocation template has no owning batch' }
        foreach ($scope in $row.destination_streams.Split(';')) {
            if ($scope -cnotin @(Get-UiEvidenceScopes $Context.Mapping $row.template_id)) { throw 'Boundary destination is absent from template' }
        }
        foreach ($profile in $Context.Profiles) {
            if ($row.state_id -cin $profile.required_values.Split(';') -or $row.state_id -cin $profile.critical_distinct_frame_values.Split(';')) { throw 'Allocation-only state leaked into ordinary profile' }
        }
        foreach ($destination in $row.destination_streams.Split(';')) {
            [pscustomobject]@{ batch_id=$row.batch_id; template_id=$row.template_id; state_id=$row.state_id; stream_id=$destination; origin_streams=$row.origin_streams }
        }
    }
}

function Get-UiBoundaryCoverageGaps {
    param([string]$BatchId, [object[]]$ManifestRows, [object]$Context, [hashtable]$Annotations)
    $allocations = @(Get-UiBoundaryAllocations $Context.BoundaryAllocations $Context | Where-Object batch_id -CEQ $BatchId)
    foreach ($allocation in $allocations) {
        $own = @($ManifestRows | Where-Object { $_.template_id -ceq $allocation.template_id -and $_.state_id -ceq $allocation.state_id -and $_.stream_id -ceq $allocation.stream_id -and $_.batch_id -ceq $BatchId })
        if (@($own | Where-Object evidence_type -CEQ 'FRAME').Count -eq 0) { "missing-boundary-frame:$($allocation.state_id):$($allocation.stream_id)" }
        $annotationRows = @($own | Where-Object evidence_type -CEQ 'ANNOTATION')
        foreach ($row in $annotationRows) {
            if ($null -ne $Annotations -and $Annotations.ContainsKey($row.evidence_id)) {
                foreach ($case in $Annotations[$row.evidence_id].cases) {
                    if ($case.origin_stream -cnotin $allocation.origin_streams.Split(';') -or $case.destination_stream -cne $allocation.stream_id) { 'undeclared-boundary-direction' }
                }
            }
        }
        foreach ($origin in $allocation.origin_streams.Split(';')) {
            $cases = @()
            foreach ($row in $annotationRows) {
                if ($null -ne $Annotations -and $Annotations.ContainsKey($row.evidence_id)) {
                    $cases += @($Annotations[$row.evidence_id].cases | Where-Object { $_.origin_stream -ceq $origin -and $_.destination_stream -ceq $allocation.stream_id })
                }
            }
            if ($cases.Count -ne 1) { "missing-or-duplicate-directed-case:$($allocation.state_id):${origin}:$($allocation.stream_id)"; continue }
            $case = $cases[0]
            $last = if ($allocation.stream_id -ceq 'S-SEMANTIC') { 'no_canvas' } else { 'add_canvas_after_announcement' }
            $steps = 'remove_outgoing_shell;add_incoming_empty_status_restore_process;focus_visible_stream_control;announce_stream_location;' + $last
            if (($case.ordered_steps -join ';') -cne $steps) { 'invalid-boundary-step-order' }
            if ($case.visible_destination_focus -isnot [bool] -or -not $case.visible_destination_focus) { 'missing-destination-visible-focus' }
            foreach ($field in @('arrival_location','announcement')) {
                if ([string]::IsNullOrWhiteSpace([string]$case.$field)) { "missing-boundary-$field" }
            }
            if ($allocation.state_id -clike 'STATE-ANCESTOR-*') {
                foreach ($field in @('requested_location','mapping_failure_reason','chosen_ancestor','substitution_wording')) {
                    if ([string]::IsNullOrWhiteSpace([string]$case.$field)) { "missing-ancestor-$field" }
                }
                if ($case.chosen_ancestor -cne $case.arrival_location) { 'ancestor-arrival-disagreement' }
            }
        }
    }
}
