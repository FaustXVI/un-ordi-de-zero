import random

from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class LoiNoeud(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        self.next_section(skip_animations=section_done)
        node = Dot()
        lineFactor = 4.5
        lineI1 = Line(start=LEFT * lineFactor + UP * lineFactor, end=ORIGIN)
        i1 = Arrow(start=LEFT + UP, end=ORIGIN).move_to(LEFT * 2 + UP * 2.5)
        i1Label = MathTex("i_1").move_to(i1.get_center() + (RIGHT + UP) * 0.25)
        lineI2 = Line(start=LEFT * lineFactor + DOWN * lineFactor, end=ORIGIN)
        i2 = Arrow(start=LEFT + DOWN, end=ORIGIN).move_to(LEFT * 2 + DOWN * 2.5)
        i2Label = MathTex("i_2").move_to(i2.get_center() + (RIGHT + DOWN) * 0.25)
        lineI3 = Line(end=RIGHT * lineFactor + UP * lineFactor, start=ORIGIN)
        i3 = Arrow(end=RIGHT + UP, start=ORIGIN).move_to(RIGHT * 2 + UP * 2.5)
        i3Label = MathTex("i_3").move_to(i3.get_center() + (LEFT + UP) * 0.25)
        lineI4 = Line(end=RIGHT * lineFactor + DOWN * lineFactor, start=ORIGIN)
        i4 = Arrow(end=RIGHT + DOWN, start=ORIGIN).move_to(RIGHT * 2 + DOWN * 2.5)
        i4Label = MathTex("i_4").move_to(i4.get_center() + (LEFT + DOWN) * 0.25)
        with self.my_voiceover(
                """Un nœud, c'est un point de notre circuit où il y a : """) as timer:
            self.play(Create(node), run_time=timer.duration)
        with self.my_voiceover(
                """une ou plusieurs intensités en entrée""") as timer:
            self.play(AnimationGroup(Create(lineI1), Create(lineI2), lag_ratio=0.66), run_time=timer.duration)
        with self.my_voiceover(
                """et une ou plusieurs intensités en sorties.""") as timer:
            self.play(AnimationGroup(Create(lineI3), Create(lineI4), lag_ratio=0.66), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Prenons un exemple avec deux intensités entrantes i1 et i2""") as timer:
            self.play(AnimationGroup(
                AnimationGroup(Create(i1), Create(i1Label), lag_ratio=0.66),
                AnimationGroup(Create(i2), Create(i2Label), lag_ratio=0.66), lag_ratio=0.66
            ), run_time=timer.duration)
        with self.my_voiceover(
                """et deux intensités sortantes i3 et i4""") as timer:
            self.play(AnimationGroup(
                AnimationGroup(Create(i3), Create(i3Label), lag_ratio=0.66),
                AnimationGroup(Create(i4), Create(i4Label), lag_ratio=0.66), lag_ratio=0.66
            ), run_time=timer.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                """
                La loi des nœuds dit que tout ce qui entre dans un nœud doit sortir.
 
 C'est ce que l'on appelle la conservation des charges électriques et c'est quelque chose qui était sous entendu 
 et nécessaire dans mon explication de la loi des mailles.
                """) as timer:
            electrons = [Dot(color=YELLOW) for i in range(0, round(timer.duration) * 2)]
            animations = [Succession(
                MoveAlongPath(e, random.choice([lineI1, lineI2]), rate_functions=linear),
                MoveAlongPath(e, random.choice([lineI3, lineI4]), rate_functions=linear)
                , rate_functions=linear
            ) for e in electrons]
            self.play(AnimationGroup(*animations, lag_ratio=0.2, rate_functions=linear), rate_functions=linear,
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        simpleSum = MathTex("i_1", "+", "i_2", "=", "i_3", "+", "i_4")
        with self.my_voiceover(
                """Ça veut dire que la somme des intensités entrantes est égale à la somme des intensités sortantes.""") as timer:
            self.play(Succession(AnimationGroup(*[FadeOut(o) for o in self.mobjects]), Create(simpleSum)),
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        oppositeSum = MathTex("i_1", "+", "i_2", "=", "(-", "i_3", ")", "+ ", "(-", "i_4", ")")
        with self.my_voiceover(
                """Cependant, une intensité peut être mesurée dans les deux sens, on peut donc tout mesurer comme si on avait que des intensités entrantes. Le signe de i3 et i4 est alors opposé""") as timer:
            self.play(TransformMatchingTex(simpleSum, oppositeSum),run_time=timer.duration)
        flippedSum = MathTex("i_1", "+", "i_2", "+ ", "i_3", "+ ", "i_4", "=", "0")
        with self.my_voiceover(
                """Si on passe i3 et i4 de l'autre côté, on obtient , i1 + i2 + i3 + i4 = 0""") as timer:
            self.play(TransformMatchingTex(oppositeSum, flippedSum),run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        finalSum = MathTex("\sum_{n}{", "i_n", "}", "=", "0")
        with self.my_voiceover(
                """Si on généralise, on retrouve la vrai formulation de la loi des nœuds : la sommes des intensités en un point, toutes mesurées dans le même sens par rapport au nœud, est égal à zéro""") as timer:
            self.play(TransformMatchingTex(flippedSum, finalSum, key_map={"i_4": "i_n"}),run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
