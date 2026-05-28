$ErrorActionPreference = "Stop"

$AppName = "CreatorKit"
$CommandName = "creatorkit"
$RepoUrl = "https://github.com/im-vedant26/CreatorKit.git"
$InstallRoot = Join-Path $env:LOCALAPPDATA $AppName
$RepoDir = Join-Path $InstallRoot "app"
$BinDir = Join-Path $InstallRoot "bin"
$LogDir = Join-Path $InstallRoot "logs"
$LauncherPath = Join-Path $BinDir "$CommandName.ps1"
$CmdLauncherPath = Join-Path $BinDir "$CommandName.cmd"
$script:InstallerErrorShown = $false

function Write-Step($Message, $Color = "Cyan") {
    Write-Host "  $Message" -ForegroundColor $Color
}

function Ensure-Command($Command, $InstallHint) {
    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        throw "$Command was not found. $InstallHint"
    }
}

function Invoke-QuietStep($Message, [scriptblock]$Action) {
    Write-Host "  $Message..." -NoNewline -ForegroundColor Cyan

    $SafeName = ($Message -replace "[^a-zA-Z0-9]+", "-").Trim("-").ToLower()
    $LogPath = Join-Path $LogDir "$SafeName.log"

    try {
        $global:LASTEXITCODE = 0
        & $Action *> $LogPath

        if ($LASTEXITCODE -ne 0) {
            throw "Command failed with exit code $LASTEXITCODE."
        }

        Write-Host " done" -ForegroundColor Green
    }
    catch {
        Write-Host " failed" -ForegroundColor Red
        Write-Host ""
        Write-Host "CreatorKit setup could not finish." -ForegroundColor Red
        Write-Host "Please try running the install command again." -ForegroundColor White
        Write-Host ""
        Write-Host "If it still fails, send this log file for help:" -ForegroundColor Yellow
        Write-Host "  $LogPath" -ForegroundColor DarkGray

        $script:InstallerErrorShown = $true
        throw
    }
}

try {
Write-Host ""
Write-Host "CreatorKit Setup" -ForegroundColor Cyan
Write-Host "----------------" -ForegroundColor DarkGray
Write-Host "This may take a few minutes the first time. You can keep this window open." -ForegroundColor DarkGray
Write-Host ""

Ensure-Command "python" "Install Python 3.10+ from https://www.python.org/downloads/ and enable 'Add Python to PATH'."
Ensure-Command "git" "Install Git from https://git-scm.com/downloads."

if (-not (Get-Command "ffmpeg" -ErrorAction SilentlyContinue)) {
    Write-Host "  FFmpeg was not found. Some audio/video files may need FFmpeg later." -ForegroundColor Yellow
    Write-Host ""
}

New-Item -ItemType Directory -Force -Path $InstallRoot, $BinDir, $LogDir | Out-Null

if (Test-Path $RepoDir) {
    if (Test-Path (Join-Path $RepoDir ".git")) {
        Invoke-QuietStep "Preparing app files" {
            git -C $RepoDir pull --ff-only
        }
    }
    else {
        Invoke-QuietStep "Preparing app files" {
            Remove-Item -LiteralPath $RepoDir -Recurse -Force
            git clone --quiet $RepoUrl $RepoDir
        }
    }
}
else {
    Invoke-QuietStep "Preparing app files" {
        git clone --quiet $RepoUrl $RepoDir
    }
}

Invoke-QuietStep "Creating app environment" {
    python -m venv (Join-Path $RepoDir "venv")
}

$PythonExe = Join-Path $RepoDir "venv\Scripts\python.exe"
Invoke-QuietStep "Preparing app engine" {
    & $PythonExe -m pip install --upgrade pip --quiet --disable-pip-version-check --progress-bar off
}
Invoke-QuietStep "Installing app engine" {
    & $PythonExe -m pip install -r (Join-Path $RepoDir "requirements.txt") --quiet --disable-pip-version-check --progress-bar off
}

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
Write-Host "CreatorKit is ready." -ForegroundColor Green
Write-Host "Start it anytime by typing:" -ForegroundColor White
Write-Host "  $CommandName" -ForegroundColor Yellow
Write-Host ""
Write-Host "If your current terminal does not recognize the command, open a new terminal and try again." -ForegroundColor DarkGray
}
catch {
    if (-not $script:InstallerErrorShown) {
        Write-Host ""
        Write-Host "CreatorKit setup could not finish." -ForegroundColor Red
        Write-Host "Please check that Python and Git are installed, then try again." -ForegroundColor White
    }
}
