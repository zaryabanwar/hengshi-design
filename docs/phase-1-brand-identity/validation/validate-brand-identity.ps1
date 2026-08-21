$ErrorActionPreference = 'Stop'

$validationDir = $PSScriptRoot
$identityDir = Split-Path -Parent $validationDir
$repoRoot = (Resolve-Path (Join-Path $identityDir '..\..')).Path
$failures = [Collections.Generic.List[string]]::new()
$passes = [Collections.Generic.List[string]]::new()
function Pass([string]$m) { $script:passes.Add($m) }
function Fail([string]$m) { $script:failures.Add($m) }
function Check([bool]$c,[string]$p,[string]$f) { if($c){Pass $p}else{Fail $f} }
function Text([string]$p) { Get-Content -Raw -LiteralPath (Join-Path $identityDir $p) }
function Rel([string]$p) { [IO.Path]::GetRelativePath($identityDir,$p).Replace('\','/') }
function Lum([string]$h) {
    $c=$h.TrimStart('#');$v=foreach($o in 0,2,4){$x=[Convert]::ToInt32($c.Substring($o,2),16)/255;if($x-le .04045){$x/12.92}else{[Math]::Pow(($x+.055)/1.055,2.4)}}
    .2126*$v[0]+.7152*$v[1]+.0722*$v[2]
}
function Contrast([string]$a,[string]$b){$x=Lum $a;$y=Lum $b;([Math]::Max($x,$y)+.05)/([Math]::Min($x,$y)+.05)}
function PngSize([string]$relative){
    $p=Join-Path $identityDir $relative;if(-not(Test-Path -LiteralPath $p -PathType Leaf)){return $null}
    $b=[IO.File]::ReadAllBytes($p);if($b.Length-lt 24){return $null};$sig=[byte[]](137,80,78,71,13,10,26,10)
    for($i=0;$i-lt 8;$i++){if($b[$i]-ne$sig[$i]){return $null}}
    [pscustomobject]@{Width=[BitConverter]::ToUInt32([byte[]]($b[19],$b[18],$b[17],$b[16]),0);Height=[BitConverter]::ToUInt32([byte[]]($b[23],$b[22],$b[21],$b[20]),0)}
}

$checkpointPath='validation/d-029-pre-stabilization-hashes.json'
$checkpointExpectedHash='E78CD5DDB1F1EB3D8003DE8369EBF436D65BC7FDCBA47C9E788C1E8A00D4527E'
$d033CheckpointPath='validation/d-033-pre-contrast-correction-hashes.json'
$d033CheckpointExpectedHash='58A1823E3261440CE4B51969F0C95FA7A63A6EC9D8EA6D1503951A89520BE0D0'
$authorizedD033CssHash='595B798239B5DB913CC89074AAEB8066184F64892258B0F4988D1FE89F507CE2'
$authorizedD033ReportHash='FC34146CB3C457AA70270B7A2B71BCBDE120292A4A4236FF3CC136C03502128B'
try{$checkpoint=Text $checkpointPath|ConvertFrom-Json;Pass 'D-029 pre-stabilization hash checkpoint parses as JSON.'}catch{Fail "D-029 checkpoint JSON: $($_.Exception.Message)"}
Check ((Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir $checkpointPath)).Hash-eq$checkpointExpectedHash) 'D-029 pre-stabilization checkpoint remains byte-for-byte unchanged.' 'D-029 pre-stabilization checkpoint hash mismatch.'
try{$d033Checkpoint=Text $d033CheckpointPath|ConvertFrom-Json;Pass 'PRE_D033_CHECKPOINT parses as JSON.'}catch{Fail "D-033 checkpoint JSON: $($_.Exception.Message)"}
Check ((Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir $d033CheckpointPath)).Hash-eq$d033CheckpointExpectedHash) 'PRE_D033_CHECKPOINT remains byte-for-byte unchanged.' 'PRE_D033_CHECKPOINT hash mismatch.'
if($checkpoint){
 $archiveNow=@(Get-ChildItem (Join-Path $identityDir 'archive') -Recurse -File|ForEach-Object{Rel $_.FullName}|Sort-Object);$archivePinned=@($checkpoint.immutableArchiveFiles.path|Sort-Object);$archiveBad=@();foreach($e in @($checkpoint.immutableArchiveFiles)){if((Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir $e.path)).Hash-ne$e.sha256){$archiveBad+=$e.path}}
 Check ((@($checkpoint.immutableArchiveFiles).Count-eq 31)-and(@(Compare-Object $archiveNow $archivePinned).Count-eq 0)-and($archiveBad.Count-eq 0)) 'All 31 recursively pinned archive files remain byte-for-byte unchanged with no additions.' "D-029 archive integrity mismatch: $($archiveBad-join', ')"
 $forbiddenBad=@();foreach($e in @($checkpoint.forbiddenAuthorityFiles)){if((Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir $e.path)).Hash-ne$e.sha256){$forbiddenBad+=$e.path}}
 Check ((@($checkpoint.forbiddenAuthorityFiles).Count-eq 24)-and($forbiddenBad.Count-eq 0)) 'All 24 forbidden identity-authority, logo, geometry, and retained-evidence files remain byte-for-byte unchanged.' "D-029 forbidden authority mismatch: $($forbiddenBad-join', ')"
 Check (($checkpoint.failedBrowserReportSha256-eq'64E5EA083A6221AA521BF3F06979927EF07C6FFBB39077DE12BDC343342A89C7')-and(@($checkpoint.mutableFiles).Count-eq 20)) 'PRE_D033_CHECKPOINT retains the D-029 failed-evidence history and exact mutable inventory.' 'PRE_D033_CHECKPOINT historical D-029 state is incomplete.'
}
$currentCssHash=(Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir 'visual-boards/identity-board.css')).Hash
$currentReportHash=(Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir 'validation/browser-audit-report.json')).Hash
$earlyCss=Text 'visual-boards/identity-board.css';$earlyHtml=Text 'visual-boards/index.html';$earlyReport=Text 'validation/browser-audit-report.json'|ConvertFrom-Json
$hasDependencyGraphic=($earlyCss-match'\.dependency-key-graphic')-and($earlyHtml-match'class="dependency-key-graphic"')
$validationState=if(($currentCssHash-eq$authorizedD033CssHash)-and($currentReportHash-eq$authorizedD033ReportHash)){'AUTHORIZED_D033_POST_SOURCE'}elseif($hasDependencyGraphic-and(($earlyReport.totalViolations-ne0)-or($earlyReport.totalIncomplete-ne0))){'AUTHORIZED_D034_REMEDIATION_SOURCE'}elseif($hasDependencyGraphic-and($earlyReport.totalViolations-eq0)-and($earlyReport.totalIncomplete-eq0)){'FINAL_FREEZE'}else{'UNRECOGNIZED'}
Check ($validationState-ne'UNRECOGNIZED') "$validationState state is recognized." 'D-034 validator state is unrecognized.'
if($validationState-eq'AUTHORIZED_D033_POST_SOURCE'){
 Check (($d033Checkpoint.survivingBrowserReport.actualSha256-eq$authorizedD033ReportHash)-and$d033Checkpoint.survivingBrowserReport.exactMatch-and($d033Checkpoint.counts.reviewReports-eq6)-and($d033Checkpoint.counts.archiveFiles-eq31)-and($d033Checkpoint.counts.forbiddenAuthorityFiles-eq24)) 'AUTHORIZED_D033_POST_SOURCE matches the frozen checkpoint, CSS, surviving report, and protected counts.' 'AUTHORIZED_D033_POST_SOURCE does not match D-033 authority.'
}
$authorityText=(Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'DECISIONS.md'))+(Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'docs/decisions-log.md'))+(Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'MANUAL_ACTIONS.md'))
Check (($authorityText-match'D-029')-and($authorityText-match'MA-017')-and($authorityText-match'one evidence-only stabilization')) 'D-029 and MA-017 approved one-pass evidence-stabilization authority is present.' 'D-029/MA-017 approval authority is missing.'

