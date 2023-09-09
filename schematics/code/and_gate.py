from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Pile_Resistance(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        battery = Battery().shift(UP + LEFT)
        resistance = Resistance().shift(UP + RIGHT)
        ameter = Ameter().shift(LEFT * 2).rotate(PI / 2)
        switch1 = Switch().shift(DOWN + RIGHT).rotate(PI)
        switch2 = Switch().shift(DOWN + LEFT).rotate(PI)
        and_gate = Circuit(
            battery,
            battery.connect(resistance),
            resistance,
            resistance.connect(switch1),
            switch1,
            switch1.connect(switch2),
            switch2,
            switch2.connect(ameter),
            ameter,
            ameter.connect(battery)
        )
        with self.my_voiceover(
                """Alors, on avait, une pile relié à une résistance, puis nos deux interrupteurs et l'amprè-mètre pour voir le courant passer.""") as timer:
            self.play(Create(and_gate), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(and_gate))
        ohmmetre = Ohmmeter().shift(UP)
        and_gate_elec = Circuit(
            ohmmetre,
            ohmmetre.connect(switch1),
            switch1,
            switch1.connect(switch2),
            switch2,
            switch2.connect(ohmmetre),
        )
        with self.my_voiceover(
                """Et en électronique, on avait remplacé notre combo pile / résistance / ampère-mètre par un ohm-mètre ce qui donne ce schema""") as timer:
            self.play(Create(and_gate_elec), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(and_gate_elec))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
