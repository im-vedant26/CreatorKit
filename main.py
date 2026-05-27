# main.py
import itertools
import getpass
import os
import shutil
import threading
import textwrap
import time
import tkinter as tk
from tkinter import filedialog

from colorama import Fore, Style, init
import pyfiglet
import yt_dlp

from transcriber import transcribe_audio, segments_to_srt, segments_to_vtt


init(autoreset=True)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_BASE = os.path.join(PROJECT_DIR, "downloaded_audio")
DOWNLOAD_FILE = DOWNLOAD_BASE + ".mp3"
OUTPUT_DIR = os.path.join(PROJECT_DIR, "outputs")
APP_NAME = "CreatorKit"
APP_COMMAND = "creatorkit"
APP_TAGLINE = "Turn audio and video into transcripts, captions, and creator-ready assets."

ACCENT = Fore.LIGHTCYAN_EX
MUTED = Fore.LIGHTBLACK_EX
TEXT = Fore.LIGHTWHITE_EX
GOOD = Fore.LIGHTGREEN_EX
WARN = Fore.YELLOW
BAD = Fore.LIGHTRED_EX
FRAME = Fore.BLUE
BORDER_H = "-"
BORDER_V = "|"
CORNER_TL = "+"
CORNER_TR = "+"
CORNER_BL = "+"
CORNER_BR = "+"
TEE_L = "+"
TEE_R = "+"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def terminal_width():
    return min(shutil.get_terminal_size((88, 20)).columns, 100)


def display_width():
    return max(72, terminal_width())


def line(char=BORDER_H):
    print(FRAME + char * display_width())


def center(text, color=TEXT):
    print(color + text.center(display_width()))


def section(title):
    print()
    print(FRAME + CORNER_TL + BORDER_H * (display_width() - 2) + CORNER_TR)
    print(FRAME + BORDER_V + " " + ACCENT + Style.BRIGHT + title.ljust(display_width() - 4) + FRAME + " " + BORDER_V)
    print(FRAME + CORNER_BL + BORDER_H * (display_width() - 2) + CORNER_BR)


def status(label, message, color=TEXT):
    print(color + f"  {label:<9}" + MUTED + "| " + TEXT + message)


def pause(message="Press Enter to continue..."):
    input(MUTED + f"\n  {message}")


def box(lines, title=None, color=TEXT):
    width = display_width()
    print(FRAME + CORNER_TL + (BORDER_H * (width - 2)) + CORNER_TR)
    if title:
        title_text = f" {title} "
        print(FRAME + BORDER_V + ACCENT + Style.BRIGHT + title_text.ljust(width - 2) + FRAME + BORDER_V)
        print(FRAME + TEE_L + (BORDER_H * (width - 2)) + TEE_R)
    for raw_line in lines:
        for wrapped in textwrap.wrap(str(raw_line), width=width - 6) or [""]:
            print(FRAME + BORDER_V + "  " + color + wrapped.ljust(width - 6) + FRAME + "  " + BORDER_V)
    print(FRAME + CORNER_BL + (BORDER_H * (width - 2)) + CORNER_BR)


def run_with_activity(message, callback):
    done = threading.Event()
    result = {}

    def worker():
        try:
            result["value"] = callback()
        except Exception as err:
            result["error"] = err
        finally:
            done.set()

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()

    frames = itertools.cycle(["|", "/", "-", "\\"])
    started = time.monotonic()
    detail_cycle = itertools.cycle(
        [
            "loading model",
            "reading audio",
            "detecting speech",
            "building transcript",
            "almost there",
        ]
    )
    detail = next(detail_cycle)
    next_detail_at = started + 8

    while not done.is_set():
        now = time.monotonic()
        if now >= next_detail_at:
            detail = next(detail_cycle)
            next_detail_at = now + 8
        elapsed = int(now - started)
        line_text = f"  {next(frames)} {message}  {MUTED}{detail} | {elapsed}s elapsed"
        print(ACCENT + line_text.ljust(display_width()), end="\r", flush=True)
        time.sleep(0.12)

    thread.join()
    elapsed = int(time.monotonic() - started)
    print(" " * display_width(), end="\r", flush=True)

    if "error" in result:
        raise result["error"]
    status("DONE", f"{message} finished in {elapsed}s.", GOOD)
    return result.get("value")


