$ErrorActionPreference = 'Stop'
$identityDir = Split-Path -Parent $PSScriptRoot
function PngDimensions([string]$path) {
    $b=[IO.File]::ReadAllBytes($path)
    $w=[BitConverter]::ToUInt32([byte[]]($b[19],$b[18],$b[17],$b[16]),0)
    $h=[BitConverter]::ToUInt32([byte[]]($b[23],$b[22],$b[21],$b[20]),0)
    "$w`x$h"
}
$files=@(Get-ChildItem (Join-Path $identityDir 'assets'),(Join-Path $identityDir 'visual-boards') -File|Sort-Object FullName)
$entries=@();$i=0
foreach($file in $files){
    $i++;$relative=[IO.Path]::GetRelativePath($identityDir,$file.FullName).Replace('\','/')
    $format=switch($file.Extension.ToLower()){'.svg'{'image/svg+xml'}'.png'{'image/png'}'.html'{'text/html'}'.css'{'text/css'}default{'application/octet-stream'}}
    $dimensions=switch($file.Extension.ToLower()){'.png'{PngDimensions $file.FullName}'.svg'{[xml]$x=Get-Content -Raw $file.FullName;"$($x.svg.width)x$($x.svg.height); viewBox $($x.svg.viewBox)"}'.html'{'responsive semantic document'}'.css'{'responsive stylesheet'}default{'not applicable'}}
    $isMark=$file.Name-match'^(logo|monogram|mark|favicon)'
    $isCapture=$file.Extension-eq'.png'
    $entries+=[ordered]@{
        id=('ASSET-{0:D3}'-f$i)
        path=$relative
        name=($file.BaseName -replace'-',' ')
        creator='Hengshi Phase 1 identity producer'
        origin=if($isCapture){'Local Playwright capture of project-authored D-034 contrast completion; no network request permitted'}else{'Original hand-authored project-local specimen implementing D-026/D-027, bounded D-028 correction, D-029 stabilization, and D-034 contrast completion'}
        format=$format
        dimensions=$dimensions
        licenseStatus='Project-original internal review asset; no public production license assigned'
        clearance=if($isMark){'UNREGISTERED — TRADEMARK NOT CLEARED'}else{'Not trademark clearance evidence; internal review only'}
        evidenceStatus='exploratory_identity_not_approved'
        permittedUse='Local founder comparison and independent design/accessibility review only'
        sha256=(Get-FileHash -Algorithm SHA256 $file.FullName).Hash
    }
}
$manifest=[ordered]@{
    schemaVersion=1
    document=[ordered]@{
        title='Hengshi Design Phase 1 brand identity asset manifest'
        version='d-034-contrast-completion'
        date='2026-07-20'
        status='internal_review_only'
        defaultCreator='Hengshi Phase 1 identity producer'
        defaultOrigin='Original hand-authored project-local specimen implementing D-026/D-027, bounded D-028 correction, D-029 stabilization, and D-034 contrast completion'
        defaultLicenseStatus='Project-original internal review asset; public production license and ownership terms not assigned by this package'
        defaultClearance='UNREGISTERED — TRADEMARK NOT CLEARED'
        thirdPartyAssetsIncluded=$false
        fontFilesIncluded=$false
        generatedImagesIncluded=$false
        protectedPrototypeAssetsIncluded=$false
    }
    entries=$entries
}
$json=$manifest|ConvertTo-Json -Depth 8
[IO.File]::WriteAllText((Join-Path $identityDir 'asset-manifest.json'),$json+"`n",[Text.UTF8Encoding]::new($false))
Write-Output "Updated asset manifest with $($entries.Count) records."
