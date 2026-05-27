# CreatorKit

CreatorKit is a creator-first CLI app for turning audio and video into transcripts, captions, and creator-ready assets.

Current features:

- Transcribe local audio/video files with Whisper.
- Download audio from supported links through `yt-dlp`.
- Export plain text transcripts.
- Export SRT subtitle files.
- Export WebVTT caption files.
- Save a complete creator project folder with TXT, SRT, and VTT together.
- Show live activity while long transcription/download tasks are running.

## Run Locally

```powershell
.\venv\Scripts\Activate.ps1
python main.py
```

## One-command Install

Windows users can install with:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

Then start CreatorKit with:

```powershell
creatorkit
```

## Requirements

- Python 3.10+
- Git
- FFmpeg available on PATH

Whisper and Torch are installed from `requirements.txt` during setup.

## Roadmap

- Cleaner transcript mode.
- Batch processing.
- YouTube descriptions.
- Summaries.
- Chapters and timestamps.
- Hook/title ideas.
- Short-form clip suggestions.
- Built-in update checks.
