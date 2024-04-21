import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True
recording = False


class TruthTable(MyScene):

    def __init__(self):
        super().__init__(recording=recording)

    def construct(self):
        self.next_section(skip_animations=section_done)
        affirm = Text("""Du courant passe.""").shift(UP * 2)
        with self.my_voiceover(
                r"""Tout ce qui va suivre tourne autour de l'affirmation suivante : `Du courant passe.`""") as timer:
            self.play(Write(affirm), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        bat = Battery().shift(UP).rotate(PI)
        switch = Switch().shift(DOWN + LEFT)
        r = Resistance().shift(DOWN + RIGHT)
        circuit = Circuit(
            bat,
            bat.connect(switch),
            switch,
            switch.connect(r),
            r,
            r.connect(bat)
        )
        with self.my_voiceover(
                r"""Ainsi, si on prends un circuit simple contenant juste une pile, un interrupteur et une résistance. """) as timer:
            self.play(Create(circuit), run_time=timer.duration)
        faux = Text("Faux")
        vrai = Text("Vrai")
        with self.my_voiceover(
                r"""Quand l'interrupteur est ouvert, l'affirmation est `Fausse`, car aucun courant ne passe.""") as timer:
            self.play(Write(faux), run_time=timer.duration)
        with self.my_voiceover(
                r"""Quand l'interrupteur est fermé,""") as timer:
            self.play(AnimationGroup(switch.animate.close(), FadeOut(faux)), run_time=timer.duration)
        with self.my_voiceover(
                r"""l'affirmation est Vrai, car du courant passe.""") as timer:
            self.play(AnimationGroup(circuit.run_electron(), Write(vrai)), run_time=timer.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                r"""Tout ce joue donc sur l'état de l'interrupteur.""") as timer:
            self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects if o != switch],
                                     switch.animate.move_to(ORIGIN + LEFT + UP), run_time=timer.duration))
        faux.next_to(switch,RIGHT)
        with self.my_voiceover(
                r"""Quand il est ouvert, on est dans l'état `Faux` : le courant ne passe pas""") as timer:
            self.play(AnimationGroup(switch.animate.open(), Write(faux), run_time=timer.duration))
        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
