from manim import ORIGIN as origin, LEFT as left, PI as pi, UP as up, DOWN as down, RIGHT as right, DARK_BLUE
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *
from electronics import Circuit, Battery, Resistance, Ameter, Branch, Junction, Contact

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class MoreResistors(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        cable_r_color = DARK_BLUE
        cable_bb_color = PINK
        cable_kt_color = ORANGE
        intarnal_color = GREEN
        self.next_section(skip_animations=section_done)
        batteryO = Battery().rotate(-PI / 2)
        battery = batteryO.copy()
        r1 = Resistance()
        r2 = Resistance()
        ameter1 = Ameter()
        ameter2 = Ameter()
        b1 = Branch(r1, ameter1, id=1)
        b2 = Branch(r2, ameter2, id=2)
        j = Junction(b1, b2)
        b3 = Branch(j)
        b3.shift(battery.exit_point() - b3.entry_point() + RIGHT)
        c = Contact().next_to(b3, RIGHT)
        parallel_circuit_full = Circuit(
            battery,
            b3,
            c,
            auto_align=False
        ).move_to(ORIGIN)
        with self.my_voiceover(
                """Bonne idée, commençons par reprendre notre circuit théorique.
""") as timer:
            self.play(Create(parallel_circuit_full), run_time=timer.duration)
        with self.my_voiceover(
                """La différence entre un fil en théorie et un fil en pratique, c'est qu'en vrai, les fils ont une résistance.""") as timer:
            self.play(Wait(), run_time=timer.duration)

        self.next_section(skip_animations=section_done)
        battery = batteryO.copy()
        rc1 = Resistance(color=cable_r_color)
        rc2 = Resistance(color=cable_r_color).rotate(PI / 2)
        rc3 = Resistance(color=cable_r_color).rotate(-PI / 2)
        rc4 = Resistance(color=cable_r_color)
        b1 = Branch(rc2.copy(), r1.copy(), ameter1.copy())
        b2 = Branch(rc3.copy(), r2.copy(), ameter2.copy())
        j = Junction(b1, b2)
        b3 = Branch(rc1.copy(), j)
        b3.shift(battery.exit_point() - b3.entry_point())
        c = c.copy().next_to(b3, RIGHT)
        b4 = Branch(rc4.copy()).next_to(battery, RIGHT).shift(UP * 2).rotate(pi)
        parallel_circuit_full_cables = Circuit(
            battery,
            b3,
            c,
            b4,
            auto_align=False
        ).move_to(origin)
        with self.my_voiceover(
                """Mettons à jour notre schema avec cette information en changeant chaque fil pour y ajouter une résistance, en bleu pour les reconnaître.""") as timer:
            self.play(
                transformCircuitById(parallel_circuit_full, parallel_circuit_full_cables),
                run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        self.wait()

        battery = batteryO.copy()
        rc5 = Resistance(color=cable_r_color)
        rc6 = Resistance(color=cable_r_color)
        rc7 = Resistance(color=cable_r_color)
        rc8 = Resistance(color=cable_r_color)
        rc9 = Resistance(color=cable_r_color).rotate(-PI / 2)
        rc10 = Resistance(color=cable_r_color).rotate(PI / 2)
        b1 = Branch(rc2.copy(), r1.copy(), rc7.copy(), ameter1.copy(), rc9.copy())
        b2 = Branch(rc3.copy(), r2.copy(), rc8.copy(), ameter2.copy(), rc10.copy())
        j = Junction(b1, b2)
        b3 = Branch(rc5.copy(), rc1.copy(), j)
        b3.shift(battery.exit_point() - b3.entry_point())
        c = c.copy().next_to(b3, RIGHT)
        b4 = Branch(rc4.copy(), rc6.copy()).next_to(battery, RIGHT).shift(UP * 2).rotate(pi)
        parallel_circuit_full_all_cables = Circuit(
            battery,
            b3,
            c,
            b4,
            auto_align=False
        ).move_to(origin)
        with self.my_voiceover(
                """Sans oublier qu'en pratique on a des fils qui vont de la pile à la breadboard et d'autres de l'ampèremètre à la breadboard .""") as timer:
            self.play(
                transformCircuitById(parallel_circuit_full_cables, parallel_circuit_full_all_cables),
                run_time=timer.duration)
        with self.my_voiceover(
                """Ca commence à prendre de la place, il va falloir écrire plus petit.""") as timer:
            self.play(parallel_circuit_full_all_cables.animate.scale(0.5),
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)

        battery = batteryO.copy()
        rbb1 = Resistance(color=cable_bb_color)
        rbb2 = Resistance(color=cable_bb_color)
        rbb3 = Resistance(color=cable_bb_color)
        rbb4 = Resistance(color=cable_bb_color)
        rbb5 = Resistance(color=cable_bb_color)
        rbb6 = Resistance(color=cable_bb_color)
        rbb7 = Resistance(color=cable_bb_color)
        rbb8 = Resistance(color=cable_bb_color)
        b1 = Branch(rc2.copy(), rbb3.copy(), r1.copy(), rbb4.copy(), rc7.copy(), ameter1.copy(), rc9.copy())
        b2 = Branch(rc3.copy(), rbb5.copy(), r2.copy(), rbb6.copy(), rc8.copy(), ameter2.copy(), rc10.copy())
        j = Junction(b1, b2)
        b3 = Branch(rc5.copy(), rbb1.copy(), rc1.copy(), rbb2.copy(), j, rbb7.copy())
        b3.shift(battery.exit_point() - b3.entry_point())
        c = c.copy().next_to(b3, RIGHT)
        b4 = Branch(rc4.copy(), rbb8.copy(), rc6.copy()).next_to(battery, RIGHT).shift(UP * 4).rotate(pi)
        parallel_circuit_full_bb = Circuit(
            battery,
            b3,
            c,
            b4,
            auto_align=False
        ).move_to(origin).scale(0.5)
        with self.my_voiceover(
                """En plus, on utilise une breadboard, qui est aussi une forme de fil aussi. On ajoute donc des résistances en rose correspondantes à chaque fois qu'on passe dans la breadboard.
""") as timer:
            self.play(
                transformCircuitById(parallel_circuit_full_all_cables, parallel_circuit_full_bb),
                run_time=timer.duration)

        self.next_section(skip_animations=section_done)

        def wrap_contacts(r, angle=0):
            id_class = r.get_id() * (-1000)
            return [Resistance(color=cable_kt_color, id=id_class - 1).rotate(angle), r,
                    Resistance(color=cable_kt_color, id=id_class + 1).rotate(angle)]

        battery = batteryO.copy()
        rkt1 = Resistance(color=cable_kt_color)
        rkt2 = Resistance(color=cable_kt_color)
        rkt3 = Resistance(color=cable_kt_color)
        rkt4 = Resistance(color=cable_kt_color)

        b1 = Branch(*wrap_contacts(rc2.copy(), angle=PI / 2), rbb3.copy(), *wrap_contacts(r1.copy()), rbb4.copy(),
                    *wrap_contacts(rc7.copy()),
                    ameter1.copy(),
                    *wrap_contacts(rc9.copy(),angle=-PI/2))
        b2 = Branch(*wrap_contacts(rc3.copy(), angle=-PI / 2), rbb5.copy(), *wrap_contacts(r2.copy()), rbb6.copy(),
                    *wrap_contacts(rc8.copy()), ameter2.copy(), *wrap_contacts(rc10.copy(),angle=PI/2))
        j = Junction(b1, b2)
        b3 = Branch(rkt1.copy(), rc5.copy(), *wrap_contacts(rbb1.copy()), rc1.copy(), rkt3.copy(),
                    rbb2.copy(), j, rbb7.copy(),rkt4.copy())
        b3.shift(battery.exit_point() - b3.entry_point())
        c = c.copy().next_to(b3, RIGHT)
        b4 = Branch(rc4.copy(), *wrap_contacts(rbb8.copy()), rc6.copy(),rkt2.copy()).next_to(battery, RIGHT).shift(UP * 8).rotate(pi)
        parallel_circuit_full_kt = Circuit(
            battery,
            b3,
            c,
            b4,
            auto_align=False
        ).move_to(origin).scale(0.33)
        with self.my_voiceover(
                """Et d'ailleurs, pour passer d'un fil à autre chose, on a des contacts à chaque fois, qui ont leur propre résistance qu'on peut représenter en orange.""") as timer:
            self.play(
                transformCircuitById(parallel_circuit_full_bb, parallel_circuit_full_kt),
                run_time=timer.duration)


        self.next_section(skip_animations=False)

        battery = batteryO.copy()
        ri1 = Resistance(color=intarnal_color).rotate(-PI/2)
        ri2 = Resistance(color=intarnal_color)
        ri3 = Resistance(color=intarnal_color)
        b1 = Branch(*wrap_contacts(rc2.copy(), angle=PI / 2), rbb3.copy(), *wrap_contacts(r1.copy()), rbb4.copy(),
                    *wrap_contacts(rc7.copy()),
                    ri2.copy(),
                    ameter1.copy(),
                    *wrap_contacts(rc9.copy(),angle=-PI/2))
        b2 = Branch(*wrap_contacts(rc3.copy(), angle=-PI / 2), rbb5.copy(), *wrap_contacts(r2.copy()), rbb6.copy(),
                    *wrap_contacts(rc8.copy()), ri3.copy(),ameter2.copy(), *wrap_contacts(rc10.copy(),angle=PI/2))
        j = Junction(b1, b2)
        b3 = Branch(ri1.copy(),rkt1.copy(), rc5.copy(), *wrap_contacts(rbb1.copy()), rc1.copy(), rkt3.copy(),
                    rbb2.copy(), j, rbb7.copy(),rkt4.copy())
        b3.shift(battery.exit_point() - b3.entry_point())
        c = c.copy().next_to(b3, RIGHT)
        b4 = Branch(rc4.copy(), *wrap_contacts(rbb8.copy()), rc6.copy(),rkt2.copy()).next_to(battery, RIGHT).shift(UP * 8).rotate(pi)
        parallel_circuit_full_final = Circuit(
            battery,
            b3,
            c,
            b4,
            auto_align=False
        ).move_to(origin).scale(0.33)
        with self.my_voiceover(
                """ Et enfin, il ne faut pas oublier que la pile a une résistance interne ainsi que les ampèremètres. Qu'on peut représenter en vert.""") as timer:
            self.play(
                transformCircuitById(parallel_circuit_full_kt, parallel_circuit_full_final),
                run_time=timer.duration)

        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
