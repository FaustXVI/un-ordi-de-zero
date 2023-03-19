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

    def electron_position_in(self, indexTarget, duration):
        return self.get_electron(indexTarget).copy() \
            .rotate(duration * PI, about_point=self.shell.get_center()) \
            .get_center()

    def get_any_electron_index(self):
        return np.random.choice([i for i, o in enumerate(self.opacities) if o.get_value() == 1], 1)[0]

    def get_any_free_electron_spot_index(self):
        return np.random.choice([i for i, o in enumerate(self.opacities) if o.get_value() == 0], 1)[0]


def compute_electrons_passing(random_result, number_sent):
    return [0, *accumulate([random_result() for _ in range(number_sent + 1)], operator.add)]


def refuse_electron(duration, start_point, indexTarget, shell):
    free_electron = Electron().move_to(entry_point)
    p = shell.get_electron(indexTarget).copy().rotate(duration * PI / 2,
                                                      about_point=shell.get_center()).get_center()
    return Succession(
        MoveAlongPath(free_electron, Line(start_point, p + (LEFT * 0.5)), run_time=duration / 2),
        MoveAlongPath(free_electron, Line(p + (LEFT * 0.5), entry_point), run_time=duration / 2)
    )


def electron_leaving_animation(shell, out_point):
    def animate(duration, lag):
        index_ejected = shell.get_any_electron_index()
        ejected = shell.electron_position_in(index_ejected, lag)
        pathLeaving = Line(ejected, out_point)
        free_electron = Electron().move_to(entry_point)
        return Succession(Wait(0.00001),
                          shell.opacities[index_ejected].animate(run_time=0).set_value(0),
                          MoveAlongPath(free_electron, pathLeaving, rate_func=linear,
                                        run_time=duration),
                          free_electron.animate(run_time=0).set_opacity(0)
                          )

    return animate


def electron_entering_animation(indexTarget, shell, start_point):
    def animate(duration, lag):
        free_electron = Electron().move_to(entry_point)
        target = shell.electron_position_in(indexTarget, lag + duration)
        pathGoing = Line(start_point, target)
        return Succession(MoveAlongPath(free_electron, pathGoing, rate_func=linear, run_time=duration),
                          shell.opacities[indexTarget].animate(run_time=0).set_value(1),
                          free_electron.animate(run_time=0).to_edge(LEFT).shift(LEFT))

    return animate


def electrons_chaining_animation(animations, duration):
    lag_ratio = 0.7
    nb_animations = len(animations)
    each_duration = duration / nb_animations
    return AnimationGroup(
        *[a(each_duration, (max(0, i - 1) * each_duration) + (i * lag_ratio * each_duration)) for (i, a) in
          enumerate(animations)],
        lag_ratio=lag_ratio)


def passing_electron(duration, entry_point, exit_point, indexTarget, shell):
    return electrons_chaining_animation(
        [
            electron_entering_animation(indexTarget, shell, entry_point),
            electron_leaving_animation(shell, exit_point)
        ], duration)


def try_eject_electron(duration, entry_point, exit_point, indexTarget, shell):
    if shell.opacities[indexTarget].get_value() == 1:
        return (refuse_electron(duration, entry_point, indexTarget, shell), 0)
    else:
        return (passing_electron(duration, entry_point, exit_point, indexTarget, shell), 1)


screen = FullScreenRectangle()
entry_point = screen.get_edge_center(LEFT) + LEFT
exit_point = screen.get_edge_center(RIGHT) + RIGHT


def single_atom_experiment_trial(carbon_valance_shell, copper_valance_shell, duration, i):
    copper_entry = entry_point + (UP * 1.5)
    copper_exit = exit_point + (UP * 1.5)
    carbon_entry = entry_point + (DOWN * 1.5)
    carbon_exit = exit_point + (DOWN * 1.5)
    anim_copper, n_copper = try_eject_electron(duration, copper_entry, copper_exit, i, copper_valance_shell)
    anim_carbon, n_carbon = try_eject_electron(duration, carbon_entry, carbon_exit, i, carbon_valance_shell)
    return (AnimationGroup(
        anim_copper,
        anim_carbon
    ), (n_copper, n_carbon))


