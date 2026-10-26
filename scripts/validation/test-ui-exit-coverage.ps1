param([switch]$FunctionsOnly)
. (Join-Path $PSScriptRoot 'ui-stream-mapping.ps1')
. (Join-Path $PSScriptRoot 'ui-exit-coverage.ps1')

# Test fixtures only: these rows/artifacts are never real reference evidence.
function New-UiExitCoverageFixture {
    param([string]$BatchId, [object]$Context)
    $batch = @($Context.Batches | Where-Object batch_id -CEQ $BatchId)[0]
    $rows = [System.Collections.Generic.List[object]]::new()
    $frames = @(Get-UiFrameObligations -Mapping $Context.Mapping -Templates $Context.Templates -Profiles $Context.Profiles)
    foreach ($id in $batch.primary_template_ids.Split(';')) {
        $t = @($Context.Templates | Where-Object template_id -CEQ $id)[0]
        $base = [regex]::Match($t.baseline_frame_name,'_STATE_(?<state>.+?)_VP_(?<viewport>.+?)_MODE_(?<mode>.+?)_(?:STREAM_|SCOPE_)')
        $state = 'STATE-' + $base.Groups['state'].Value.Replace('_','-')
        $viewport = 'VP-' + $base.Groups['viewport'].Value.Replace('_','-')
        $mode = 'MODE-' + $base.Groups['mode'].Value.Replace('_','-')
        $scopes = @(Get-UiEvidenceScopes -Mapping $Context.Mapping -TemplateId $id)
        $profileIds = @($t.state_profile,$t.viewport_profile,$t.mode_profile,$t.browser_profile,$t.time_limit_branch)
        foreach ($scope in $scopes) { if ($scope -cne 'STREAM-SCOPE-EXCLUDED') { $profileIds += 'DS-' + $scope } }
        $profileIds = @($profileIds | Sort-Object -Unique -CaseSensitive)
        $add = {
            param($type,$instance,$s,$v,$m,$scope,$owner)
            $segment = if ($scope -ceq 'STREAM-SCOPE-EXCLUDED') {'SCOPE_EXCLUDED'} else {'STREAM_' + $scope.Substring(2)}
            $identity = "HSD_UIR_${BatchId}_$($id.Replace('-','_'))_${instance}_$($s.Replace('-','_'))_$($v.Replace('-','_'))_$($m.Replace('-','_'))_${segment}_V01"
            $revision = @($rows | Where-Object { $_.evidence_id.StartsWith($identity.Substring(0,$identity.Length-2),[StringComparison]::Ordinal) }).Count + 1
            $identity=$identity.Substring(0,$identity.Length-2)+('{0:D2}' -f $revision)
            $rowProfiles=@($profileIds|Where-Object{$_ -cnotlike 'DS-S-*' -or $_ -ceq ('DS-'+$scope)})
            $rows.Add([pscustomobject]@{ evidence_id=$identity;batch_id=$BatchId;evidence_type=$type;template_id=$id;instance_id=$instance.Replace('_','-');state_id=$s;viewport_id=$v;mode_id=$m;stream_id=$scope;profile_ids=($rowProfiles -join ';');prim_ids=$t.primitive_dependencies;time_limit_branch=$owner.time_limit_branch;revision=('V{0:D2}' -f $revision) })
        }
        foreach ($scope in $scopes) { & $add FRAME REF $state $viewport $mode $scope $t }
        foreach($v in @('VP-320','VP-NARROW','VP-LANDSCAPE','VP-TABLET','VP-DESKTOP','VP-WIDE','VP-ZOOM-400')){ & $add FRAME REF $state $v $mode $scopes[0] $t }
        foreach ($frame in @($frames | Where-Object template_id -CEQ $id)) { & $add VARIANT REF $frame.state_id $viewport $mode $frame.stream_id $t }
        foreach ($pair in @(@($t.state_profile,'state'),@($t.viewport_profile,'viewport'),@($t.mode_profile,'mode'))) {
            $profile = @($Context.Profiles | Where-Object profile_id -CEQ $pair[0])[0]
            foreach ($value in $profile.required_values.Split(';')) {
                $s=$state;$v=$viewport;$m=$mode
                switch ($pair[1]) {state {$s=$value} viewport {$v=$value} mode {$m=$value}}
                & $add VARIANT REF $s $v $m $scopes[0] $t
            }
        }
        & $add ANNOTATION REF $state $viewport $mode $scopes[0] $t
        if ($BatchId -cin @('B01','B05','B06','B08')) { & $add PROTOTYPE REF $state $viewport $mode $scopes[0] $t }
        foreach ($route in @($Context.Routes | Where-Object { $_.template_id -ceq $id -and $_.baseline_frame_name -clike ("HSD_UIR_${BatchId}_*") })) {
            $match=[regex]::Match($route.baseline_frame_name,'_STATE_(?<state>.+?)_VP_(?<viewport>.+?)_MODE_(?<mode>.+?)_(?:STREAM_(?<stream>HIGH|MEDIUM|LOW|SEMANTIC)|SCOPE_(?<scope>EXCLUDED))_')
            $scope=if($match.Groups['scope'].Success){'STREAM-SCOPE-EXCLUDED'}else{'S-'+$match.Groups['stream'].Value}
            & $add ROUTE_INSTANCE_SHEET $route.route_instance_id.Replace('-','_') ('STATE-'+$match.Groups['state'].Value.Replace('_','-')) ('VP-'+$match.Groups['viewport'].Value.Replace('_','-')) ('MODE-'+$match.Groups['mode'].Value.Replace('_','-')) $scope $route
            if ($route.route_id -ceq 'ROUTE-PRIVACY') {
                foreach ($privacyScope in $scopes) {
                    & $add FRAME $route.route_instance_id.Replace('-','_') ('STATE-'+$match.Groups['state'].Value.Replace('_','-')) ('VP-'+$match.Groups['viewport'].Value.Replace('_','-')) ('MODE-'+$match.Groups['mode'].Value.Replace('_','-')) $privacyScope $route
                }
            }
        }
    }
    return @($rows.ToArray())
}

