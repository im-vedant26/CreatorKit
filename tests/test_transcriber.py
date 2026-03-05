import importlib.util
import pathlib
import sys
import types
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
TRANSCRIBER_PATH = ROOT / "transcriber.py"


def load_transcriber_with_fake_whisper(fake_load_model):
    """Load transcriber.py with an injected fake whisper module."""
    fake_whisper = types.SimpleNamespace(load_model=fake_load_model)
    previous = sys.modules.get("whisper")
    sys.modules["whisper"] = fake_whisper
    try:
        spec = importlib.util.spec_from_file_location("transcriber_under_test", TRANSCRIBER_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if previous is None:
            sys.modules.pop("whisper", None)
        else:
            sys.modules["whisper"] = previous


class FakeModel:
    def transcribe(self, _file_path, task="transcribe"):
        return {
            "text": f"text:{task}",
            "segments": [{"start": 0.0, "end": 1.0, "text": "hello"}],
        }


class TestTranscriber(unittest.TestCase):
    def test_segments_to_srt_format(self):
        module = load_transcriber_with_fake_whisper(lambda _name: FakeModel())
        segments = [
            {"start": 0.0, "end": 1.234, "text": " Hello "},
            {"start": 61.5, "end": 62.0, "text": "World"},
        ]

        result = module.segments_to_srt(segments)

        self.assertIn("1\n00:00:00,000 --> 00:00:01,234\nHello", result)
        self.assertIn("2\n00:01:01,500 --> 00:01:02,000\nWorld", result)

    def test_model_loading_is_cached_per_model_name(self):
        calls = {"count": 0}

        def fake_load_model(_name):
            calls["count"] += 1
            return FakeModel()

        module = load_transcriber_with_fake_whisper(fake_load_model)
        module._load_model.cache_clear()

        module.transcribe_audio("a.mp3", task="transcribe", model_name="small")
        module.transcribe_audio("b.mp3", task="translate", model_name="small")

        self.assertEqual(calls["count"], 1)


if __name__ == "__main__":
    unittest.main()
