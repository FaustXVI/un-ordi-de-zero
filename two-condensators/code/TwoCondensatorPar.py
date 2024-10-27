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

class TwoCondensatorPar(MyScene):

    def __init__(self):
        super().__init__(recording=recording)

    def construct(self):
        battery = Battery().rotate(PI).shift(UP * 3)
        c1 = Condensator()
        c2 = Condensator().next_to(c1, DOWN, 1)
        par = Junction(c1, c2).next_to(battery, DOWN, 1)
        contact1 = Contact().next_to(par, LEFT)
        contact2 = Contact().next_to(par, RIGHT)
        cableToC2 = par.connect(contact2)
        circuit = Circuit(battery, battery.connect(contact1), contact1, contact1.connect(par), par,
                          cableToC2, contact2, contact2.connect(battery))
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                r"""Comme tout à l'heure, commençons par un schéma du circuit avec deux condensateurs en parallèles.""") as timer:
            self.play(Create(circuit), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        maille = MathTex("U", "=", "U_{C_1}", "=", "U_{C_2}").next_to(circuit, DOWN, 1)
        with self.my_voiceover(
                r"""La loi des mailles nous dit que U = Uc1 = Uc2""") as timer:
            self.play(Write(maille), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                r"""Si on regarde une moitié du circuit, ou vois que les charges des deux condensateurs se rejoignent.""") as timer:
            self.play(Indicate(VGroup(*c1.submobjects[-3:], *c2.submobjects[-3:], *par.submobjects[-2].submobjects[-1:],
                                      *par.submobjects[-3].submobjects[-1:], cableToC2)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        qeq = MathTex("Q_{eq}", "=", "Q_{C_1}", "+", "Q_{C_2}").next_to(maille, DOWN, 1).shift(LEFT * 2)
        with self.my_voiceover(
                r"""On a donc""") as timer:
            self.play(Write(qeq), run_time=timer.duration)
        condo = MathTex("Q", "=", "C", r"\times", "U").next_to(qeq, RIGHT, 1)
        with self.my_voiceover(
                r"""De plus on sait que pour tout condensateur Q = C*U""") as timer:
            self.play(Write(condo), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        qeqCondo = MathTex("Q_{eq}", "=", "C_{C_1}", r"\times", "U_{C_1}", "+", "C_{C_2}", r"\times",
                           "U_{C_2}").next_to(maille, DOWN, 1)
        with self.my_voiceover(
                r"""Ce qui nous donne Qeq = Cc1Uc1 + Cc2Uc2""") as timer:
            self.play(TransformMatchingTex(VGroup(qeq, condo), qeqCondo), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        qeqCondoU = MathTex("Q_{eq}", "=", "C_{C_1}", r"\times", "U", "+", "C_{C_2}", r"\times", "U").next_to(circuit,
                                                                                                              DOWN, 1)
        with self.my_voiceover(
                r"""En utilisant la formule de la loi des mailles on obtient :""") as timer:
            self.play(TransformMatchingTex(VGroup(qeqCondo, maille), qeqCondoU), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        qeqFac = MathTex("Q_{eq}", "=", "(", "C_{C_1}", "+", "C_{C_2}", ")", r"\times", "U").next_to(circuit,
                                                                                                     DOWN, 1)
        with self.my_voiceover(
                r"""Ce qui nous donne Qeq = (Cc1 + Cc2)*U""") as timer:
            self.play(TransformMatchingTex(qeqCondoU, qeqFac), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        ceq = MathTex("C_{eq}", "=", "C_{C_1}", "+", "C_{C_2}").next_to(circuit, DOWN, 1)
        with self.my_voiceover(
                r"""En réutilisant la formule des condensateurs on trouve Ceq = Cc1 + Cc2""") as timer:
            self.play(TransformMatchingTex(qeqFac, ceq), run_time=timer.duration)
        self.next_section(skip_animations=False)
        ceqG = MathTex("C_{eq}", "=", r"\sum_i" "C_i").next_to(circuit, DOWN, 1)
        with self.my_voiceover(
                r"""Ce qu'on peut généraliser par Ceq = sum Ci""") as timer:
            self.play(TransformMatchingTex(ceq, ceqG), run_time=timer.duration)
        self.play(FadeOut(circuit), run_time=2)
        self.play(ceqG.animate.move_to(ORIGIN), run_time=2)
        self.next_section(skip_animations=False)
        ceq2C = MathTex("C_{eq}", "=", r"2" "C")
        with self.my_voiceover(
                r"""Dans le cadre de deux condensateurs équivalants on trouve que Ceq = 2C""") as timer:
            self.play(TransformMatchingTex(ceqG, ceq2C), run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.play(FadeOut(*self.mobjects), run_time=3)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
