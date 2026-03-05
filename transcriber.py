# transcriber.py
import whisper
import warnings
from functools import lru_cache

# Suppress the FP16 warning on CPU
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

@lru_cache(maxsize=3)
def _load_model(model_name):
    return whisper.load_model(model_name)

def transcribe_audio(file_path, task="transcribe", model_name="small"):
    model = _load_model(model_name)
    result = model.transcribe(file_path, task=task)
    text = result["text"]
    segments = result["segments"]
    return text, segments

def segments_to_srt(segments):
    """
    Convert Whisper segments list to SRT formatted string.
    """
    def format_timestamp(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

    srt_output = ""
    for i, segment in enumerate(segments, start=1):
        start = format_timestamp(segment['start'])
        end = format_timestamp(segment['end'])
        text = segment['text'].strip()
        srt_output += f"{i}\n{start} --> {end}\n{text}\n\n"
    
    return srt_output
