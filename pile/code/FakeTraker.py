class FakeTracker:

    def __init__(self, duration = 1) -> None:
        super().__init__()
        self.duration = duration

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass
