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

$required=@(
 'README.md','01-identity-principles.md','02-visual-directions.md','03-logo-system.md','04-color-and-typography.md','05-imagery-iconography-and-data.md','06-motion-sound-and-3d.md','07-accessibility-seo-and-applications.md','BRAND_IDENTITY.md','geometry-spec.json','semantic-tokens.json','asset-manifest.json','traceability.csv','handoff.md','producer-inspection.md',
 'visual-boards/index.html','visual-boards/identity-board.css','visual-boards/scale-evidence.html',
 'assets/logo-framework-relay-primary.svg','assets/logo-framework-relay-light.svg','assets/logo-framework-relay-mono.svg','assets/logo-framework-relay-reverse.svg','assets/mark-framework-relay.svg','assets/mark-framework-relay-small.svg','assets/favicon-framework-relay.svg','assets/current-hybrid-framework-relay.svg','assets/logo-quiet-framework.svg','assets/logo-resonant-field.svg','assets/direction-a-signal-ledger.svg','assets/direction-b-quiet-framework.svg','assets/direction-c-resonant-field.svg','assets/icon-data-specimen.svg','assets/og-evidence-in-motion.svg',
 'assets/identity-board-preview.png','assets/identity-board-wide.png','assets/identity-board-medium.png','assets/identity-board-narrow.png','assets/identity-board-forced-colors.png','assets/identity-board-grayscale.png','assets/identity-board-print.png','assets/identity-scale-evidence.png',
 'archive/iteration-2-signal-ledger-logo/README.md','archive/iteration-2-signal-ledger-logo/baseline-inventory.json','archive/iteration-2-signal-ledger-logo/geometry-spec.json',
 'validation/capture-identity-evidence.mjs','validation/audit-identity-board.mjs','validation/browser-audit-report.json','validation/validation-report.md','validation/update-asset-manifest.ps1','validation/validate-brand-identity.ps1',
 'reviews/design-review-iteration-1.md','reviews/design-review-iteration-2.md','accessibility/accessibility-audit-iteration-1.md','accessibility/accessibility-audit-iteration-2.md'
)
$missing=@($required|Where-Object{-not(Test-Path -LiteralPath (Join-Path $identityDir $_) -PathType Leaf)})
Check ($missing.Count-eq 0) 'All final producer deliverables, frozen reports, and archive files exist.' "Missing: $($missing-join', ')"

# The four prior independent reports are immutable. Only exact iteration-3 names may follow.
$reviewHashes=@{
 'reviews/design-review-iteration-1.md'='12014D5772250EF8B2BA07B911D833B4F53C4CA880961BA55F5B4DCF07CE78DD'
 'accessibility/accessibility-audit-iteration-1.md'='532779730294F74716D85115514E3EAA749FF9FAA6EEE48B20CFECF2BEED70D2'
 'reviews/design-review-iteration-2.md'='490A4391327D476014CC1B758EDFDDF66DE4C8A03628BE116659E5ADA272D895'
 'accessibility/accessibility-audit-iteration-2.md'='FD06D3500F797A2148B7432C6AB2F7F6CF613D71732710BCBE54E65C8761B519'
}
$optionalI3=@('reviews/design-review-iteration-3.md','accessibility/accessibility-audit-iteration-3.md')
$actualReports=@(Get-ChildItem (Join-Path $identityDir 'reviews'),(Join-Path $identityDir 'accessibility') -Recurse -File|ForEach-Object{Rel $_.FullName}|Sort-Object)
$allowedReports=@($reviewHashes.Keys)+$optionalI3
$unexpectedReports=@($actualReports|Where-Object{$_-notin$allowedReports});$missingReports=@($reviewHashes.Keys|Where-Object{$_-notin$actualReports})
Check (($unexpectedReports.Count-eq 0)-and($missingReports.Count-eq 0)) 'Reviewer destinations contain four frozen reports and only exact optional iteration-3 filenames.' "Reviewer allowlist failure: unexpected=$($unexpectedReports-join', '); missing=$($missingReports-join', ')"
$hashBad=@();foreach($p in $reviewHashes.Keys){if((Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $identityDir $p)).Hash-ne$reviewHashes[$p]){$hashBad+=$p}}
Check ($hashBad.Count-eq 0) 'All four prior independent reports remain byte-for-byte unchanged.' "Prior report hash mismatch: $($hashBad-join', ')"
$optionalBad=@();foreach($p in $optionalI3){if(Test-Path -LiteralPath (Join-Path $identityDir $p)){ $c=Text $p;if($c-notmatch'(?i)iteration\s*3'-or$c-notmatch'(?im)^#{1,3}\s+.*(?:review|audit)'-or$c-notmatch'(?im)^\*\*Verdict:\*\*\s*(?:PASS|REVISE|BLOCKED)\b'){$optionalBad+=$p}}}
Check ($optionalBad.Count-eq 0) 'Any optional iteration-3 report has deterministic identity, heading, and verdict structure.' "Optional iteration-3 report invalid: $($optionalBad-join', ')"

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

