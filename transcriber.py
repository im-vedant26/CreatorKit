# transcriber.py
import whisper
import warnings
from functools import lru_cache

# Suppress the FP16 warning on CPU
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")


@lru_cache(maxsize=3)
def load_whisper_model(model_name):
    return whisper.load_model(model_name)


def transcribe_audio(file_path, task="transcribe", model_name="small"):
    model = load_whisper_model(model_name)
    result = model.transcribe(file_path, task=task)
    text = result["text"]
    segments = result["segments"]
    return text, segments


def format_timestamp(seconds, separator=","):
    total_millis = round(seconds * 1000)
    hours = total_millis // 3_600_000
    minutes = (total_millis % 3_600_000) // 60_000
    secs = (total_millis % 60_000) // 1000
    millis = total_millis % 1000
    return f"{hours:02}:{minutes:02}:{secs:02}{separator}{millis:03}"


def segments_to_srt(segments):
    """Convert Whisper segments list to SRT formatted string."""
    srt_output = ""
    for i, segment in enumerate(segments, start=1):
        start = format_timestamp(segment['start'], separator=",")
        end = format_timestamp(segment['end'], separator=",")
        text = segment['text'].strip()
        srt_output += f"{i}\n{start} --> {end}\n{text}\n\n"

    return srt_output


def segments_to_vtt(segments):
    """Convert Whisper segments list to WebVTT formatted string."""
    lines = ["WEBVTT", ""]
    for segment in segments:
        start = format_timestamp(segment['start'], separator=".")
        end = format_timestamp(segment['end'], separator=".")
        text = segment['text'].strip()
        lines.extend([f"{start} --> {end}", text, ""])
    return "\n".join(lines)
