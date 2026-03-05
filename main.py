import os
import tkinter as tk
from tkinter import filedialog

import pyfiglet
import yt_dlp
from colorama import Fore, init

from transcriber import segments_to_srt, transcribe_audio

init(autoreset=True)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PREVIEW_LIMIT = 5000


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    ascii_banner = pyfiglet.figlet_format("AI Transcriber")
    print(Fore.CYAN + ascii_banner)
    print(Fore.LIGHTWHITE_EX + "Made by Vedant | Simple. Clean. Aesthetic.\n")


def browse_file():
    """Open a native file dialog and return the selected path."""
    root = None
    try:
        root = tk.Tk()
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
    except tk.TclError as err:
        print(Fore.RED + f"\n[ERROR] Could not open file picker: {err}")
        print(Fore.YELLOW + "Tip: Use a desktop session with Tk support.\n")
        return ""
    finally:
        if root is not None:
            try:
                root.destroy()
            except Exception:
                pass

    if file_path:
        print(Fore.LIGHTWHITE_EX + f"\nSelected: {file_path}\n")
    else:
        print(Fore.RED + "\nNo file selected.\n")

    return file_path


def save_file_dialog(default_filename, extension, filetypes):
    """Open a native save dialog and return the selected path."""
    root = None
    try:
        root = tk.Tk()
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
    except tk.TclError as err:
        print(Fore.RED + f"\n[ERROR] Could not open save dialog: {err}")
        return ""
    finally:
        if root is not None:
            try:
                root.destroy()
            except Exception:
                pass

    return file_path


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
    """Download audio from URL and return local mp3 path."""
    print(Fore.LIGHTCYAN_EX + "\nDownloading audio from link... Please wait...\n")
    output_base = os.path.join(PROJECT_DIR, "downloaded_audio")
    final_output_path = output_base + ".mp3"

    try:
        _yt_dlp_download(url, output_base)
        print(Fore.GREEN + "Audio downloaded successfully.\n")
        return final_output_path
    except Exception as err:
        print(Fore.RED + f"Download failed: {err}\n")

    print(Fore.YELLOW + "This often happens when the post requires login (private/age-gated).")
    print(Fore.LIGHTWHITE_EX + "Options:")
    print("  1) Retry using browser cookies (automatic).")
    print("  2) Provide a cookies.txt file.")
    print("  3) Skip and return to main menu.\n")

    while True:
        choice = input(Fore.CYAN + "Choose retry option [1/2/3]: ").strip()
        if choice == "1":
            for browser in ["chrome", "edge", "firefox"]:
                try:
                    print(Fore.LIGHTCYAN_EX + f"\nRetrying with browser cookies ({browser})...\n")
                    _yt_dlp_download(url, output_base, extra_opts={"cookies_from_browser": browser})
                    print(Fore.GREEN + "Audio downloaded successfully using browser cookies.\n")
                    return final_output_path
                except Exception as err:
                    print(Fore.YELLOW + f"Attempt with '{browser}' failed: {err}")

            print(Fore.RED + "\nAll automatic browser-cookie retries failed.")
            continue

        if choice == "2":
            cookie_path = input(Fore.LIGHTWHITE_EX + "\nEnter full path to cookies.txt: ").strip()
            if not cookie_path or not os.path.exists(cookie_path):
                print(Fore.RED + "Invalid cookies file path.")
                if input(Fore.CYAN + "Try again? (y/n): ").lower().strip() == "y":
                    continue
                return None

            try:
                print(Fore.LIGHTCYAN_EX + "\nRetrying with provided cookies file...\n")
                _yt_dlp_download(url, output_base, extra_opts={"cookiefile": cookie_path})
                print(Fore.GREEN + "Audio downloaded successfully using cookies file.\n")
                return final_output_path
            except Exception as err:
                print(Fore.RED + f"Retry with cookies file failed: {err}")
                if input(Fore.CYAN + "Try another option? (y/n): ").lower().strip() == "y":
                    continue
                return None

        if choice == "3":
            print(Fore.CYAN + "\nSkipping download and returning to main menu...\n")
            return None

        print(Fore.RED + "Invalid option. Enter 1, 2 or 3.")


def delete_temp_file(path):
    if not path:
        return
    try:
        if os.path.exists(path):
            os.remove(path)
            print(Fore.GREEN + "Temporary audio file deleted to save storage.")
    except Exception as err:
        print(Fore.RED + f"Failed to delete temporary file: {err}")


