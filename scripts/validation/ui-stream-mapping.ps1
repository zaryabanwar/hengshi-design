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

function Assert-UiStreamActionContract {
    param([Parameter(Mandatory)][string]$Text)
    $rows = [regex]::Matches($Text, '(?m)^\|[ \t]*ACT-09[ \t]+[^|\r\n]+\|(?<success>[^|\r\n]*)\|(?<pending>[^|\r\n]*)\|(?<recovery>[^|\r\n]*)\|[ \t]*\r?$')
    if ($rows.Count -ne 1) { throw 'Missing or duplicate stream action: ACT-09' }
    $contracts = @{
        success = @(
            'only after explicit Apply activation by Enter, Space, pointer or touch, or native Enter submission of the same form',
            'group accessible name reports the new in-force stream',
            'location preserved',
            'native radio anatomy and advance advisement follow FR-3D-014 and NFR-A11Y-004'
        )
        pending = @(
            'checked radio reports the pending selection',
            'group accessible name still reports the in-force stream',
            'Arrow, Tab, pointer and touch selection change only checked state',
            'no stream application, reload, transition or other accessibility-tree change',
            'never apply on focus, selection, blur, arrow movement or timeout',
            'requested stream above the WebGL ceiling; change failure; preference cannot persist'
        )
        recovery = @(
            'remain on the prior stream and say why',
            'the ceiling is stated, not silently substituted',
            'persistence failure follows ACT-11 and the choice still applies for the session',
            'no content loss in any stream'
        )
    }
    foreach ($cell in $contracts.Keys) {
        $body = ($rows[0].Groups[$cell].Value -replace '[*`]', '') -replace '\s+', ' '
        foreach ($clause in $contracts[$cell]) {
            if (-not $body.Contains($clause)) { throw "Stream action contract missing: ${cell}:$clause" }
        }
    }
}

function Assert-UiStreamAcceptanceContract {
    param([Parameter(Mandatory)][string]$Text)
    # This validates the acceptance definition, not a browser execution result.
    $rows = [regex]::Matches($Text, '(?m)^\|[ \t]*UXTEST-046[ \t]*\|[^|\r\n]*\|(?<criteria>[^|\r\n]*)\|[ \t]*\r?$')
    if ($rows.Count -ne 1) { throw 'Missing or duplicate stream acceptance test: UXTEST-046' }
    $body = ($rows[0].Groups['criteria'].Value -replace '[*`]', '') -replace '\s+', ' '
    foreach ($clause in @(
        'four native radio inputs sharing one name inside a fieldset with a legend',
        'separate, always-present Apply submit button',
        'group accessible name identifies the delivery stream control and reports the in-force stream',
        'checked radio reports the pending selection',
        'Apply has a distinct accessible name stating that it applies the selection',
        'Arrow, Tab, pointer and touch selection change only the checked state',
        'no stream application, reload, transition or other accessibility-tree change',
        'only explicit Apply activation by Enter, Space, pointer or touch, or native Enter submission of the same form',
        'Fail if focus, selection, blur, arrow movement or timeout applies a stream',
        'persistent visible text inside the fieldset before Apply in both DOM reading order and visual order',
        'programmatically associated with both the group and the Apply button',
        'not tooltip, title, hover-only, focus-only or accessible-description-only',
        'same wording in every stream',
        'applying the pending selection re-enters the experience in the chosen stream while preserving the current location',
        'sighted mouse users, keyboard users without assistive technology, screen-reader users and screen-magnifier users at 400% zoom',
        'Streams above the capability ceiling are present, disabled, and state the reason; none is hidden',
        'control is reachable and operable in all four streams',
        'does not move focus within a shell, and preserves scroll, open panel, and route',
        'never on the document body; the outgoing shell leaves the accessibility tree before the incoming shell is added',
        'a held slot, a verified email, and entered values are all still present, with nothing re-entered',
        'change is refused and explained under ACT-11 and the visitor keeps their work',
        'any automatic canvas entry'
    )) {
        if (-not $body.Contains($clause)) { throw "Stream acceptance contract missing: $clause" }
    }
    if ($body -match 'visible text adjacent to the control|arrowing through options changes nothing') {
        throw 'Ambiguous stream acceptance criteria'
    }
}

