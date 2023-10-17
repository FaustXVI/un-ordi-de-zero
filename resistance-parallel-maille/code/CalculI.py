from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class CalculI(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        loi_ohm = MathTex(r"U", " = ", "R", r"\times", "I")
        loi_ohm_1_5_V = MathTex(r"1.5", " = ", "R", r"\times", "I")
        loi_ohm_values = MathTex(r"1.5", " = ", "1000", r"\times", "I")
        i_frac = MathTex(*my_frac(["1.5"], ["1000"]), " = ", "I")
        i_value = MathTex(r"0.0015", " = ", "I")
        with self.my_voiceover(
                """Pour chaque branche, la loi d'ohm nous dit que U = R fois I""") as timer:
            self.play(Write(loi_ohm), run_time=timer.duration)
        with self.my_voiceover(
                """Or on viens de dire que $U$ est égal à la tension de notre pile. Et comme on la choisie, on peut la fixer à la valeur que l'on veut, par exemple, 1.5 V""") as timer:
            self.play(TransformMatchingTex(loi_ohm, loi_ohm_1_5_V), run_time=timer.duration)
        with self.my_voiceover(
                """Ensuite, dans la même logique, on choisie R donc on peut y mettre valeur que l'on veut, par exemple 1000 ohm""") as timer:
            self.play(TransformMatchingTex(loi_ohm_1_5_V, loi_ohm_values), run_time=timer.duration)
        with self.my_voiceover(
                """Donc I est égal à 1.5 sur 1000""") as timer:
            self.play(TransformMatchingTex(loi_ohm_values, i_frac), run_time=timer.duration)
        with self.my_voiceover(
                """soit 0.0015 Ampères""") as timer:
            self.play(TransformMatchingTex(i_frac, i_value), run_time=timer.duration)
        with self.my_voiceover(
                """donc 1.5 milli-ampères""") as timer:
            self.wait(timer.duration)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