$required=@(
 'README.md','01-identity-principles.md','02-visual-directions.md','03-logo-system.md','04-color-and-typography.md','05-imagery-iconography-and-data.md','06-motion-sound-and-3d.md','07-accessibility-seo-and-applications.md','BRAND_IDENTITY.md','geometry-spec.json','semantic-tokens.json','asset-manifest.json','traceability.csv','handoff.md','producer-inspection.md',
 'visual-boards/index.html','visual-boards/identity-board.css','visual-boards/scale-evidence.html',
 'assets/logo-framework-relay-primary.svg','assets/logo-framework-relay-light.svg','assets/logo-framework-relay-mono.svg','assets/logo-framework-relay-reverse.svg','assets/mark-framework-relay.svg','assets/mark-framework-relay-small.svg','assets/favicon-framework-relay.svg','assets/current-hybrid-framework-relay.svg','assets/logo-quiet-framework.svg','assets/logo-resonant-field.svg','assets/direction-a-signal-ledger.svg','assets/direction-b-quiet-framework.svg','assets/direction-c-resonant-field.svg','assets/icon-data-specimen.svg','assets/og-evidence-in-motion.svg',
 'assets/identity-board-preview.png','assets/identity-board-wide.png','assets/identity-board-medium.png','assets/identity-board-narrow.png','assets/identity-board-forced-colors.png','assets/identity-board-grayscale.png','assets/identity-board-print.png','assets/identity-scale-evidence.png',
 'archive/iteration-2-signal-ledger-logo/README.md','archive/iteration-2-signal-ledger-logo/baseline-inventory.json','archive/iteration-2-signal-ledger-logo/geometry-spec.json',
 'archive/d-028-correction-1-pre-exception/README.md','archive/d-028-correction-1-pre-exception/baseline-inventory.json',
 'validation/d-029-pre-stabilization-hashes.json','validation/capture-identity-evidence.mjs','validation/audit-identity-board.mjs','validation/browser-audit-report.json','validation/validation-report.md','validation/update-asset-manifest.ps1','validation/validate-brand-identity.ps1',
 'reviews/design-review-iteration-1.md','reviews/design-review-iteration-2.md','reviews/design-review-iteration-3.md','accessibility/accessibility-audit-iteration-1.md','accessibility/accessibility-audit-iteration-2.md','accessibility/accessibility-audit-iteration-3.md'
)
$missing=@($required|Where-Object{-not(Test-Path -LiteralPath (Join-Path $identityDir $_) -PathType Leaf)})
Check ($missing.Count-eq 0) 'All final producer deliverables, frozen reports, and archive files exist.' "Missing: $($missing-join', ')"

