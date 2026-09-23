# Shared by the design and production validators. No repository writes.
function Assert-UiStreamStyleGuideContract {
    param([Parameter(Mandatory)][string]$Text)
    $section = [regex]::Match($Text, '(?ms)^#### 8\.2\.4 [^\r\n]+\r?\n(?<body>.*?)(?=^#{1,4} |\z)')
    if (-not $section.Success) { throw 'Missing stream control style-guide section' }
    $body = ($section.Groups['body'].Value -replace '[*`]', '') -replace '\s+', ' '
    # Guard the approved behavioral contract, not visual or assistive-technology conformance.
    foreach ($clause in @(
        'four native radio inputs sharing one name inside a fieldset with a legend',
        'separate, always-present Apply submit button',
        'group accessible name identifies the delivery stream control and reports the in-force stream',
        'checked radio reports the pending selection',
        'Arrow, Tab, pointer and touch selection change only the checked state',
        'never applies on focus, selection, blur, arrow movement or timeout',
        'native Enter submission of the same form',
        'persistent visible text inside the fieldset',
        'before Apply in both DOM reading order and visual order',
        'programmatically associated with both the group and the Apply button',
        'not tooltip, title, hover-only, focus-only or accessible-description-only',
        'same wording in every stream'
    )) {
        if (-not $body.Contains($clause)) { throw "Stream style-guide contract missing: $clause" }
    }
    if ($body -match 'visible text adjacent to the control|Selecting a radio changes nothing') {
        throw 'Ambiguous stream style-guide wording'
    }
}

function Assert-UiStreamRequirementsContract {
    param([Parameter(Mandatory)][string]$Text)
    # Inspect each requirement's description cell, never adjacent rows or status cells.
    $contracts = @{
        'FR-3D-014' = @(
            'present and keyboard operable in every stream, including S-SEMANTIC',
            'four native radio inputs sharing one name inside a fieldset with a legend',
            'separate, always-present Apply submit button',
            'Arrow, Tab, pointer and touch selection change only the checked state',
            'without applying a stream, reloading, starting a transition or altering the accessibility tree beyond checked state',
            'applies only after explicit Apply activation by Enter, Space, pointer or touch, or native Enter submission of the same form',
            'never applies on focus, selection, blur, arrow movement or timeout',
            'above the capability ceiling remain present and disabled with a textual reason, not hidden'
        )
        'NFR-A11Y-004' = @(
            'group accessible name identifies the delivery stream control and reports the in-force stream',
            'checked radio reports the pending selection',
            'in-force value remains unchanged until explicit submission applies the selection',
            'Apply has a distinct accessible name stating that it applies the selection',
            'persistent visible text inside the fieldset before Apply in both DOM reading order and visual order',
            'programmatically associated with both the group and the Apply button',
            'not tooltip, title, hover-only, focus-only or accessible-description-only',
            'same wording in every stream',
            're-enters the experience in the chosen stream while preserving the current location'
        )
    }
    foreach ($id in $contracts.Keys) {
        $rows = [regex]::Matches($Text, ('(?m)^\|[ \t]*' + [regex]::Escape($id) + '[ \t]*\|(?<body>[^|\r\n]*)\|'))
        if ($rows.Count -ne 1) { throw "Missing or duplicate stream requirement: $id" }
        $body = ($rows[0].Groups['body'].Value -replace '[*`]', '') -replace '\s+', ' '
        foreach ($clause in $contracts[$id]) {
            if (-not $body.Contains($clause)) { throw "Stream requirement contract missing: ${id}:$clause" }
        }
        if ($body -match 'selection alone changes nothing|visible text adjacent to the control') {
            throw "Ambiguous stream requirement: $id"
        }
    }
}

function Assert-UiStreamControlContract {
    param([Parameter(Mandatory)][object[]]$Primitives)
    # These are definition-record checks, not evidence of a rendered accessible UI.
    $required = @{
        required_anatomy = @(
            'delivery stream control',
            'stream fieldset',
            'stream legend naming delivery stream control and in-force stream',
            'four native stream radio inputs sharing one name',
            'separate always-present Apply submit button',
            'persistent visible stream advisement inside fieldset before Apply in DOM reading and visual order'
        )
        transactional_or_content_states = @('stream-in-force', 'stream-pending')
        responsive_and_mode_obligations = @(
            'stream group accessible name reports in-force stream until explicit submit',
            'checked stream radio reports pending selection independently of in-force stream',
            'stream radio names use peer vocabulary without lesser-choice labels',
            'above-ceiling stream radios remain present with textual unavailability',
            'Apply accessible name states it applies the selection and differs from group and radio names',
            'stream selection by arrow Tab pointer or touch changes only checked state without applying reloading transitioning or other accessibility-tree changes',
            'stream applies only on explicit Apply activation by Enter Space pointer or touch or native Enter submission of the same form',
            'stream never applies on focus selection blur or timeout',
            'stream advisement is programmatically associated with both fieldset and Apply',
            'stream advisement explains re-entry into the chosen stream while preserving current location',
            'stream advisement uses identical visible wording in every stream and is not tooltip title hover-only focus-only or accessible-description-only'
        )
        implementation_evidence_expectations = @(
            'Stream control review states announcements on group entry pending-radio change and reaching Apply',
            'Stream advisement review covers sighted mouse keyboard without AT screen reader and 400% magnifier before operation'
        )
    }
    foreach ($id in @('PRIM-001', 'PRIM-042', 'PRIM-043', 'PRIM-044')) {
        $rows = @($Primitives | Where-Object primitive_id -CEQ $id)
        if ($rows.Count -ne 1) { throw "Missing or duplicate stream control host: $id" }
        foreach ($column in $required.Keys) {
            $property = $rows[0].PSObject.Properties[$column]
            $values = if ($null -eq $property) { @() } else { @(([string]$property.Value).Split(';') | ForEach-Object { $_.Trim() }) }
            foreach ($token in $required[$column]) {
                if ($token -cnotin $values) { throw "Stream control contract missing: ${id}:${column}:$token" }
            }
        }
        if ('stream-selected' -cin $rows[0].transactional_or_content_states.Split(';')) {
            throw "Ambiguous stream-selected state: $id"
        }
    }
}

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

    Assert-UiStreamControlContract -Primitives $Primitives
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
