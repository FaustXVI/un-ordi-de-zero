import math
import operator
from itertools import accumulate

from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True


class Internal_Resistance(MyScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        tension = MathTex("U", "=", "1,5")
        uri = MathTex("U", "=", "R", r"\times", "I")
        v_u = MathTex("1,5", "=", "R", r"\times", "I")
        VGroup(tension, uri).arrange(DOWN)
        with self.my_voiceover("""Prenons une pile de 1,5 volts donc U = 1,5""") as timer:
            self.play(Create(tension), run_time=timer.duration)
        with self.my_voiceover(
                """La loi d'ohm reste vrai même si on met la pile en court circuit, donc on a toujours U = RI""") as timer:
            self.play(Create(uri), run_time=timer.duration)
        with self.my_voiceover("""Ce qui nous donne 1,5 = RI""") as timer:
            self.play(TransformMatchingTex(VGroup(tension, uri), v_u), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        r0 = MathTex("R", "=", "0").shift(UP)
        replace = MathTex("1,5", "=", "0", r"\times", "I")
        absurd = MathTex("1,5", "=", "0")
        rn0 = MathTex("R", r"\neq", "0").shift(UP)
        with self.my_voiceover("""Si R = 0 comme tu l'as dit""") as timer:
            self.play(Create(r0), run_time=timer.duration)
        with self.my_voiceover("""On obtient 1,5 = 0 * I""") as timer:
            self.play(TransformMatchingTex(VGroup(v_u, r0), replace), run_time=timer.duration)
        with self.my_voiceover("""soit 1,5 = 0""") as timer:
            self.play(TransformMatchingTex(replace, absurd), run_time=timer.duration)
        with self.my_voiceover("""ce qui est impossible""") as timer:
            self.play(Indicate(absurd, color=RED), run_time=timer.duration)
        with self.my_voiceover("""il faut donc que R soit différent de 0""") as timer:
            self.play(TransformMatchingTex(absurd, v_u), Create(rn0), run_time=timer.duration,
                      rate_func=rate_functions.ease_out_quad)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover("""On peut arriver à la même conclusion, autrement.""") as timer:
            self.play(FadeOut(rn0), run_time=timer.duration, rate_func=rate_functions.ease_in_quad)
        r_formula = MathTex("I", "=", *my_frac(["1,5"], ["R"]))
        with self.my_voiceover(
                """En utilisant l'équation pour trouver intensité dans notre cirucuit, on obtient I = 1,5 / R""") as timer:
            self.play(TransformMatchingTex(v_u, r_formula), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        i_formula = lambda x: 1.5 / x
        precision = 5
        r_min = 1 / (10 ** precision)
        axes = Axes(x_range=[0, 1, 0.1],
                    y_range=[0, precision],
                    tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 30,
                                 "decimal_number_config": {"num_decimal_places": 1, "group_with_commas": False}},
                    y_axis_config={"decimal_number_config": {"num_decimal_places": 0}, "scaling": LogBase()}
                    )
        graph = axes.plot(i_formula, x_range=[r_min, 1, 0.001], color=BLUE_E, use_smoothing=False)
        with self.my_voiceover(
                """On peut alors tracer une courbe représentant les valeurs de I en fonction de R""") as timer:
            self.play(r_formula.animate.to_edge(UR), Succession(Create(axes), Create(graph)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        text_r = Variable(1, MathTex("R"), num_decimal_places=precision)
        text_i = Variable(i_formula(1), MathTex("I"))
        VGroup(text_r, text_i).arrange_in_grid(col_alignments="l")
        r_value = text_r.tracker
        text_i.add_updater(lambda v: v.tracker.set_value(i_formula(r_value.get_value())))
        dot = Dot()
        dot.add_updater(lambda x: x.move_to(axes.c2p(r_value.get_value(), i_formula(r_value.get_value()))))
        with self.my_voiceover(
                """Prendre n'importe quel valeur de R par exemple 1 et regarder la valeur de I associée, pour l'instant 1,5""") as timer:
            self.play(Create(dot, run_time=0.5), Succession(Create(text_r), Create(text_i)), run_time=timer.duration)
        self.next_section(skip_animations=False)
        with self.my_voiceover(
                """On vois que plus on se rapproche de 0 plus I est grand et tends vers l'infini ce qui veut dire que notre batterie doit produire un nombre de plus en plus grand d'éléctrons.
                On a alors deux problèmes : 
                1 notre battrie à un nombre fini d'éléctrons et ne peux pas en produire à l'infini.
                2 la réaction chimique de la battrie a une vitesse finie et donc a un production d'éléctrons pas secondes finie""",
                15) as timer:
            self.play(r_value.animate.set_value(r_min), run_time=timer.duration, rate_func=rate_functions.ease_out_quad)
        with self.my_voiceover(
                """Une batterie a donc forcément une résistance interne""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
