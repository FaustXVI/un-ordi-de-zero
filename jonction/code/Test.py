from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Test(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        battery = Battery().shift(LEFT * 2).rotate(-PI / 2)
        r1 = Resistance().shift(UP)
        r2 = Resistance().shift(DOWN)
        ameter1 = Ameter().shift(UP + RIGHT * 2)
        ameter2 = Ameter().shift(DOWN + RIGHT * 2)
        j1 = Junction(Branch(r1, r1.connect(ameter1), ameter1), Branch(r2, r2.connect(ameter2), ameter2)).shift(DOWN)
        j2 = Junction(Branch(r1), Branch(r2)).shift(DOWN)
        c = Contact(j1.exit_point() + RIGHT)

        circuit1 = Circuit(
            battery,
            battery.connect(j1),
            j1,
            j1.connect(c),
            c,
            c.connect(battery)
        )
        circuit2 = Circuit(
            battery,
            battery.connect(j2),
            j2,
            j2.connect(c),
            c,
            c.connect(battery)
        )
        self.play(Create(circuit1), run_time=3)
        self.wait()
        self.play(Transform(circuit1, circuit2), run_time=3)
        self.wait()
        self.play(FadeOut(circuit2))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
