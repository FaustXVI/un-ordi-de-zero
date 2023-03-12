from abc import ABC

from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService


class FakeTracker:

    def __init__(self, duration=1) -> None:
        super().__init__()
        self.duration = duration

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass


class MyScene(VoiceoverScene, ABC):
    def my_voiceover(self, text, duration=3):
        if self.recording:
            return self.voiceover(text)
        else:
            return FakeTracker(duration)

    def my_frac(d, n):
        return [r"{", r"{", *d, r"}", r"\over", r"{", *n, r"}", r"}"]

    def __init__(self, recording, **kwargs):
        super().__init__(**kwargs)
        self.recording = recording
        self.set_speech_service(RecorderService(device_index=12))
