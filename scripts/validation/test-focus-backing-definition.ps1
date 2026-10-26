Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
function Assert-BackingContract([string]$Text) {
    $normalized = ($Text -replace '[*`]', '') -replace '\s+', ' '
    foreach ($clause in @('opaque backing', 'both sides of the complete', 'immediately adjacent', 'must not obscure', 'Native radios', 'D-054')) {
        if (-not $normalized.Contains($clause)) { throw "Missing backing safeguard: $clause" }
    }
}
$srs = Get-Content (Join-Path $root 'docs/active/Hengshi_Design_SRS_v3.md') -Raw
$row = [regex]::Match($srs, '(?m)^\| NFR-A11Y-005 \|(?<body>[^|]+)\|').Groups['body'].Value
Assert-BackingContract $row
foreach ($clause in @('both sides of the complete', 'must not obscure', 'Native radios')) {
    $rejected = $false
    try { Assert-BackingContract ($row.Replace($clause, 'REMOVED')) } catch { $rejected = $true }
    if (-not $rejected) { throw "Unsafe requirement mutation accepted: $clause" }
}
function Assert-FocusVisibility([string]$Text) {
    foreach ($clause in @('author-created content must not entirely hide it', 'Preserve stronger existing HUD/focus visibility safeguards')) {
        if (-not $Text.Contains($clause)) { throw "Missing visibility safeguard: $clause" }
    }
}
$visibility = [regex]::Match($srs, '(?m)^\| NFR-A11Y-008 \|(?<body>[^|]+)\|').Groups['body'].Value
Assert-FocusVisibility $visibility
$rejected = $false
try { Assert-FocusVisibility ($visibility.Replace('Preserve stronger existing HUD/focus visibility safeguards', '')) } catch { $rejected = $true }
if (-not $rejected) { throw 'Minimum requirement erased stronger HUD safeguards' }
$baseline = Get-Content (Join-Path $root 'docs/phase-1-ui-reference-design/DESIGN_SYSTEM_IMPLICATIONS.md') -Raw
if ($baseline -match 'an optional\s+WebGL layer' -or $baseline -notmatch 'S-SEMANTIC is a peer stream, not a verification mode') { throw 'Peer stream/context vocabulary regressed' }
Write-Output 'RESULT=PASS backed-focus definition; missing perimeter coverage, occlusion safeguard and native-radio separation rejected'