if($tokens){
 Check (($tokens.document.version-eq'producer-iteration-3-final')-and($tokens.identityReconciliation.currentCandidate.name-eq'Framework Relay')-and($tokens.identityReconciliation.supersededLogo.status-eq'founder_rejected_archived_not_current')) 'Semantic tokens identify the final current hybrid and superseded logo.' 'Identity reconciliation token semantics drifted.'
 $requiredColors=@('#0B0F14','#161D26','#2A3542','#D8D3C8','#F3F1EA','#FAF9F6','#FFFFFF','#000000','#00D4FF','#FFB000','#B6F36B','#A98CFF','#006D82','#8A5600','#4F7D18','#6D52B5')
 $tokenText=Text 'semantic-tokens.json';$docText=Text '04-color-and-typography.md';$css=Text 'visual-boards/identity-board.css';$colorBad=@()
 foreach($h in $requiredColors|Where-Object{$_-ne'#000000'}){if($tokenText-notmatch[regex]::Escape($h)){$colorBad+="tokens:$h"};if($docText-notmatch[regex]::Escape($h)){$colorBad+="doc:$h"};if($css-notmatch[regex]::Escape($h.ToLower())){$colorBad+="css:$h"}}
 Check ($colorBad.Count-eq 0) 'All dark- and light-surface colors close across docs, tokens, and CSS.' "Color closure gaps: $($colorBad-join', ')"
 $contrastBad=@();foreach($p in @($tokens.declaredContrastPairings)){$actual=Contrast $p.foreground $p.background;if([Math]::Abs($actual-[double]$p.expectedRatio)-gt .01-or$actual-lt[double]$p.minimum){$contrastBad+="$($p.foreground)/$($p.background)"}}
 Check ($contrastBad.Count-eq 0) 'Every declared contrast ratio recomputes and meets its threshold.' "Contrast mismatch: $($contrastBad-join'; ')"
}