# All six prior independent reports are immutable. Only exact D-029 verification names may follow.
$reviewHashes=@{
 'reviews/design-review-iteration-1.md'='12014D5772250EF8B2BA07B911D833B4F53C4CA880961BA55F5B4DCF07CE78DD'
 'accessibility/accessibility-audit-iteration-1.md'='532779730294F74716D85115514E3EAA749FF9FAA6EEE48B20CFECF2BEED70D2'
 'reviews/design-review-iteration-2.md'='490A4391327D476014CC1B758EDFDDF66DE4C8A03628BE116659E5ADA272D895'
 'accessibility/accessibility-audit-iteration-2.md'='FD06D3500F797A2148B7432C6AB2F7F6CF613D71732710BCBE54E65C8761B519'
 'reviews/design-review-iteration-3.md'='95C5E18B58E7915837EDDF8A8B4B3BA2EACCB1461C4856F7854F92076937140F'
 'accessibility/accessibility-audit-iteration-3.md'='EADE90EF12C4B27C703B69D44982F1B4F5CF2E6E65CB940CDC929C0B4F9A0CED'
}
$optionalVerification=@('reviews/design-verification-evidence-stabilization-1.md','accessibility/accessibility-verification-evidence-stabilization-1.md')
$actualReports=@(Get-ChildItem (Join-Path $identityDir 'reviews'),(Join-Path $identityDir 'accessibility') -Recurse -File|ForEach-Object{Rel $_.FullName}|Sort-Object)
$allowedReports=@($reviewHashes.Keys)+$optionalVerification
$unexpectedReports=@($actualReports|Where-Object{$_-notin$allowedReports});$missingReports=@($reviewHashes.Keys|Where-Object{$_-notin$actualReports})
Check (($unexpectedReports.Count-eq 0)-and($missingReports.Count-eq 0)) 'Reviewer destinations contain six frozen reports and only exact optional D-029 verification filenames.' "Reviewer allowlist failure: unexpected=$($unexpectedReports-join', '); missing=$($missingReports-join', ')"
$hashBad=@();foreach($p in $reviewHashes.Keys){if((Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir $p)).Hash-ne$reviewHashes[$p]){$hashBad+=$p}}
Check ($hashBad.Count-eq 0) 'All six prior independent reports remain byte-for-byte unchanged.' "Prior report hash mismatch: $($hashBad-join', ')"
$optionalBad=@();foreach($p in $optionalVerification){if(Test-Path -LiteralPath (Join-Path $identityDir $p)){ $c=Text $p;if($c-notmatch'(?i)D-029|evidence stabilization'-or$c-notmatch'(?im)^#{1,3}\s+.*(?:verification|review|audit)'-or$c-notmatch'(?im)^\*\*Verdict:\*\*\s*(?:PASS|REVISE|BLOCKED)\b'){$optionalBad+=$p}}}
Check ($optionalBad.Count-eq 0) 'Any optional D-029 verification report has deterministic authority, heading, and verdict structure.' "Optional D-029 verification report invalid: $($optionalBad-join', ')"

# CR-001 archive baseline and anchors.
try{$baseline=Text 'archive/iteration-2-signal-ledger-logo/baseline-inventory.json'|ConvertFrom-Json;Pass 'Archive baseline inventory parses as JSON.'}catch{Fail "Archive baseline JSON: $($_.Exception.Message)"}
if($baseline){
 Check (($baseline.document.currentUsePermitted-eq$false)-and($baseline.document.status-eq'superseded_internal_review_and_rollback_only')) 'Archive is explicitly superseded and not permitted for current use.' 'Archive current-use semantics drifted.'
 $anchors=@{
  'asset-manifest.json'='AB54DF15DD0C095EA8976FFA69C72ED107589E5DAFBEBBFE282BD554FE6F9FA3';'BRAND_IDENTITY.md'='95711633ED5695A2F22E34FD54D4F5C4040FD8AF6F96FC3B04DB58B3C0122CF0';'geometry-spec.json'='03A97795E196477D77C33DEDCF3DEF63FAB517CA97C1591688B1FEB2FEA51877';'reviews/design-review-iteration-2.md'='490A4391327D476014CC1B758EDFDDF66DE4C8A03628BE116659E5ADA272D895';'accessibility/accessibility-audit-iteration-2.md'='FD06D3500F797A2148B7432C6AB2F7F6CF613D71732710BCBE54E65C8761B519'
 }
 $anchorBad=@();foreach($p in $anchors.Keys){$e=@($baseline.cr001Anchors|Where-Object{$_.path-eq$p});if($e.Count-ne 1-or$e[0].sha256-ne$anchors[$p]){$anchorBad+=$p}}
 Check ($anchorBad.Count-eq 0) 'All five CR-001 intake anchors are recorded exactly.' "CR-001 anchor mismatch: $($anchorBad-join', ')"
 $sourceBad=@();foreach($e in @($baseline.supersededSources)){$p=Join-Path $identityDir $e.archivePath;if(-not(Test-Path -LiteralPath $p)-or(Get-FileHash -Algorithm SHA256 -LiteralPath $p).Hash-ne$e.sha256){$sourceBad+=$e.archivePath}}
 Check ((@($baseline.supersededSources).Count-eq 8)-and($sourceBad.Count-eq 0)) 'All eight superseded geometry/logo sources match their archive hashes.' "Superseded archive mismatch: $($sourceBad-join', ')"
}
try{$exceptionBaseline=Text 'archive/d-028-correction-1-pre-exception/baseline-inventory.json'|ConvertFrom-Json;Pass 'D-028 pre-exception baseline parses as JSON.'}catch{Fail "D-028 baseline JSON: $($_.Exception.Message)"}
if($exceptionBaseline){
 Check (($exceptionBaseline.document.currentUsePermitted-eq$false)-and($exceptionBaseline.document.authority-match'D-028')-and($exceptionBaseline.document.status-eq'pre_exception_unresolved_revise_package')) 'D-028 baseline is explicitly unresolved, non-current, and correction-authorized.' 'D-028 baseline semantics drifted.'
 $exceptionSourceBad=@();foreach($e in @($exceptionBaseline.producerSources)){$p=Join-Path $identityDir $e.archivePath;if(-not(Test-Path -LiteralPath $p)-or(Get-FileHash -Algorithm SHA256 -LiteralPath $p).Hash-ne$e.sha256){$exceptionSourceBad+=$e.archivePath}}
 Check ((@($exceptionBaseline.producerSources).Count-eq 19)-and($exceptionSourceBad.Count-eq 0)) 'All 19 changed pre-exception producer sources match their archived hashes.' "D-028 source baseline mismatch: $($exceptionSourceBad-join', ')"
 $exceptionReportBad=@();foreach($e in @($exceptionBaseline.immutableReports)){if($reviewHashes[$e.path]-ne$e.sha256){$exceptionReportBad+=$e.path}}
 Check ((@($exceptionBaseline.immutableReports).Count-eq 6)-and($exceptionReportBad.Count-eq 0)) 'D-028 baseline records all six immutable report hashes exactly.' "D-028 report baseline mismatch: $($exceptionReportBad-join', ')"
 Check (@($exceptionBaseline.invalidatedEvidence).Count-eq 8) 'D-028 baseline records all eight pre-exception evidence hashes.' 'D-028 invalidated-evidence inventory count drifted.'
}
$legacyCurrent=@('logo-signal-ledger-primary.svg','logo-signal-ledger-dark.svg','logo-signal-ledger-mono.svg','logo-signal-ledger-reverse.svg','monogram-signal-ledger.svg','mark-signal-ledger-small.svg','favicon-concept.svg')
$legacyPresent=@($legacyCurrent|Where-Object{Test-Path -LiteralPath (Join-Path $identityDir "assets/$_")})
Check ($legacyPresent.Count-eq 0) 'Superseded Signal Ledger logo sources are absent from the current asset root.' "Superseded logo remains current: $($legacyPresent-join', ')"

