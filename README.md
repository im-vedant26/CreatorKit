<div align="center">

<img src="https://img.shields.io/badge/CreatorKit-v0.1-22D3EE?style=for-the-badge&labelColor=0F172A&color=22D3EE" alt="CreatorKit"/>

<h1>
  <img src="https://img.shields.io/badge/─────────────────────────────────-0F172A?style=flat-square" alt=""/><br/>
  <code>CreatorKit</code>
</h1>

**Turn audio and video into transcripts, captions, and creator-ready assets.**<br/>
**From a clean interactive terminal. No scripts. No config.**

<br/>

[![MIT License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square&labelColor=0F172A)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-22D3EE?style=flat-square&labelColor=0F172A)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-94A3B8?style=flat-square&labelColor=0F172A)]()
[![Open Source](https://img.shields.io/badge/Open-Source-22C55E?style=flat-square&labelColor=0F172A)](https://github.com/im-vedant26/CreatorKit)

<br/>

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

```bash
creatorkit
```

<sub>One command to install. One command to run.</sub>

</div>

<br/>

---

## Terminal Preview

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ ║
║   ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗║
║   ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝║
║   ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗║
║   ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║║
║    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝║
║                                                              ║
║         Creator-first terminal app  ·  v0.1                 ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   What would you like to do?                                 ║
║                                                              ║
║   [ 1 ]  Transcribe a local file                             ║
║   [ 2 ]  Download & transcribe from a link                   ║
║   [ 3 ]  Translate speech to English                         ║
║   [ 4 ]  Export  →  TXT  /  SRT  /  VTT  /  Creator Folder  ║
║   [ Q ]  Quit                                                ║
║                                                              ║
║   > _                                                        ║
╚══════════════════════════════════════════════════════════════╝
```

---

## What CreatorKit does

You record a podcast. You film a tutorial. You capture an interview.

CreatorKit takes that raw file — or a link — and outputs the assets you actually need: a full transcript, subtitle files for your editor, caption files for your platform. All from a single interactive menu. No flags to memorize. No Python knowledge required.

> Built for **YouTubers, podcasters, educators, short-form creators, and video editors.**
> You don't need to be a developer to use it.

---

## Features

| | Feature | What it does |
|---|---|---|
| `TRN` | **Transcribe local files** | Drop in any audio or video file — get a full transcript |
| `DL` | **Download from links** | Paste a supported URL — CreatorKit fetches and transcribes |
| `EN` | **Translate to English** | Transcribe non-English audio directly into English |
| `TXT` | **Export transcript** | Clean plain-text file of the full spoken content |
| `SRT` | **Export subtitles** | Subtitle file ready for Premiere, DaVinci, or any editor |
| `VTT` | **Export captions** | WebVTT caption file for YouTube, web players, and platforms |
| `PKG` | **Creator Folder** | TXT + SRT + VTT saved together in one organized output folder |
| `...` | **Live activity indicator** | Real-time terminal feedback during long transcription steps |

---

## Installation

### Windows — One Command

Open PowerShell and run:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

The installer sets everything up. When it's done, open any terminal and type `creatorkit`.

---

### Manual Install

For developers, or if you're on a non-Windows system:

**Prerequisites**

```
Python 3.10+   Git   FFmpeg (on system PATH)
```

**Setup**

```bash
git clone https://github.com/im-vedant26/CreatorKit.git
cd CreatorKit
pip install -r requirements.txt
```

<details>
<summary>Python dependencies</summary>

```
openai-whisper
torch
tqdm
colorama
pyfiglet
ffmpeg-python
yt-dlp
```

</details>

> The one-command installer is Windows-only for now. Manual install works wherever the dependencies are supported.

---

## Usage

```bash
creatorkit
```

That's it. An interactive menu opens — no arguments, no flags.

From there:

```
[ 1 ]  Point CreatorKit at a local audio or video file
[ 2 ]  Paste a link — it downloads and transcribes automatically
[ 3 ]  Use translate mode for non-English content
[ 4 ]  Choose your export: TXT, SRT, VTT, or the full Creator Folder
```

Your exports land in a clean `outputs/` folder, organized by file.

---

## Output

```
outputs/
└── my_video/
    ├── my_video_transcript.txt     ← full transcript
    ├── my_video_captions.srt       ← subtitle file
    └── my_video_captions.vtt       ← caption file
```

---

## Roadmap

| Feature | Status |
|---|---|
| Clean transcript mode — filler words removed | `planned` |
| Batch processing — multiple files at once | `planned` |
| Summarization | `planned` |
| YouTube description generator | `planned` |
| Chapters and timestamp generation | `planned` |
| Hook and title idea suggestions | `planned` |
| Short-form clip suggestions | `planned` |
| Built-in update checker | `planned` |

---

## Contributing

CreatorKit is open source. Contributions are welcome — whether it's a bug fix, a new export format, a UX improvement, or documentation.

```bash
# Fork, clone, build
git clone https://github.com/your-username/CreatorKit.git
cd CreatorKit

# Open a pull request when ready
```

Not sure where to start? Browse [open issues](https://github.com/im-vedant26/CreatorKit/issues) or open one describing what you'd like to work on.

---

## License

MIT — see [LICENSE](./LICENSE) for details.

---

<div align="center">

<sub>
  <a href="https://github.com/im-vedant26/CreatorKit">GitHub</a> ·
  <a href="https://github.com/im-vedant26/CreatorKit/issues">Report a Bug</a> ·
  <a href="https://github.com/im-vedant26/CreatorKit/issues">Request a Feature</a>
</sub>

<br/><br/>

<img src="https://img.shields.io/badge/Built%20for%20creators.-22D3EE?style=flat-square&labelColor=0F172A" alt="Built for creators."/>

</div>
<div align="center">

<img src="https://img.shields.io/badge/CreatorKit-v0.1-22D3EE?style=for-the-badge&labelColor=0F172A&color=22D3EE" alt="CreatorKit"/>

<h1>
  <img src="https://img.shields.io/badge/─────────────────────────────────-0F172A?style=flat-square" alt=""/><br/>
  <code>CreatorKit</code>
</h1>

**Turn audio and video into transcripts, captions, and creator-ready assets.**<br/>
**From a clean interactive terminal. No scripts. No config.**

<br/>

[![MIT License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square&labelColor=0F172A)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-22D3EE?style=flat-square&labelColor=0F172A)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-94A3B8?style=flat-square&labelColor=0F172A)]()
[![Open Source](https://img.shields.io/badge/Open-Source-22C55E?style=flat-square&labelColor=0F172A)](https://github.com/im-vedant26/CreatorKit)

<br/>

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

```bash
creatorkit
```

<sub>One command to install. One command to run.</sub>

</div>

<br/>

---

## Terminal Preview

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ ║
║   ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗║
║   ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝║
║   ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗║
║   ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║║
║    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝║
║                                                              ║
║         Creator-first terminal app  ·  v0.1                 ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   What would you like to do?                                 ║
║                                                              ║
║   [ 1 ]  Transcribe a local file                             ║
║   [ 2 ]  Download & transcribe from a link                   ║
║   [ 3 ]  Translate speech to English                         ║
║   [ 4 ]  Export  →  TXT  /  SRT  /  VTT  /  Creator Folder  ║
║   [ Q ]  Quit                                                ║
║                                                              ║
║   > _                                                        ║
╚══════════════════════════════════════════════════════════════╝
```

---

## What CreatorKit does

You record a podcast. You film a tutorial. You capture an interview.

CreatorKit takes that raw file — or a link — and outputs the assets you actually need: a full transcript, subtitle files for your editor, caption files for your platform. All from a single interactive menu. No flags to memorize. No Python knowledge required.

> Built for **YouTubers, podcasters, educators, short-form creators, and video editors.**
> You don't need to be a developer to use it.

---

## Features

| | Feature | What it does |
|---|---|---|
| `TRN` | **Transcribe local files** | Drop in any audio or video file — get a full transcript |
| `DL` | **Download from links** | Paste a supported URL — CreatorKit fetches and transcribes |
| `EN` | **Translate to English** | Transcribe non-English audio directly into English |
| `TXT` | **Export transcript** | Clean plain-text file of the full spoken content |
| `SRT` | **Export subtitles** | Subtitle file ready for Premiere, DaVinci, or any editor |
| `VTT` | **Export captions** | WebVTT caption file for YouTube, web players, and platforms |
| `PKG` | **Creator Folder** | TXT + SRT + VTT saved together in one organized output folder |
| `...` | **Live activity indicator** | Real-time terminal feedback during long transcription steps |

---

## Installation

### Windows — One Command

Open PowerShell and run:

```powershell
irm https://raw.githubusercontent.com/im-vedant26/CreatorKit/main/scripts/install.ps1 | iex
```

The installer sets everything up. When it's done, open any terminal and type `creatorkit`.

---

### Manual Install

For developers, or if you're on a non-Windows system:

**Prerequisites**

```
Python 3.10+   Git   FFmpeg (on system PATH)
```

**Setup**

```bash
git clone https://github.com/im-vedant26/CreatorKit.git
cd CreatorKit
pip install -r requirements.txt
```

<details>
<summary>Python dependencies</summary>

```
openai-whisper
torch
tqdm
colorama
pyfiglet
ffmpeg-python
yt-dlp
```

</details>

> The one-command installer is Windows-only for now. Manual install works wherever the dependencies are supported.

---

## Usage

```bash
creatorkit
```

That's it. An interactive menu opens — no arguments, no flags.

From there:

```
[ 1 ]  Point CreatorKit at a local audio or video file
[ 2 ]  Paste a link — it downloads and transcribes automatically
[ 3 ]  Use translate mode for non-English content
[ 4 ]  Choose your export: TXT, SRT, VTT, or the full Creator Folder
```

Your exports land in a clean `outputs/` folder, organized by file.

---

## Output

```
outputs/
└── my_video/
    ├── my_video_transcript.txt     ← full transcript
    ├── my_video_captions.srt       ← subtitle file
    └── my_video_captions.vtt       ← caption file
```

---

## Roadmap

| Feature | Status |
|---|---|
| Clean transcript mode — filler words removed | `planned` |
| Batch processing — multiple files at once | `planned` |
| Summarization | `planned` |
| YouTube description generator | `planned` |
| Chapters and timestamp generation | `planned` |
| Hook and title idea suggestions | `planned` |
| Short-form clip suggestions | `planned` |
| Built-in update checker | `planned` |

---

## Contributing

CreatorKit is open source. Contributions are welcome — whether it's a bug fix, a new export format, a UX improvement, or documentation.

```bash
# Fork, clone, build
git clone https://github.com/your-username/CreatorKit.git
cd CreatorKit

# Open a pull request when ready
```

Not sure where to start? Browse [open issues](https://github.com/im-vedant26/CreatorKit/issues) or open one describing what you'd like to work on.

---

## License

MIT — see [LICENSE](./LICENSE) for details.

---

<div align="center">

<sub>
  <a href="https://github.com/im-vedant26/CreatorKit">GitHub</a> ·
  <a href="https://github.com/im-vedant26/CreatorKit/issues">Report a Bug</a> ·
  <a href="https://github.com/im-vedant26/CreatorKit/issues">Request a Feature</a>
</sub>

<br/><br/>

<img src="https://img.shields.io/badge/Built%20for%20creators.-22D3EE?style=flat-square&labelColor=0F172A" alt="Built for creators."/>

</div>
