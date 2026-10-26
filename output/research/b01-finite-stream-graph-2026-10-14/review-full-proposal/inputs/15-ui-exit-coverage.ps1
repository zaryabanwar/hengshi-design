# Pure necessary coverage checks under EC-01..06/10..16 and N-04.
# PASS here is not qualitative profile evidence, review acceptance or conformance.
function Get-UiExitCoverageGaps {
    param([string]$BatchId, [object[]]$ManifestRows, [object]$Context)
    $batch = @($Context.Batches | Where-Object batch_id -CEQ $BatchId)
    if ($batch.Count -ne 1) { throw 'Unknown batch coverage owner' }
    $primary = @($batch[0].primary_template_ids.Split(';') | Where-Object { $_ })
    if ($primary.Count -eq 0) { throw 'Batch has no primary exit templates' }
    $rows = @()
    $seenIds = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    $allowedTypes = @('FRAME','FOCUSED_FRAME','VARIANT','ANNOTATION','PROTOTYPE','ROUTE_INSTANCE_SHEET')
    $visualTypes = @('FRAME','FOCUSED_FRAME','VARIANT')
    foreach ($row in $ManifestRows) {
        if (-not $seenIds.Add([string]$row.evidence_id)) { 'duplicate-evidence-id'; continue }
        if (@(@('evidence_type','profile_ids','prim_ids','time_limit_branch') | Where-Object { $_ -cnotin @($row.PSObject.Properties.Name) }).Count -gt 0) { 'missing-manifest-metadata'; continue }
        try { $resolved = Get-UiResolvedManifestRow -Row $row -Context $Context }
        catch { $resolved = $null }
        if ($null -eq $resolved -or $row.batch_id -cne $BatchId) { 'invalid-manifest-identity'; continue }
        if ($row.evidence_type -cnotin $allowedTypes) { 'invalid-evidence-type'; continue }
        $profiles = @(([string]$row.profile_ids).Split(';') | Where-Object { $_ })
        $primitives = @(([string]$row.prim_ids).Split(';') | Where-Object { $_ })
        if ($profiles.Count -eq 0 -or @($profiles | Where-Object { $_ -cnotin $Context.Profiles.profile_id }).Count -gt 0) { 'unresolved-profile-binding'; continue }
        if ($primitives.Count -eq 0 -or @($primitives | Where-Object { -not $Context.Mapping.PrimitivePresence.ContainsKey($_) }).Count -gt 0) { 'unresolved-primitive-binding'; continue }
        $template = @($Context.Templates | Where-Object template_id -CEQ $resolved.TemplateId)[0]
        $owner = $template
        if ($resolved.InstanceId -cne 'REF') {
            $owners = @($Context.Routes | Where-Object { $_.route_instance_id.Replace('-','_') -ceq $resolved.InstanceId -and $_.template_id -ceq $resolved.TemplateId })
            $owners += @($Context.Flows | Where-Object { $_.source_id.Replace('-','_') -ceq $resolved.InstanceId -and $resolved.TemplateId -cin $_.template_ids.Split(';') })
            $owner = $owners[0]
        }
        $branch = if ($owner.PSObject.Properties['time_limit_branch']) { $owner.time_limit_branch } else { $template.time_limit_branch }
        if ($row.time_limit_branch -ceq 'TL-EXCEPTION' -or $row.time_limit_branch -cne $branch) { 'time-limit-branch-disagreement'; continue }
        $allowedProfiles = @($owner.state_profile,$owner.viewport_profile,$owner.mode_profile,$template.browser_profile,$branch)
        if ($resolved.StreamId -cne 'STREAM-SCOPE-EXCLUDED') { $allowedProfiles += 'DS-' + $resolved.StreamId }
        if (@($profiles | Where-Object { $_ -cnotin $allowedProfiles }).Count -gt 0) { 'profile-owner-disagreement'; continue }
        if (@($primitives | Where-Object { $_ -cnotin $template.primitive_dependencies.Split(';') }).Count -gt 0) { 'primitive-owner-disagreement'; continue }
        $rows += [pscustomobject]@{ Row=$row; Identity=$resolved; Profiles=$profiles; Primitives=$primitives }
    }
    $frames = @(Get-UiFrameObligations -Mapping $Context.Mapping -Templates $Context.Templates -Profiles $Context.Profiles)
    foreach ($id in $primary) {
        $templates = @($Context.Templates | Where-Object template_id -CEQ $id)
        if ($templates.Count -ne 1) { "unresolved-primary-template:$id"; continue }
        $template = $templates[0]
        $own = @($rows | Where-Object { $_.Identity.TemplateId -ceq $id })
        foreach ($type in @('FRAME','ANNOTATION')) {
            if (@($own | Where-Object { $_.Row.evidence_type -ceq $type }).Count -eq 0) { "missing-type:${id}:$type" }
        }
        if ($BatchId -cin @('B01','B05','B06','B08') -and -not [string]::IsNullOrWhiteSpace($template.interaction_focus_notes) -and @($own | Where-Object { $_.Row.evidence_type -ceq 'PROTOTYPE' }).Count -eq 0) { "missing-type:${id}:PROTOTYPE" }
        foreach ($primitive in $template.primitive_dependencies.Split(';')) {
            if (@($own | Where-Object { $primitive -cin $_.Primitives }).Count -eq 0) { "missing-primitive:${id}:$primitive" }
        }
        $profileIds = @($template.state_profile,$template.viewport_profile,$template.mode_profile,$template.browser_profile,$template.time_limit_branch)
        foreach ($scope in @(Get-UiEvidenceScopes -Mapping $Context.Mapping -TemplateId $id)) {
            if ($scope -cne 'STREAM-SCOPE-EXCLUDED') { $profileIds += 'DS-' + $scope }
        }
        foreach ($profileId in @($profileIds | Sort-Object -Unique -CaseSensitive)) {
            $profile = @($Context.Profiles | Where-Object profile_id -CEQ $profileId)
            if ($profile.Count -ne 1) { "unresolved-assigned-profile:${id}:$profileId"; continue }
            if (@($own | Where-Object { $profileId -cin $_.Profiles }).Count -eq 0) { "missing-profile:${id}:$profileId" }
            if ($profile[0].dimension -cnotin @('state','viewport','mode')) { continue }
            $field = @{state='StateId';viewport='ViewportId';mode='ModeId'}[$profile[0].dimension]
            foreach ($value in $profile[0].required_values.Split(';')) {
                $covered = @($own | Where-Object { $_.Identity.$field -ceq $value -and $profileId -cin $_.Profiles })
                if ($covered.Count -eq 0) { "missing-axis:${id}:${profileId}:$value" }
                if ($value -cin $profile[0].critical_distinct_frame_values.Split(';') -and @($covered | Where-Object { $_.Row.evidence_type -cin $visualTypes }).Count -eq 0) { "missing-critical-frame:${id}:${profileId}:$value" }
            }
        }
        # These complete-FRAME viewport minima are explicit in each VP row.
        $completeFrameValues = @{
            'VP-PUBLIC'=@('VP-320','VP-DESKTOP')
            'VP-INTERACTIVE'=@('VP-320','VP-LANDSCAPE','VP-DESKTOP')
            'VP-WORLD'=@('VP-320','VP-LANDSCAPE','VP-DESKTOP','VP-ZOOM-400')
            'VP-STAFF'=@('VP-320','VP-TABLET','VP-DESKTOP','VP-ZOOM-400')
        }
        foreach ($value in $completeFrameValues[$template.viewport_profile]) {
            if (@($own | Where-Object { $_.Identity.ViewportId -ceq $value -and $_.Row.evidence_type -ceq 'FRAME' }).Count -eq 0) { "missing-complete-viewport-frame:${id}:$value" }
        }
        $baselineMatch = [regex]::Match($template.baseline_frame_name,'_STATE_(?<state>.+?)_VP_(?<viewport>.+?)_MODE_(?<mode>.+?)_(?:STREAM_|SCOPE_)')
        if (-not $baselineMatch.Success) { "invalid-baseline:$id"; continue }
        $baselineState = 'STATE-' + $baselineMatch.Groups['state'].Value.Replace('_','-')
        $baselineViewport = 'VP-' + $baselineMatch.Groups['viewport'].Value.Replace('_','-')
        $baselineMode = 'MODE-' + $baselineMatch.Groups['mode'].Value.Replace('_','-')
        foreach ($frame in @($frames | Where-Object template_id -CEQ $id)) {
            $covered = @($own | Where-Object { $_.Identity.StateId -ceq $frame.state_id -and $_.Identity.StreamId -ceq $frame.stream_id -and $_.Row.evidence_type -cin $visualTypes })
            if ($frame.state_id -ceq $baselineState) {
                $covered = @($covered | Where-Object { $_.Identity.InstanceId -ceq 'REF' -and $_.Identity.ViewportId -ceq $baselineViewport -and $_.Identity.ModeId -ceq $baselineMode -and $_.Row.evidence_type -ceq 'FRAME' })
            }
            if ($covered.Count -eq 0) { "missing-stream-frame:${id}:$($frame.state_id):$($frame.stream_id)" }
        }
    }
    foreach ($route in $Context.Routes) {
        if ($route.template_id -cnotin $primary -or $route.baseline_frame_name -cnotlike ('HSD_UIR_' + $BatchId + '_*')) { continue }
        if (@($rows | Where-Object { $_.Identity.TemplateId -ceq $route.template_id -and $_.Identity.InstanceId -ceq $route.route_instance_id.Replace('-','_') -and $_.Row.evidence_type -ceq 'ROUTE_INSTANCE_SHEET' }).Count -eq 0) { "missing-route-instance:$($route.route_instance_id)" }
        # D-051/EC-31 explicitly require the privacy notice itself in every stream.
        if ($route.route_id -ceq 'ROUTE-PRIVACY') {
            foreach ($scope in @(Get-UiEvidenceScopes -Mapping $Context.Mapping -TemplateId $route.template_id)) {
                if (@($rows | Where-Object { $_.Identity.TemplateId -ceq $route.template_id -and $_.Identity.InstanceId -ceq $route.route_instance_id.Replace('-','_') -and $_.Identity.StreamId -ceq $scope -and $_.Row.evidence_type -cin @('FRAME','FOCUSED_FRAME') }).Count -eq 0) { "missing-privacy-instance-frame:$scope" }
            }
        }
    }
}
