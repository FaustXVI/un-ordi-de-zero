from manim import UP as up, DOWN as down, LEFT as left, PI as pi, UP as up1, DOWN as down1, RIGHT
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *
from electronics import Circuit, Battery, Resistance, Ameter, Branch, Junction, Contact

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
        u_battery = Arrow(start=battery.exit_point(), end=battery.entry_point()).shift(UP)
        u_resistance = Arrow(start=resistance.entry_point(), end=resistance.exit_point()).shift(DOWN)
        conservationEnergie = MathTex(r"\sum_{n}{E\ consommee_n}", " = ", r"\sum_{n}{E\ produite_n}")
        conservationTension = MathTex(r"\sum_{n}{U\ consommee_n}", " = ", r"\sum_{n}{U\ produite_n}")
        conservationTensionZero = MathTex(r"\sum_{n}{U\ consommee_n}", " = ", r"0")
        loiMaille = MathTex(r"""\sum_{n}{U_n}""", " = ", "0")
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
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """De plus, maintenant que toutes les flèches sont dans le même sens, on obtient ce que l'on appelle une maille orientée.""") as timer:
            arrow = Arc(radius=1, start_angle=PI / 2.25, angle=-1.9 * PI)
            arrow.add_tip()
            arrow.move_to(ORIGIN)
            arrow.scale(1 / 3)
            self.play(
                Succession(FadeIn(arrow, run_time=timer.duration * 0.1),
                           Rotate(arrow, angle=-2 * PI),
                           FadeOut(arrow, run_time=timer.duration * 0.1)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Si on reviens à notre équation,""") as timer:
            self.play(FadeOut(simple_circuit, u_resistance, u_battery),
                      conservationTension.animate.scale(2).move_to(ORIGIN), run_time=timer.duration)
        with self.my_voiceover(
                """nous n'avons plus de tension produite, donc leur somme vaut zéro.""") as timer:
            self.play(TransformMatchingTex(conservationTension, conservationTensionZero,
                                           key_map={r"\sum_{n}{U\ produite_n}": "0"}), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """On retrouve alors la loi des mailles telle qu'elle est habituellement exprimée : La somme des tensions dans une maille orientée est égale à zéro.""") as timer:
            self.play(TransformMatchingTex(conservationTensionZero, loiMaille, fade_transform_mismatches=True),
                      run_time=timer.duration)
        self.next_section(skip_animations=section_done)

        battery = Battery().shift(left * 2).rotate(-pi / 2)
        r1 = Resistance().shift(up1)
        r2 = Resistance().shift(down1)
        ameter1 = Ameter().shift(up1 + RIGHT * 2)
        ameter2 = Ameter().shift(down1 + RIGHT * 2)
        b1 = Branch(r1, r1.connect(ameter1), ameter1)
        b2 = Branch(r2, r2.connect(ameter2), ameter2)
        j = Junction(b1, b2).shift(down1)
        c = Contact(j.exit_point() + RIGHT)
        parallel_circuit_full = Circuit(
            battery,
            battery.connect(j),
            j,
            j.connect(c),
            c,
            c.connect(battery)
        ).move_to(ORIGIN)
        c1 = Contact(ameter1.exit_point())
        c2 = Contact(ameter2.exit_point())
        b1prime = Branch(r1.copy(), r1.connect(c1), c1)
        b2prime = Branch(r2.copy(), r2.connect(c2), c2)
        j2 = Junction(b1prime, b2prime)
        parallel_circuit = Circuit(
            battery.copy(),
            battery.connect(j2),
            j2,
            j2.connect(c),
            c.copy(),
            c.connect(battery)
        )
        with self.my_voiceover(
                """Maintenant que nous avons correctement défini la loi des mailles, mettons la de coté et""") as timer:
            self.play(loiMaille.animate.scale(1 / 2).to_corner(UP + LEFT), run_time=timer.duration)
        with self.my_voiceover(
                """regardons ce que cela donne sur notre circuit avec nos résistances en parallèles""") as timer:
            self.play(Create(parallel_circuit_full), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """On y vois une grande boucle composée de notre circuit""") as timer:
            arrow = Arc(radius=parallel_circuit_full.width / 2, start_angle=PI / 2.25, angle=-1.9 * PI)
            arrow.add_tip()
            arrow.move_to(parallel_circuit_full.get_center())
            arrow.scale(0.85)
            self.play(
                Succession(FadeIn(arrow, run_time=timer.duration * 0.1),
                           Rotate(arrow, angle=-2 * PI),
                           FadeOut(arrow, run_time=timer.duration * 0.1)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """ainsi qu'une petite boucle intérieure.""") as timer:
            arrow = Arc(radius=j.width / 2, start_angle=PI / 2.25, angle=-1.9 * PI)
            arrow.add_tip()
            arrow.move_to(j.get_center())
            arrow.scale(1 / 4)
            self.play(
                Succession(FadeIn(arrow, run_time=timer.duration * 0.1),
                           Rotate(arrow, angle=-2 * PI),
                           FadeOut(arrow, run_time=timer.duration * 0.1)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Les ampères mètres n'étant là que pour nous permettre de mesurer, on peut les supprimer le temps de notre réflexion.""") as timer:
            self.play(FadeOut(parallel_circuit_full), FadeIn(parallel_circuit), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        dotA = Dot(point=battery.exit_point())
        dotB = Dot(point=j2.entry_point())
        dotC = Dot(point=j2.exit_point())
        dotD = Dot(point=battery.entry_point())
        a = MathTex("A").next_to(dotA.get_center(), direction=LEFT)
        b = MathTex("B").next_to(dotB.get_center(), direction=DOWN + LEFT)
        c = MathTex("C").next_to(dotC.get_center(), direction=DOWN + RIGHT)
        d = MathTex("D").next_to(dotD.get_center(), direction=LEFT)
        with self.my_voiceover(
                """On peut y placer 4 points.""") as timer:
            self.play(Wait(), run_time=timer.duration)
        with self.my_voiceover(
                """A sur l'anode de notre plie,""") as timer:
            self.play(Create(VGroup(a, dotA)), run_time=timer.duration)
        with self.my_voiceover(
                """B à la création des branches,""") as timer:
            self.play(Create(VGroup(b, dotB)), run_time=timer.duration)
        with self.my_voiceover(
                """C à la fin des branches,""") as timer:
            self.play(Create(VGroup(c, dotC)), run_time=timer.duration)
        with self.my_voiceover(
                """D sur la cathode de notre pile.""") as timer:
            self.play(Create(VGroup(d, dotD)), run_time=timer.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                """Dans notre boucle intérieure, la loi des mailles nous dit que U_{bc} + U_{cb} = 0""") as timer:
            little_loop_maille = MathTex("U_{bc} + U_{cb} = 0").move_to(j2.get_center())
            self.play(Write(little_loop_maille), run_time=timer.duration)
        with self.my_voiceover(
                """ ce qui est plutôt logique puisqu'on mesure la même tension dans deux sens différents.""") as timer:
            self.play(Wait(), run_time=timer.duration)
        with self.my_voiceover(
                """Notre boucle extérieure est plus intérésante.""") as timer:
            self.play(FadeOut(little_loop_maille), run_time=timer.duration)
        self.next_section(skip_animations=False)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
