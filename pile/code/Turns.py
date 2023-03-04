from manim import *
from manim.__main__ import main
class HundredTurns(Scene):
    def construct(self):
        self.add(Tex("\\Large{100 tours plus tard}"))
        self.wait(3)

class ThousandTurns(Scene):
    def construct(self):
        self.add(Tex("\\Large{1000 tours plus tard}"))
        self.wait(3)

if __name__ == "__main__":
    main(["-pql", __file__], prog_name='invoked-command')