def electron_passing(valance_size, nb_electrons_on_valance):
    return 0 if np.random.randint(valance_size) < nb_electrons_on_valance else 1


def electron_passing_copper():
    return electron_passing(8, 1)


def electron_passing_carbon():
    return electron_passing(8, 4)


nb_electrons = 10000


class Resistivity(MyScene):

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
                refuse_electron(traker.duration, screen.get_edge_center(LEFT) + LEFT, 0, copper_valance_shell))
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
        self.play(passing_electron(3, entry_point, exit_point, 0, copper_valance_shell))

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
                (animation, (n_copper, n_carbon)) = single_atom_experiment_trial(carbon_valance_shell,
                                                                                 copper_valance_shell,
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
        with self.my_voiceover(
                f"""Pour ça on va refaire la simulation avec {nb_electrons} ! Et on va dessiner les résultats sur un graphique""") as traker:
            self.wait(traker.duration)
        axes = Axes(x_range=[0, nb_electrons, nb_electrons / 10],
                    y_range=[0, nb_electrons, nb_electrons / 10],
                    tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 30,
                                 "decimal_number_config": {"num_decimal_places": 0, "group_with_commas": False}})
        electrons_copper = compute_electrons_passing(electron_passing_copper, nb_electrons)
        electrons_carbon = compute_electrons_passing(electron_passing_carbon, nb_electrons)
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
            self.play(*[FadeOut(o, rate_func=rate_functions.ease_out_expo) for o in
                        [axes, graph_copper, graph_carbon, labels]],
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
            self.play(*[FadeOut(o, rate_func=rush_into) for o in self.mobjects], run_time=traker.duration)


class Resistance(MyScene):
    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                f"""On va faire trois simulation""") as traker:
            self.wait(traker.duration)

        self.next_section(skip_animations=section_done)
        carbon1_nucleus = MathTex("C")
        carbon1_shell = Shell(8)
        carbon2_nucleus = MathTex("C").shift(DOWN * 1.5)
        carbon2_shell = Shell(8).shift(DOWN * 1.5)
        self.add(carbon1_shell)
        self.add(carbon2_shell)
        with self.my_voiceover(
                f"""La première, que nous avons déjà faite, avec un atome de carbone. On appellera cette simulation, la simulation «atome»""") as traker:
            self.play(FadeIn(carbon1_nucleus), *[carbon1_shell.fade_electron_in(i * 2) for i in range(4)],
                      run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                f"""Dans la deuxième simulation, on va ajouter de l'épaisseur en ajoutant un atome au dessus""") as traker:
            self.play(VGroup(carbon1_nucleus, carbon1_shell).animate.shift(UP * 1.5), FadeIn(carbon2_nucleus),
                      *[carbon2_shell.fade_electron_in(i * 2) for i in range(4)], run_time=traker.duration)
        with self.my_voiceover(
                f"""Quand on envoie un éléctron il y a alors trois scénarios possible""") as traker:
            self.wait(traker.duration)
        with self.my_voiceover(
                f"""Soit l'electron passe par l'atome du dessus et on reçoit un éléctron de l'autre côté""") as traker:
            self.play(passing_electron(traker.duration, entry_point, exit_point,
                                       carbon1_shell.get_any_free_electron_spot_index(), carbon1_shell))
        with self.my_voiceover(
                f"""Soit il passe par l'atome du dessous et on reçoit un éléctron de l'autre côté""") as traker:
            self.play(passing_electron(traker.duration, entry_point, exit_point,
                                       carbon2_shell.get_any_free_electron_spot_index(), carbon2_shell))
        with self.my_voiceover(
                f"""Soit il se fait rejeter par les deux atomes du dessous et on ne reçoit rien de l'autre côté""") as traker:
            self.play(refuse_electron(traker.duration / 2, entry_point, carbon1_shell.get_any_electron_index(),
                                      carbon1_shell))
            self.play(refuse_electron(traker.duration / 2, entry_point, carbon2_shell.get_any_electron_index(),
                                      carbon2_shell))
        with self.my_voiceover(
                f"""On appellera cette simulation, la simulation «épaisseur»""") as traker:
            self.wait(traker.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                f"""Dans la troisième simulation, on va ajouter de la longueur en mettant le second atome après le premier""") as traker:
            self.play(
                VGroup(carbon1_nucleus, carbon1_shell).animate.shift(DOWN * 1.5 + LEFT * 1.5),
                VGroup(carbon2_nucleus, carbon2_shell).animate.shift(UP * 1.5 + RIGHT * 1.5)
                , run_time=traker.duration)
        with self.my_voiceover(
                f"""Quand on envoie un éléctron il y a aussi trois scénarios possible""") as traker:
            self.wait(traker.duration)
        with self.my_voiceover(
                f"""Soit il se fait rejeter par le premier atome et on reçoit rien de l'autre côté""") as traker:
            self.play(
                refuse_electron(traker.duration, entry_point, carbon1_shell.get_any_electron_index(), carbon1_shell))
        with self.my_voiceover(
                f"""Soit l'électron du premier atome se fait rejeter par le second atome et on ne reçoit rien de l'autre côté""") as traker:
            rejection_position = carbon2_shell.electron_position_in(carbon2_shell.get_any_electron_index(),
                                                                    1.7 * (traker.duration / 3)) + LEFT * 0.5
            free_e = Electron().move_to(entry_point)
            self.play(electrons_chaining_animation(
                [
                    electron_entering_animation(carbon1_shell.get_any_free_electron_spot_index(), carbon1_shell,
                                                entry_point),
                    lambda d, l: Succession(electron_leaving_animation(carbon1_shell, rejection_position)(d / 2, l),
                                            Succession(Wait(0.0001),
                                                       MoveAlongPath(free_e, Line(rejection_position, entry_point),
                                                                     run_time=d / 2)))
                ], traker.duration))
        with self.my_voiceover(
                f"""Soit les deux atomes laissent passer les éléctrons et on reçoit un électron de l'autre côté""") as traker:
            new_c2_electron = carbon2_shell.get_any_free_electron_spot_index()
            self.play(electrons_chaining_animation(
                [
                    electron_entering_animation(carbon1_shell.get_any_free_electron_spot_index(), carbon1_shell,
                                                entry_point),
                    lambda d, l: Succession(
                        electron_leaving_animation(carbon1_shell, carbon2_shell.electron_position_in(
                            new_c2_electron, l + d))(d, l),
                        carbon2_shell.opacities[new_c2_electron].animate(run_time=0).set_value(1)),
                    electron_leaving_animation(carbon2_shell, exit_point),
                ], traker.duration))
        with self.my_voiceover(
                f"""On appellera cette simulation, la simulation «longueur»""") as traker:
            self.wait(traker.duration)
        self.next_section(skip_animations=section_done)
        axes = Axes(x_range=[0, nb_electrons, nb_electrons / 10],
                    y_range=[0, nb_electrons, nb_electrons / 10],
                    tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 30,
                                 "decimal_number_config": {"num_decimal_places": 0, "group_with_commas": False}})
        electrons_copper = compute_electrons_passing(electron_passing_carbon, nb_electrons)
        electrons_2_copper_vertical = compute_electrons_passing(
            lambda: electron_passing_carbon() or electron_passing_carbon(), nb_electrons)
        electrons_2_copper_horizontal = compute_electrons_passing(
            lambda: electron_passing_carbon() and electron_passing_carbon(), nb_electrons)
        graph_of = lambda array: lambda x: array[round(x)]
        graph_copper = axes.plot(graph_of(electrons_copper), x_range=[0, nb_electrons], dt=1, use_smoothing=False,
                                 color=ORANGE)
        graph_copper_vertical = axes.plot(graph_of(electrons_2_copper_vertical), x_range=[0, nb_electrons], dt=1,
                                          use_smoothing=False,
                                          color=GREEN)
        graph_copper_horizontal = axes.plot(graph_of(electrons_2_copper_horizontal), x_range=[0, nb_electrons], dt=1,
                                            use_smoothing=False,
                                            color=RED)
        labels = axes.get_axis_labels(x_label=Tex("Électrons envoyés"), y_label=Tex("Électrons reçus"))
        result_copper = MathTex(electrons_copper[nb_electrons]).next_to(graph_copper.points[-1], buff=0.1)
        result_copper_vertical = MathTex(electrons_2_copper_vertical[nb_electrons]).next_to(
            graph_copper_vertical.points[-1], buff=0.1)
        result_copper_horizontal = MathTex(electrons_2_copper_horizontal[nb_electrons]).next_to(
            graph_copper_horizontal.points[-1], buff=0.1)
        with self.my_voiceover(
                f"""Comme précédement, on va essayer de faire passer {nb_electrons} et comparer les courbes""") as traker:
            self.play(Create(axes), Create(labels), run_time=traker.duration)
        with self.my_voiceover(
                f"""On va tracer la simulation atome en orange, l'epaisseur en vert et la longueur en rouge""") as traker:
            self.play(FadeIn(VGroup(Tex("Atome", color=ORANGE), Tex(r"Épaisseur", color=GREEN),
                                    Tex("Longueur", color=RED))
                             .arrange_in_grid(3, 1, col_alignments="l")
                             .next_to(axes[1].get_end(), RIGHT + DOWN, buff=1)
                             ),
                      run_time=traker.duration)
        with self.my_voiceover(
                f"""La simulation avec un atome laisse passer {result_copper} éléctrons, ce qui est proche de notre simulation précédente""") as traker:
            self.play(Create(graph_copper), FadeIn(result_copper, rate_func=rate_functions.ease_in_quart),
                      run_time=traker.duration)
        with self.my_voiceover(
                f"""La simulation avec deux atomes disposées en epaisseur laisse passer {result_copper_vertical} électrons""") as traker:
            self.play(Create(graph_copper_vertical),
                      FadeIn(result_copper_vertical, rate_func=rate_functions.ease_in_quart),
                      run_time=traker.duration)
        with self.my_voiceover(
                f"""La simulation avec deux atomes disposées en longueur laisse passer {result_copper_horizontal} électrons""") as traker:
            self.play(Create(graph_copper_horizontal),
                      FadeIn(result_copper_horizontal, rate_func=rate_functions.ease_in_quart),
                      run_time=traker.duration)
        with self.my_voiceover(
                f"""Donc l'épaisseur a l'air de réduire la résistance et la longueur a l'air de l'augmenter""") as traker:
            self.wait(traker.duration)
        with self.my_voiceover(
                f"""Maintenant qu'on a ça en tête, je te propose de regarder la formule qui permet de calculer une résistance""") as traker:
            self.play(*[FadeOut(o) for o in self.mobjects], run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        r_eq = MathTex("R", " = ", r"\rho", *my_frac(["l"], ["A"]))
        with self.my_voiceover(
                f"""R, la valeur de notre résistance, est égale à """) as traker:
            self.play(FadeIn(r_eq[:2]), run_time=traker.duration)
        with self.my_voiceover(
                f"""Rho, la résistivité de la matière qu'on utilise""") as traker:
            self.play(FadeIn(r_eq[2]), run_time=traker.duration)
        with self.my_voiceover(
                f"""fois l sur A""") as traker:
            self.play(FadeIn(r_eq[3:]), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                f"""ou l est la longueur de la résistance""") as traker:
            self.play(Circumscribe(r_eq.get_part_by_tex("l")), run_time=traker.duration)
        with self.my_voiceover(
                f"""et A est l'air d'une coupe de la résistance. Dit autrement, son épaisseur.""") as traker:
            self.play(Circumscribe(r_eq.get_part_by_tex("A")), run_time=traker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                f"""Dit autrement, plus une résistance est longue, plus elle résiste et plus elle est épaisse, moins elle résiste.""") as traker:
            self.play(*[FadeOut(o) for o in self.mobjects], run_time=traker.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          "Resistance"
          ], prog_name='invoked-command')
