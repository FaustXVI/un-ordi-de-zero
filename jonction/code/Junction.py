from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class JunctionSc(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=False)
        battery = Battery().shift(LEFT * 2).rotate(-PI / 2)
        r1 = Resistance().shift(UP)
        r2 = Resistance().shift(DOWN)
        ameter1 = Ameter().shift(UP + RIGHT * 2)
        ameter2 = Ameter().shift(DOWN + RIGHT * 2)
        b1 = Branch(r1, r1.connect(ameter1), ameter1)
        b2 = Branch(r2, r2.connect(ameter2), ameter2)
        j = Junction(b1, b2).shift(DOWN)
        c = Contact(j.exit_point() + RIGHT)

        pile_res_schema = Circuit(
            battery,
            battery.connect(j),
            j,
            j.connect(c),
            c,
            c.connect(battery)
        )
        with self.my_voiceover(
                """On va bien entendu avoir une pile, puis notre jonction.

On va faire deux branches identiques avec :

- une résistance pour éviter les courts circuits
- un ampère-mètre pour voir le courant passer

Si notre jonction fonctionne correctement, on verra une valeur sur les deux ampère-mètres en même temps.""") as timer:
            self.play(Create(pile_res_schema), run_time=timer.duration)
        self.wait(2)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
