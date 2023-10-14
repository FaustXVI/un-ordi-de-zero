from manim import UP as up, DOWN as down
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *
from electronics import Circuit, Battery, Resistance

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


class LoiMaille(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        battery = Battery().shift(up)
        resistance = Resistance().shift(down).rotate(PI)
        simple_circuit = Circuit(
            battery,
            battery.connect(resistance),
            resistance,
            resistance.connect(battery)
        )
        u_battery = Arrow(start=battery.entry_point(), end=battery.exit_point()).shift(UP)
        u_resistance = Arrow(start=resistance.entry_point(), end=resistance.exit_point()).shift(DOWN)

        parallel_circuit = self.create_parallel_circuit()
        conservationEnergie = MathTex(r"\sum_{n}", r"{E\ consommee_n}", " = ", r"\sum_{n}", r"{E\ produite_n}")
        conservationTension = MathTex(r"\sum_{n}", r"{U\ consommee_n}", " = ", r"\sum_{n}", r"{U\ produite_n}")
        loiMaille = MathTex(r"""\sum_{n}{U_n} = 0""")
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Pour rappel, la loi des mailles s'intéresse aux tensions, et les tensions c'est une histoire d'énergie. Il faut donc respecter la loi de conservation de l'énergie, c'est à dire que la somme des énergies consommées doit être égale à la somme des énergie produites.""") as timer:
            self.play(Write(conservationEnergie), run_time=timer.duration)
        with self.my_voiceover(
                """Comme nous on parle d'électricité, on parle d'énergie par Coulomb, dit autrement, de tensions. On obtient donc la somme des tensions consommées est égale à la somme des tensions produites""") as timer:
            self.play(TransformMatchingTex(conservationEnergie, conservationTension), run_time=timer.duration)
        with self.my_voiceover(
                """Mettons ça de côté pour voir ce que ça donne""") as timer:
            self.play(conservationTension.animate.scale(1 / 2).to_corner(LEFT + UP), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """sur un circuit très simple, composé d'une pile et d'une résistance.""") as timer:
            self.play(Create(simple_circuit), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """La tension consommée par la résistance doit être égale à celle générée par la pile.""") as timer:
            self.play(Succession(FadeIn(u_resistance), FadeIn(u_battery)), run_time=timer.duration)
        with self.my_voiceover(
                """On constate que les flèches des tensions vont dans des sens différents par rapport au circuit, qu'on appel aussi maille.""") as timer:
            self.wait(timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Or, il est facile d'inverser le sens d'une flèche, il suffit de prendre la mesure dans l'autre sens.Cela reviens à mesurer une tension produite comme si c'était une tension consommée.""") as timer:
            self.play(Rotate(u_battery), run_time=timer.duration)
        with self.my_voiceover(
                """On aura juste une valeur négative dans le cas où il s'agit d'un tension produite mesurée à l'envers.""") as timer:
            self.wait(timer.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                """De plus, maintenant que toutes les flèches sont dans le même sens, on obtient ce que l'on appelle une maille orientée.""") as timer:
            self.play(Create(Arc(angle=1.75*PI)), run_time=timer.duration)
        self.wait()

    def create_parallel_circuit(self):
        battery = Battery().shift(LEFT * 2).rotate(-PI / 2)
        r1 = Resistance().shift(UP)
        r2 = Resistance().shift(DOWN)
        ameter1 = Ameter().shift(UP + RIGHT * 2)
        ameter2 = Ameter().shift(DOWN + RIGHT * 2)
        b1 = Branch(r1, r1.connect(ameter1), ameter1)
        b2 = Branch(r2, r2.connect(ameter2), ameter2)
        j = Junction(b1, b2).shift(DOWN)
        c = Contact(j.exit_point() + RIGHT)
        return Circuit(
            battery,
            battery.connect(j),
            j,
            j.connect(c),
            c,
            c.connect(battery)
        )


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
