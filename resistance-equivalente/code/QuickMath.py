import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Demo(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        self.next_section(skip_animations=False)
        equiv_general = MathTex("R", "=", *my_frac(["1"], ["\sum\limits_{n}", *my_frac(["1"], ["R", "_n"])]))
        self.add(equiv_general)
        equiv_eq = MathTex("R", "=", *my_frac(["1"], [*my_frac(["1"], ["R", "_{branche}"]), "\sum\limits_{n}", "1 "]))
        with self.my_voiceover(
                r"""Comme les deux résistances sont égales, on peut les factoriser""") as timer:
            self.play(TransformMatchingTex(equiv_general, equiv_eq),
                      run_time=timer.duration)
        result_all = MathTex("R", "=", *my_frac(["1"], [*my_frac(["1"], ["R", "_{branche}"]), r"\times", "2"]))
        with self.my_voiceover(
                r"""La somme est alors égale aux nombre de branches, soit deux.""") as timer:
            self.play(TransformMatchingTex(equiv_eq, result_all),
                      run_time=timer.duration)
        result = MathTex("R", "=", *my_frac(["1"], ["2"]), "R", "_{branche}")
        with self.my_voiceover(
                r"""Et comme l'inverse de l'inverse d'une valeur est égale à la valeur elle-même, on obtient : R = \frac{1}{2} R_{branche}""") as timer:
            self.play(TransformMatchingTex(result_all, result),
                      run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
