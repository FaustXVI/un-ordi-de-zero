import functools
import math
import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

recording = False
section_done = False and not recording


# frame_factor = 3
# config.frame_width = 16 * frame_factor
# config.frame_height = 9 * frame_factor
# config.frame_rate = 30

class TwoCondensatorSerie(MyScene):

    def __init__(self):
        super().__init__(recording=recording)

    def construct(self):
        self.next_section(skip_animations=section_done)
        battery = Battery().rotate(PI).shift(UP * 3)
        c1 = Condensator().next_to(battery, DOWN, 1).shift(LEFT)
        c2 = Condensator().next_to(c1, RIGHT, 0)
        connectionC1C2 = c1.connect(c2)
        circuit = Circuit(battery, battery.connect(c1), c1, connectionC1C2, c2, c2.connect(battery))
        with self.my_voiceover(r"""Commençons par faire un circuit avec deux condensateurs en série :""") as timer:
            self.play(Create(circuit), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        dot_a = Dot(c1.entry_point())
        dot_b = Dot(c2.entry_point())
        dot_c = Dot(c2.exit_point())
        a = MathTex("A").next_to(dot_a, DOWN)
        b = MathTex("B").next_to(dot_b, DOWN)
        c = MathTex("C").next_to(dot_c, DOWN)
        with self.my_voiceover(r"""On va y placer 3 poins, A, B et C""") as timer:
            self.play(Create(VGroup(dot_a, a, dot_b, b, dot_c, c)), run_time=timer.duration)
        maille = MathTex("U", "=", "U_{AB}", "+", "U_{BC}").next_to(circuit, DOWN, 1)
        with self.my_voiceover(
                r"""La loi des mailles nous dit que si la pile de ce circuit a une tension U, alors U = Uab + Ubc""") as timer:
            self.play(Write(maille), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        sub_circuit = VGroup(*c1.submobjects[-3:], *c2.submobjects[:3], connectionC1C2, dot_b)
        with self.my_voiceover(
                r"""Regardons une sous partie du circuit qui est entre les deux condensateurs. Sans tension, comme le reste de notre circuit, cette partie est électriquement neutre. Quand on met une tension, aucune charge n'est créée, elles ne font que se déplacer. Cela veut dire que si une plaque a N charges, il faut que l'autre aie le même nombre de charges opposées.""") as timer:
            self.play(Indicate(sub_circuit, scale_factor=1.25, rate_func=rate_functions.there_and_back_with_pause),
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        q_form = MathTex("Q_{AB}", "=", "Q_{BC}", "=", "Q_{eq}").next_to(maille, DOWN, 1).shift(LEFT * 2)
        with self.my_voiceover(
                r"""On obtient alors Qab = Qbc = Qeq, la charge de notre condensateur équivalent""") as timer:
            self.play(Write(q_form), run_time=timer.duration)
        qcu = MathTex("Q", "=", "C", r"\times", "U").next_to(q_form, RIGHT, 1)
        with self.my_voiceover(
                r"""On sait aussi que pour tout condensateur : Q = CU""") as timer:
            self.play(Write(qcu), run_time=timer.duration)
        uqc = MathTex("U", "=", *my_frac(["Q"], ["C"])).next_to(q_form, RIGHT, 1)
        with self.my_voiceover(
                r"""soit U = Q/C""") as timer:
            self.play(TransformMatchingTex(qcu, uqc), run_time=timer.duration)
        maillec = MathTex("U", "=", *my_frac(["Q_{AB}"], ["C_{AB}"]), "+", *my_frac(["Q_{BC}"], ["C_{BC}"])).next_to(
            circuit, DOWN, 1)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                r"""si on utilise ça dans notre formule de la loi des mailles on obtient : U = Qab/Cab + Qbc / Cbc""") as timer:
            self.play(TransformMatchingTex(VGroup(maille, uqc), maillec), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        mailleeq = MathTex("U", "=", *my_frac(["Q_{eq}"], ["C_{AB}"]), "+", *my_frac(["Q_{eq}"], ["C_{BC}"])).next_to(
            circuit, DOWN, 1)
        with self.my_voiceover(
                r"""Et comme on a le même nombre de charges on obtient : U = Qeq/Cab + Qeq/Cbc""") as timer:
            self.play(TransformMatchingTex(VGroup(maillec, q_form), mailleeq), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        maille_fac = MathTex("U", "=", "Q_{eq}", r"\times", "(", *my_frac(["1"], ["C_{AB}"]), "+",
                             *my_frac(["1"], ["C_{BC}"]), ")").next_to(
            circuit, DOWN, 1)
        with self.my_voiceover(
                r"""On peut factoriser Q pour obtenir""") as timer:
            self.play(TransformMatchingTex(mailleeq, maille_fac), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        uqc.next_to(maille_fac, DOWN, 1)
        with self.my_voiceover(
                r"""Et comme dit précédement, on sait que U = Q/C""") as timer:
            self.play(Write(uqc), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        result = MathTex(*my_frac(["1"], ["C_{eq}"]), "=", *my_frac(["1"], ["C_{AB}"]), "+",
                         *my_frac(["1"], ["C_{BC}"])).next_to(circuit, DOWN, 1)
        with self.my_voiceover(
                r"""On obtient donc 1/Ceq = 1/Cab +  1/Cbc""") as timer:
            self.play(TransformMatchingTex(VGroup(maille_fac, uqc), result), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        result_g = MathTex(*my_frac(["1"], ["C_{eq}"]), "=", r"\sum_{i}", *my_frac(["1"], ["C_i"])).next_to(circuit,
                                                                                                            DOWN, 1)
        with self.my_voiceover(
                r"""Si on généralise on retrouve la vrai formule pour trouver notre capacité équivalante: 1/Ceq = somme 1/Ci""") as timer:
            self.play(TransformMatchingTex(result, result_g), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        self.play(FadeOut(VGroup(circuit, dot_a, dot_b, dot_c, a, c, b)), run_time=2)
        self.play(result_g.animate.move_to(ORIGIN), run_time=2)
        self.next_section(skip_animations=False)
        demo_form = MathTex(*my_frac(["1"], ["C_{eq}"]), "=", *my_frac(["1"], ["C"]), "+", *my_frac(["1"], ["C"]))
        with self.my_voiceover(
                r"""Dans notre cas on met deux condensateurs de capacité identique C, on obtient 1/Ceq = 1/C + 1/C""") as timer:
            self.play(TransformMatchingTex(result_g, demo_form), run_time=timer.duration)
        demo_form2 = MathTex(*my_frac(["1"], ["C_{eq}"]), "=", *my_frac(["2"], ["C"]))
        with self.my_voiceover(
                r"""soit 1/Ceq = 2/C""") as timer:
            self.play(TransformMatchingTex(demo_form, demo_form2), run_time=timer.duration)
        demo_final = MathTex("C_{eq}", "=", *my_frac(["C"], ["2"]))
        with self.my_voiceover(
                r"""et donc Ceq = C/2""") as timer:
            self.play(TransformMatchingTex(demo_form2, demo_final), run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.play(FadeOut(*self.mobjects), run_time=3)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
