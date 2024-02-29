import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


class RChoice(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        uA = MathTex("10^{-7}", " ", "A").shift(UP + LEFT)
        with self.my_voiceover(
                r"""Notre ampère-mètre peut mesurer des micro ampère avec un chiffre après la virgule soit une résolution à $10^{-7}$.""") as timer:
            self.play(Write(uA), run_time=timer.duration)
        Rmax = MathTex("10^{6}", " ", r"\Omega").next_to(uA, DOWN).align_to(uA, RIGHT)
        with self.my_voiceover(
                r"""La résistance la plus grosse que j'ai à disposition est de $1M\Omega$ soit $10^6$.""") as timer:
            self.play(Write(Rmax), run_time=timer.duration)
        U = MathTex("1.5", " ", "V").next_to(Rmax, DOWN).align_to(Rmax, RIGHT)
        with self.my_voiceover(
                r""" Si je mesure une tension de $1.5V$ avec cette résistance,""") as timer:
            self.play(Write(U), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        brace = Brace(VGroup(uA, Rmax, U), RIGHT)
        Iread = MathTex("1", ".", "5", " ", r"\mu", "A").next_to(brace, RIGHT)
        with self.my_voiceover(
                r"""je devrait lire $1.5\mu A$ sur mon ampère mètre.""") as timer:
            self.play(Succession(Write(brace), Write(Iread)), run_time=timer.duration)
        imp = MathTex(r"\pm", r"1", r"\%").next_to(Iread, RIGHT)
        with self.my_voiceover(
                r"""Cependant, si je tiens compte de la résolution de mon ampère mètre et de son exactitude de $\pm$ 1%,""") as timer:
            self.play(Write(imp), run_time=timer.duration)
        Iread_max = MathTex("1.6", r"\mu", "A").next_to(Iread, UP)
        Iread_min = MathTex("1.4", r"\mu", "A").next_to(Iread, DOWN)
        with self.my_voiceover(
                r"""je me rends compte que ma mesure affichera quelque chose entre $1.4\mu A$ et $1.6\mu A$""") as timer:
            self.play(Succession(Write(Iread_min), Write(Iread_max)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        realImp = MathTex(r"\pm", r"1", r"0", r"\%").next_to(Iread, RIGHT)
        with self.my_voiceover(
                r"""ce qui se traduit par une imprécision de $\pm$ 10%""") as timer:
            self.play(TransformMatchingTex(VGroup(Iread_max, Iread_min, imp), realImp, fade_transform_mismatches=True),
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                r"""ce que je trouve trop important""") as timer:
            self.play(realImp.animate.set_color(RED), run_time=timer.duration)
        finalR = MathTex("10^{5}", " ", r"\Omega").next_to(uA, DOWN).align_to(uA, RIGHT)
        with self.my_voiceover(
                r"""Si j'utilise une résistance de $100K\Omega$ soit $10^5$,""") as timer:
            self.play(Succession(Indicate(Rmax), TransformMatchingTex(Rmax, finalR)), run_time=timer.duration)
        IreadFinal = MathTex("1", "5", ".", "0", " ", r"\mu", "A").next_to(brace, RIGHT)
        with self.my_voiceover(
                r"""je devrait lire $15.0\mu A$""") as timer:
            self.play(
                AnimationGroup(TransformMatchingTex(Iread, IreadFinal), realImp.animate.next_to(IreadFinal, RIGHT)),
                run_time=timer.duration)
        imp.next_to(IreadFinal, RIGHT)
        with self.my_voiceover(
                r"""et en prenant en compte de nouveau la résolution et une exactitude de $\pm$ 1%,""") as timer:
            self.play(TransformMatchingTex(realImp, imp), run_time=timer.duration)
        self.next_section(skip_animations=False)
        Iread_max = MathTex("15.2", r"\mu", "A").next_to(IreadFinal, UP)
        Iread_min = MathTex("14.8", r"\mu", "A").next_to(IreadFinal, DOWN)
        with self.my_voiceover(
                r"""il devrait s'afficher quelque chose entre $14.8\mu A$ et $15.2 \mu A$""") as timer:
            self.play(Succession(Write(Iread_min), Write(Iread_max)), run_time=timer.duration)
        impFinal = MathTex(r"\pm", r"2", r"\%").next_to(IreadFinal, RIGHT)
        with self.my_voiceover(
                r"""ce qui fait une imprécision de $\pm$ 2% qui est bien plus acceptable.""") as timer:
            self.play(TransformMatchingTex(VGroup(Iread_max, Iread_min, imp), impFinal, fade_transform_mismatches=True),
                      run_time=timer.duration)
        with self.my_voiceover(
                r"""ce qui est bien plus acceptable.""") as timer:
            self.play(impFinal.animate.set_color(GREEN), run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
