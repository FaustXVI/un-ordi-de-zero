from abc import ABC

from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

from FakeTraker import FakeTracker

recording = False


def my_frac(d, n):
    return [r"{", r"{", *d, r"}", r"\over", r"{", *n, r"}", r"}"]


class K_Correction(VoiceoverScene, ABC):

    def my_voiceover(self, text, duration=1):
        if recording:
            return self.voiceover(text)
        else:
            return FakeTracker(duration)

    def construct(self):
        self.set_speech_service(RecorderService(device_index=12))
        champ_terrestre = MathTex(r"B_{t} = ", r"5 \times 10^{-5}")
        angle_formula_min = MathTex(r"\alpha", r"_{5 \times 10^{-7}}", r"\approx", r" 1")
        iron_permeability = MathTex(r"k =", r"100")
        new_iron_permeability = MathTex(r"k =", r"1")
        coil_formula_mu_l = MathTex(r"B ", "=", "k", r"\times", r"4 \pi \times 10^{-7}", r"\times",
                                    *my_frac(["N"], ["10^{-2}"]),
                                    "I")
        Group(coil_formula_mu_l, iron_permeability, champ_terrestre, angle_formula_min).arrange(DOWN)
        new_iron_permeability.move_to(iron_permeability.get_center())
        with self.my_voiceover(text=
                               """Pour rappel, on a calculé la valeur de notre champ magnétique en utilisant la formule B = 100 x 4 pi 10-7 N / 10-2 I"""
                               ) as tracker:
            self.play(FadeIn(coil_formula_mu_l), run_time=tracker.duration)
        with self.my_voiceover(text=
                               """Et nous avons utilisé un perméabilité du fer k = 100"""
                               ) as tracker:
            self.play(FadeIn(iron_permeability), run_time=tracker.duration)
        with self.my_voiceover(text=
                               r"Vu qu'on ne va pas changer le nombre de tours et que I n'a pas de raison de changer non plus, notre calcul de B sera directement proportionnel à la valeur qu'on affect à k"
                               ) as tracker:
            self.wait(tracker.duration)
        with self.my_voiceover(text=
                               r"Donc si on prends k = 1 alors B sera 100 plus faible que ce qu'on avait calculé avant") as tracker:
            self.play(TransformMatchingTex(iron_permeability, new_iron_permeability), run_time=tracker.duration)
        with self.my_voiceover(text=
                               r"Et s'était donné comme objectif de produire un champ égal au champ terrestre"
                               ) as tracker:
            self.play(FadeIn(champ_terrestre), run_time=tracker.duration)
        with self.my_voiceover(text=
                               r"Or On a déjà calculé que notre boussole bougerai d'un peu moins de 1 degré pour un champs 100 fois plus faible que le champ terrestre"
                               ) as tracker:
            self.play(FadeIn(angle_formula_min), run_time=tracker.duration)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
