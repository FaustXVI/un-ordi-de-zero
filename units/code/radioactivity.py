import math
import operator
from itertools import accumulate

from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Electron(Dot):

    def __init__(self, **kwargs):
        super().__init__(color=YELLOW, **kwargs)


class Proton(Dot):

    def __init__(self, **kwargs):
        super().__init__(color=RED, **kwargs)


class Neutron(Dot):

    def __init__(self, **kwargs):
        super().__init__(color=BLUE, **kwargs)


class Radioactivity(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        shell = Circle(radius=1, color=WHITE, stroke_width=1, )
        shell.add_updater(lambda m, dt: m.rotate(dt * PI))
        electron = Electron()
        electron.add_updater(lambda m, dt: m.move_to(shell.get_start()))
        core = VGroup().rotate(angle=PI / 4)
        core.add(Proton())
        with self.my_voiceover("""Prenons l'élément le plus simple de l'univer : l'hydrogène.""") as t:
            self.play(Create(shell), Create(electron), Create(core), run_time=t.duration)
        with self.my_voiceover("""Il est composé d'un éléctron""") as t:
            self.play(Indicate(electron, scale_factor=2), run_time=t.duration)
        with self.my_voiceover("""et d'un noyau composé d'un seul proton""") as t:
            self.play(Indicate(core, color=core.submobjects[0].get_color(), scale_factor=2), run_time=t.duration)
        self.wait()
        n_core = core.copy().add(Neutron()).arrange(buff=0).rotate(angle=PI / 4)
        with self.my_voiceover(
                """Comme tous les éléments de l'univers, l'hydrogène existe en différentes version.""") as t:
            self.play(ReplacementTransform(core, n_core), run_time=t.duration)
        neutron = Neutron()
        n2_core = n_core.copy().add(neutron).arrange_in_grid(buff=0)
        neutron.shift(RIGHT * neutron.radius)
        n2_core.rotate(angle=PI / 4)
        with self.my_voiceover(
                """Les différentes versions on un nombre de neutrons différents""") as t:
            self.play(ReplacementTransform(n_core, n2_core), run_time=t.duration)
        n3_core = n2_core.copy().add(Neutron()).arrange_in_grid(buff=0).rotate(angle=PI / 4)
        with self.my_voiceover(
                """C'est ce qu'on appèle des isotopes""") as t:
            self.play(ReplacementTransform(n2_core, n3_core), run_time=t.duration)
        with self.my_voiceover(
                """Or la grande majorité des isotopes sont instables car ils ont trop ou pas assez de neutrons""") as t:
            for _ in range(math.floor(t.duration)):
                self.play(Wiggle(n3_core, scale_value=1.3, rotation_angle=0.05 * TAU, run_time=1))
        n_radio = n3_core.copy()
        n = n_radio.submobjects[-1]
        n_radio.remove(n)
        self.remove(n3_core)
        self.add(n_radio)
        with self.my_voiceover(
                """Donc dans le temps, il vont se débarasser d'une manière ou d'une autre de neutrons.""") as t:
            self.play(n.animate(rate_functions=linear).to_edge(RIGHT).shift(RIGHT), run_time=t.duration)
        with self.my_voiceover(
                """C'est ce qu'on appelle la radioactivité""") as t:
            self.play(*[FadeOut(o) for o in self.mobjects], run_time=t.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