def print_header():
    width = display_width()
    ascii_banner = pyfiglet.figlet_format(APP_NAME, font="small")
    print()
    print(FRAME + CORNER_TL + BORDER_H * (width - 2) + CORNER_TR)
    for row in ascii_banner.rstrip().splitlines():
        print(FRAME + BORDER_V + ACCENT + Style.BRIGHT + row.center(width - 2) + FRAME + BORDER_V)
    print(FRAME + TEE_L + BORDER_H * (width - 2) + TEE_R)
    print(FRAME + BORDER_V + TEXT + f"  {APP_TAGLINE}".ljust(width - 2) + FRAME + BORDER_V)
    print(FRAME + BORDER_V + MUTED + "  Creator-first CLI for videos, podcasts, reels, and subtitles".ljust(width - 2) + FRAME + BORDER_V)
    print(FRAME + CORNER_BL + BORDER_H * (width - 2) + CORNER_BR)


def current_user_name():
    try:
        name = getpass.getuser().strip()
        return name or "creator"
    except Exception:
        return "creator"


def print_goodbye():
    print(TEXT + f"\n  Thanks for using {APP_NAME}, {current_user_name()}.")


def print_menu(title, options):
    print()
    print(ACCENT + Style.BRIGHT + f"  {title}")
    print(MUTED + "  " + BORDER_H * min(display_width() - 2, 60))
    for key, label, hint in options:
        key_box = WARN + f"[{key}] "
        print(key_box + TEXT + f"{label:<24}" + MUTED + hint)


def ask_choice(prompt, valid_choices, default=None):
    choices = "/".join(valid_choices)
    suffix = f" [{choices}]"
    if default:
        suffix += f" default: {default}"

    while True:
        value = input(ACCENT + f"\n  > {prompt}{suffix}: " + TEXT).strip().lower()
        if not value and default:
            return default
        if value in valid_choices:
            return value
        status("ERROR", f"Choose one of: {choices}", BAD)


def browse_file():
    """
    Open a native file dialog and return the selected path.
    Keeps the Tk root topmost so the dialog is less likely to open behind the terminal.
    """
    root = tk.Tk()
    try:
        root.withdraw()
        root.attributes("-topmost", True)
        root.update()
        file_path = filedialog.askopenfilename(
            parent=root,
            title="Select your audio or video file",
            filetypes=[
                ("Audio/Video Files", "*.mp3 *.mp4 *.wav *.m4a *.mov *.avi"),
                ("All files", "*.*"),
            ],
        )
    finally:
        try:
            root.destroy()
        except Exception:
            pass

    if file_path:
        status("SELECTED", file_path, GOOD)
    else:
        status("CANCELLED", "No file selected.", WARN)

    return file_path


def save_file_dialog(default_filename, extension, filetypes):
    root = tk.Tk()
    try:
        root.withdraw()
        root.attributes("-topmost", True)
        root.update()
        file_path = filedialog.asksaveasfilename(
            parent=root,
            title="Select location to save file",
            initialfile=default_filename,
            defaultextension=extension,
            filetypes=filetypes,
        )
    finally:
        try:
            root.destroy()
        except Exception:
            pass
    return file_path


def safe_name(value):
    name = os.path.splitext(os.path.basename(value))[0].strip()
    cleaned = "".join(char if char.isalnum() or char in ("-", "_", " ") else "_" for char in name)
    cleaned = "_".join(cleaned.split())
    return cleaned or "creator_project"


def write_text_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def create_project_output_folder(file_path):
    base_name = safe_name(file_path)
    folder = os.path.join(OUTPUT_DIR, base_name)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
        return folder

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    folder = os.path.join(OUTPUT_DIR, f"{base_name}_{timestamp}")
    os.makedirs(folder, exist_ok=True)
    return folder


