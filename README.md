<div align="center">

<img src="https://img.shields.io/badge/CreatorKit-v0.2-22D3EE?style=for-the-badge&labelColor=0F172A&color=22D3EE" alt="CreatorKit v0.2"/>

# `CreatorKit`

**The creator-first terminal app for transcripts, captions, and content assets.**

Turn audio and video into creator-ready assets from a clean interactive terminal.

[![MIT License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square&labelColor=0F172A)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-22D3EE?style=flat-square&labelColor=0F172A)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-94A3B8?style=flat-square&labelColor=0F172A)]()
[![Open Source](https://img.shields.io/badge/Open-Source-22C55E?style=flat-square&labelColor=0F172A)](https://github.com/im-vedant26/CreatorKit)

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

```bash
creatorkit
```

<sub>Install once. Run from any terminal.</sub>

</div>

---

## Terminal Preview

```text
+----------------------------------------------------------------------------------+
|                                   CreatorKit                                      |
+----------------------------------------------------------------------------------+
|  Turn audio and video into transcripts, captions, and creator-ready assets.       |
|  Creator-first CLI for videos, podcasts, reels, and subtitles                     |
+----------------------------------------------------------------------------------+

  Input
  ------------------------------------------------------------
  [1] Upload from your device     audio or video file
  [2] Paste a video link          YouTube, Instagram, and more
  [3] Exit                        close the app

  > Enter your choice [1/2/3]:

  Processing
  ------------------------------------------------------------
  / Transcribing audio  building transcript | 42s elapsed
```

> CreatorKit is terminal-based, but designed to feel like an app: focused menus, clear progress, and exports creators actually use.

---

## What CreatorKit Does

You record a podcast. You film a tutorial. You capture an interview, class, reel, or long-form video.

CreatorKit takes that raw file, or a supported link, and turns it into assets you can use immediately: transcripts, subtitles, captions, and organized output files. No flags to memorize. No Python knowledge required after installation.

Built for **YouTubers, podcasters, educators, short-form creators, video editors, and anyone working with audio or video content.**

---

## Features

| Code | Feature | What it does |
|---|---|---|
| `TRN` | **Transcribe local files** | Select audio or video from your device and generate a transcript. |
| `DL` | **Download from links** | Paste a supported URL and CreatorKit downloads the best available audio. |
| `EN` | **Translate to English** | Use Whisper translate mode for non-English speech. |
| `TXT` | **Export transcript** | Save the spoken content as a plain text file. |
| `SRT` | **Export subtitles** | Save subtitle files for editors and platforms. |
| `VTT` | **Export captions** | Save WebVTT captions for YouTube and web players. |
| `PKG` | **Creator Folder** | Save TXT, SRT, and VTT together in one organized output folder. |
| `...` | **Live activity** | See elapsed time and activity while long tasks are running. |

---

## Installation

### Windows - One Command

Open PowerShell and run:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

After installation, open a new terminal and run:

```bash
creatorkit
```

The installer downloads CreatorKit directly, creates an isolated Python environment, and tries to install a supported 64-bit Python 3.12 and FFmpeg automatically on fresh Windows laptops when `winget` is available.

If you need to remove CreatorKit later, run:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/uninstall.ps1 | iex
```

Running the installer again also repairs an existing CreatorKit install.

### Updating CreatorKit

CreatorKit checks for updates when it starts. If a newer version is available, the app will ask before running the official updater.

Users who installed an older version before the update checker was added should run the installer command once to receive the updater.

You can also update or repair CreatorKit manually anytime by rerunning the same installer command:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

After an update finishes, restart CreatorKit:

```bash
creatorkit
```

### Manual Install

Use this if you prefer to install manually on Windows or want to control the steps yourself.

Prerequisites:

```text
Python 3.10+   Git   FFmpeg on PATH
```

Setup:

```bash
git clone https://github.com/im-vedant26/CreatorKit.git
cd CreatorKit
python -m venv venv
pip install -r requirements.txt
python main.py
```

<details>
<summary>Python dependencies</summary>

```text
openai-whisper
torch
tqdm
colorama
pyfiglet
ffmpeg-python
yt-dlp
```

</details>

> The one-command installer is Windows-only for now.

---

## Usage

```bash
creatorkit
```

CreatorKit opens an interactive menu. No arguments or flags are required.

From there, you can:

```text
[1] Choose a local audio or video file
[2] Paste a supported link for download and transcription
[3] Select transcription or English translation mode
[4] Export as TXT, SRT, VTT, or a complete Creator Folder
```

### Link Download Notes

CreatorKit uses `yt-dlp` for online links. Some providers, including YouTube and Instagram, may block anonymous downloads, reset the connection, require login cookies, or change their page format.

If a link fails:

```text
1. Open the link in Chrome, Edge, or Firefox and make sure it plays there.
2. Retry in CreatorKit using browser cookies.
3. If needed, update CreatorKit by running the installer command again.
```

When a provider blocks direct access, uploading the audio/video file from your device still works.

---

## Output

The Creator Folder export creates an organized package:

```text
outputs/
  my_video/
    my_video_transcript.txt
    my_video_captions.srt
    my_video_captions.vtt
```

---

## Roadmap

| Feature | Status |
|---|---|
| Clean transcript mode | `planned` |
| Batch processing | `planned` |
| Summaries | `planned` |
| YouTube description generator | `planned` |
| Chapters and timestamp generation | `planned` |
| Hook and title suggestions | `planned` |
| Short-form clip suggestions | `planned` |
| Built-in update checker | `shipped` |

---

## Contributing

CreatorKit is open source. Contributions are welcome, whether it is a bug fix, new export format, UX improvement, testing help, or documentation.

```bash
git clone https://github.com/your-username/CreatorKit.git
cd CreatorKit
```

Not sure where to start? Browse [open issues](https://github.com/im-vedant26/CreatorKit/issues) or open one describing what you would like to work on.

---

## License

MIT. See [LICENSE](./LICENSE) for details.

---

<div align="center">

<sub>
  <a href="https://github.com/im-vedant26/CreatorKit">GitHub</a> |
  <a href="https://github.com/im-vedant26/CreatorKit/issues">Report a Bug</a> |
  <a href="https://github.com/im-vedant26/CreatorKit/issues">Request a Feature</a>
</sub>

<br/><br/>

<img src="https://img.shields.io/badge/Built%20for%20creators-22D3EE?style=flat-square&labelColor=0F172A" alt="Built for creators"/>

</div>
