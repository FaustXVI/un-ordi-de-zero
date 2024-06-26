import operator
from itertools import accumulate

from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False

config.background_color = WHITE

Mobject.set_default(color=BLACK)
Dot.set_default(color=BLACK)
Arc.set_default(color=BLACK, stroke_color=BLACK)


class SI(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        units = [r"Unus",r"A = \frac{C}{s}", r"V = \frac{J}{C}", r"J = N \times m", r"N = \frac{kg \times m}{s^2}",
                 r"\Omega = \frac{V}{A}", r"U = R \times I", r"R =\frac{U}{I}", ]
        tex_units = [MathTex(unit).scale(5) for unit in units]
        self.play(Create(tex_units[0]))
        for i in range(1, len(units)):
            self.wait()
            self.play(FadeOut(tex_units[i - 1]))
            self.wait()
            self.play(Create(tex_units[i]))
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
