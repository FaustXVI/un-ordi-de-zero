from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

from FakeTraker import FakeTracker

section_done = True
recording = False


def my_frac(d, n):
    return [r"{", r"{", *d, r"}", r"\over", r"{", *n, r"}", r"}"]


class ChemicalReaction(VoiceoverScene):

    def myVoiceOver(self, text, duration=1):
        if recording:
            return self.voiceover(text)
        else:
            return FakeTracker(duration)

    def construct(self):
        self.next_section(skip_animations=section_done)
        self.set_speech_service(RecorderService())
        tesla = MathTex("T", "esla")
        champ_terrestre = VGroup(MathTex(r"B_{t} = "), MathTex(r"5 \times 10^{-5}"), MathTex(r"T")).arrange()
        angle_formula = MathTex(r"\alpha", r"=",
                                r" 90 \times ",
                                *my_frac(["B"], [r"B", r" + ", r"B_{t}"]))
        angle_formula_eq_dev = MathTex(r"\alpha", r"_{5 \times 10^{-5}}",
                                       r"=",
                                       r" 90 \times ",
                                       *my_frac([r"5 \times 10^{-5}"],
                                                [r"5 \times 10^{-5}", r" + ", r"5 \times 10^{-5}"])
                                       )
        angle_formula_eq = MathTex(r"\alpha", r"_{5 \times 10^{-5}}", r"\approx", r" 45")
        angle_formula_min_dev = MathTex(r"\alpha", r"_{5 \times 10^{-7}}",
                                        r"=",
                                        r" 90 \times ",
                                        *my_frac([r"5 \times 10^{-7}"],
                                                 [r"5 \times 10^{-7}", r" + ", r"5 \times 10^{-5}"]))

        angle_formula_min = MathTex(r"\alpha", r"_{5 \times 10^{-7}}", r"\approx", r" 1")
        angle_formula_max_dev = MathTex(r"\alpha", r"_{5 \times 10^{-3}}",
                                        r"=",
                                        r" 90 \times ",
                                        *my_frac([r"5 \times 10^{-3}"],
                                                 [r"5 \times 10^{-3}", r" + ", r"5 \times 10^{-5}"]))

        angle_formula_max = MathTex(r"\alpha", r"_{5 \times 10^{-3}}", r"\approx", r" 89")
        cable_formula = MathTex(r"{{B = }}{ \frac{\mu_0}{2 \pi r} } {{I}}")
        mu_0 = VGroup(MathTex(r"\mu_0 ="), MathTex(r"4 \pi \times 10^{-7}")).arrange().next_to(cable_formula, UP)
        cable_formula_with_mu = MathTex(r"{{B = }}\frac{4 \pi \times 10^{-7}}{2 \pi r}{{I}}")
        cable_distance = MathTex(r"r = {{10^-2}}").next_to(cable_formula_with_mu, UP)
        cable_formula_with_mu_r = MathTex(r"{{B = }}\frac{4 \pi \times 10^{-7}}{ 2 \pi \times 10^-2 }{{I}}")
        cable_reduced_formula = MathTex(r"{{B = }}2 \times 10^-5 {{I}}")
        potato_intesity = VGroup(MathTex(r"I \approx "), MathTex(r"10^-4")).arrange().next_to(cable_reduced_formula, UP)
        cable_reduced_formula_before_final = MathTex(r"{{B = }}2 \times 10^-5 {{\times }}{{10^-4}}")
        cable_field = MathTex(r"{{B = }}2 \times 10^-9")

        coil_formula = MathTex(r"B ", "=", "k", "\mu_0", r"\frac{N}{L}", "I")
        coil_formula_mu = MathTex(r"B ", "=", "k", r"\times", r"4 \pi \times 10^{-7}", r"\times", r"\frac{N}{L}", "I")
        coil_length = VGroup(MathTex(r"L ="), MathTex(r"10^{-2}")).arrange().next_to(cable_formula, UP)
        coil_formula_mu_l = MathTex(r"B ", "=", "k", r"\times", r"4 \pi \times 10^{-7}", r"\times",
                                    r"\frac{N}{10^{-2}}",
                                    "I")
        iron_permeability = VGroup(MathTex(r"k ="), MathTex(r"100")).arrange().next_to(cable_formula, UP)
        coil_formula_mu_l_k = MathTex(r"B ", "=", "100", r"\times", r"4 \pi \times 10^{-7}", r"\times",
                                      r"\frac{N}{10^{-2}}",
                                      "I")
        coil_formula_mu_l_k_i = MathTex(r"B ", "=", "100", r"\times", r"4 \pi \times 10^{-7}", r"\times",
                                        r"\frac{N}{10^{-2}}",
                                        "10^-4")
        coil_formula_without_n = MathTex(r"5 \times 10^{-5}", "=", "100", r"\times", r"4 \pi \times 10^{-7}", r"\times",
                                         r"\frac{N}{10^{-2}}",
                                         "10^-4")
        coil_formula_reduced = MathTex(r"5 \times 10^{-5}", "=", r"4 \pi \times 10^{-7}", r"N")
        n_formula = MathTex(r"N", "=", "{", r"4 \pi \times 10^{-7}", r"\over", r"5 \times 10^{-5}", "}")
        n_40 = MathTex(r"N", "=", "40")
        n_100 = MathTex(r"N", "=", "100")

        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Une boussole, ça suit le champ magnétique terrestre et un champ manétique, ça se mesure en Teslas") as tracker:
            self.play(Create(tesla), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Le champ magnétique terrestre, en France, fait environ 5 * 10-5 Teslas et on le notera B T") as tracker:
            self.play(TransformMatchingTex(tesla, champ_terrestre), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Cette valeur sera important pour la suite, gardons la dans un coin",
                              duration=3) as tracker:
            self.play(champ_terrestre.animate.scale(1 / 2).to_edge(UL, buff=1), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique B perpendiculaire au champ terrestre et suffisament fort, on verra la boussole bouger"
                              r"Le mouvement de l'aiguille est propotionnel à rapport entre le champ créé et le champ terrestre"
                              r"On peut calculer l'angle dont va se déplacer l'aiguille avec la formule alpha = 90 * B / (B + 5*10-5)") as tracker:
            self.play(FadeIn(angle_formula), run_time=tracker.duration)
        angle_formula.save_state()
        self.next_section(skip_animations=False)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique égal au champ terrestre", duration=3) as tracker:
            self.play(TransformMatchingTex(Group(angle_formula, champ_terrestre.copy()), angle_formula_eq_dev),
                      run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Alors l'aiguille devrait bouger à 45 degrées") as tracker:
            self.play(TransformMatchingTex(angle_formula_eq_dev, angle_formula_eq, key_map={"=": r"\approx"}),
                      run_time=tracker.duration)

        self.play(angle_formula_eq.animate.scale(1 / 2).next_to(champ_terrestre, DOWN, aligned_edge=LEFT))
        self.play(Restore(angle_formula))
        self.next_section(skip_animations=False)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique 100 fois plus faible", duration=3) as tracker:
            self.play(TransformMatchingTex(angle_formula, angle_formula_min_dev), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Alors l'aiguille devrait bouger de seulement 1 degré") as tracker:
            self.play(TransformMatchingTex(angle_formula_min_dev, angle_formula_min, key_map={"=": r"\approx"}),
                      run_time=tracker.duration)

        self.play(angle_formula_min.animate.scale(1 / 2).next_to(angle_formula_eq, DOWN, aligned_edge=LEFT))
        self.play(Restore(angle_formula))
        self.next_section(skip_animations=False)
        with self.myVoiceOver(text=
                              r"Si on applique un champ magnétique 100 fois plus for") as tracker:
            self.play(TransformMatchingTex(angle_formula, angle_formula_max_dev), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Alors l'aiguille devrait bouger à 89 degré") as tracker:
            self.play(TransformMatchingTex(angle_formula_max_dev, angle_formula_max, key_map={"=": r"\approx"}),
                      run_time=tracker.duration)

        self.play(angle_formula_max.animate.scale(1 / 2).next_to(angle_formula_min, DOWN, aligned_edge=LEFT))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Si on arrive à exprimer la relation entre notre champ magnétique et le nombre d'éléctrons qui se déplacent (c'est à dire l'intensité) alors on aura un ampèremetre") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"La formule du champ magnétique d'un fil traversé par un courant est B=mu0 / 2 PI r fois I") as tracker:
            self.play(Create(cable_formula), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Mu 0 est une constante de la perméabilité magnétique du vide et vaut 4 PI 10-7") as tracker:
            self.play(Create(mu_0), run_time=tracker.duration)
        self.play(TransformMatchingTex(Group(cable_formula, mu_0), cable_formula_with_mu), run_time=2)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"r est la distance entre le fil et le point qu'on mesure. Notre boussole devrais être à environ 1 cm soit 10-2 m") as tracker:
            self.play(Create(cable_distance), run_time=tracker.duration)
        self.play(TransformMatchingTex(Group(cable_formula_with_mu, cable_distance), cable_formula_with_mu_r),
                  run_time=2)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"En simplifiant, on obtient B = 2 fois 10-5 I") as tracker:
            self.play(TransformMatchingTex(cable_formula_with_mu_r, cable_reduced_formula), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Sauf qu'une patate s'est pas très puissant et que l'intensité qu'on en tirera sera de l'ordre du dixeme de milli-ampère, soit 10-4 ampères") as tracker:
            self.play(Create(potato_intesity), run_time=tracker.duration)
        self.play(
            TransformMatchingTex(Group(cable_reduced_formula, potato_intesity), cable_reduced_formula_before_final),
            run_time=2)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"On obtient alors un champ magnétique de l'ordre de 2 10-9 Teslas") as tracker:
            self.play(TransformMatchingTex(cable_reduced_formula_before_final, cable_field), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Ceci est 100 fois trop faible pour faire bouger notre boussolle ne serai-ce que d'un degre") as tracker:
            self.play(Indicate(angle_formula_min), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Il va falloir augmenter notre champ magnétique en créant une bobine") as tracker:
            self.play(Uncreate(cable_field), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Le champ magnétique d'une bobine suit la formule suivante : B = K mu 0 N / L I") as tracker:
            self.play(Create(coil_formula), run_time=tracker.duration)
        self.next_section(skip_animations=True)
        with self.myVoiceOver(text=
                              r"Mu 0 est la même constant qu'auparavant qui vaut 4 PI 10-7") as tracker:
            self.play(Create(mu_0), run_time=tracker.duration)
        self.play(TransformMatchingTex(Group(coil_formula, mu_0), coil_formula_mu))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"L est la longuer de la bobine, pour nous éviter trop de travail, une bobine de 1 cm devrait suffir") as tracker:
            self.play(Create(coil_length), run_time=tracker.duration)
        self.play(TransformMatchingTex(Group(coil_formula_mu, coil_length), coil_formula_mu_l))
        with self.myVoiceOver(text=
                              r"Il nous reste alors deux inconnue sur lequelles nous avons la main") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"K, qui est la permeabilité relative du matériau que nous allons mettre au centre de la bobine") as tracker:
            self.play(Indicate(coil_formula_mu_l.get_part_by_tex("k")), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"et N, qui est le nombre de tours de la bobine. C'est ce que nous voulons calculer.") as tracker:
            self.play(Indicate(coil_formula_mu_l.get_part_by_tex("N")[0]), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Le fer a une permeabilité fort mais diminue très vite si le fer n'est pas pur."
                              r"Nous utiliserons donc un clou en fer pour notre bobine et un K = 100 dans nos calculs") as tracker:
            self.play(Create(iron_permeability), run_time=tracker.duration)
        self.play(TransformMatchingTex(Group(coil_formula_mu_l, iron_permeability), coil_formula_mu_l_k))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Pour trouver N, partons du principe que notre patate nous donne 10-4 ampères") as tracker:
            self.play(Create(potato_intesity), run_time=tracker.duration)
        self.play(TransformMatchingTex(Group(coil_formula_mu_l_k, potato_intesity), coil_formula_mu_l_k_i))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Notre objectif est de produire un champ magnétique égal à celui du champ terrestre") as tracker:
            self.play(Indicate(champ_terrestre), run_time=tracker.duration)
        self.play(TransformMatchingTex(Group(coil_formula_mu_l_k_i, champ_terrestre.copy()), coil_formula_without_n),
                  run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Si on simplifie nos calculs, on obtiens 5 10-5 = 4 PI 10 -7 N") as tracker:
            self.play(TransformMatchingTex(coil_formula_without_n, coil_formula_reduced), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Soit 5 10-5 // 4 PI 10 -7 = N") as tracker:
            self.play(TransformMatchingTex(coil_formula_reduced, n_formula), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=
                              r"Ce qui donne environ N = 40") as tracker:
            self.play(TransformMatchingTex(n_formula, n_40), run_time=tracker.duration)
        with self.myVoiceOver(text=
                              r"Pour être tranquilles, je te propose de prendre de la marge et de faire 100 tours"
                              ) as tracker:
            self.play(TransformMatchingTex(n_40, n_100), run_time=tracker.duration)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