function Assert-UiStreamCoverageContract {
    param([Parameter(Mandatory)][object[]]$Flows)
    $rows = @($Flows | Where-Object coverage_id -CEQ 'COV-ACT-09')
    if ($rows.Count -ne 1) { throw 'Missing or duplicate stream coverage: COV-ACT-09' }
    $contracts = @{
        success_or_expected_state = @(
            'applied only after explicit Apply activation or native Enter submission of the same form',
            'group accessible name reports the new in-force stream',
            'persistence is reported only after a successful preference write',
            'announced politely without interrupting',
            'focus stays on the operated control within a shell',
            'across the semantic boundary focus moves to the destination shell delivery stream control reporting the new stream',
            'scroll, open panel and route preserved',
            'control anatomy and advance advisement follow FR-3D-014 and NFR-A11Y-004'
        )
        error_empty_pending_state = @(
            'checked radio reports the pending selection',
            'group accessible name still reports the in-force stream',
            'selection changes only checked state without applying a stream, reloading or initiating a transition',
            'no accessibility-tree change beyond checked state',
            'never apply on focus, selection, blur, arrow movement or timeout',
            'Chosen stream above the WebGL ceiling; change failure; preference write failure'
        )
        recovery = @(
            'Selection is bounded by the WebGL ceiling and is never silently substituted',
            'on change failure retain the prior stream and explain why',
            'on write failure the choice applies for the current session',
            'persistence failure is explained without blocking, following the ACT-11 pattern',
            'no destination and no content is lost in any stream'
        )
    }
    foreach ($column in $contracts.Keys) {
        $property = $rows[0].PSObject.Properties[$column]
        $body = if ($null -eq $property) { '' } else { [string]$property.Value }
        foreach ($clause in $contracts[$column]) {
            if (-not $body.Contains($clause)) { throw "Stream coverage contract missing: ${column}:$clause" }
        }
    }
}

function Assert-UiStreamAcceptanceTraceContract {
    param([Parameter(Mandatory)][object[]]$Trace)
    $rows = @($Trace | Where-Object trace_id -CEQ 'TR-TEST-046')
    if ($rows.Count -ne 1) { throw 'Missing or duplicate stream acceptance trace: TR-TEST-046' }
    $row = $rows[0]
    if ($row.source_id -cne 'UXTEST-046' -or $row.source_type -cne 'ux_test' -or
        $row.source_artifact -cne 'docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md') {
        throw 'Wrong stream acceptance trace source'
    }
    foreach ($clause in @(
        'four native radio inputs sharing one name inside a fieldset with a legend',
        'separate always-present Apply submit button',
        'group accessible name reports the in-force stream while the checked radio reports the pending selection',
        'Apply has a distinct accessible name stating it applies the selection',
        'selection changes only checked state without applying reloading transitioning or other accessibility-tree changes',
        'only explicit Apply activation or native Enter submission of the same form',
        'never apply on focus selection blur arrow movement or timeout',
        'persistent visible text inside the fieldset before Apply in both DOM reading order and visual order',
        'programmatically associated with both the group and the Apply button',
        'not tooltip title hover-only focus-only or accessible-description-only',
        'same wording in every stream',
        'applying the pending selection re-enters the experience while preserving current location',
        'sighted mouse users keyboard users without assistive technology screen-reader users and screen-magnifier users at 400% zoom',
        'ceiling-excluded streams are disabled with a stated reason rather than hidden',
        'reachable in all four streams and on ROUTE-HOME first frame in every stream including S-HIGH with the canvas not entered',
        'without moving focus within a shell and preserves scroll open panel and route',
        'destination shell stream control and never the document body with the outgoing shell removed from the accessibility tree first',
        'a held slot a verified email and entered values survives every crossing including the semantic one or the change is refused and explained under ACT-11',
        'UXTEST-046 execution evidence remains required'
    )) {
        if (-not ([string]$row.required_future_evidence).Contains($clause)) { throw "Stream acceptance trace evidence missing: $clause" }
    }
    if ($row.status_or_gate -cne 'contracted_future') { throw 'Stream acceptance trace evidence must remain future' }
}

