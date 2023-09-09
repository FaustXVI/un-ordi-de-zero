from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import Cable

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Schemas(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        cable = Cable()
        with self.my_voiceover("""Prenons une pile de 1,5 volts donc U = 1,5""") as timer:
            self.play(Create(cable), run_time=timer.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