try{$geometry=Text 'geometry-spec.json'|ConvertFrom-Json;Pass 'Current geometry authority parses as JSON.'}catch{Fail "Geometry JSON: $($_.Exception.Message)"}
try{$tokens=Text 'semantic-tokens.json'|ConvertFrom-Json;Pass 'Semantic tokens parse as JSON.'}catch{Fail "Token JSON: $($_.Exception.Message)"}
try{$manifest=Text 'asset-manifest.json'|ConvertFrom-Json;Pass 'Manifest parses as JSON.'}catch{Fail "Manifest JSON: $($_.Exception.Message)"}
try{$browserAudit=Text 'validation/browser-audit-report.json'|ConvertFrom-Json;Pass 'Browser audit report parses as JSON.'}catch{Fail "Browser audit JSON: $($_.Exception.Message)"}
try{$trace=@(Import-Csv (Join-Path $identityDir 'traceability.csv'));Pass 'Traceability parses as CSV.'}catch{Fail "Traceability CSV: $($_.Exception.Message)"}

# One exact 80-unit current authority and two bounded optical variants.
if($geometry){
 Check (($geometry.document.version-eq'framework-relay-master-80-v1')-and($geometry.master.viewBox-eq'0 0 80 80')) 'Geometry names one Framework Relay 80-unit authority.' 'Current geometry authority/version mismatch.'
 $m=$geometry.master
 Check (($m.frame.topLeft-eq'M30 10 H10 V30')-and($m.frame.topRight-eq'M50 10 H70 V30')-and($m.frame.bottomRight-eq'M70 50 V70 H50')-and($m.frame.bottomLeft-eq'M30 70 H10 V50')-and($m.frame.strokeWidth-eq 6)-and($m.relay.path-eq'M16 52 H32 V40 H48 V28 H64')-and($m.relay.strokeWidth-eq 5)-and($m.relay.checkpoint.x-eq 61)-and($m.relay.checkpoint.y-eq 25)-and($m.relay.checkpoint.width-eq 6)) 'Master framework, relay, and checkpoint values are exact.' 'Master geometry values drifted.'
 $standard=@('logo-framework-relay-primary.svg','logo-framework-relay-light.svg','logo-framework-relay-mono.svg','logo-framework-relay-reverse.svg','mark-framework-relay.svg');$geoBad=@()
 foreach($n in $standard){$s=Text "assets/$n";foreach($needle in @('data-geometry="framework-relay-master-80-v1"','M30 10 H10 V30','M50 10 H70 V30','M70 50 V70 H50','M30 70 H10 V50','M16 52 H32 V40 H48 V28 H64','stroke-width="5"')){if($s-notmatch[regex]::Escape($needle)){$geoBad+="${n}:$needle"}}}
 Check ($geoBad.Count-eq 0) 'All current standard SVGs use the exact machine-readable master.' "Standard geometry mismatch: $($geoBad-join'; ')"
 $small=Text 'assets/mark-framework-relay-small.svg';$fav=Text 'assets/favicon-framework-relay.svg'
 Check (($small-match'data-geometry="framework-relay-small-24-v1"')-and($small-match'd="M5 16 H10 V12 H14 V8 H19"')-and($fav-match'data-geometry="framework-relay-favicon-16-v1"')-and($fav-match'd="M4 11 H7 V8 H10 V5 H12"')-and($fav-match'stroke-width="2"')) 'Optical 24px and 16px variants match their bounded specifications.' 'Optical variant geometry mismatch.'
 $screen=[double]$geometry.lockup.minimumScreenWidthCssPx;$font=[double]$geometry.lockup.wordmark.fontSize;$stroke=[double]$geometry.master.relay.strokeWidth;$vbw=420
 Check (([Math]::Round($font*$screen/$vbw,2)-ge 12)-and([Math]::Round($stroke*$screen/$vbw,2)-ge 2)-and([Math]::Round($font*144/$vbw,2)-lt 12)-and([Math]::Round($stroke*144/$vbw,2)-lt 2)) 'Size arithmetic supports 168px and rejects 144px against 12px/2px floors.' 'Minimum-size arithmetic does not support the documented boundary.'
}
$principles=Text '01-identity-principles.md';$currentProducerFiles=@(Get-ChildItem $identityDir -Recurse -File|Where-Object{$_.Extension-in@('.md','.json','.csv','.html','.css','.svg','.ps1','.mjs')-and$_.FullName-notmatch'[\\/]archive[\\/]'-and$_.FullName-notmatch'[\\/](reviews|accessibility)[\\/]'-and$_.FullName-notmatch'[\\/]validation[\\/]validate-brand-identity\.ps1$'});$staleMark=@()
foreach($f in $currentProducerFiles){$c=Get-Content -Raw $f.FullName;if($c-match'(?i)diagonal signal path in the recommended mark|recommended mark.{0,120}two accountable rails|recommended mark.{0,160}joining field'){$staleMark+=Rel $f.FullName}}
Check (($staleMark.Count-eq 0)-and($principles-match'four open governed brackets')-and($principles-match'non-diagonal stepped evidence relay')-and$principles-match'square checkpoint'-and$principles-match'founder-rejected, superseded') 'Current normative text defines only Framework Relay; rejected geometry is explicit archive history.' "Stale/rejected current mark authority remains: $($staleMark-join', ')"
$application=Text 'assets/current-hybrid-framework-relay.svg'
Check (($application-match'data-embedded-geometry="framework-relay-master-80-v1"')-and($application-match'data-master-transform="translate\(88 54\) scale\(\.62\)"')-and($application-match'data-checkpoint-local="61 25 6 6"')-and($application-match'data-checkpoint-rendered="125.82 69.50 3.72 3.72"')-and($application-match'<rect x="61" y="25" width="6" height="6" fill="#00D4FF" stroke="none"/>')-and($application-notmatch'x="140\.7" y="84\.4"')) 'Embedded application checkpoint is inside the exact transformed Framework Relay master.' 'Embedded current-application checkpoint transform or assertion drifted.'

