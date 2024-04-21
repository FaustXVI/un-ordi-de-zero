import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False
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
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                r"""Tout se joue donc sur l'état de l'interrupteur.""") as timer:
            self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects if o != switch],
                                     switch.animate.move_to(ORIGIN + (LEFT * 4) + UP), run_time=timer.duration))
        faux.next_to(switch, RIGHT)
        with self.my_voiceover(
                r"""Quand il est ouvert, on est dans l'état `Faux` : le courant ne passe pas""") as timer:
            self.play(AnimationGroup(switch.animate.open(), Write(faux), run_time=timer.duration))
        switch2 = switch.copy()
        self.play(switch2.animate.move_to(ORIGIN + (LEFT * 4) + DOWN))
        vrai.next_to(switch2, RIGHT)
        with self.my_voiceover(
                r"""Quand il est fermé, on est dans l'état `Vrai` : le courant passe""") as timer:
            self.play(AnimationGroup(switch2.animate.close(), Write(vrai), run_time=timer.duration))
        self.next_section(skip_animations=section_done)
        switch3 = switch.copy()
        switch4 = switch2.copy()
        faux2 = faux.copy()
        vrai2 = vrai.copy()
        c1 = VGroup(switch3, faux2)
        c2 = VGroup(switch4, vrai2)
        with self.my_voiceover(
                r"""On peut maintenant regarder ce qu'il se passe quand on met deux interrupteurs dans le circuit en faisant un tableau avec les états du premier interrupteur en lignes et les états du second en colonnes.""") as timer:
            self.play(
                AnimationGroup(c1.animate.move_to(ORIGIN + UP * 2), c2.animate.move_to(ORIGIN + UP * 2 + (RIGHT * 4)),
                               run_time=timer.duration))
        with self.my_voiceover(
                r"""En logique, on appelle ces tableaux des tables de vérités et seul les états `Vrai` et `Faux` nous interessent.""") as timer:
            self.play(AnimationGroup(FadeOut(switch), FadeOut(switch2), FadeOut(switch3), FadeOut(switch4)),
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        l1 = Line(UP * 2, DOWN * 2).shift(LEFT * 1.5)
        l2 = Line(UP * 2, DOWN * 2).shift(RIGHT * 1.5)
        l3 = Line(LEFT * 5, RIGHT * 5).shift(UP * 0.75)
        l4 = Line(LEFT * 5, RIGHT * 5).shift(DOWN * 0.75)
        lines = VGroup(l1, l2, l3, l4)
        headers = VGroup(faux, faux2, vrai, vrai2)
        table = VGroup(lines, headers)
        tableLine1 = ORIGIN
        tableCol1 = ORIGIN
        tableLine2 = DOWN * 1.5
        tableCol2 = RIGHT * 3
        lineHeaderShift = LEFT * 3
        colHeaderShift = UP * 1.5
        with self.my_voiceover(
                r"""Et chaque opération logique, comme le `ET` ou le `OU`, on leur propre table de vérité.""") as timer:
            self.play(
                Succession(AnimationGroup(
                    faux.animate.move_to(lineHeaderShift + tableLine1),
                    vrai.animate.move_to(lineHeaderShift + tableLine2),
                    faux2.animate.move_to(colHeaderShift + tableCol1),
                    vrai2.animate.move_to(colHeaderShift + tableCol2)
                ),
                    Create(lines)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        et = Text("ET").move_to(lineHeaderShift + colHeaderShift + tableCol1 + tableLine1)
        ou = Text("OU").move_to(lineHeaderShift + colHeaderShift + tableCol1 + tableLine1)
        f1 = Text("Faux").move_to(UP*10)
        f2 = Text("Faux").move_to(UP*10)
        f3 = Text("Faux").move_to(UP*10)
        v1 = Text("Vrai").move_to(UP*10)
        v2 = Text("Vrai").move_to(UP*10)
        v3 = Text("Vrai").move_to(UP*10)
        values = VGroup(f1, f2, f3, v1, v2, v3)
        with self.my_voiceover(
                r"""Par exemple, pour l'opération `ET` on obtient""") as timer:
            self.play(Write(et), run_time=timer.duration)
        f1.move_to(tableCol1 + tableLine1)
        f2.move_to(tableCol2 + tableLine1)
        f3.move_to(tableCol1 + tableLine2)
        v1.move_to(tableCol2 + tableLine2)
        with self.my_voiceover(
                r"""`FAUX` et `FAUX` donne `FAUX`""") as timer:
            self.play(Write(f1), run_time=timer.duration)
        with self.my_voiceover(
                r"""`FAUX` et `VRAI` donne `FAUX`""") as timer:
            self.play(Write(f2), run_time=timer.duration)
        with self.my_voiceover(
                r"""`VRAI` et `FAUX` donne `FAUX`""") as timer:
            self.play(Write(f3), run_time=timer.duration)
        with self.my_voiceover(
                r"""`VRAI` et `VRAI` donne `VRAI`""") as timer:
            self.play(Write(v1), run_time=timer.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                r"""Ce qui correspond bien à ce qu'on avait observé lors de la création de notre porte `ET`.""") as timer:
            self.play(Wait(), run_time=timer.duration)
        with self.my_voiceover(
                r"""Si maintenant on regarde l'opération `OU` on obtient""") as timer:
            self.play(AnimationGroup(FadeOut(values), Transform(et, ou)), run_time=timer.duration)
        f1.move_to(tableCol1 + tableLine1)
        v1.move_to(tableCol2 + tableLine1)
        v2.move_to(tableCol1 + tableLine2)
        v3.move_to(tableCol2 + tableLine2)
        with self.my_voiceover(
                r"""`FAUX` ou `FAUX` donne `FAUX`""") as timer:
            self.play(Write(f1), run_time=timer.duration)
        with self.my_voiceover(
                r"""`FAUX` ou `VRAI` donne `VRAI`""") as timer:
            self.play(Write(v1), run_time=timer.duration)
        with self.my_voiceover(
                r"""`VRAI` ou `FAUX` donne `VRAI`""") as timer:
            self.play(Write(v2), run_time=timer.duration)
        with self.my_voiceover(
                r"""`VRAI` ou `VRAI` donne `VRAI`""") as timer:
            self.play(Write(v3), run_time=timer.duration)
        with self.my_voiceover(
                r"""Ce qui correspond bien à notre circuit actuel.""") as timer:
            self.play(Wait(), run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
