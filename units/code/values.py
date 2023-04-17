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


class Values(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        numbers = [r"1,248 \times 10^{15}", r"8 \times 10^{-16}", r"6,241509 \times 10^{18}"]
        tex_numbers = [MathTex(unit).scale(4) for unit in numbers]
        self.play(Write(tex_numbers[0]))
        for i in range(1, len(numbers)):
            self.wait(3)
            self.play(FadeOut(tex_numbers[i - 1]))
            self.wait(3)
            self.play(Write(tex_numbers[i]))
        self.wait(3)
        self.play(FadeOut(tex_numbers[-1]))
        self.wait(3)


if __name__ == "__main__":
    main(["-tpqh",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
