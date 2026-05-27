<div align="center">

# CreatorKit

**The creator-first terminal app for transcripts, captions, and content assets.**

Turn your audio and video into usable content — in seconds, from your terminal.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)]()
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://github.com/im-vedant26/CreatorKit)

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

Then just run:

```bash
creatorkit
```

</div>

---

## What CreatorKit does

You record a podcast. You film a YouTube video. You capture a lecture or an interview.

Now what?

CreatorKit takes that raw audio or video file — or a link — and turns it into the assets you actually need: a full transcript, subtitle files for your editor, caption files for your platform. All from your terminal, in a clean interactive menu. No scripts to write. No flags to memorize.

> **CreatorKit is built for YouTubers, podcasters, educators, short-form creators, and anyone who works with audio or video content.** You don't need to be a developer to use it.

---

## Terminal Preview

```
  ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ ██╗  ██╗██╗████████╗
 ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██║ ██╔╝██║╚══██╔══╝
 ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝█████╔╝ ██║   ██║
 ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗██╔═██╗ ██║   ██║
 ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║██║  ██╗██║   ██║
  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝

  Creator-first terminal app for transcripts, captions & content assets.

  ──────────────────────────────────────────────────
   [1]  Transcribe a local file
   [2]  Download & transcribe from a link
   [3]  Translate speech to English
   [4]  Export options (TXT / SRT / VTT / Creator Folder)
   [Q]  Quit
  ──────────────────────────────────────────────────

  > Select an option:
```

---

## Features

| Feature | Description |
|---|---|
| 🎙 **Transcribe local files** | Drop in any audio or video file and get a full transcript |
| 🔗 **Download from links** | Paste a supported URL — CreatorKit downloads and transcribes it |
| 🌐 **Translate to English** | Transcribe non-English audio directly into English |
| 📄 **Export TXT** | Clean transcript saved as a plain text file |
| 🎬 **Export SRT** | Subtitle file ready for your video editor |
| 📺 **Export VTT** | Caption file for YouTube, web players, and platforms |
| 📁 **Creator Folder** | Save TXT + SRT + VTT together in one organized output folder |
| ⏳ **Live activity indicator** | Real-time terminal feedback during transcription and download steps |

---

## Installation

### Windows — One Command

Open PowerShell and run:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

The installer handles everything. After it completes, you can run `creatorkit` from any terminal.

---

### Manual Install (Developers)

If you prefer to install manually or are on a non-Windows system:

**Requirements:**

- Python 3.10 or higher
- Git
- FFmpeg (must be on your system PATH)

**Steps:**

```bash
git clone https://github.com/im-vedant26/CreatorKit.git
cd CreatorKit
pip install -r requirements.txt
```

**Python dependencies:**

```
openai-whisper
torch
tqdm
colorama
pyfiglet
ffmpeg-python
yt-dlp
```

> **Note:** The one-command installer is currently Windows only. Manual install works on any platform where the dependencies are supported.

---

## Usage

After installing, open any terminal and run:

```bash
creatorkit
```

You'll see an interactive menu. No flags, no arguments required.

**From the menu you can:**

- Choose a local audio or video file to transcribe
- Paste a link to download and transcribe directly
- Select translate mode for non-English content
- Pick your export format — TXT, SRT, VTT, or the full Creator Folder

CreatorKit handles the rest. Your files land in an organized `outputs/` folder.

---

## Output Structure

Every transcription run creates a clean folder with your exports:

```
outputs/
└── my_video/
    ├── my_video_transcript.txt
    ├── my_video_captions.srt
    └── my_video_captions.vtt
```

---

## Roadmap

CreatorKit is actively evolving. Here's what's coming:

| Feature | Status |
|---|---|
| Clean transcript mode (filler words removed) | Planned |
| Batch processing (multiple files at once) | Planned |
| Summarization | Planned |
| YouTube description generator | Planned |
| Chapters & timestamp generation | Planned |
| Hook and title ideas | Planned |
| Short-form clip suggestions | Planned |
| Built-in update checker | Planned |

---

## Contributing

CreatorKit is open source and community contributions are welcome.

Whether you want to fix a bug, improve the CLI experience, add a new export format, or just clean up documentation — feel free to open an issue or pull request.

```bash
# Fork the repo, then:
git clone https://github.com/your-username/CreatorKit.git
cd CreatorKit
# Make your changes, then open a PR
```

If you're not sure where to start, browse [open issues](https://github.com/im-vedant26/CreatorKit/issues) or open a new one describing what you'd like to work on.

---

## License

MIT License. See [LICENSE](./LICENSE) for details.

---

<div align="center">

Built for creators. Open to everyone.

[GitHub](https://github.com/im-vedant26/CreatorKit) · [Report a Bug](https://github.com/im-vedant26/CreatorKit/issues) · [Request a Feature](https://github.com/im-vedant26/CreatorKit/issues)

</div>