function Assert-UiStreamTraceContract {
    param([Parameter(Mandatory)][object[]]$Trace)
    $sources = @{ 'TR-REQ-103' = 'NFR-A11Y-004'; 'TR-REQ-111' = 'FR-3D-014' }
    $clauses = @{
        'TR-REQ-103' = @(
            'present discoverable and keyboard operable in every stream',
            'group accessible name identifies the delivery stream control and reports the in-force stream',
            'checked radio reports the pending selection',
            'Apply has a distinct accessible name stating it applies the selection',
            'persistent visible text inside the fieldset before Apply in both DOM reading order and visual order',
            'programmatically associated with both the group and the Apply button',
            'not tooltip title hover-only focus-only or accessible-description-only',
            'same wording in every stream',
            'applying the pending selection re-enters the experience while preserving the current location',
            'UXTEST-046 execution evidence remains required'
        )
        'TR-REQ-111' = @(
            'four native radio inputs sharing one name inside a fieldset with a legend',
            'separate always-present Apply submit button',
            'selection changes only checked state without applying a stream reloading transitioning or other accessibility-tree changes',
            'only explicit Apply activation or native Enter submission of the same form',
            'never apply on focus selection blur arrow movement or timeout',
            'streams above the capability ceiling remain present and disabled with a textual reason rather than hidden',
            'preference write failure is explained without blocking under ACT-11 and the choice still applies for the session',
            'UXTEST-046 execution evidence remains required'
        )
    }
    foreach ($id in $sources.Keys) {
        $rows = @($Trace | Where-Object trace_id -CEQ $id)
        if ($rows.Count -ne 1) { throw "Missing or duplicate stream trace: $id" }
        $row = $rows[0]
        if ($row.source_id -cne $sources[$id] -or $row.source_type -cne 'requirement' -or
            $row.source_artifact -cne 'docs/active/Hengshi_Design_SRS_v3.md') { throw "Wrong stream trace source: $id" }
        $records = @(([string]$row.contract_records).Split(';'))
        foreach ($record in @('PRIM-001','PRIM-042','PRIM-043','PRIM-044','COV-ACT-09','B01')) {
            if ($record -cnotin $records) { throw "Missing stream trace binding: ${id}:$record" }
        }
        foreach ($clause in $clauses[$id]) {
            if (-not ([string]$row.required_future_evidence).Contains($clause)) { throw "Stream trace evidence missing: ${id}:$clause" }
        }
        if ($row.status_or_gate -cne 'contracted_future_visual_evidence_required') {
            throw "Stream trace evidence must remain future: $id"
        }
    }
    Assert-UiStreamAcceptanceTraceContract -Trace $Trace
}

function Assert-UiStreamBatchContract {
    param([Parameter(Mandatory)][object[]]$Batches)
    $rows = @($Batches | Where-Object batch_id -CEQ 'B01')
    if ($rows.Count -ne 1) { throw 'Missing or duplicate stream batch: B01' }
    $batch = $rows[0]
    foreach ($clause in @(
        'semantic shell (PRIM-001, ACT-09)',
        'one frame per stream',
        'four native radio inputs sharing one name inside a fieldset with a legend',
        'separate always-present Apply submit button',
        'group accessible name reports the in-force stream while the checked radio reports the pending selection',
        'Apply accessible name states that it applies the selection',
        'persistent visible text inside the fieldset before Apply in both DOM reading order and visual order',
        'programmatically associated with both the group and the Apply button',
        'not tooltip title hover-only focus-only or accessible-description-only',
        'same wording in every stream',
        'applying the pending selection re-enters the experience while preserving current location',
        'keyboard and screen-reader execution evidence must verify names associations and activation',
        'selection changes only checked state without applying reloading transitioning or other accessibility-tree changes',
        'only explicit Apply activation or native Enter submission of the same form',
        'never apply on focus selection blur arrow movement or timeout',
        'screenshots alone cannot establish keyboard operability or accessible names',
        'STATE-STREAM-CHANGED on TPL-GLOBAL-NAVIGATION in each of the four streams',
        'STATE-PREFERENCE-WRITE-FAILED on TPL-GLOBAL-NAVIGATION in each of the four streams',
        'Explicitly NOT required in B01: Reception, rooms, hotspots, the HUD'
    )) {
        if (-not ([string]$batch.required_visual_evidence).Contains($clause)) { throw "Stream batch evidence missing: $clause" }
    }
    if ('UXTEST-046' -cnotin ([string]$batch.supporting_or_final_evidence_ids).Split(';')) {
        throw 'Missing stream batch test binding: UXTEST-046'
    }
    if ($batch.status -cne 'future_not_authorized') { throw 'B01 authorization must remain held' }
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
