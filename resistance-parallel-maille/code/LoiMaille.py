from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


class LoiMaille(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        battery = Battery().shift(LEFT * 2).rotate(-PI / 2)
        r1 = Resistance().shift(UP)
        r2 = Resistance().shift(DOWN)
        ameter1 = Ameter().shift(UP + RIGHT * 2)
        ameter2 = Ameter().shift(DOWN + RIGHT * 2)
        b1 = Branch(r1, r1.connect(ameter1), ameter1)
        b2 = Branch(r2, r2.connect(ameter2), ameter2)
        j = Junction(b1, b2).shift(DOWN)
        c = Contact(j.exit_point() + RIGHT)

        circuit = Circuit(
            battery,
            battery.connect(j),
            j,
            j.connect(c),
            c,
            c.connect(battery)
        )
        loiMaille = MathTex(r"""\sum_{n}{U_n} = 0""")
        with self.my_voiceover(
                """La loi des mailles dit que la somme des tension est égal à 0""") as timer:
            self.play(Write(loiMaille), run_time=timer.duration)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