def main():
    while True:
        clear_screen()
        print_header()

        print(Fore.YELLOW + "Choose input method:\n")
        print("1. Upload from your device")
        print("2. Paste a video link (Instagram / YouTube / etc.)")
        print("3. Exit")
        choice = input(Fore.LIGHTWHITE_EX + "\nEnter your choice [1/2/3]: ").strip()

        downloaded_from_link = False

        if choice == "1":
            file_path = browse_file()
            if not file_path:
                input(Fore.LIGHTWHITE_EX + "Press Enter to return to main menu...")
                continue
        elif choice == "2":
            link = input(Fore.YELLOW + "\nPaste the video link: ").strip()
            if not link:
                print(Fore.RED + "No link provided.")
                input(Fore.LIGHTWHITE_EX + "\nPress Enter to continue...")
                continue
            file_path = download_video_from_link(link)
            if not file_path:
                input(Fore.LIGHTWHITE_EX + "\nPress Enter to continue...")
                continue
            downloaded_from_link = True
        elif choice == "3":
            print(Fore.LIGHTWHITE_EX + "\nExiting. Have a great day, Vedant!")
            break
        else:
            print(Fore.RED + "Invalid choice.")
            input(Fore.LIGHTWHITE_EX + "\nPress Enter to continue...")
            continue

        ask_again = True
        try:
            print(Fore.LIGHTWHITE_EX + f"Selected File: {file_path}\n")
            print(Fore.YELLOW + "\nChoose transcription mode:")
            print("1. Original Language (Transcribe)")
            print("2. Translate to English")
            mode_choice = input(Fore.LIGHTWHITE_EX + "\nEnter choice [1/2]: ").strip()
            task_mode = "translate" if mode_choice == "2" else "transcribe"

            print(Fore.YELLOW + "\nChoose AI Model (Accuracy vs Speed):")
            print("1. Small (Fast, Lower Accuracy)")
            print("2. Medium (Balanced)")
            print("3. Large (Slow, Best Accuracy)")
            model_choice = input(Fore.LIGHTWHITE_EX + "\nEnter choice [1/2/3]: ").strip()

            if model_choice == "2":
                model_name = "medium"
            elif model_choice == "3":
                model_name = "large"
            else:
                model_name = "small"

            print(Fore.LIGHTCYAN_EX + f"\nTranscribing with '{model_name}' model... Please wait...\n")
            try:
                output_text, srt_output = transcribe_audio(
                    file_path,
                    task=task_mode,
                    model_name=model_name,
                )
            except Exception as err:
                print(Fore.RED + f"Transcription failed: {err}")
                input(Fore.LIGHTWHITE_EX + "\nPress Enter to return to main menu...")
                continue

            print(Fore.GREEN + "Transcription complete.\n")
            preview = output_text[:PREVIEW_LIMIT]
            if len(output_text) > PREVIEW_LIMIT:
                preview += "..."
            print(Fore.LIGHTWHITE_EX + preview)

            print(Fore.YELLOW + "\nChoose format to save:")
            print("1. TXT (Plain Text)")
            print("2. SRT (Subtitles with timestamps)")
            print("3. Do not save, return to main menu")
            save_choice = input(Fore.LIGHTWHITE_EX + "\nEnter choice [1/2/3]: ").strip()

            if save_choice == "1":
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                default_name = f"{base_name}_transcription.txt"
                save_path = save_file_dialog(
                    default_name,
                    ".txt",
                    [("Text Files", "*.txt"), ("All files", "*.*")],
                )
                if save_path:
                    with open(save_path, "w", encoding="utf-8") as handle:
                        handle.write(output_text)
                    print(Fore.GREEN + f"Saved as '{save_path}'.")
                else:
                    print(Fore.YELLOW + "Save cancelled.")
            elif save_choice == "2":
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                default_name = f"{base_name}.srt"
                save_path = save_file_dialog(
                    default_name,
                    ".srt",
                    [("SRT Files", "*.srt"), ("All files", "*.*")],
                )
                if save_path:
                    with open(save_path, "w", encoding="utf-8") as handle:
                        handle.write(segments_to_srt(srt_output))
                    print(Fore.GREEN + f"Saved as '{save_path}'.")
                else:
                    print(Fore.YELLOW + "Save cancelled.")
            elif save_choice == "3":
                ask_again = False
                print(Fore.CYAN + "\nReturning to main menu...\n")
            else:
                ask_again = False
                print(Fore.RED + "Invalid choice. Returning to main menu...")

            if ask_again:
                again = input(Fore.YELLOW + "\nDo you want to transcribe another file? (y/n): ").lower().strip()
                if again != "y":
                    print(Fore.LIGHTWHITE_EX + "\nExiting. Have a great day, Vedant!")
                    break
        finally:
            if downloaded_from_link:
                delete_temp_file(file_path)


if __name__ == "__main__":
    main()