if($tokens){
 Check (($tokens.document.version-eq'd-028-correction-1-of-1')-and($tokens.identityReconciliation.currentCandidate.name-eq'Framework Relay')-and($tokens.identityReconciliation.currentCandidate.status-eq'd_028_correction_1_of_1_pending_independent_verification')-and($tokens.identityReconciliation.supersededLogo.status-eq'founder_rejected_archived_not_current')) 'Semantic tokens identify D-028 correction 1 of 1 and preserve the hybrid/archive boundary.' 'Identity reconciliation token semantics drifted.'
 $requiredColors=@('#0B0F14','#161D26','#2A3542','#D8D3C8','#F3F1EA','#FAF9F6','#FFFFFF','#000000','#00D4FF','#FFB000','#B6F36B','#A98CFF','#006D82','#8A5600','#4F7D18','#6D52B5')
 $tokenText=Text 'semantic-tokens.json';$docText=Text '04-color-and-typography.md';$css=Text 'visual-boards/identity-board.css';$colorBad=@()
 foreach($h in $requiredColors|Where-Object{$_-ne'#000000'}){if($tokenText-notmatch[regex]::Escape($h)){$colorBad+="tokens:$h"};if($docText-notmatch[regex]::Escape($h)){$colorBad+="doc:$h"};if($css-notmatch[regex]::Escape($h.ToLower())){$colorBad+="css:$h"}}
 Check ($colorBad.Count-eq 0) 'All dark- and light-surface colors close across docs, tokens, and CSS.' "Color closure gaps: $($colorBad-join', ')"
 $contrastBad=@();foreach($p in @($tokens.declaredContrastPairings)){$actual=Contrast $p.foreground $p.background;if([Math]::Abs($actual-[double]$p.expectedRatio)-gt .01-or$actual-lt[double]$p.minimum){$contrastBad+="$($p.foreground)/$($p.background)"}}
 Check ($contrastBad.Count-eq 0) 'Every declared contrast ratio recomputes and meets its threshold.' "Contrast mismatch: $($contrastBad-join'; ')"
}