# Evidence-state grammar and separate direct-labelled data series close R-020.
$grammar=[ordered]@{verified=@('filled-circle','solid','none');demo=@('open-diamond','dash-dot','10 4 2 4');proposed=@('filled-square','short-dash','8 6');conditional=@('filled-triangle','long-dash','16 7');unavailable=@('filled-bar','dotted','2 7');error=@('open-octagon','double-solid','none')}
$html=Text 'visual-boards/index.html';$icon=Text 'assets/icon-data-specimen.svg';$grammarBad=@()
if($tokens){foreach($k in $grammar.Keys){$e=$tokens.evidenceState.$k;$g=$grammar[$k];if($e.marker-ne$g[0]-or$e.line-ne$g[1]-or$e.dashArray-ne$g[2]){$grammarBad+="tokens:$k"};$needle='data-state="{0}" data-marker="{1}" data-line="{2}"' -f $k,$g[0],$g[1];if($html-notmatch[regex]::Escape($needle)){$grammarBad+="html:$k"};if($icon-notmatch[regex]::Escape($g[0].Replace('-',' '))){$grammarBad+="svg:$k"}}}
Check ($grammarBad.Count-eq 0) 'Six-state marker/line grammar is exact in JSON, HTML, and SVG accessible text.' "Evidence grammar mismatch: $($grammarBad-join', ')"
$series=[ordered]@{'Context baseline'='1 5 9 5';'Dependency map'='12 3 3 3 3 3';'Decision frame'='solid';'Evidence depth'='5 5';'Risk view'='13 4 4 4'};$seriesBad=@()
foreach($name in $series.Keys){if($icon-notmatch[regex]::Escape($name)){$seriesBad+="svg-label:$name"};if($html-notmatch[regex]::Escape($name)){$seriesBad+="html-label:$name"};if($series[$name]-ne'solid'-and$icon-notmatch[regex]::Escape('stroke-dasharray="'+$series[$name]+'"')){$seriesBad+="svg-pattern:$name"}}
Check ($seriesBad.Count-eq 0) 'Five illustrative series are directly labelled with distinct patterns in visible and semantic evidence.' "Direct-label closure mismatch: $($seriesBad-join', ')"
Check (($html-match'closes R-020')-and((Text '05-imagery-iconography-and-data.md')-match'closes R-020')-and((Text 'BRAND_IDENTITY.md')-match'closes R-020')) 'R-020 closure is explicit in board, specialist guide, and consolidated guidance.' 'R-020 closure statement missing.'
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
Check ($pngBad.Count-eq 0) 'All eight wide, medium, narrow, mode, print, preview, and scale PNGs are valid.' "PNG evidence invalid: $($pngBad-join', ')"
if($browserAudit){$incomplete=@($browserAudit.checks|ForEach-Object{@($_.incomplete)});Check (($browserAudit.iteration-eq 3)-and($browserAudit.totalViolations-eq 0)-and($incomplete.Count-eq 0)-and$browserAudit.temporaryProfileRemoved) 'Iteration-3 automated audit reports zero violations, zero incomplete checks, and profile cleanup.' "Browser audit not clean or current: iteration=$($browserAudit.iteration), violations=$($browserAudit.totalViolations), incomplete=$($incomplete.Count), cleanup=$($browserAudit.temporaryProfileRemoved)"}

if($manifest){
 $entries=@($manifest.entries);$assetPaths=@(Get-ChildItem (Join-Path $identityDir 'assets'),(Join-Path $identityDir 'visual-boards') -File|ForEach-Object{Rel $_.FullName}|Sort-Object);$manifestPaths=@($entries.path|Sort-Object)
 Check (($manifest.document.version-eq'producer-iteration-3-final')-and(@(Compare-Object $assetPaths $manifestPaths).Count-eq 0)) 'Final manifest covers each current asset and visual-board source exactly once.' 'Manifest version or inventory differs from current filesystem.'
 $manifestBad=@();foreach($e in $entries){foreach($field in @('id','path','name','creator','origin','format','dimensions','licenseStatus','clearance','evidenceStatus','permittedUse','sha256')){if([string]::IsNullOrWhiteSpace([string]$e.$field)){$manifestBad+="$($e.id):$field"}};$p=Join-Path $identityDir $e.path;if((Get-FileHash -Algorithm SHA256 $p).Hash-ne$e.sha256){$manifestBad+="$($e.path):hash"}}
 Check ($manifestBad.Count-eq 0) 'Every current manifest record is complete and every checksum matches.' "Manifest errors: $($manifestBad-join', ')"
 Check (-not$manifest.document.thirdPartyAssetsIncluded-and-not$manifest.document.fontFilesIncluded-and-not$manifest.document.generatedImagesIncluded-and-not$manifest.document.protectedPrototypeAssetsIncluded) 'Manifest excludes third-party, font, generated, and protected prototype assets.' 'Manifest inclusion boundary failed.'
}

if($trace){$ids=@(1..27|ForEach-Object{'D-{0:D3}'-f$_})+@('CR-001');Check (($trace.Count-eq 28)-and(@(Compare-Object ($ids|Sort-Object) ($trace.decision_id|Sort-Object)).Count-eq 0)) 'Traceability covers D-001 through D-027 plus CR-001 exactly once.' 'Decision/change-request traceability mismatch.'}
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
