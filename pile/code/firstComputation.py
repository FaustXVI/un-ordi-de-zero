from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

from FakeTraker import FakeTracker

section_done = True


class ChemicalReaction(VoiceoverScene):

    def myVoiceOver(self, text, duration=1):
        if section_done:
            return FakeTracker(duration)
        else:
            return self.voiceover(text)

    def construct(self):
        self.next_section(skip_animations=section_done)
        service = GTTSService(lang="fr") if section_done else RecorderService()
        self.set_speech_service(service)
        tesla = MathTex("T", "esla")
        champ_terrestre = MathTex(r"B_{t} = {{5 \times 10^{-5}}}", "T")
        angle_formula = MathTex(r"\alpha", r"&= 90 \times \frac{B}{B + B_{t}}")
        angle_formula_eq_dev = MathTex(r"\alpha", "_{t}", r"&= 90 \times \frac{5 \times 10^{-5}}{5 \times 10^{-5} + {{5 \times 10^{-5}}}}")
        angle_formula_eq = MathTex(r"\alpha", "_{t}", r"&\approx 45")
        angle_formula_min_dev = MathTex(r"\alpha", r"_{\frac{t}{100}}", r"&= 90 \times \frac{5 \times 10^{-7}}{5 \times 10^{-7} + {{5 \times 10^{-5}}}}")
        angle_formula_min = MathTex(r"\alpha", r"_{0.01t}", r"&\approx 1")
        angle_formula_max_dev = MathTex(r"\alpha", "_{100t}", r"&= 90 \times \frac{5 \times 10^{-3}}{5 \times 10^{-3} + {{5 \times 10^{-5}}}}")
        angle_formula_max = MathTex(r"\alpha", "_{100t}", r"&\approx 89")
        cable_formula = MathTex(r"B &= \frac{\mu_0 I}{2 \pi r}")
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Une boussole, ça suit le champ magnétique terrestre et un champ manétique, ça se mesure en Teslas") as tracker:
            self.play(Create(tesla), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Le champ magnétique terrestre, en France, fait environ 5 * 10-5 Teslas et on le notera B T") as tracker:
            self.play(TransformMatchingTex(tesla, champ_terrestre), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Cette valeur sera important pour la suite, gardons la dans un coin") as tracker:
            self.play(champ_terrestre.animate.scale(1 / 2).to_edge(UL, buff=1), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique B perpendiculaire au champ terrestre et suffisament fort, on verra la boussole bouger"
                              r"Le mouvement de l'aiguille est propotionnel à rapport entre le champ créé et le champ terrestre"
                              r"On peut calculer l'angle dont va se déplacer l'aiguille avec la formule alpha = 90 * B / (B + 5*10-5)") as tracker:
            self.play(Create(angle_formula), run_time=tracker.duration)
        angle_formula.save_state()
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique égal au champ terrestre") as tracker:
            self.play(TransformMatchingTex(Group(angle_formula, champ_terrestre.copy()), angle_formula_eq_dev), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Alors l'aiguille devrait bouger à 45 degrées") as tracker:
            self.play(TransformMatchingTex(angle_formula_eq_dev, angle_formula_eq), run_time=tracker.duration)

        self.next_section(skip_animations=section_done)
        self.play(angle_formula_eq.animate.scale(1 / 2).next_to(champ_terrestre, DOWN, aligned_edge=LEFT))
        self.play(Restore(angle_formula))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique 100 fois plus faible") as tracker:
            self.play(TransformMatchingTex(angle_formula, angle_formula_min_dev), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Alors l'aiguille devrait bouger de seulement 1 degré") as tracker:
            self.play(TransformMatchingTex(angle_formula_min_dev, angle_formula_min), run_time=tracker.duration)

        self.next_section(skip_animations=section_done)
        self.play(angle_formula_min.animate.scale(1 / 2).next_to(angle_formula_eq, DOWN, aligned_edge=LEFT))
        self.play(Restore(angle_formula))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique 100 fois plus for") as tracker:
            self.play(TransformMatchingTex(angle_formula, angle_formula_max_dev), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Alors l'aiguille devrait bouger à 89 degré") as tracker:
            self.play(TransformMatchingTex(angle_formula_max_dev, angle_formula_max), run_time=tracker.duration)

        self.next_section(skip_animations=section_done)
        self.play(angle_formula_max.animate.scale(1 / 2).next_to(angle_formula_min, DOWN, aligned_edge=LEFT))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Si on arrive à exprimer la relation entre notre champ magnétique et le nombre d'éléctrons qui se déplacent (c'est à dire l'intensité) alors on aura un ampèremetre") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=False)
        with self.myVoiceOver(text=
                              r"La formule du champ magnétique d'un fil traversé par un courant est B=mu0 I / 2 PI r") as tracker:
            self.play(Create(cable_formula), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Mu 0 est une constante de la perméabilité magnétique du vide et vaut 4 PI 10-7"
                              r"r est la distance entre le fil et le point qu'on mesure. Notre boussole devrais être à environ 1 cm soit 10-2 m"
                              r"En simplifiant, on obtient B = 2I 10-5"
                              r"Sauf qu'une patate s'est pas très puissant et que l'intensité qu'on en tirera sera de l'ordre du dixeme de milli-ampère, soit 10-4 ampères"
                              r"On obtient alors un champ magnétique de l'ordre de 2 10-9 Teslas ce qui est bien trop faible pour notre boussole"
                              r"Il va falloir augmenter notre champ magnétique en créant une bobine"
                              r"Le champ magnétique d'une bobine suit la formule suivante : B = K mu 0 N / L I"
                              r"Mu 0 est la même constant qu'auparavant qui vaut 4 PI 10-7"
                              r"L est la longuer de la bobine, pour nous éviter trop de travail, une bobine de 1 cm devrait suffir"
                              r"Il nous reste alors deux inconnue sur lequelles nous avons la main"
                              r"K, qui est la permeabilité relative du matériau que nous allons mettre au centre de la bobine"
                              r"Le fer a une permeabilité fort mais diminue très vite si le fer n'est pas pur. Nous utiliserons donc un clou en fer pour notre bobine et un K = 100 dans nos calculs"
                              r"N est le nombre de tours de la bobine. C'est ce que nous voulons calculer."
                              r"Partons du principe que notre patate nous donne 10-4 ampères"
                              r"Notre objectif est de produire un champ magnétique égal à celui du champ terrestre"
                              r"Si on simplifie nos calculs, on obtiens 5 10-5 = 4 PI 10 -7 N"
                              r"Soit 5 10-5 // 4 PI 10 -7 = N"
                              r"Ce qui donne environ N = 40"
                              r"Pour être tranquilles, je te propose de prendre de la marge et de faire 100 tours"
                              ) as tracker:
            self.wait(tracker.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
