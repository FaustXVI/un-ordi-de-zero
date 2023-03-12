from colour import Color
from manim import *
from manim.__main__ import main
from MyScene import MyScene

section_done = True


class Electron(Dot):

    def __init__(self, **kwargs):
        super().__init__(color=YELLOW, **kwargs)


class Shell(VGroup):

    def __init__(self, n, radius=1, **kwargs):
        self.opacities = [ValueTracker(0) for _ in range(n)]
        self.shell = Circle(radius=radius, color=WHITE, stroke_width=1, stroke_opacity=0)
        self.electrons = [Electron(fill_opacity=0) for _ in range(n)]
        self.shell.add_updater(lambda m, dt: m.rotate(dt * PI).set_stroke(opacity=self.opacities[0].get_value()))
        for i in range(n):
            self.electrons[i].add_updater(
                lambda m, dt, i=i: m.move_to(self.shell.get_start()).rotate(2 * PI * (i / n),
                                                                            about_point=self.shell.get_center()).set_fill(
                    opacity=self.opacities[i].get_value()))
        super().__init__(self.shell, *self.electrons, **kwargs)

    def fade_electron_in(self, n):
        return self.opacities[n].animate.set_value(1)

    def fade_out(self):
        return AnimationGroup(*[o.animate.set_value(0) for o in self.opacities])

    def get_electron(self, n):
        return self.electrons[n]


class Resistivity_Part_1(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        screen = FullScreenRectangle()
        ptable = [
            ["H", "He"],
            ["Li", "Be", "B", "C", "N", "O", "F", "Ne"],
            ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"],
        ]
        elements = [MathTex(s) for l in ptable for s in l]
        nucleus = elements[0]
        shellValances = [len(line) for line in ptable]
        shells = [Shell(n, radius=(i + 1) * 0.5) for i, n in enumerate(shellValances)]
        firstShell = shells[0]
        make_transition = lambda element, shell, electron: AnimationGroup(shell.fade_electron_in(electron),
                                                                          nucleus.animate.become(element))
        transitions = [make_transition(MathTex(element), shells[line_number], electron_number) for line_number, line in
                       enumerate(ptable) for electron_number, element in enumerate(line)]

        valanceShell = Shell(8)
        copper = MathTex("Cu")
        free_electron = Electron().to_edge(LEFT, buff=0).shift(LEFT)
        self.add(*shells)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Pour commencer, sache qu'on va utiliser un modèle atomique suffisament correct pour comprendre le concept de resistance mais qui reste bien plus simple que le modèle atomique réel""") as traker:
            text = Text(r"Simplifications devant !")
            self.play(Succession(FadeIn(text), Wait(), FadeOut(text)), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                "Un atome, c'est composé d'un noyeau qu'on va représenter par la lettre de l'élément") as traker:
            self.play(FadeIn(nucleus), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("et d'éléctrons qui tournent autour du noyau") as traker:
            self.play(firstShell.fade_electron_in(0), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("""Les éléctrons se répartissent en couches et on ne  peut passer à la couche N+1 qu'après avoir remplis complètement la couche N.\n
        Les 3 premières couches contiennent respectivement 2, 8, 8 éléctrons""") as traker:
            self.play(Succession(*transitions[1:]), run_time=max(traker.duration, len(elements)))
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """La dernière couche d'électrons d'un atome est appelé la couche de valence.""") as traker:
            self.play(Indicate(shells[-1]), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """C'est la seule qui va nous interesser, donc à partir de maintenant, c'est la seule qu'on va représenter""") as traker:
            self.play(*[s.fade_out() for s in shells[:-1]], run_time=traker.duration)
        self.play(shells[-1].animate.scale(2 / 3))
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Pour la suite, nous allons regarder un atome de cuivre qui a la particularité de n'avoir qu'un seul electron sur sa couche de valance""") as traker:
            self.add(valanceShell)
            self.play(Succession(AnimationGroup(shells[-1].fade_out(), FadeOut(nucleus)),
                                 AnimationGroup(FadeIn(copper), valanceShell.fade_electron_in(0))),
                      run_time=traker.duration)
            self.remove(nucleus, *shells)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Quand un electron libre arrive à proximité de l'atome, il y a deux scenarios possible""",
                duration=1.33) as traker:
            free_electron.save_state()
            self.add(free_electron)
            self.wait(traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Soit il arrive à un endroit où il y a déjà un électron. Et dans ce cas l'électron déjà en place repousse l'électron libre""") as traker:
            p = valanceShell.get_electron(0).copy().rotate(traker.duration * PI / 2,
                                                           about_point=valanceShell.get_center()).get_center()
            path = Line(screen.get_edge_center(LEFT) + LEFT, p + (LEFT * 0.5))
            self.play(MoveAlongPath(free_electron, path, rate_func=there_and_back), run_time=traker.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                """Soit il arrive à un endroit où il n'y a pas d'électron et se met sur la couche de valance""") as traker:
            p = valanceShell.get_electron(4).copy().rotate(traker.duration * PI,
                                                           about_point=valanceShell.get_center()).get_center()
            path = Line(screen.get_edge_center(LEFT) + LEFT, p)
            self.play(MoveAlongPath(free_electron, path, rate_func=linear), run_time=traker.duration)
            free_electron.to_edge(LEFT).shift(LEFT)
            valanceShell.opacities[4].set_value(1)

        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
