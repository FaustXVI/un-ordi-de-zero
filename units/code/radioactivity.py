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
        core = VGroup().rotate(angle=PI/4)
        core.add(Proton())
        self.play(Create(shell), Create(electron), Create(core))
        self.wait()
        n_core = core.copy().add(Neutron()).arrange(buff=0).rotate(angle=PI/4)
        self.play(ReplacementTransform(core, n_core))
        neutron = Neutron()
        n2_core = n_core.copy().add(neutron).arrange_in_grid(buff=0)
        neutron.shift(RIGHT*neutron.radius)
        n2_core.rotate(angle=PI/4)
        self.play(ReplacementTransform(n_core, n2_core))
        n3_core = n2_core.copy().add(Neutron()).arrange_in_grid(buff=0).rotate(angle=PI/4)
        self.play(ReplacementTransform(n2_core,n3_core))
        self.play(Wiggle(n3_core,scale_value=1.3,rotation_angle=0.05*TAU,n_wiggles=10))
        n_radio = n3_core.copy()
        n = n_radio.submobjects[-1]
        n_radio.remove(n)
        self.remove(n3_core)
        self.add(n_radio)
        self.play(n.animate.to_edge(RIGHT).shift(RIGHT))
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
