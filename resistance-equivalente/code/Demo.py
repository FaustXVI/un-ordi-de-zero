import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


class Demo(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        general_ohm = MathTex("U", "=", "R", r"\times", "I")
        with self.my_voiceover(
                """On veut remplacer nos deux résistances par une seule résistance $R$ sans impact sur le reste du circuit.
                Dit autrement on veut que la tension $U$ et l'intensité $I$ dans le reste du circuit ne soit pas modifié.
La loi d'ohm nous dit que U = R I""") as timer:
            self.play(Write(general_ohm), run_time=timer.duration)
        noeud = MathTex("I_1", "+", "I_2", "=", "I").shift(DOWN)
        with self.my_voiceover(
                """La loi des nœuds nous dit que $I_1 + I_2 = I$""") as timer:
            self.play(Write(noeud), run_time=timer.duration)
        is_ohm = MathTex("U", "=", "R", r"\times", "(", "I_1", "+", "I_2", ")")
        with self.my_voiceover(
                r"""On obtiens donc $U = R \times (I_1 + I_2)$""") as timer:
            self.play(TransformMatchingTex(VGroup(general_ohm, noeud), is_ohm), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        b1_ohm = MathTex("U_1", "=", "R_1", r"\times", "I_1").shift(DOWN + LEFT * 2)
        b2_ohm = MathTex("U_2", "=", "R_2", r"\times", "I_2").shift(DOWN + RIGHT * 2)
        with self.my_voiceover(
                r"""Pour chacune de nos branches, d'après la loi d'ohm on a: 
> - $U_1 = R_1 \times I_1$
> - $U_2 = R_2 \times I_2$""") as timer:
            self.play(Succession(Write(b1_ohm), Write(b2_ohm)), run_time=timer.duration)
        i1 = MathTex("I_1", "=", *my_frac(["U_1"], ["R_1"])).shift(DOWN + LEFT * 2)
        i2 = MathTex("I_2", "=", *my_frac(["U_2"], ["R_2"])).shift(DOWN + RIGHT * 2)
        with self.my_voiceover(
                r"""On peut alors trouver que 
> - $I_1 = \frac{U_1}{R_1}$
> - $I_2 = \frac{U_2}{R_2}$""") as timer:
            self.play(AnimationGroup(TransformMatchingTex(b1_ohm, i1), TransformMatchingTex(b2_ohm, i2)),
                      run_time=timer.duration)
        extended_ohm = MathTex("U", "=", "R", r"\times", "(", *my_frac(["U_1"], ["R_1"]), "+",
                               *my_frac(["U_2"], ["R_2"]), ")")
        with self.my_voiceover(
                r"""En combinant nos équations on obtient
>   $$U = R \times ( \frac{U_1}{R_1} + \frac{U_2}{R_2})$$""") as timer:
            self.play(TransformMatchingTex(VGroup(i1, i2, is_ohm), extended_ohm),
                      run_time=timer.duration)
        self.next_section(skip_animations=False)
        mailles = MathTex("U_1", "=", "U_2", "=" , "U").shift(DOWN)
        with self.my_voiceover(
                r"""La loi des mailles nous dit que $U_1 = U_2 = U$""") as timer:
            self.play(Write(mailles), run_time=timer.duration)
        extended_ohm_u = MathTex("U", "=", "R", r"\times", "(", *my_frac(["U"], ["R_1"]), "+",
                               *my_frac(["U"], ["R_2"]), ")")
        with self.my_voiceover(
                r"""En combinant nos équations on obtient
>   $$U = R \times ( \frac{U_1}{R_1} + \frac{U_2}{R_2})$$""") as timer:
            self.play(TransformMatchingTex(VGroup(mailles,extended_ohm), extended_ohm_u),
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
