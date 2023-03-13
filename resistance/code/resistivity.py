from colour import Color
from manim import *
from manim.__main__ import main
from MyScene import MyScene

section_done = False


class Electron(Dot):

    def __init__(self, **kwargs):
        super().__init__(color=YELLOW, **kwargs)


class Shell(VGroup):

    def __init__(self, n, radius=1, **kwargs):
        self.opacities = [ValueTracker(0) for _ in range(n)]
        self.shell = Circle(radius=radius, color=WHITE, stroke_width=1, stroke_opacity=0)
        self.electrons = [Electron(fill_opacity=0) for _ in range(n)]
        self.shell_opacity = ValueTracker(0)
        self.shell.add_updater(
            lambda m, dt: m.rotate(dt * PI).set_stroke(opacity=self.shell_opacity.get_value()))
        for i in range(n):
            self.electrons[i].add_updater(
                lambda m, dt, i=i: m.move_to(self.shell.get_start()).rotate(2 * PI * (i / n),
                                                                            about_point=self.shell.get_center()).set_fill(
                    opacity=self.opacities[i].get_value()))
        super().__init__(self.shell, *self.electrons, **kwargs)

    def fade_electron_in(self, n):
        return AnimationGroup(self.opacities[n].animate.set_value(1), self.shell_opacity.animate.set_value(1))

    def fade_out(self):
        return AnimationGroup(*[o.animate.set_value(0) for o in [*self.opacities, self.shell_opacity]])

    def get_electron(self, n):
        return self.electrons[n]


