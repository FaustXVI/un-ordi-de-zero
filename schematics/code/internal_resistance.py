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
        self.play(FadeOut(cable))
        battery = Battery()
        with self.my_voiceover("""Ensuite, on a la pile, qu'on représente avec deux barres verticales.
La bare la plus longue représente la cathode, qu'on marque souvent avec un + sur les piles.
Et le côté le plus court représente l'anode.""") as timer:
            self.play(Create(battery), run_time=timer.duration)
        self.play(FadeOut(battery))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