# Evidence-state grammar and one separate direct-labelled data-series authority.
$grammar=[ordered]@{verified=@('filled-circle','solid','none');demo=@('open-diamond','dash-dot','10 4 2 4');proposed=@('filled-square','short-dash','8 6');conditional=@('filled-triangle','long-dash','16 7');unavailable=@('filled-bar','dotted','2 7');error=@('open-octagon','double-solid','none')}
$html=Text 'visual-boards/index.html';$icon=Text 'assets/icon-data-specimen.svg';$grammarBad=@()
Check (($html-match'<p class="state proposed" data-evidence-state="proposed" data-marker="filled-square" data-line="short-dash" data-dash-array="8 6">■ ┅ Proposed method</p>')-and($html-notmatch'<p class="state proposed"[^>]*aria-label=')) 'Proposed-state paragraph exposes its visible redundant text without prohibited ARIA.' 'Proposed-state paragraph semantics are not stabilized.'
$css=Text 'visual-boards/identity-board.css';Check (($css-match'(?s)\.dependency-key\s*\{[^}]*color:\s*var\(--ink\);[^}]*background:\s*var\(--paper\);[^}]*\}')-and($css-match'h1 \{ max-width: 100%; font-size: clamp\(2\.5rem, 13\.5vw, 3rem\); overflow-wrap: anywhere; \}')-and($css-match'\.variant-grid figure\.reverse figcaption \{ color: CanvasText; \}')-and($css-match'\.masthead \.eyebrow, \.dark \.eyebrow, \.gate \.eyebrow[^\{]*\{ color: #000; \}')-and(($validationState-eq'AUTHORIZED_D033_POST_SOURCE')-or($hasDependencyGraphic-and($html-match'<svg class="dependency-key-graphic"[^>]*aria-hidden="true"')-and($html-match'<strong class="series-label">Dependency map</strong><span class="series-pattern">ring · custom <code>12 3 3 3 3 3</code>')))) 'Authorized contrast source preserves D-029 closures, dependency foreground/background and meaning, and print contrast surfaces.' 'Authorized contrast source semantics are incomplete.'
$auditScript=Text 'validation/audit-identity-board.mjs';$captureScript=Text 'validation/capture-identity-evidence.mjs';$manifestScript=Text 'validation/update-asset-manifest.ps1'
Check (($auditScript-match'board-medium-900')-and($auditScript-match'board-print')-and($auditScript-match'replaced_by_computed_system_palette_check')-and($auditScript-match'D-034 contrast completion')-and($captureScript-match'd034-contrast-completion')-and($manifestScript-match'd-034-contrast-completion')) 'D-034 audit, capture, and manifest scripts identify the completion state and required modes.' 'D-034 evidence script closure is incomplete.'
if($tokens){foreach($k in $grammar.Keys){$e=$tokens.evidenceState.$k;$g=$grammar[$k];if($e.marker-ne$g[0]-or$e.line-ne$g[1]-or$e.dashArray-ne$g[2]){$grammarBad+="tokens:$k"};$needle='data-state="{0}" data-marker="{1}" data-line="{2}"' -f $k,$g[0],$g[1];if($html-notmatch[regex]::Escape($needle)){$grammarBad+="html:$k"};if($icon-notmatch[regex]::Escape($g[0].Replace('-',' '))){$grammarBad+="svg:$k"}}}
Check ($grammarBad.Count-eq 0) 'Six-state marker/line grammar is exact in JSON, HTML, and SVG accessible text.' "Evidence grammar mismatch: $($grammarBad-join', ')"
$directionA=Text 'assets/direction-a-signal-ledger.svg';$directionB=Text 'assets/direction-b-quiet-framework.svg'
$verifiedNeedles=@('data-evidence-state="verified"','data-marker="filled-circle"','data-line="solid"','data-context="visible-label-source-date-required"','SOURCE + DATE REQUIRED')
$reservedBad=@();foreach($pair in @(@('current-hybrid-framework-relay.svg',$application),@('direction-a-signal-ledger.svg',$directionA))){foreach($needle in $verifiedNeedles){if($pair[1]-notmatch[regex]::Escape($needle)){$reservedBad+="$($pair[0]):$needle"}}}
foreach($needle in $verifiedNeedles){if($directionB-notmatch[regex]::Escape($needle)){$reservedBad+="direction-b-quiet-framework.svg:$needle"}}
foreach($needle in @('data-evidence-state="conditional"','data-marker="filled-triangle"','data-line="long-dash"','data-dash-array="16 7"','stroke-dasharray="16 7"')){if($directionB-notmatch[regex]::Escape($needle)){$reservedBad+="direction-b-quiet-framework.svg:$needle"}}
foreach($needle in @('data-evidence-state="proposed"','data-marker="filled-square"','data-line="short-dash"','data-dash-array="8 6"')){if($html-notmatch[regex]::Escape($needle)){$reservedBad+="index.html:$needle"}}
$reservedVisuals=@();$reservedSvgFiles=@(Get-ChildItem (Join-Path $identityDir 'assets') -Filter '*.svg' -File);foreach($f in @($reservedSvgFiles)+@(Get-Item (Join-Path $identityDir 'visual-boards/index.html'))){$c=Get-Content -Raw $f.FullName;if($c-match'(?i)>\s*(?:VERIFIED(?: INPUT| SOURCE)?|REVIEW NEEDED|PROPOSED(?: METHOD)?|UNAVAILABLE|ERROR)\b|Hengshi-owned demo'){$reservedVisuals+=Rel $f.FullName}}
$reservedExpected=@('assets/current-hybrid-framework-relay.svg','assets/direction-a-signal-ledger.svg','assets/direction-b-quiet-framework.svg','assets/icon-data-specimen.svg','visual-boards/index.html')
Check (($reservedBad.Count-eq 0)-and(@(Compare-Object ($reservedExpected|Sort-Object) ($reservedVisuals|Sort-Object -Unique)).Count-eq 0)) 'Every current visual-source reserved evidence label uses or documents its exact redundant grammar.' "Reserved evidence-state visual mismatch: details=$($reservedBad-join'; '); files=$($reservedVisuals-join', ')"
$series=[ordered]@{'Context baseline'='1 5 9 5';'Dependency map'='12 3 3 3 3 3';'Decision frame'='solid';'Evidence depth'='5 5';'Risk view'='13 4 4 4'};$seriesBad=@()
foreach($name in $series.Keys){if($icon-notmatch[regex]::Escape($name)){$seriesBad+="svg-label:$name"};if($html-notmatch[regex]::Escape($name)){$seriesBad+="html-label:$name"};if($series[$name]-ne'solid'-and$icon-notmatch[regex]::Escape('stroke-dasharray="'+$series[$name]+'"')){$seriesBad+="svg-pattern:$name"}}
$seriesDoc=Text '05-imagery-iconography-and-data.md';$brandDoc=Text 'BRAND_IDENTITY.md'
if($tokens){$tokenSeries=@($tokens.dataSeries.contextBaseline,$tokens.dataSeries.dependencyMap,$tokens.dataSeries.decisionFrame,$tokens.dataSeries.evidenceDepth,$tokens.dataSeries.riskView);if($tokens.dataSeries.authority-ne'single_current_mapping_D_028_correction_1_of_1'-or$tokens.dataSeries.minimumVisibleEndpointLabelCssPx-ne 12-or($tokenSeries.label-join'|')-ne($series.Keys-join'|')){$seriesBad+='token-authority'}}
foreach($needle in @('class="responsive-series-chart"','class="series-label">Context baseline','class="series-label">Dependency map','class="series-label">Decision frame','class="series-label">Evidence depth','class="series-label">Risk view')){if($html-notmatch[regex]::Escape($needle)){$seriesBad+="responsive:$needle"}}
Check (($seriesBad.Count-eq 0)-and($seriesDoc-notmatch'(?m)^### Series encoding\s*$')-and($seriesDoc-notmatch'\| 1 \| Cyan \| Circle \| Solid \|')) 'One five-series mapping authority agrees across tokens, SVG, semantic list, responsive labels, and guidance.' "Data-series authority conflict: $($seriesBad-join', ')"
Check (($html-match'R-020 remains in progress until independent accessibility verification passes')-and($seriesDoc-match'R-020 remains in progress')-and($brandDoc-match'(?s)closure\s+remains pending independent accessibility verification')-and$html-notmatch'closes R-020 for this package') 'R-020 correction evidence is recorded without premature closure.' 'R-020 status is missing or prematurely closed.'
Check (($html-match'data-direction-key="structured-trajectory-retained"')-and($html-match'data-direction-key="governed-modularity-source"')-and($html-match'data-direction-key="framework-relay-current"')-and$html-match'Superseded:'-and$html-match'Closed historical:'-and$html-notmatch'Founder comparison') 'Board distinguishes retained, source, current, superseded, and closed semantics without an A/B/C gate.' 'Board reconciliation semantics are incomplete.'

