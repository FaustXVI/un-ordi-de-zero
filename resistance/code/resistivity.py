import operator
from itertools import accumulate

from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


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

    def electron_passing(self, valance_size, nb_electrons_on_valance):
        return 0 if np.random.randint(valance_size) < nb_electrons_on_valance else 1

    def electron_passing_copper(self):
        return self.electron_passing(8, 1)

    def electron_passing_carbon(self):
        return self.electron_passing(8, 4)

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
                """Bon, pour commencer, faut garder en tête que je vais simplifier pas mal de choses. Ceci dit, ce que je vais te montrer est suffisament correct pour comprendre le concept de résistivité""") as traker:
            text = Text(r"Simplifications devant !")
            self.play(Succession(FadeIn(text), Wait(), FadeOut(text)), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                "Un atome, c'est composé d'un noyeau qu'on va représenter par la lettre de l'élément en question, ici l'hydrogène") as traker:
            self.play(FadeIn(nucleus), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("Autour du noyau, il y a des électrons qui tournent") as traker:
            self.play(firstShell.fade_electron_in(0), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("""À chaque fois qu'on passe à un atome plus lourd, son besoin en éléctrons grandit.\n
        Les éléctrons se répartissent en couches et on ne  peut passer à la couche N+1 qu'après avoir remplis complètement la couche N.\n
        Les 3 premières couches contiennent respectivement 2, 8 et 8 éléctrons""") as traker:
            self.play(Succession(*transitions[1:]), run_time=max(traker.duration, len(elements)))
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """La dernière couche d'électrons, celle qui est le plus à l'exterieur, est appelé la couche de valence.""") as traker:
            self.play(Indicate(shells[-1], scale_factor=1.5), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """C'est la seule qui va nous interesser, donc à partir de maintenant, c'est la seule qu'on va représenter""") as traker:
            self.play(*[s.fade_out() for s in shells[:-1]], run_time=traker.duration * 0.6)
            self.play(shells[-1].animate.scale(2 / 3), run_time=traker.duration * 0.4)
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
                """Faisons une simulation afin de comparer ce qui se passe avec un atome de cuivre et un atome de carbone""") as traker:
            self.add(carbon_valance_shell)
            self.play(copper_valance_shell.animate.shift(UP * 1.5), copper.animate.shift(UP * 1.5),
                      run_time=traker.duration / 2)
            self.play(FadeIn(carbon), *[carbon_valance_shell.fade_electron_in(n * 2) for n in range(4)],
                      run_time=traker.duration / 2)
        self.next_section(skip_animations=section_done)
        nb_trials = 50
        with self.my_voiceover(
                f"""On va essayer de faire passer {nb_trials} electrons et compter combien arrivent à passer pour chaque atome""") as traker:
            self.play(*[FadeIn(nb, scale=3) for nb in [nb_send, nb_copper_pass, nb_carbon_pass]],
                      run_time=traker.duration)

        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """C'est parti. On va accelerer un peu au milieu car sinon ça serai vraiment long.""") as traker:
            total_duration = 25
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
        with self.my_voiceover(f"""Le cuivre a laissé passer {nb_copper_pass.get_value()} éléctrons !""") as traker:
            self.play(Indicate(nb_copper_pass, scale_factor=2), run_time=traker.duration)
        with self.my_voiceover(f"""Et le carbon en a laissé passer seulement {nb_carbon_pass.get_value()}""") as traker:
            self.play(Indicate(nb_carbon_pass, scale_factor=2), run_time=traker.duration)
        with self.my_voiceover(
                f"""On commence à voir quelque chose d'interessant mais là, c'est une simulation avec seulement {nb_trials} electrons.\n
                Ça sera bien d'avoir plus d'éléctrons pour valider.""") as traker:
            self.play(AnimationGroup(copper_valance_shell.fade_out(), carbon_valance_shell.fade_out(),
                                     FadeOut(copper, carbon, nb_copper_pass, nb_carbon_pass, nb_send),
                                     rate_func=rate_functions.ease_in_expo), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        nb_electrons = 10000
        with self.my_voiceover(
                f"""Pour ça on va refaire la simulation avec {nb_electrons} ! Et on va dessiner les résultats sur un graphique""") as traker:
            self.wait(traker.duration)
        axes = Axes(x_range=[0, nb_electrons, nb_electrons / 10],
                    y_range=[0, nb_electrons, nb_electrons / 10],
                    tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 30,
                                 "decimal_number_config": {"num_decimal_places": 0, "group_with_commas": False}})
        electrons_copper = self.compute_electrons_passing(self.electron_passing_copper, nb_electrons)
        electrons_carbon = self.compute_electrons_passing(self.electron_passing_carbon, nb_electrons)
        graph_of = lambda array: lambda x: array[round(x)]
        graph_copper = axes.plot(graph_of(electrons_copper), x_range=[0, nb_electrons], dt=1, use_smoothing=False,
                                 color=ORANGE)
        copper_text = MathTex("Cuivre", color=ORANGE).next_to(axes[1].get_end(), RIGHT + DOWN, buff=1)
        graph_carbon = axes.plot(graph_of(electrons_carbon), x_range=[0, nb_electrons], dt=1, use_smoothing=False,
                                 color=RED)
        carbon_text = MathTex("Carbone", color=RED).next_to(copper_text, DOWN)
        labels = axes.get_axis_labels(x_label=Tex("Électrons envoyés"), y_label=Tex("Électrons reçus"))
        with self.my_voiceover(
                f"""En absisse, on va mettre le nombre d'electrons qu'on va envoyer et on va monter jusqu'à {nb_electrons}""") as traker:
            self.play(Create(axes[0]), Create(labels[0]), run_time=traker.duration)
        with self.my_voiceover(
                f"""En ordonnée, on va le nombre d'electrons qui arrivent à passer""") as traker:
            self.play(Create(axes[1]), Create(labels[1]), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                f"""Si on trace le cuivre en orange et le carbon en rouge""") as traker:
            self.play(Create(graph_copper), Create(graph_carbon), FadeIn(carbon_text), FadeIn(copper_text),
                      run_time=traker.duration)
        nb_copper_electrons = MathTex(electrons_copper[nb_electrons])
        with self.my_voiceover(
                f"""On vois que le cuivre fin loin devant avec {electrons_copper[nb_electrons]} électrons qui passent""") as traker:
            result_copper = nb_copper_electrons.next_to(graph_copper.points[-1], buff=0.1)
            self.play(FadeIn(result_copper), run_time=traker.duration)
        nb_carbon_electrons = MathTex(electrons_carbon[nb_electrons])
        with self.my_voiceover(
                f"""alors que le carbone n'en a laissé passer que {electrons_carbon[nb_electrons]}""") as traker:
            result_carbon = nb_carbon_electrons.next_to(graph_carbon.points[-1], buff=0.1)
            self.play(FadeIn(result_carbon), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        conductivity_copper = MathTex(r"\sigma", "_{", "Cuivre", "}", "=",
                                      *my_frac([f"{electrons_copper[nb_electrons]}"], [f"{nb_electrons}"]))
        conductivity_carbon = MathTex(r"\sigma", "_{", "Carbone", "}", "=",
                                      *my_frac([f"{electrons_carbon[nb_electrons]}"], [f"{nb_electrons}"]))
        VGroup(conductivity_copper, conductivity_carbon).arrange(DOWN, buff=1)
        with self.my_voiceover(
                f"""Si on note sigma la conductivité d'un élément, alors, dans notre simulation, le cuivre a une conductivité de {electrons_copper[nb_electrons]} sur {nb_electrons}
        et le carbone a une conductivité de {electrons_carbon[nb_electrons]} / {nb_electrons}""") as traker:
            self.play(*[FadeOut(o,rate_func=rate_functions.ease_out_expo) for o in [axes, graph_copper, graph_carbon, labels]],
                      TransformMatchingTex(Group(nb_copper_electrons, copper_text), conductivity_copper),
                      TransformMatchingTex(Group(nb_carbon_electrons, carbon_text), conductivity_carbon),
                      run_time=traker.duration)
        resistivity_copper = MathTex(r"\rho", "_{", "Cuivre", "}", "=",
                                     *my_frac([nb_electrons], [electrons_copper[nb_electrons]]))
        resistivity_carbon = MathTex(r"\rho", "_{", "Carbone", "}", "=",
                                     *my_frac([nb_electrons], [electrons_carbon[nb_electrons]]))
        VGroup(resistivity_copper, resistivity_carbon).arrange(DOWN, buff=1)
        self.next_section(skip_animations=section_done)
        self.wait()
        with self.my_voiceover(
                f"""La résistivité, c'est l'inverse de la conductivité et elle est notée Rho""") as traker:
            self.play(
                TransformMatchingTex(conductivity_copper, resistivity_copper),
                TransformMatchingTex(conductivity_carbon, resistivity_carbon),
                run_time=traker.duration)
        resistivity_copper_value = MathTex(r"\rho", "_{", "Cuivre", "}", r"\approx",
                                           locale.format_string('%.3f', nb_electrons / electrons_copper[nb_electrons]))
        resistivity_carbon_value = MathTex(r"\rho", "_{", "Carbone", "}", r"\approx",
                                           locale.format_string('%.3f', nb_electrons / electrons_carbon[nb_electrons]))
        VGroup(resistivity_copper_value, resistivity_carbon_value).arrange(DOWN, buff=1)
        self.next_section(skip_animations=section_done)
        self.wait()
        with self.my_voiceover(
                f"""On peut calculer la résistivité du cuivre et du carbon dans notre simulation""") as traker:
            self.play(
                TransformMatchingTex(resistivity_copper, resistivity_copper_value, transform_mismatches=True,
                                     key_map={"=": r"\approx"}),
                TransformMatchingTex(resistivity_carbon, resistivity_carbon_value, transform_mismatches=True,
                                     key_map={"=": r"\approx"}),
                run_time=traker.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                f"""On voit alors que le carbon a une résistivité plus grande que le cuivre, ce qui est effectivement le cas dans la réalité mais avec des valeurs différentes""") as traker:
            self.play(*[FadeOut(o,rate_func=rush_into) for o in self.mobjects], run_time=traker.duration)

    def compute_electrons_passing(self, random_result, number_sent):
        return [0, *accumulate([random_result() for _ in range(number_sent + 1)], operator.add)]


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          ], prog_name='invoked-command')
