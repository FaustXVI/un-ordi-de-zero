from manim import *
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Pile_Resistance(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        self.next_section(skip_animations=section_done)
        battery = Battery().shift(UP / 2)
        resistance = Resistance().shift(DOWN / 2 + RIGHT).rotate(PI)
        ameter = Ameter().shift(DOWN / 2 + LEFT).rotate(PI)
        pile_res_schema = Circuit(
            battery,
            battery.connect(resistance),
            resistance,
            resistance.connect(ameter),
            ameter,
            ameter.connect(battery)
        )
        spin = ImageMobject(
            "../../notes-un-pas-apres-l-autre/images/schematiques/sprintronics-pile-resistance.png").shift(
            DOWN * 2 + LEFT * 3).scale(0.5)
        elec = ImageMobject(
            "../../notes-un-pas-apres-l-autre/images/schematiques/electronics-pile-resistance.png").shift(
            DOWN * 2 + RIGHT * 3).scale(0.5)
        with self.my_voiceover(
                """Pour représenter ce circuit, on dessine notre symbol de pile, celui de la résistance et celui de l'ampère-mètre. Enfin on relie le tout par des fils.""") as timer:
            self.play(Create(pile_res_schema), run_time=timer.duration)
        self.wait(2)
        with self.my_voiceover(
                """Physiquement, en spintronics, ça donne ça.""") as timer:
            self.play(pile_res_schema.animate.shift(UP), FadeIn(spin), run_time=timer.duration)
        self.wait()
        with self.my_voiceover(
                """Et en électronique, ça donne ça.""") as timer:
            self.play(FadeIn(elec), run_time=timer.duration)
        self.wait()
        self.play(FadeOut(spin, elec, pile_res_schema))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