# Source structure, local-only behavior, rendering evidence, and accessibility audit.
$svgFiles=@(Get-ChildItem (Join-Path $identityDir 'assets') -Filter '*.svg' -File);$svgBad=@();foreach($f in $svgFiles){try{[xml]$x=Get-Content -Raw $f.FullName;if(-not$x.svg.title-or-not$x.svg.desc-or-not$x.svg.width-or-not$x.svg.height-or-not$x.svg.viewBox){$svgBad+=$f.Name}}catch{$svgBad+=$f.Name}}
Check ($svgBad.Count-eq 0) 'All current SVGs parse and expose title, description, dimensions, and viewBox.' "SVG invalid: $($svgBad-join', ')"
$clearanceBad=@($svgFiles|Where-Object{$_.Name-match'^(logo|mark|favicon)'}|Where-Object{(Get-Content -Raw $_.FullName)-notmatch'UNREGISTERED.+TRADEMARK NOT CLEARED'}|ForEach-Object Name)
Check ($clearanceBad.Count-eq 0) 'Every current logo/mark SVG embeds the clearance boundary.' "Clearance missing: $($clearanceBad-join', ')"
$visualFiles=@((Join-Path $identityDir 'visual-boards/index.html'),(Join-Path $identityDir 'visual-boards/identity-board.css'),(Join-Path $identityDir 'visual-boards/scale-evidence.html'))+@($svgFiles.FullName);$external=@();foreach($f in $visualFiles){$c=(Get-Content -Raw $f).Replace('http://www.w3.org/2000/svg','');if($c-match'(?i)https?://|//[a-z0-9.-]+/'){$external+=Rel $f}}
Check ($external.Count-eq 0) 'Visual deliverables contain no external URL or runtime dependency.' "External references: $($external-join', ')"
$pngExpect=@{'assets/identity-board-preview.png'=1440;'assets/identity-board-wide.png'=1440;'assets/identity-board-medium.png'=900;'assets/identity-board-narrow.png'=390;'assets/identity-board-forced-colors.png'=900;'assets/identity-board-grayscale.png'=900;'assets/identity-board-print.png'=1200;'assets/identity-scale-evidence.png'=1200};$pngBad=@()
foreach($p in $pngExpect.Keys){$s=PngSize $p;if($null-eq$s-or$s.Width-ne$pngExpect[$p]-or$s.Height-lt 900){$pngBad+=$p}}
Check ($pngBad.Count-eq 0) 'All eight pinned pre-stabilization and retained scale PNGs are structurally valid.' "PNG evidence invalid: $($pngBad-join', ')"
if($browserAudit){
 $textSpacing=@($browserAudit.checks|Where-Object -Property id -EQ 'board-text-spacing-320')[0];$forced=@($browserAudit.checks|Where-Object -Property id -EQ 'board-forced-colors')[0];$allIncomplete=@($browserAudit.checks.incomplete);$allTargets=(@($allIncomplete.targets)|ForEach-Object{$_})-join'|'
 Check (($checkpoint.failedBrowserReportSha256-eq'64E5EA083A6221AA521BF3F06979927EF07C6FFBB39077DE12BDC343342A89C7')-and($d033Checkpoint.survivingBrowserReport.requiredSha256-eq$authorizedD033ReportHash)) 'PRE_D033_CHECKPOINT preserves the historical failed report and D-033 preserves the surviving contrast report without requiring either as current final evidence.' 'Historical browser-evidence chain is incomplete.'
 if($validationState-eq'AUTHORIZED_D033_POST_SOURCE'){
  Check (($browserAudit.totalViolations-eq1)-and($browserAudit.totalIncomplete-eq4)-and($allTargets-match'\.dependency-key')) 'AUTHORIZED_D033_POST_SOURCE contains the exact surviving contrast blocker awaiting retest.' 'AUTHORIZED_D033_POST_SOURCE browser signature drifted.'
 }elseif($validationState-eq'AUTHORIZED_D034_REMEDIATION_SOURCE'){
  $print=@($browserAudit.checks|Where-Object -Property id -EQ 'board-print')[0]
  Check (($browserAudit.totalViolations-eq0)-and($browserAudit.totalIncomplete-eq4)-and($allTargets-match'\.dependency-key')-and($print.violationCount-eq0)-and(@($print.incomplete).Count-eq0)) 'AUTHORIZED_D034_REMEDIATION_SOURCE retains only the four diagnosed non-text dependency-key incomplete results; print is clean.' 'AUTHORIZED_D034_REMEDIATION_SOURCE evidence contains an unexpected blocker.'
 }else{
  $forcedMinimum=[double]$forced.measurements.minimumForcedColorContrast
  Check (($browserAudit.totalViolations-eq0)-and($browserAudit.totalIncomplete-eq0)-and($browserAudit.totalCleanConsoleErrors-eq0)-and($browserAudit.totalPageErrors-eq0)-and(@($browserAudit.externalRequests).Count-eq0)-and$browserAudit.temporaryProfileRemoved-and($textSpacing.measurements.scrollWidth-eq$textSpacing.measurements.clientWidth)-and($forcedMinimum-ge21)) 'FINAL_FREEZE browser evidence is clean, local-only, residue-free, reflow-safe, and forced-colors contrast is at least 21:1.' 'FINAL_FREEZE browser evidence is not clean.'
 }
}

