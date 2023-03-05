from abc import ABC

from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

from FakeTraker import FakeTracker

section_done = False
recording = True


def my_frac(d, n):
    return [r"{", r"{", *d, r"}", r"\over", r"{", *n, r"}", r"}"]


class K_Correction(VoiceoverScene, ABC):

    def my_voiceover(self, text, duration=1):
        if recording:
            return self.voiceover(text)
        else:
            return FakeTracker(duration)

    def construct(self):
        formula_Bp = MathTex("B_p", "=", *my_frac(["B_b"], ["R", "^2"]))
        formula_R = MathTex("R", "=", *my_frac(["d"], ["r"]))
        radius = MathTex("r", "=", r"25 \times 10^{-4}").to_edge(UP, buff=2)
        formula_R_radius = MathTex("R", "=", *my_frac(["d"], [r"25 \times 10^{-4}"]))
        distance = MathTex("d", "=", r"3 \times 10^{-2}").to_edge(UP, buff=2)
        formula_R_complete = MathTex("R", "=", *my_frac([r"3 \times 10^{-2}"], [r"25 \times 10^{-4}"]))
        R_result = MathTex("R", "=", "12")
        formula_Bp_final = MathTex("B_p", "=", *my_frac(["B_b"], ["12", "^2"]))
        Bp_result = MathTex("B_p", "=", *my_frac(["B_b"], ["144"]))
        self.set_speech_service(RecorderService(device_index=12))
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(text=
                               """
                               Quand on s'éloigne d'une bobine, le champ diminue de manière inversement proporstionnel au carré de la distance relative au rayon.
                               """
                               ) as tracker:
            self.wait(tracker.duration)
        with self.my_voiceover(text=
                               """
                               Ce qu'on peut écrire Bp = Bb / R2
                               """
                               ) as tracker:
            self.play(FadeIn(formula_Bp), run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               Où Bp est la valeur du champ au point qui nous interresse
                               """
                               ) as tracker:
            self.play(Circumscribe(formula_Bp.get_part_by_tex("B_p")), run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               Bb est la valeur du champ au centre de notre bobine
                               """
                               ) as tracker:
            self.play(Circumscribe(formula_Bp.get_part_by_tex("B_b")), run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               R est la distance relative au rayon entre la bobine et le point qui nous interresse.
                               """
                               ) as tracker:
            self.play(Circumscribe(formula_Bp.get_part_by_tex("R")), run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               L'élément clé ici, c'est R. Mettons cette formule dans un coin pour s'en souvenir.
                               """
                               ) as tracker:
            self.play(formula_Bp.animate.scale(1 / 2).to_edge(UL), run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               Le terme distance relative au rayon veut dire qu'au lieu de compter la distance en unité absolue comme des cm, on va utiliser comme unité le rayon de la bobine.
                               """
                               ) as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(text=
                               """
                               Pour ça il faut diviser notre distance en unité absolue par le rayon de notre clou. Ce qui donne R = d / r
                               """
                               ) as tracker:
            self.play(FadeIn(formula_R), run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               Notre clou fait 2,5 mm de rayon soit 25 fois 10-4 m
                               """
                               ) as tracker:
            self.play(FadeIn(radius), run_time=tracker.duration)
        self.play(TransformMatchingTex(VGroup(formula_R, radius), formula_R_radius))
        with self.my_voiceover(text=
                               """
                               Notre boussolle se trouve, après mesure, à 3 cm de notre bobine soit 3 x 10-2 m
                               """
                               ) as tracker:
            self.play(FadeIn(distance), run_time=tracker.duration)
        self.play(TransformMatchingTex(VGroup(formula_R_radius,distance), formula_R_complete))
        self.wait(2)
        with self.my_voiceover(text=
                               """
                               On obtien alors R = 12
                               """
                               ) as tracker:
            self.play(TransformMatchingTex(formula_R_complete, R_result, transform_mismatches=True),
                      run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(text=
                               """
                               On peut alors reprendre notre formule précédente
                               """
                               ) as tracker:
            self.play(AnimationGroup(R_result.animate.to_edge(UP, buff=2), formula_Bp.animate.scale(2).move_to(ORIGIN)),
                      run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               Y remplacer R par sa valeur
                               """
                               ) as tracker:
            self.play(TransformMatchingTex(VGroup(formula_Bp, R_result), formula_Bp_final),
                      run_time=tracker.duration)
        self.wait()
        with self.my_voiceover(text=
                               """
                               On apprends alors que notre champ est 144 fois plus faible que prévu. 
                               """
                               ) as tracker:
            self.play(TransformMatchingTex(formula_Bp_final, Bp_result, transform_mismatches=True),
                      run_time=tracker.duration)
        with self.my_voiceover(text=
                               """
                               Si on veut voir quelquechose avec notre situation actuelle, il va falloir faire 144 fois plus de tours soit prêt de 6 000 tours.
                               Avant d'en arriver là, je te propose d'être optimiste car on a un clou en fer et on calcul avec k = 1. Or k = 1 c'est l'équivalant d'avoir de l'air au centre de notre bobine.
                               On sait que k est inférieur à 100 mais il est peut-être égale à 1 non plus. Enlève le scotch histoire d'être le plus pur possible et commence par faire une bobine de 1 000 tours et si ça marche pas monte à 6 000.
                               """
                               ) as tracker:
            self.wait(tracker.duration)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