if ($FunctionsOnly) { return }
$root=(Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$design=Join-Path $root 'docs/phase-1-ui-reference-design'
$context=[pscustomobject]@{Batches=@(Import-Csv "$design/design-batch-plan.csv");Templates=@(Import-Csv "$design/reference-template-inventory.csv");Profiles=@(Import-Csv "$design/responsive-state-mode-matrix.csv");Routes=@(Import-Csv "$design/foundation-route-coverage.csv");Flows=@(Import-Csv "$design/foundation-flow-coverage.csv")}
$context|Add-Member Mapping (Get-UiStreamMapping -Primitives @(Import-Csv "$design/component-primitives.csv") -Templates $context.Templates)
$checks=0
function Assert-Test($Condition,$Name){if(-not $Condition){throw "FAIL: $Name"};$script:checks++}
foreach($batch in @('B01','B02','B08')){
    $fixture=@(New-UiExitCoverageFixture $batch $context)
    $gaps=@(Get-UiExitCoverageGaps $batch $fixture $context)
    Assert-Test ($gaps.Count -eq 0) ("complete necessary fixture: $batch :"+($gaps -join ','))
}
$fixture=@(New-UiExitCoverageFixture B02 $context)
Assert-Test (@(Get-UiExitCoverageGaps B02 @($fixture|Where-Object evidence_type -CNE ROUTE_INSTANCE_SHEET) $context) -match 'missing-route-instance').Count 'route sheets cannot disappear'
$fixture=@(New-UiExitCoverageFixture B01 $context)
Assert-Test (@(Get-UiExitCoverageGaps B01 @($fixture|Where-Object evidence_type -CNE PROTOTYPE) $context) -match 'missing-type:.+:PROTOTYPE').Count 'prototype cannot disappear'
Assert-Test (@(Get-UiExitCoverageGaps B01 @($fixture|Where-Object viewport_id -CNE VP-320) $context) -match 'missing-axis:.+:VP-320').Count 'viewport axis cannot disappear'
Assert-Test (@(Get-UiExitCoverageGaps B01 @($fixture|Where-Object mode_id -CNE MODE-FORCED-COLORS) $context) -match 'missing-axis:.+:MODE-FORCED-COLORS').Count 'mode axis cannot disappear'
Assert-Test (@(Get-UiExitCoverageGaps B01 @($fixture|Where-Object state_id -CNE STATE-NO-RESULTS) $context) -match 'missing-axis:.+:STATE-NO-RESULTS').Count 'ordinary state axis cannot disappear'
$changed=@($fixture|ForEach-Object{$_.PSObject.Copy()});$changed[0].prim_ids='PRIM-999'
Assert-Test ('unresolved-primitive-binding' -cin @(Get-UiExitCoverageGaps B01 $changed $context)) 'unknown primitive rejected'
$changed=@($fixture|ForEach-Object{$_.PSObject.Copy()});$changed[0].viewport_id='VP-BOGUS'
Assert-Test ('invalid-manifest-identity' -cin @(Get-UiExitCoverageGaps B01 $changed $context)) 'column mismatch rejected before coverage'
$changed=@($fixture|ForEach-Object{$_.PSObject.Copy()});$changed[0].profile_ids='SP-UNKNOWN'
Assert-Test ('unresolved-profile-binding' -cin @(Get-UiExitCoverageGaps B01 $changed $context)) 'unknown profile rejected'
$changed=@($fixture|ForEach-Object{$_.PSObject.Copy()});$changed[0].profile_ids+=';SP-BOOKING'
Assert-Test ('profile-owner-disagreement' -cin @(Get-UiExitCoverageGaps B01 $changed $context)) 'known foreign profile rejected'
$changed=@($fixture|ForEach-Object{$_.PSObject.Copy()});$changed[0].profile_ids+=';DS-S-SEMANTIC'
Assert-Test ('profile-owner-disagreement' -cin @(Get-UiExitCoverageGaps B01 $changed $context)) 'one stream cannot claim a peer profile'
$withoutComplete=@($fixture|Where-Object{ -not($_.evidence_type -ceq 'FRAME' -and $_.viewport_id -ceq 'VP-320')})
Assert-Test (@(Get-UiExitCoverageGaps B01 $withoutComplete $context) -match 'missing-complete-viewport-frame:.+:VP-320').Count 'variant cannot replace required complete viewport frame'
$changed=@($fixture|ForEach-Object{$_.PSObject.Copy()});foreach($row in $changed){$row.prim_ids=(@($row.prim_ids.Split(';')|Where-Object{$_ -cne 'PRIM-062'}) -join ';')}
Assert-Test (@(Get-UiExitCoverageGaps B01 $changed $context) -match 'missing-primitive:.+:PRIM-062').Count 'known required primitive cannot disappear from binding union'
Assert-Test ('duplicate-evidence-id' -cin @(Get-UiExitCoverageGaps B01 ($fixture + $fixture[0]) $context)) 'duplicate evidence identity rejected'
$withoutSemanticForcedColors=@($fixture|Where-Object{ -not($_.stream_id -ceq 'S-SEMANTIC' -and $_.mode_id -ceq 'MODE-FORCED-COLORS')})
Assert-Test (@(Get-UiExitCoverageGaps B01 $withoutSemanticForcedColors $context) -match 'missing-stream-frame:TPL-SYSTEM-RECOVERY:STATE-ERROR:S-SEMANTIC').Count 'semantic forced-colors system-recovery baseline cannot disappear'
$rehomed=@($fixture|ForEach-Object{$_.PSObject.Copy()})
foreach($row in $rehomed){
    if($row.stream_id -ceq 'S-SEMANTIC' -and $row.mode_id -ceq 'MODE-FORCED-COLORS'){
        $row.stream_id='S-HIGH';$row.evidence_id=$row.evidence_id.Replace('_STREAM_SEMANTIC_','_STREAM_HIGH_');$row.profile_ids=$row.profile_ids.Replace('DS-S-SEMANTIC','DS-S-HIGH')
    }
}
Assert-Test (@(Get-UiExitCoverageGaps B01 $rehomed $context) -match 'missing-stream-frame:TPL-SYSTEM-RECOVERY:STATE-ERROR:S-SEMANTIC').Count 'peer-stream forced-colors cannot discharge semantic recovery baseline'
$privacyFixture=@(New-UiExitCoverageFixture B02 $context)
$withoutPrivacyStream=@($privacyFixture|Where-Object{ -not($_.instance_id -ceq 'INST-ROUTE-PRIVACY' -and $_.stream_id -ceq 'S-HIGH' -and $_.evidence_type -ceq 'FRAME')})
Assert-Test ('missing-privacy-instance-frame:S-HIGH' -cin @(Get-UiExitCoverageGaps B02 $withoutPrivacyStream $context)) 'privacy notice frame required in every stream'
foreach($substitution in @('REF','INST-ROUTE-CREDITS')){
    $changed=@($privacyFixture|ForEach-Object{$_.PSObject.Copy()})
    foreach($row in $changed){
        if($row.instance_id -ceq 'INST-ROUTE-PRIVACY' -and $row.evidence_type -ceq 'FRAME'){
            $row.evidence_id=$row.evidence_id.Replace('_INST_ROUTE_PRIVACY_',('_'+$substitution.Replace('-','_')+'_'))
            $row.instance_id=$substitution
        }
    }
    Assert-Test ('missing-privacy-instance-frame:S-SEMANTIC' -cin @(Get-UiExitCoverageGaps B02 $changed $context)) ("privacy cannot inherit $substitution evidence")
}
Write-Output "RESULT=PASS CHECKS=$checks; necessary computable coverage only, not exit certification"
