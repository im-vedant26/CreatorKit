# AI Transcriber

Interactive CLI app to transcribe or translate audio/video using OpenAI Whisper.

## What It Does

- Transcribe local files (`.mp3`, `.mp4`, `.wav`, `.m4a`, `.mov`, `.avi`)
- Download audio from links using `yt-dlp` (YouTube/Instagram/etc.)
- Translate speech to English
- Export output as `.txt` or `.srt`

## Demo Flow

1. Choose input source (local file or URL).
2. Choose mode (`transcribe` or `translate`).
3. Choose Whisper model (`small`, `medium`, `large`).
4. Save result as TXT/SRT or skip.

## Requirements

- Python 3.10+
- `ffmpeg` installed and available in `PATH`

## Setup

```bash
git clone <your-repo-url>
cd ai_transcriber

python -m venv venv
```

Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Tests

Run unit tests:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

Run syntax checks:
```bash
python -m py_compile main.py transcriber.py utils.py
```

## Project Layout

```text
.
|- main.py
|- transcriber.py
|- utils.py
|- requirements.txt
|- tests/
|  |- test_transcriber.py
|- .github/workflows/ci.yml
|- README.md
|- CONTRIBUTING.md
|- LICENSE
```

## Troubleshooting

- `ModuleNotFoundError`: activate virtual env and reinstall deps.
- `ffmpeg not found`: install ffmpeg and verify `ffmpeg -version`.
- Tk dialogs fail to open: run from a desktop session with Tk support.
- URL download blocked: retry with browser cookies or `cookies.txt`.

## License

MIT. See [LICENSE](LICENSE).
