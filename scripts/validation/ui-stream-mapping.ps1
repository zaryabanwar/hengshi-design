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
