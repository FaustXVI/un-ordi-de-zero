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
        self.next_section(skip_animations=section_done)
        general_ohm = MathTex("U", "=", "R", r"\times", "I")
        with self.my_voiceover(
                """Dire qu'on veut remplacer nos deux résistances par une seule résistance $R$ 
                sans impact sur le reste du circuit, 
                c'est dire que dans l'équation de la loi d'ohm, U=R I, 
                on veut que la tension $U$ et l'intensité $I$ restent les mêmes.""") as timer:
            self.play(Write(general_ohm), run_time=timer.duration)
        noeud = MathTex("I_1", "+", "I_2", "=", "I").shift(DOWN * 1.5)
        with self.my_voiceover(
                """La loi des nœuds nous dit que $I_1 + I_2 = I$""") as timer:
            self.play(Write(noeud), run_time=timer.duration)
        is_ohm = MathTex("U", "=", "R", r"\times", "(", "I_1", "+", "I_2", ")")
        with self.my_voiceover(
                r"""On obtiens donc $U = R \times (I_1 + I_2)$""") as timer:
            self.play(TransformMatchingTex(VGroup(general_ohm, noeud), is_ohm), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        b1_ohm = MathTex("U_1", "=", "R_1", r"\times", "I_1").shift(DOWN * 1.5 + LEFT * 2)
        b2_ohm = MathTex("U_2", "=", "R_2", r"\times", "I_2").shift(DOWN * 1.5 + RIGHT * 2)
        with self.my_voiceover(
                r"""Pour chacune de nos branches, d'après la loi d'ohm on a: 
> - $U_1 = R_1 \times I_1$
> - $U_2 = R_2 \times I_2$""") as timer:
            self.play(Succession(Write(b1_ohm), Write(b2_ohm)), run_time=timer.duration)
        i1 = MathTex("I_1", "=", *my_frac(["U_1"], ["R_1"])).shift(DOWN * 1.5 + LEFT * 2)
        i2 = MathTex("I_2", "=", *my_frac(["U_2"], ["R_2"])).shift(DOWN * 1.5 + RIGHT * 2)
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
        self.next_section(skip_animations=section_done)
        mailles = MathTex("U_1", "=", "U_2", "=", "U ").shift(DOWN * 1.5)
        with self.my_voiceover(
                r"""La loi des mailles nous dit que $U_1 = U_2 = U$""") as timer:
            self.play(Write(mailles), run_time=timer.duration)
        extended_ohm_u = MathTex("U", "=", "R", r"\times", "(", *my_frac(["U "], ["R_1"]), "+",
                                 *my_frac(["U "], ["R_2"]), ")")
        with self.my_voiceover(
                r"""On obtient alors $$U = R \times ( \frac{U}{R_1} + \frac{U}{R_2})$$""") as timer:
            self.play(TransformMatchingTex(VGroup(extended_ohm, mailles), extended_ohm_u),
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        extended_equiv = MathTex(*my_frac(["1"], ["R"]), "=", *my_frac(["1"], ["U"]), r"\times", "(",
                                 *my_frac(["U "], ["R_1"]), "+",
                                 *my_frac(["U "], ["R_2"]), ")")
        with self.my_voiceover(
                r"""Et en passant $U$ et $R$ de l'autre côté, on obtient :
 $$\frac{1}{R} = \frac{1}{U} \times ( \frac{U}{R_1} + \frac{U}{R_2})$$""") as timer:
            self.play(TransformMatchingTex(extended_ohm_u, extended_equiv),
                      run_time=timer.duration)
        equiv = MathTex(*my_frac(["1"], ["R"]), "=", *my_frac(["1 "], ["R_1"]), "+", *my_frac(["1 "], ["R_2"]))
        with self.my_voiceover(
                r"""On peut simplifier à droite en suppriment les $U$ :
$$\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}$$""") as timer:
            self.play(TransformMatchingTex(extended_equiv, equiv),
                      run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.remove(equiv)
        equiv = MathTex(*my_frac(["1"], ["R"]), "=", *my_frac(["1 "], ["R_1"]), "+", *my_frac(["1 "], ["R", "_2"]))
        self.add(equiv)
        equiv_general_inv = MathTex(*my_frac(["1"], ["R"]), "=", "\sum\limits_{n}", *my_frac(["1 "], ["R", "_n"]))
        with self.my_voiceover(
                r"""Si on généralise pour $N$ résistances en parallèles, on trouve que l'inverse de la résistance équivalente est égale à la somme des inverses des résistances mises en parallèles.
$$\frac{1}{R} = \sum\limits_{n}{\frac{1}{R_n}}$$""") as timer:
            self.play(TransformMatchingTex(equiv, equiv_general_inv, key_map={"+": "\sum\limits_{n}", "_2": "_n"}),
                      run_time=timer.duration)
        equiv_general = MathTex("R", "=", *my_frac(["1"],["\sum\limits_{n}", *my_frac(["1 "], ["R", "_n"])]))
        with self.my_voiceover(
                r"""ou encore que la résistance équivalente est égale à l'inverse de la somme des inverses des résistances mises en parallèles.
$$R = \frac{1}{ \sum\limits_{n} {\frac{1}{R_n}} }$$""") as timer:
            self.play(TransformMatchingTex(equiv_general_inv,equiv_general),
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