def export_project_folder(file_path, output_text, srt_segments):
    folder = create_project_output_folder(file_path)
    base_name = safe_name(file_path)
    files = {
        f"{base_name}_transcript.txt": output_text,
        f"{base_name}_captions.srt": segments_to_srt(srt_segments),
        f"{base_name}_captions.vtt": segments_to_vtt(srt_segments),
    }

    for filename, content in files.items():
        write_text_file(os.path.join(folder, filename), content)

    status("SAVED", f"Creator project folder: {folder}", GOOD)
    return folder


def _yt_dlp_download(url, outpath, extra_opts=None):
    opts = {
        "outtmpl": outpath,
        "quiet": True,
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "noplaylist": True,
    }
    if extra_opts:
        opts.update(extra_opts)
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])


def download_video_from_link(url):
    """Download audio from a link and return the local MP3 path."""
    section("Download")
    status("WORKING", "Downloading best available audio. This can take a moment.", ACCENT)

    try:
        run_with_activity("Downloading audio", lambda: _yt_dlp_download(url, DOWNLOAD_BASE))
        return DOWNLOAD_FILE
    except Exception as err:
        status("ERROR", f"Anonymous download failed: {err}", BAD)

    box(
        [
            "Some links need login cookies, especially private, age-gated, or platform-limited posts.",
            "1. Retry using browser cookies automatically",
            "2. Use a cookies.txt file",
            "3. Return to main menu",
        ],
        title="Download needs access",
    )

    while True:
        choice = ask_choice("Retry option", ["1", "2", "3"], default="3")

        if choice == "1":
            for browser in ["chrome", "edge", "firefox"]:
                try:
                    status("RETRY", f"Trying {browser} browser cookies...", ACCENT)
                    run_with_activity(
                        f"Downloading with {browser} cookies",
                        lambda browser=browser: _yt_dlp_download(
                            url,
                            DOWNLOAD_BASE,
                            extra_opts={"cookies_from_browser": browser},
                        ),
                    )
                    return DOWNLOAD_FILE
                except Exception as err:
                    status("WARN", f"{browser} cookies failed: {err}", WARN)
            status("ERROR", "All browser-cookie attempts failed.", BAD)

        elif choice == "2":
            cookie_path = input(ACCENT + "\n  > Full path to cookies.txt: " + TEXT).strip().strip('"')
            if not cookie_path or not os.path.exists(cookie_path):
                status("ERROR", "That cookies file path does not exist.", BAD)
                continue
            try:
                status("RETRY", "Trying provided cookies file...", ACCENT)
                run_with_activity(
                    "Downloading with cookies file",
                    lambda: _yt_dlp_download(url, DOWNLOAD_BASE, extra_opts={"cookiefile": cookie_path}),
                )
                return DOWNLOAD_FILE
            except Exception as err:
                status("ERROR", f"Retry with cookies file failed: {err}", BAD)

        elif choice == "3":
            status("SKIP", "Returning to main menu.", ACCENT)
            return None


def show_transcript_preview(text):
    section("Transcript")
    clean_text = text.strip() or "(No transcript text returned.)"
    max_chars = 12000
    preview = clean_text[:max_chars]
    width = max(60, terminal_width() - 4)

    for paragraph in preview.splitlines() or [preview]:
        wrapped = textwrap.fill(paragraph, width=width) if paragraph.strip() else ""
        print(TEXT + "  " + wrapped)

    if len(clean_text) > max_chars:
        hidden = len(clean_text) - max_chars
        print(MUTED + f"\n  Preview truncated. {hidden:,} more characters can still be saved to TXT.")


