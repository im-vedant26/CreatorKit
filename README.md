# AI Transcriber

Interactive CLI app to transcribe or translate audio/video using OpenAI Whisper.

## Table of Contents

- [What It Does](#what-it-does)
- [Prerequisites](#prerequisites)
- [Quick Start (5-10 Minutes)](#quick-start-5-10-minutes)
- [Verify Setup](#verify-setup)
- [Run](#run)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## What It Does

- Transcribe local files (`.mp3`, `.mp4`, `.wav`, `.m4a`, `.mov`, `.avi`)
- Download audio from links using `yt-dlp` (YouTube/Instagram/etc.)
- Translate speech to English
- Export output as `.txt` or `.srt`

## Prerequisites

- Python 3.10 or newer
- `ffmpeg` installed and available in your system `PATH`
- A terminal (PowerShell, Command Prompt, Terminal, or Bash)

Check Python:

```bash
python --version
```

Install `ffmpeg`:

Windows (PowerShell with `winget`):

```powershell
winget install --id Gyan.FFmpeg -e
ffmpeg -version
```

Windows (PowerShell with `choco`):

```powershell
choco install ffmpeg -y
ffmpeg -version
```

macOS (Homebrew):

```bash
brew install ffmpeg
ffmpeg -version
```

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y ffmpeg
ffmpeg -version
```

## Quick Start (5-10 Minutes)

1. Clone and enter the repository.

```bash
git clone <your-repo-url>
cd ai_transcriber
```

2. Create a virtual environment.

```bash
python -m venv venv
```

3. Activate the virtual environment.

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

Windows (Command Prompt):

```bat
venv\Scripts\activate.bat
```

macOS/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

## Verify Setup

Run these checks before first use.

1. Confirm your virtual environment is active.

Windows (PowerShell/CMD expected):

```bash
where python
```

macOS/Linux expected:

```bash
which python
```

Expected: Python path should point to `venv`.

2. Dependency import smoke check.

```bash
python -c "import pyfiglet, colorama, yt_dlp, whisper, torch; print('imports_ok')"
```

Expected output:

```text
imports_ok
```

3. Run unit tests.

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Expected output includes:

```text
Ran 2 tests
OK
```

4. Optional syntax check.

```bash
python -m py_compile main.py transcriber.py utils.py
```

Expected: no output means success.

## Run

Start the app:

```bash
python main.py
```

Expected: you should see the `AI Transcriber` banner and interactive menu.

## Troubleshooting

If you see `ModuleNotFoundError`:

```bash
# ensure venv is active, then reinstall
pip install -r requirements.txt
```

If `ffmpeg` is missing (`ffmpeg not found`):

```bash
ffmpeg -version
```

If command fails, install `ffmpeg` using the platform commands in [Prerequisites](#prerequisites), then restart your terminal.

If Tk file dialog does not open or shows `tkinter`/`TclError` issues:

- Run from a desktop session (not a headless/remote shell without GUI).
- Try manual direct run from terminal:

```bash
python main.py
```

If PowerShell blocks venv activation (`running scripts is disabled`):

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

## License

MIT. See [LICENSE](LICENSE).
