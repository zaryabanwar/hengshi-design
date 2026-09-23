# Shared by the design and production validators. No repository writes.
function Get-UiStreamMapping {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][object[]]$Primitives,
        [Parameter(Mandatory)][object[]]$Templates
    )

    $streams = @('S-HIGH', 'S-LOW', 'S-MEDIUM', 'S-SEMANTIC')
    $worldStreams = @('S-HIGH', 'S-LOW', 'S-MEDIUM')
    $excluded = 'STREAM-SCOPE-EXCLUDED'
    # These are alternative hosts, not mandatory content dependencies.
    $hostContracts = @{
        'PRIM-001' = $streams
        'PRIM-042' = $worldStreams
        'PRIM-043' = $worldStreams
        'PRIM-044' = $worldStreams
        'PRIM-046' = @($excluded)
    }
    $primitiveMap = [System.Collections.Generic.Dictionary[string, object]]::new([StringComparer]::Ordinal)
    foreach ($p in $Primitives) {
        $id = [string]$p.primitive_id
        if ($id -cnotmatch '^PRIM-\d{3}$' -or $primitiveMap.ContainsKey($id)) {
            throw "Missing or duplicate primitive ID: $id"
        }
        $values = @(([string]$p.stream_presence).Split(';') | ForEach-Object { $_.Trim() })
        $sorted = @($values | Sort-Object -Unique -CaseSensitive)
        if (($values -join ';') -cne ($sorted -join ';') -or
            @($values | Where-Object { $_ -cnotin ($streams + $excluded) }).Count -gt 0 -or
            ($excluded -cin $values -and $values.Count -ne 1)) {
            throw "Invalid stream declaration: $id"
        }
        if ($hostContracts.ContainsKey($id) -and
            ($values -join ';') -cne ($hostContracts[$id] -join ';')) {
            throw "Host stream contract mismatch: $id"
        }
        $primitiveMap.Add($id, $values)
    }

    $templateMap = [System.Collections.Generic.Dictionary[string, object]]::new([StringComparer]::Ordinal)
    $scopeMap = [System.Collections.Generic.Dictionary[string, string]]::new([StringComparer]::Ordinal)
    $hostMap = [System.Collections.Generic.Dictionary[string, object]]::new([StringComparer]::Ordinal)
    foreach ($t in $Templates) {
        $id = [string]$t.template_id
        if ($id -cnotmatch '^TPL-[A-Z0-9]+(?:-[A-Z0-9]+)*$' -or $templateMap.ContainsKey($id)) {
            throw "Missing or duplicate template ID: $id"
        }
        $deps = @(([string]$t.primitive_dependencies).Split(';') | ForEach-Object { $_.Trim() })
        if (@($deps | Sort-Object -Unique -CaseSensitive).Count -ne $deps.Count) {
            throw "Duplicate dependency: $id"
        }
        foreach ($dep in $deps) {
            if (-not $primitiveMap.ContainsKey($dep)) { throw "Unresolved dependency: ${id}:$dep" }
        }
        $hosts = @($deps | Where-Object { $hostContracts.ContainsKey($_) })
        if ($hosts.Count -eq 0) { throw "Missing host: $id" }
        $hostMap.Add($id, $hosts)
        if ('PRIM-046' -cin $hosts) {
            if ($hosts.Count -ne 1) { throw "Mixed public and staff hosts: $id" }
            $scopeMap.Add($id, $excluded)
            $templateMap.Add($id, @())
            continue
        }

        $candidate = @($hosts | ForEach-Object { $primitiveMap[$_] } | Sort-Object -Unique -CaseSensitive)
        foreach ($dep in $deps) {
            if ($dep -cin $hosts) { continue }
            $supported = $primitiveMap[$dep]
            if ($excluded -cin $supported) { throw "Excluded component on public template: ${id}:$dep" }
            $candidate = @($candidate | Where-Object { $_ -cin $supported })
        }
        if ($candidate.Count -eq 0) { throw "No compatible stream: $id" }
        $scopeMap.Add($id, 'PUBLIC')
        $templateMap.Add($id, $candidate)
    }
    return [pscustomobject]@{
        PrimitivePresence = $primitiveMap
        TemplatePresence = $templateMap
        TemplateScope = $scopeMap
        TemplateHosts = $hostMap
    }
}

