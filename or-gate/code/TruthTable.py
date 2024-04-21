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
        self.next_section(skip_animations=False)
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
                r"""Ainsi, si on prends un circuit simple contenant juste une pile et un interrupteur. """) as timer:
            self.play(Write(circuit), run_time=timer.duration)
        faux = Text("Faux")
        vrai = Text("Vrai")
        with self.my_voiceover(
                r"""Quand l'interrupteur est ouvert, l'affirmation est `Fausse`, car aucun courant ne passe.""") as timer:
            self.play(Write(faux), run_time=timer.duration)
        with self.my_voiceover(
                r"""Quand l'interrupteur est fermé, l'affirmation est Vrai, car du courant passe.""") as timer:
            self.play(AnimationGroup(switch.animate.close(), Transform(faux, vrai), circuit.run_electron()), run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
