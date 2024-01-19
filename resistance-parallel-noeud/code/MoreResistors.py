from manim import ORIGIN as origin, LEFT as left, PI as pi, UP as up, DOWN as down, RIGHT as right, DARK_BLUE
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *
from electronics import Circuit, Battery, Resistance, Ameter, Branch, Junction, Contact

locale.setlocale(locale.LC_ALL, 'en_US.utf8')

section_done = False


class MoreResistors(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        cable_r_color = DARK_BLUE
        cable_bb_color = PINK
        cable_kt_color = ORANGE
        intarnal_color = GREEN
        self.next_section(skip_animations=section_done)
        batteryO = Battery().rotate(-PI / 2)
        battery = batteryO.copy()
        r1 = Resistance()
        r2 = Resistance()
        ameter1 = Ameter()
        ameter2 = Ameter()
        b1 = Branch(r1, ameter1, id=1)
        b2 = Branch(r2, ameter2, id=2)
        j = Junction(b1, b2)
        b3 = Branch(j)
        b3.shift(battery.exit_point() - b3.entry_point() + RIGHT)
        c = Contact().next_to(b3, RIGHT)
        parallel_circuit_full = Circuit(
            battery,
            b3,
            c,
            auto_align=False
        ).move_to(ORIGIN)
        with self.my_voiceover(
                """Bonne idée, commençons par reprendre notre circuit théorique.
""") as timer:
            self.play(Create(parallel_circuit_full), run_time=timer.duration)
        with self.my_voiceover(
                """La différence entre un fil en théorie et un fil en pratique, c'est qu'en vrai, les fils ont une résistance.""") as timer:
            self.play(Wait(), run_time=timer.duration)

        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