function Get-UiEvidenceScopes {
    param([Parameter(Mandatory)][object]$Mapping, [Parameter(Mandatory)][string]$TemplateId)
    if (-not $Mapping.TemplatePresence.ContainsKey($TemplateId)) { throw "Unknown template: $TemplateId" }
    if ($Mapping.TemplateScope[$TemplateId] -ceq 'STREAM-SCOPE-EXCLUDED') {
        return 'STREAM-SCOPE-EXCLUDED'
    }
    return $Mapping.TemplatePresence[$TemplateId]
}

function Get-UiFrameObligations {
    param(
        [Parameter(Mandatory)][object]$Mapping,
        [Parameter(Mandatory)][object[]]$Templates,
        [Parameter(Mandatory)][object[]]$Profiles
    )
    $profilesById = [System.Collections.Generic.Dictionary[string, object]]::new([StringComparer]::Ordinal)
    foreach ($p in $Profiles) {
        if ($profilesById.ContainsKey($p.profile_id)) { throw "Duplicate profile: $($p.profile_id)" }
        $profilesById.Add($p.profile_id, $p)
    }
    $streamCritical = @($Profiles | Where-Object dimension -CEQ 'stream' |
        ForEach-Object { $_.critical_distinct_frame_values.Split(';') } |
        Where-Object { $_ -clike 'STATE-*' } | Sort-Object -Unique -CaseSensitive)
    foreach ($stream in @('HIGH','LOW','MEDIUM','SEMANTIC')) {
        $id = 'DS-S-' + $stream
        if (-not $profilesById.ContainsKey($id) -or $profilesById[$id].dimension -cne 'stream') {
            throw "Missing stream profile: $id"
        }
    }
    foreach ($t in $Templates) {
        if (-not $profilesById.ContainsKey($t.state_profile)) { throw "Unknown state profile: $($t.template_id)" }
        $profile = $profilesById[$t.state_profile]
        if ($profile.dimension -cne 'state') { throw "Not a state profile: $($t.state_profile)" }
        $required = @($profile.required_values.Split(';'))
        $critical = @($profile.critical_distinct_frame_values.Split(';'))
        foreach ($state in $critical) {
            if ($state -cnotin $required) { throw "Critical state is not required: $($profile.profile_id):$state" }
        }
        $baseline = [regex]::Match($t.baseline_frame_name, '_STATE_(.+?)_VP_')
        if (-not $baseline.Success) { throw "Missing baseline state: $($t.template_id)" }
        $baselineState = 'STATE-' + $baseline.Groups[1].Value.Replace('_','-')
        if ($baselineState -cnotin $required) { throw "Unknown baseline state: $($t.template_id)" }
        $states = @($baselineState)
        if ($Mapping.TemplateScope[$t.template_id] -ceq 'PUBLIC') {
            foreach ($state in @('STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED')) {
                if ($state -cnotin $required -or $state -cnotin $streamCritical) {
                    throw "Missing required stream state: $($profile.profile_id):$state"
                }
            }
            foreach ($state in @($required | Where-Object { $_ -cin $streamCritical })) {
                if ($state -cnotin $critical) { throw "Missing critical stream state: $($profile.profile_id):$state" }
                $states += $state
            }
        }
        foreach ($state in @($states | Sort-Object -Unique -CaseSensitive)) {
            foreach ($scope in @(Get-UiEvidenceScopes -Mapping $Mapping -TemplateId $t.template_id)) {
                [pscustomobject]@{ template_id=$t.template_id; state_id=$state; stream_id=$scope }
            }
        }
    }
}
