from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


class FourcheSc(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        b1 = Cable(LEFT, RIGHT + UP)
        b2 = Cable(LEFT, RIGHT + DOWN)
        c = Cable(LEFT * 3, LEFT)

        self.play(Succession(Create(c), Wait(3), AnimationGroup(Create(b1), Create(b2)), Wait(20)),
                  rate_func=linear)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
