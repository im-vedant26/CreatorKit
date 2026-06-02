<div align="center">

<img src="https://img.shields.io/badge/CreatorKit-v0.4.0-22D3EE?style=for-the-badge&labelColor=0F172A&color=22D3EE" alt="CreatorKit v0.4.0"/>

# `CreatorKit`

**The creator-first terminal app for transcripts, captions, and content assets.**

Turn audio and video into creator-ready assets from a clean interactive terminal.

[![MIT License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square&labelColor=0F172A)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-22D3EE?style=flat-square&labelColor=0F172A)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%2B%20macOS-94A3B8?style=flat-square&labelColor=0F172A)]()
[![Open Source](https://img.shields.io/badge/Open-Source-22C55E?style=flat-square&labelColor=0F172A)](https://github.com/im-vedant26/CreatorKit)

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

```bash
curl -fsSL https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.sh | bash
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
  [2] Paste a media link          Instagram and other supported sites
  [3] Paste transcript            use text or captions you can legally use
  [4] Exit                        close the app

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
| `TXTIN` | **Paste transcript** | Use transcript text or captions you have permission to process. |
| `EN` | **Translate to English** | Use Whisper translate mode for non-English speech. |
| `TXT` | **Export transcript** | Save the spoken content as a plain text file. |
| `SRT` | **Export subtitles** | Save subtitle files for editors and platforms. |
| `VTT` | **Export captions** | Save WebVTT captions for YouTube and web players. |
| `AST` | **Creator Assets** | Generate clean transcript, chapters, description draft, and caption snippets. |
| `PKG` | **Creator Package** | Save the full Creator Launch Pack in one organized folder. |
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

The installer downloads CreatorKit, creates an isolated Python environment, installs the app dependencies, and creates the `creatorkit` launcher. Python 3.10+ and Git should already be installed. FFmpeg is recommended for audio/video handling.

If you need to remove CreatorKit later, run:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/uninstall.ps1 | iex
```

Running the installer again also repairs an existing CreatorKit install.

### macOS - One Command

Open Terminal and run:

```bash
curl -fsSL https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.sh | bash
```

After installation, open a new terminal and run:

```bash
creatorkit
```

The macOS installer creates a local app environment under `~/.creatorkit`, installs the Python dependencies, and creates a `creatorkit` launcher in `~/.local/bin`.

FFmpeg is required for many audio/video formats. If FFmpeg is missing, install it with Homebrew:

```bash
brew install ffmpeg
```

### Updating CreatorKit

CreatorKit checks for updates when it starts. If a newer version is available, the app will ask before running the official updater.

Users who installed an older version before the update checker was added should run the installer command once to receive the updater.

You can also update or repair CreatorKit manually anytime by rerunning the same installer command:

Windows:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.sh | bash
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

> Linux support is planned for the next platform update.

---

## Usage

```bash
creatorkit
```

CreatorKit opens an interactive menu. No arguments or flags are required.

From there, you can:

```text
[1] Choose a local audio or video file
[2] Paste a supported media link for download and transcription
[3] Paste transcript text or captions when media download is blocked
[4] Select transcription or English translation mode
[5] Export as TXT, SRT, VTT, Creator Assets, or a complete Creator Package
```

### Creator Assets

CreatorKit can turn a transcript into local first-draft publishing assets:

```text
Clean transcript
Chapter timestamps
YouTube description draft
Caption snippets
```

These assets are generated locally from the transcript and timestamps. No API key is required.

### Creator Package

The Creator Package is the full Creator Launch Pack: transcript, captions when available, publishing drafts, platform captions, clip ideas, pinned comments, keywords, hashtags, and one combined `publish_pack.md` file.

### Link Download Notes

CreatorKit uses `yt-dlp` for supported online links. Some providers, including Instagram and similar sites, may block anonymous downloads, reset the connection, require login cookies, or change their page format.

YouTube link support is temporarily disabled while we stabilize the local workflow and keep the product legally and operationally reliable.

If a link fails:

```text
1. Upload your own audio/video file.
2. Paste transcript text or captions you have permission to use.
3. For videos you uploaded, download your file from YouTube Studio and upload it to CreatorKit.
4. If needed, update CreatorKit by running the installer command again.
```

When a provider blocks direct access, uploading the audio/video file from your device still works.

---

## Output

The Creator Package export creates an organized folder:

```text
outputs/
  my_video/
    01_transcript.txt
    02_clean_transcript.txt
    03_captions.srt
    04_captions.vtt
    05_chapters.txt
    06_youtube_description.txt
    07_title_ideas.txt
    08_hook_ideas.txt
    09_platform_captions.txt
    10_clip_ideas.txt
    11_pinned_comments.txt
    12_hashtags_keywords.txt
    publish_pack.md
```

Caption files are included when the source has timestamps. Pasted transcripts without timestamps still export the transcript and creator asset files.

---

## Roadmap

| Feature | Status |
|---|---|
| Clean transcript mode | `shipped` |
| Batch processing | `planned` |
| Creator assets | `shipped` |
| YouTube description generator | `shipped` |
| Chapters and timestamp generation | `shipped` |
| Hook and title suggestions | `planned` |
| Caption snippets | `shipped` |
| Built-in update checker | `shipped` |
| Linux support | `planned` |
| MCP and skills layer | `planned` |

---

## Contributing

CreatorKit is open source. Contributions are welcome, whether it is a bug fix, new export format, UX improvement, testing help, or documentation.

```bash
git clone https://github.com/im-vedant26/CreatorKit.git
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