def save_transcript(file_path, output_text, srt_segments):
    print_menu(
        "Save Output",
        [
            ("1", "TXT", "plain text transcript"),
            ("2", "SRT", "subtitle file for editing and platforms"),
            ("3", "VTT", "web captions for YouTube/web players"),
            ("4", "Creator folder", "TXT, SRT, and VTT together"),
            ("5", "Do not save", "return to main menu"),
        ],
    )
    save_choice = ask_choice("Choose save format", ["1", "2", "3", "4", "5"])

    if save_choice == "5":
        status("SKIP", "Output was not saved.", ACCENT)
        return

    if save_choice == "4":
        export_project_folder(file_path, output_text, srt_segments)
        return

    base_name = safe_name(file_path)
    if save_choice == "1":
        default_name = f"{base_name}_transcription.txt"
        save_path = save_file_dialog(default_name, ".txt", [("Text Files", "*.txt"), ("All files", "*.*")])
        content = output_text
    elif save_choice == "2":
        default_name = f"{base_name}.srt"
        save_path = save_file_dialog(default_name, ".srt", [("SRT Files", "*.srt"), ("All files", "*.*")])
        content = segments_to_srt(srt_segments)
    else:
        default_name = f"{base_name}.vtt"
        save_path = save_file_dialog(default_name, ".vtt", [("WebVTT Files", "*.vtt"), ("All files", "*.*")])
        content = segments_to_vtt(srt_segments)

    if not save_path:
        status("CANCELLED", "Save cancelled.", WARN)
        return

    write_text_file(save_path, content)
    status("SAVED", save_path, GOOD)


def cleanup_downloaded_file(file_path):
    try:
        if file_path and os.path.abspath(file_path) == os.path.abspath(DOWNLOAD_FILE) and os.path.exists(file_path):
            os.remove(file_path)
            status("CLEANUP", "Temporary downloaded audio deleted.", GOOD)
    except Exception as err:
        status("WARN", f"Could not delete temporary audio: {err}", WARN)


def run_transcription(file_path):
    section("Setup")
    status("FILE", file_path, TEXT)

    print_menu(
        "Transcription Mode",
        [
            ("1", "Original language", "transcribe exactly as spoken"),
            ("2", "Translate to English", "Whisper translation mode"),
        ],
    )
    mode_choice = ask_choice("Choose mode", ["1", "2"], default="1")
    task_mode = "translate" if mode_choice == "2" else "transcribe"

    print_menu(
        "AI Model",
        [
            ("1", "Small", "fastest, lower accuracy"),
            ("2", "Medium", "balanced"),
            ("3", "Large", "slowest, best accuracy"),
        ],
    )
    model_choice = ask_choice("Choose model", ["1", "2", "3"], default="1")
    model_name = {"1": "small", "2": "medium", "3": "large"}[model_choice]

    section("Processing")
    box(
        [
            f"Model: Whisper {model_name}",
            f"Mode: {task_mode}",
            "The app is working while the animation is moving. Large files and large models can take several minutes.",
        ],
        title="Session",
    )

    output_text, srt_segments = run_with_activity(
        "Transcribing audio",
        lambda: transcribe_audio(file_path, task=task_mode, model_name=model_name),
    )
    return output_text, srt_segments


def main():
    while True:
        clear_screen()
        print_header()

        print_menu(
            "Input",
            [
                ("1", "Upload from your device", "audio or video file"),
                ("2", "Paste a video link", "YouTube, Instagram, and more"),
                ("3", "Exit", "close the app"),
            ],
        )
        choice = ask_choice("Enter your choice", ["1", "2", "3"])

        if choice == "1":
            file_path = browse_file()
            if not file_path:
                pause("Press Enter to return to main menu...")
                continue

        elif choice == "2":
            link = input(ACCENT + "\n  > Paste the video link: " + TEXT).strip()
            if not link:
                status("ERROR", "No link provided.", BAD)
                pause()
                continue
            file_path = download_video_from_link(link)
            if not file_path:
                pause()
                continue

        else:
            print_goodbye()
            break

        try:
            output_text, srt_segments = run_transcription(file_path)
            show_transcript_preview(output_text)
            save_transcript(file_path, output_text, srt_segments)
        except KeyboardInterrupt:
            print()
            status("STOPPED", "Operation cancelled by user.", WARN)
        except Exception as err:
            status("ERROR", f"Transcription failed: {err}", BAD)
        finally:
            if choice == "2":
                cleanup_downloaded_file(file_path)

        again = ask_choice("Transcribe another file?", ["y", "n"], default="y")
        if again != "y":
            print_goodbye()
            break


if __name__ == "__main__":
    main()
