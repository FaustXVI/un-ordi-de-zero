from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Schemas(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        cable = Cable()
        with self.my_voiceover("""Oui, commençons par le plus simple de tous : le fil.
        On peut le représenter avec un simple trait""") as timer:
            self.play(Create(cable), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(cable))
        self.next_section(skip_animations=section_done)
        battery = Battery()
        with self.my_voiceover("""Ensuite, on a la pile, qu'on représente avec deux barres verticales.
La bare la plus longue représente la cathode, qu'on marque souvent avec un + sur les piles.
Et le côté le plus court représente l'anode.""") as timer:
            self.play(Create(battery), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(battery))
        self.next_section(skip_animations=section_done)
        ameter = Ameter()
        with self.my_voiceover("""On peut représenter l'ampère-mètre avec un cercle et un A dedans.""") as timer:
            self.play(Create(ameter), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(ameter))
        self.next_section(skip_animations=section_done)
        resistance = Resistance()
        with self.my_voiceover("""La résistance se dessine comme un fil en zigzag""") as timer:
            self.play(Create(resistance), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(resistance))
        self.next_section(skip_animations=section_done)
        ohmmeter = Ohmmeter()
        with self.my_voiceover("""Le ohm-mètre se dessine comme l'ampère-mètre mais avec un omega à la place du A""") as timer:
            self.play(Create(ohmmeter), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(ohmmeter))
        self.next_section(skip_animations=section_done)
        switch = Switch()
        with self.my_voiceover("""Et enfin, l'interrupteur se représente comme un clapet.
Ainsi, on peut le dessiner ouvert""") as timer:
            self.play(Create(switch), run_time=timer.duration)
            self.wait()
        with self.my_voiceover("""Ou fermé""") as timer:
            self.play(switch.animate.close(), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(switch))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
