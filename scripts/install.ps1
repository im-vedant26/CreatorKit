$ErrorActionPreference = "Stop"

$AppName = "CreatorKit"
$CommandName = "creatorkit"
$RepoUrl = "https://github.com/im-vedant26/CreatorKit.git"
$InstallRoot = Join-Path $env:LOCALAPPDATA $AppName
$RepoDir = Join-Path $InstallRoot "app"
$BinDir = Join-Path $InstallRoot "bin"
$LauncherPath = Join-Path $BinDir "$CommandName.ps1"
$CmdLauncherPath = Join-Path $BinDir "$CommandName.cmd"

function Write-Step($Message) {
    Write-Host "[CreatorKit] $Message" -ForegroundColor Cyan
}

function Ensure-Command($Command, $InstallHint) {
    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        throw "$Command was not found. $InstallHint"
    }
}

Write-Host ""
Write-Host "CreatorKit Installer" -ForegroundColor Cyan
Write-Host "--------------------" -ForegroundColor DarkGray

Ensure-Command "python" "Install Python 3.10+ from https://www.python.org/downloads/ and enable 'Add Python to PATH'."
Ensure-Command "git" "Install Git from https://git-scm.com/downloads."

if (-not (Get-Command "ffmpeg" -ErrorAction SilentlyContinue)) {
    Write-Host "[CreatorKit] FFmpeg was not found on PATH. Some audio/video files may fail until FFmpeg is installed." -ForegroundColor Yellow
}

New-Item -ItemType Directory -Force -Path $InstallRoot, $BinDir | Out-Null

if (Test-Path $RepoDir) {
    Write-Step "Updating existing app files..."
    git -C $RepoDir pull --ff-only
}
else {
    Write-Step "Downloading CreatorKit..."
    git clone $RepoUrl $RepoDir
}

Write-Step "Creating Python environment..."
python -m venv (Join-Path $RepoDir "venv")

$PythonExe = Join-Path $RepoDir "venv\Scripts\python.exe"
Write-Step "Installing dependencies..."
& $PythonExe -m pip install --upgrade pip
& $PythonExe -m pip install -r (Join-Path $RepoDir "requirements.txt")

Write-Step "Creating launcher command..."
$Launcher = @"
`$ErrorActionPreference = "Stop"
`$AppDir = "$RepoDir"
& "`$AppDir\venv\Scripts\python.exe" "`$AppDir\main.py" @args
"@
Set-Content -Path $LauncherPath -Value $Launcher -Encoding UTF8

$CmdLauncher = @"
@echo off
"$RepoDir\venv\Scripts\python.exe" "$RepoDir\main.py" %*
"@
Set-Content -Path $CmdLauncherPath -Value $CmdLauncher -Encoding ASCII

$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if (($UserPath -split ";") -notcontains $BinDir) {
    Write-Step "Adding CreatorKit to your user PATH..."
    [Environment]::SetEnvironmentVariable("Path", "$UserPath;$BinDir", "User")
    $env:Path = "$env:Path;$BinDir"
}

Write-Host ""
Write-Host "CreatorKit installed successfully." -ForegroundColor Green
Write-Host "Start it anytime with:" -ForegroundColor White
Write-Host "  $CommandName" -ForegroundColor Yellow
Write-Host ""
Write-Host "If your current terminal does not recognize the command, open a new terminal and try again." -ForegroundColor DarkGray