class Resistivity_Part_1(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def refuse_electron(self, duration, entry_point, indexTarget, shell):
        free_electron = Electron().move_to(entry_point)
        p = shell.get_electron(indexTarget).copy().rotate(duration * PI / 2,
                                                          about_point=shell.get_center()).get_center()
        path = Line(entry_point, p + (LEFT * 0.5))
        return MoveAlongPath(free_electron, path, rate_func=there_and_back, run_time=duration)

    def try_eject_electron(self, duration, entry_point, exit_point, indexTarget, shell):
        if shell.opacities[indexTarget].get_value() == 1:
            return (self.refuse_electron(duration, entry_point, indexTarget, shell), 0)
        else:
            return (self.eject_electron(duration, entry_point, exit_point, indexTarget, shell), 1)

    def eject_electron(self, duration, entry_point, exit_point, indexTarget, shell):
        free_electron = Electron().move_to(entry_point)
        free_electron_2 = free_electron.copy()
        indexEjected = np.random.choice([i for i, o in enumerate(shell.opacities) if o.get_value() == 1], 1)[0]
        eTarget = shell.get_electron(indexTarget)
        lag_ratio = 0.7
        target = eTarget.copy().rotate(duration / 2 * PI,
                                       about_point=shell.get_center()).get_center()
        pathGoing = Line(entry_point, target)
        eEjected = shell.get_electron(indexEjected)
        ejected = eEjected.copy().rotate(lag_ratio * duration / 2 * PI,
                                         about_point=shell.get_center()).get_center()
        pathLeaving = Line(ejected, exit_point)
        ejectionAnimation = AnimationGroup(
            Succession(MoveAlongPath(free_electron, pathGoing, rate_func=linear, run_time=duration / 2),
                       shell.opacities[indexTarget].animate(run_time=0).set_value(1),
                       free_electron.animate(run_time=0).to_edge(LEFT).shift(LEFT)),
            Succession(Wait(0.00001), shell.opacities[indexEjected].animate(run_time=0).set_value(0),
                       MoveAlongPath(free_electron_2, pathLeaving, rate_func=linear, run_time=duration / 2)),
            lag_ratio=lag_ratio)
        return ejectionAnimation

    def experiment_trial(self, carbon_valance_shell, copper_valance_shell, duration, i):
        screen = FullScreenRectangle()
        entry_point = screen.get_edge_center(LEFT) + LEFT
        exit_point = screen.get_edge_center(RIGHT) + RIGHT
        copper_entry = entry_point + (UP * 1.5)
        copper_exit = exit_point + (UP * 1.5)
        carbon_entry = entry_point + (DOWN * 1.5)
        carbon_exit = exit_point + (DOWN * 1.5)
        anim_copper, n_copper = self.try_eject_electron(duration, copper_entry, copper_exit, i, copper_valance_shell)
        anim_carbon, n_carbon = self.try_eject_electron(duration, carbon_entry, carbon_exit, i, carbon_valance_shell)
        return (AnimationGroup(
            anim_copper,
            anim_carbon
        ), (n_copper, n_carbon))

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

        copper_valance_shell = Shell(8)
        copper = MathTex("Cu")
        carbon_valance_shell = Shell(8).shift(DOWN * 1.5)
        carbon = MathTex("C").shift(DOWN * 1.5)
        free_electron = Electron().to_edge(LEFT, buff=0).shift(LEFT)
        nb_send = Integer(0).to_edge(LEFT)
        nb_copper_pass = Integer(0).to_edge(RIGHT).shift(UP * 1.5)
        nb_carbon_pass = Integer(0).to_edge(RIGHT).shift(DOWN * 1.5)
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
            self.add(copper_valance_shell)
            self.play(Succession(AnimationGroup(shells[-1].fade_out(), FadeOut(nucleus)),
                                 AnimationGroup(FadeIn(copper), copper_valance_shell.fade_electron_in(0))),
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
            self.play(
                self.refuse_electron(traker.duration, screen.get_edge_center(LEFT) + LEFT, 0, copper_valance_shell))
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Soit il arrive à un endroit où il n'y a pas d'électron et se met sur la couche de valance""") as traker:
            p = copper_valance_shell.get_electron(4).copy().rotate(traker.duration * PI,
                                                                   about_point=copper_valance_shell.get_center()).get_center()
            path = Line(screen.get_edge_center(LEFT) + LEFT, p)
            self.play(MoveAlongPath(free_electron, path, rate_func=linear), run_time=traker.duration)
            free_electron.to_edge(LEFT).shift(LEFT)
            copper_valance_shell.opacities[4].set_value(1)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """L'atome a alors un electron en trop et va rejeter l'autre électron de sa couche de valance""") as traker:
            p = copper_valance_shell.get_electron(0).get_center()
            path = Line(p, screen.get_edge_center(RIGHT) + RIGHT)
            free_electron.move_to(p)
            copper_valance_shell.opacities[0].set_value(0)
            self.play(MoveAlongPath(free_electron, path, rate_func=linear), run_time=traker.duration)

        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Maintenant, il faut garder en tête que c'est comme si un electron en poussait un autre. Sans pause, ça ressemble à ça.""") as traker:
            self.wait(traker.duration)
        self.next_section(skip_animations=section_done)
        entry_point = screen.get_edge_center(LEFT) + LEFT
        exit_point = screen.get_edge_center(RIGHT) + RIGHT
        self.play(self.eject_electron(3, entry_point, exit_point, 0, copper_valance_shell))

        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Faisons une experience en comparant un atome de cuivre avec un atome de carbone""") as traker:
            self.add(carbon_valance_shell)
            self.play(copper_valance_shell.animate.shift(UP * 1.5), copper.animate.shift(UP * 1.5),
                      run_time=traker.duration / 2)
            self.play(FadeIn(carbon), *[carbon_valance_shell.fade_electron_in(n * 2) for n in range(4)],
                      run_time=traker.duration / 2)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """On va essayer de faire passer 50 electrons et compter combien arrivent à passer pour chaque atome""") as traker:
            self.play(*[FadeIn(nb, scale=3) for nb in [nb_send, nb_copper_pass, nb_carbon_pass]],
                      run_time=traker.duration)

        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """C'est parti. On va accelerer un peu au milieu car sinon ça serai vraiment long.""") as traker:
            total_duration = 25
            nb_trials = 50
            for i in range(nb_trials):
                duration = (total_duration / nb_trials) * 2 * abs(
                    1 - rate_functions.there_and_back(i / (nb_trials - 1)))
                nb_send.set_value(nb_send.get_value() + 1)
                (animation, (n_copper, n_carbon)) = self.experiment_trial(carbon_valance_shell, copper_valance_shell,
                                                                          duration,
                                                                          np.random.randint(8))
                self.play(animation)
                nb_copper_pass.set_value(nb_copper_pass.get_value() + n_copper)
                nb_carbon_pass.set_value(nb_carbon_pass.get_value() + n_carbon)

        self.next_section(skip_animations=section_done)
        with self.my_voiceover("""Le cuivre a laissé passer 48 éléctrons""") as traker:
            self.play(Indicate(nb_copper_pass, scale_factor=2), run_time=traker.duration)
        with self.my_voiceover("""Et le carbon en a laissé passer seulement 24""") as traker:
            self.play(Indicate(nb_carbon_pass, scale_factor=2), run_time=traker.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                """Le cuivre est donc un meilleur conducteur que le carbone. Dit autrement, le carbone a une résistance plus élevée que le cuivre""") as traker:
            self.play(AnimationGroup(copper_valance_shell.fade_out(), carbon_valance_shell.fade_out(),
                  FadeOut(copper, carbon, nb_copper_pass, nb_carbon_pass, nb_send),rate_func=rate_functions.ease_in_expo), run_time=traker.duration)
        self.next_section(skip_animations=False)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
