import math
import operator
from itertools import accumulate

from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Demonstration(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("""On a 3 composants dans notre circuit""", 2) as timer:
            self.wait(timer.duration)
        tension = MathTex("U")
        r1 = MathTex("R_1")
        r2 = MathTex("R_2")
        VGroup(tension, r1, r2).arrange(DOWN)
        with self.my_voiceover("""Une pile qui produit une tension U""", 2) as timer:
            self.play(Create(tension), run_time=timer.duration, rate_func=rate_functions.ease_out_quad)
        with self.my_voiceover("""Une première résistance avec une valeur R1""", 2) as timer:
            self.play(Create(r1), run_time=timer.duration, rate_func=rate_functions.ease_out_quad)
        with self.my_voiceover("""et une deuxième résistance avec une valeur R2""", 2) as timer:
            self.play(Create(r2), run_time=timer.duration, rate_func=rate_functions.ease_out_quad)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("""Si on mesure la tension aux bornes des résistances, d'après la loi d'ohm on a""",
                               2) as timer:
            self.wait(timer.duration)
        self.next_section(skip_animations=section_done)
        ur1 = MathTex("U_{R_1}", "=", "R_1", r"\times", "I_{R_1}")
        ur2 = MathTex("U_{R_2}", "=", "R_2", r"\times", "I_{R_2}")
        sum_u = MathTex("U", "=", "U_{R_1}", "+", "U_{R_2}")
        equations = VGroup(sum_u, ur1, ur2).arrange(DOWN)
        with self.my_voiceover("""UR1 = R1 * IR1""") as timer:
            self.play(TransformMatchingTex(r1, ur1), run_time=timer.duration)
        with self.my_voiceover("""et UR2 = R2 * IR2""") as timer:
            self.play(TransformMatchingTex(r2, ur2), run_time=timer.duration)
        with self.my_voiceover("""La loi des mailles nous dit aussi que""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover("""U = UR1 + UR2""") as timer:
            self.play(TransformMatchingTex(tension, sum_u), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        first_uri = MathTex("U", "=", "R_1", r"\times", "I_{R_1}", "+", "R_2", r"\times", "I_{R_2}")
        with self.my_voiceover("""U = UR1 + UR2""") as timer:
            self.play(TransformMatchingTex(equations, first_uri), run_time=timer.duration)
        with self.my_voiceover("""Et la loi des nœuds nous dit que""", 2) as timer:
            self.wait(timer.duration)
        self.next_section(skip_animations=section_done)
        noeuds = MathTex("I_{R_1}", "=", "I_{R_2}", "=", "I").shift(UP)
        with self.my_voiceover("""IR1 = IR2 qu'on peut donc seulement noter I""", 2) as timer:
            self.play(Create(noeuds), run_time=timer.duration)
        expanded = MathTex("U", "=", "R_1", r"\times", "I", "+", "R_2", r"\times", "I")
        factored = MathTex("U", "=", "(", "R_1", "+", "R_2", ")", r"\times", "I")
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("""On obtient alors, U = R1 * I + R2 * I""", 5) as timer:
            self.play(TransformMatchingTex(VGroup(first_uri, noeuds), expanded), run_time=timer.duration,
                      rate_func=rate_functions.ease_in_quart)
        with self.my_voiceover("""Si on factorise I, on a U = (R1 + R2) * I""", 4) as timer:
            self.play(TransformMatchingTex(expanded, factored),
                      run_time=timer.duration, rate_func=rate_functions.ease_in_quart)
        self.next_section(skip_animations=False)
        with self.my_voiceover("""On retrouve alors la loi d'ohm avec une résistance égale à R1 + R2""", 4) as timer:
            self.play(Indicate(
                VGroup(factored.get_parts_by_tex("("), factored.get_parts_by_tex("R_1"), factored.get_parts_by_tex("+"),
                       factored.get_parts_by_tex("R_2"), factored.get_parts_by_tex(")"))), run_time=timer.duration)
        with self.my_voiceover(
                """La résistance d'un circuit composé de deux résistance est donc égal à la somme des résistances""",
                4) as timer:
            self.play(FadeOut(factored), run_time=timer.duration, rate_func=rate_functions.ease_in_quart)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
