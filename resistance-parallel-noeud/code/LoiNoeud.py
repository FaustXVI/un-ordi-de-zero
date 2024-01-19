from manim import ORIGIN as origin, LEFT as left, PI as pi, UP as up, DOWN as down, RIGHT as right, DARK_BLUE
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *
from electronics import Circuit, Battery, Resistance, Ameter, Branch, Junction, Contact

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


class LoiNoeud(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                """Un nœud, c'est un point de notre circuit où il y a""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover(
                """une ou plusieurs intensités en entrée""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover(
                """et une ou plusieurs intensités en sorties.""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover(
                """Prenons un exemple avec deux intensités entrantes i1 et i2""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover(
                """et deux intensités sortantes i3 et i4""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover(
                """
                La loi des nœuds dit que tout ce qui entre dans un nœud doit sortir.
 
 C'est ce que l'on appelle la conservation des charges électriques et c'est quelque chose qui était sous entendu et nécessaire dans mon explication de la loi des mailles.
                """) as timer:
            # multiples electrons entering / exiting from différent points
            self.wait(timer.duration)
        with self.my_voiceover(
                """Ça veut dire que la somme des intensités entrantes est égale à l'opposé de la somme des intensités sortantes.""") as timer:
            # i_1 + i_2 = i_3 + i_4
            self.wait(timer.duration)
        with self.my_voiceover(
                """Cependant, une intensité peut être mesurée dans les deux sens, on peut donc tout mesurer comme si on avait que des intensités entrantes. On a juste à inverser i3 et i4""") as timer:
            # i_1 + i_2 = (-i_3) + (-i_4)
            self.wait(timer.duration)
        with self.my_voiceover(
                """Si on passe i3 et i4 de l'autre côté, on obtient""") as timer:
            # i_1 + i_2 + i_3 + i_4 = 0
            self.wait(timer.duration)
        with self.my_voiceover(
                """Si on généralise, on retrouve la vrai formulation de la loi des nœuds : la sommes des intensités en un point, toutes mesurées dans le même sens par rapport au nœud, est égal à zéro""") as timer:
            # \sum_{n}{i_n} = 0
            self.wait(timer.duration)
        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
