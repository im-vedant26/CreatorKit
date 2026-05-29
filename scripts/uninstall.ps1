$ErrorActionPreference = "Stop"

$AppName = "CreatorKit"
$CommandName = "creatorkit"
$InstallRoot = Join-Path $env:LOCALAPPDATA $AppName
$BinDir = Join-Path $InstallRoot "bin"

function Write-Step($Message, $Color = "Cyan") {
    Write-Host "  $Message" -ForegroundColor $Color
}

function Assert-UnderPath($ChildPath, $ParentPath) {
    $ResolvedChild = [System.IO.Path]::GetFullPath($ChildPath)
    $ResolvedParent = [System.IO.Path]::GetFullPath($ParentPath)

    if (-not $ResolvedChild.StartsWith($ResolvedParent, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to remove path outside the CreatorKit install root."
    }
}

Write-Host ""
Write-Host "CreatorKit Uninstall" -ForegroundColor Cyan
Write-Host "--------------------" -ForegroundColor DarkGray
Write-Host ""

if (-not (Test-Path $InstallRoot)) {
    Write-Host "CreatorKit is not installed in the expected location." -ForegroundColor Yellow
    return
}

Assert-UnderPath $InstallRoot $env:LOCALAPPDATA

$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($UserPath) {
    $UpdatedPath = (($UserPath -split ";") | Where-Object { $_ -and $_.TrimEnd("\") -ne $BinDir.TrimEnd("\") }) -join ";"
    [Environment]::SetEnvironmentVariable("Path", $UpdatedPath, "User")
    $MachinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $env:Path = @($MachinePath, $UpdatedPath) -join ";"
}

Write-Step "Removing CreatorKit files..."
Remove-Item -LiteralPath $InstallRoot -Recurse -Force

Write-Host ""
Write-Host "CreatorKit has been removed." -ForegroundColor Green
Write-Host "Open a new terminal if you want PATH changes to refresh immediately." -ForegroundColor DarkGray