if($manifest){
 $entries=@($manifest.entries);$assetPaths=@(Get-ChildItem (Join-Path $identityDir 'assets'),(Join-Path $identityDir 'visual-boards') -File|ForEach-Object{Rel $_.FullName}|Sort-Object);$manifestPaths=@($entries.path|Sort-Object)
 if($validationState-ne'FINAL_FREEZE'){
  Check (($manifest.document.version-eq'producer-iteration-3-final')-and(@(Compare-Object $assetPaths $manifestPaths).Count-eq 0)-and((Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir 'asset-manifest.json')).Hash-eq'B6A3824C6751A69DACC746ABCB160CC92C5C7B0ED78720F3FDEE7166AF4FB3A4')) 'AUTHORIZED_D033_POST_SOURCE retains the pinned pre-refresh manifest and exact inventory.' 'AUTHORIZED_D033_POST_SOURCE manifest differs.'
 }else{
  $manifestHashBad=@($entries|Where-Object{(Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir $_.path)).Hash-ne$_.sha256})
  Check (($manifest.document.version-eq'd-034-contrast-completion')-and(@(Compare-Object $assetPaths $manifestPaths).Count-eq0)-and($manifestHashBad.Count-eq0)) 'FINAL_FREEZE manifest covers the exact current asset/source inventory with matching hashes.' 'FINAL_FREEZE manifest inventory or hashes differ.'
 }
 $manifestBad=@();foreach($e in $entries){foreach($field in @('id','path','name','creator','origin','format','dimensions','licenseStatus','clearance','evidenceStatus','permittedUse','sha256')){if([string]::IsNullOrWhiteSpace([string]$e.$field)){$manifestBad+="$($e.id):$field"}}}
 Check ($manifestBad.Count-eq 0) 'Every pinned pre-stabilization manifest record is structurally complete.' "Manifest errors: $($manifestBad-join', ')"
 Check (-not$manifest.document.thirdPartyAssetsIncluded-and-not$manifest.document.fontFilesIncluded-and-not$manifest.document.generatedImagesIncluded-and-not$manifest.document.protectedPrototypeAssetsIncluded) 'Manifest excludes third-party, font, generated, and protected prototype assets.' 'Manifest inclusion boundary failed.'
}

if($trace){
 $ids=@(1..28|ForEach-Object{'D-{0:D3}'-f$_})+@('CR-001');Check (($trace.Count-eq 29)-and(@(Compare-Object ($ids|Sort-Object) ($trace.decision_id|Sort-Object)).Count-eq 0)) 'Traceability covers D-001 through D-028 plus CR-001 exactly once.' 'Decision/change-request traceability mismatch.'
 $authorityBad=@();foreach($id in @('D-027','D-028','CR-001')){$row=@($trace|Where-Object{$_.decision_id-eq$id});if($row.Count-ne 1){$authorityBad+="${id}:row";continue};foreach($p in @($row[0].strategy_source-split';')){if([string]::IsNullOrWhiteSpace($p)-or-not(Test-Path -LiteralPath (Join-Path $repoRoot $p) -PathType Leaf)){$authorityBad+="${id}:$p"}}}
 $d027=@($trace|Where-Object{$_.decision_id-eq'D-027'});$cr001=@($trace|Where-Object{$_.decision_id-eq'CR-001'})
 Check (($authorityBad.Count-eq 0)-and($d027[0].strategy_source-match'docs/decisions-log\.md')-and($cr001[0].strategy_source-match'docs/requirements/CHANGE_REQUEST_CR-001\.md')) 'D-027, D-028, and CR-001 authority paths are exact and resolve to current local files.' "Trace authority path failure: $($authorityBad-join', ')"
}
$font=@(Get-ChildItem $identityDir -Recurse -File|Where-Object{$_.Extension-match'^\.(woff2?|ttf|otf|eot)$'});Check ($font.Count-eq 0) 'No font software is packaged.' "Font files found: $($font.Name-join', ')"
$producerText=@(Get-ChildItem $identityDir -Recurse -File|Where-Object{$_.Extension-in@('.md','.json','.csv','.html','.css','.svg','.ps1','.mjs')-and$_.FullName-notmatch'[\\/](reviews|accessibility)[\\/]'});$lint=@()
foreach($f in $producerText){$c=Get-Content -Raw $f.FullName;if($f.Name-ne'validate-brand-identity.ps1'-and$c-match'(?i)\b(?:TODO|TBD|FIXME|XXX|REPLACE_ME|LOREM IPSUM)\b'){$lint+="marker:$(Rel $f.FullName)"};if(-not$c.EndsWith("`n")){$lint+="newline:$(Rel $f.FullName)"};$n=0;foreach($line in Get-Content $f.FullName){$n++;if($line-match'[ \t]+$'){$lint+="space:$(Rel $f.FullName):$n"}}}
Check ($lint.Count-eq 0) 'Producer text has no draft markers, trailing whitespace, or missing final newlines.' "Text hygiene: $($lint-join', ')"
$browserNames='^(Cookies(?:-journal)?|History(?:-journal)?|Cache|Code Cache|GPUCache|Extensions|Local State|Singleton.*|Visited Links|Web Data(?:-journal)?)$';$residue=@(Get-ChildItem $identityDir -Recurse -Force|Where-Object{$_.Name-match$browserNames-or$_.FullName-match'[\\/]edge-profile[\\/]'});Check ($residue.Count-eq 0) 'No browser profile, cookie, history, cache, or lock residue remains.' "Browser residue: $($residue.FullName-join', ')"
$claims=@();foreach($f in $visualFiles){if((Get-Content -Raw $f)-match'(?i)world[- ]first|unrivalled|best[- ]in[- ]class|trusted by|award[- ]winning|global offices|proven client|leading provider'){$claims+=Rel $f}}
Check ($claims.Count-eq 0) 'Visual evidence contains no unsupported novelty, geography, client, or superiority claim.' "Unsupported claims: $($claims-join', ')"
Push-Location $repoRoot;try{$out=&git diff --check -- 'docs/phase-1-brand-identity' 2>&1;$code=$LASTEXITCODE;$status=@(&git status --short -- 'docs/phase-1-brand-identity')}finally{Pop-Location}
Check ($code-eq 0) 'Scoped git whitespace check passes.' "git diff --check failed: $($out-join'; ')";Check (@($status|Where-Object{$_-match'^[AMDRC][^?]'}).Count-eq 0) 'No identity artifact is staged.' 'Identity artifacts are staged.'

$passes|ForEach-Object{Write-Output "PASS: $_"}
if($failures.Count){$failures|ForEach-Object{Write-Output "FAIL: $_"};Write-Output "PASSES: $($passes.Count)";Write-Output "FAILURES: $($failures.Count)";Write-Output 'RESULT: FAIL';exit 1}
Write-Output "PASSES: $($passes.Count)";Write-Output 'FAILURES: 0';Write-Output 'RESULT: PASS'
