from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

from FakeTraker import FakeTracker

section_done = False

COPPER = ORANGE
ELECTRON_COLOR = YELLOW


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
        self.next_section(skip_animations=section_done)
        acid = MathTex("H^+", "_", "3", "PO_4^{3-}")
        extended_acid = MathTex("3", "H^+", "     ", "PO_4^{3-}")
        zinc_and_extended_acid = MathTex("Zn     ", "3", "H^+", "     ", "PO_4^{3-}")
        zinc_and_acid = MathTex("Zn", "     ", "3", "H^+", "     ", "PO_4^{3-}")
        za = MathTex("Zn", "    "," 3","H^+     ","PO_4^{3-}")
        balanced_zinc_and_acid = MathTex("3", "Zn", "    "," 6","H^+     ","2","PO_4^{3-}")
        step1_zinc_and_acid = MathTex("3", "Zn", "^{2+}", "    ", " 6", "H^+     ", "2", "PO_4^{3-}")
        step2_zinc_and_acid = MathTex("3", "Zn", "^{2+}", "    ", " 3", "H_2     ", "2", "PO_4^{3-}")
        balanced_zinc_acid_copper = MathTex("3", "Zn", "    ", " 6", "H^+     ", "2", "PO_4^{3-}", "     3 Cu")
        zinc_acid_copper = MathTex("3", "Zn", "    ", " 6", "H^+", "     ", "2", "PO_4^{3-}", "     ", "3", "Cu")
        step1_zinc_acid_copper = MathTex("3", "Zn", "    ", " 3", "H_2", "     ", "2", "PO_4^{3-}", "     ", "3", "Cu")
        step2_zinc_acid_copper = MathTex("3", "Zn", "    ", " 3", "H_2", "     ", "2", "PO_4^{3-}", "     ", "3", "Cu",
                                         "^{2+}")
        step2bis_zinc_acid_copper = MathTex("3", "Zn", "     3H_2     2PO_4^{3-}     3Cu^{2+}")
        step3_zinc_acid_copper = MathTex("3", "Zn","^{2+}", "     3H_2     2PO_4^{3-}     3Cu^{2+}")
        step4_zinc_acid_copper = MathTex("3", "Zn", "^{2+}", "     ", "3", "H_2", "     ", "2", "PO_4^{3-}",
                                         "     ",
                                         "3", "Cu", "^{2+}")
        step5_zinc_acid_copper = MathTex("3Zn^{2+}     3H_2     2PO_4^{3-}     ","3Cu", "^{2+}")
        final_eq = MathTex("3Zn^{2+}     3H_2     2PO_4^{3-}     ","  ","3Cu","^{ }")
        with self.myVoiceOver(
                text=r"Les patates contiennent de l'acide phosphoric qu'on not H 3+ PO4 3-.") as tracker:
            self.play(FadeIn(acid), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Cela veut dire qu'il est composé de 3 ions H ayant une charge positive et un ion PO4 ayant 3 changes négatives."
                     r"Les ions, c'est des éléments qui on gagné ou perdu des éléctrons"
                     r"Les ions négatifs, appelés les anions, sont attiré par les ions positifs appelés les cations") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Pour nous aider à visualiser, on vas étendre notre formule") as tracker:
            self.play(TransformMatchingTex(acid, extended_acid), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Si on ajoute du zinc, noté Zn, qu'on trouve sur la majorité des clous.") as tracker:
            self.play(TransformMatchingTex(extended_acid, zinc_and_extended_acid), run_time=tracker.duration)
            self.remove(zinc_and_extended_acid)
            self.add(zinc_and_acid)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"L'acide va réagir avec en lui prenant deux electrons pour les donner aux cations d'hydrogène.") as tracker:
            arc = ArcBetweenPoints(zinc_and_acid.get_part_by_tex("Zn").get_edge_center(UP),
                                   zinc_and_acid.get_part_by_tex("H^+").get_edge_center(UP), -PI / 2)
            elec = [Dot(color=ELECTRON_COLOR).move_to(zinc_and_acid.get_part_by_tex("Zn").get_edge_center(UP)) for _ in
                    range(0, 2)]
            self.play(
                AnimationGroup(
                    AnimationGroup(
                        *[Succession(FadeIn(e, rate_func=rate_functions.ease_in_expo),
                                     MoveAlongPath(e, arc, rate_func=linear),
                                     FadeOut(e, rate_func=rate_functions.ease_out_expo)) for e in elec],
                        lag_ratio=0.1
                    ),
                    lag_ratio=0.75,
                    run_time=tracker.duration
                )
            )

        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Cependant, notre équation n'est pas équilibré car le Zinc ne peux donner que deux électrons et nous avons besoin de 3 pour l'hydrogène") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"On peut équilibrer notre équation en utilisant 3 Zinc pour 2 acide phosphorique") as tracker:
            self.remove(zinc_and_acid)
            self.add(za)
            self.play(TransformMatchingTex(za, balanced_zinc_and_acid), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Il y a alors 6 éléctrons qui peuvent partir du zinc pour aller aux cations hydrogène",
                duration=3) as tracker:
            arc = ArcBetweenPoints(balanced_zinc_and_acid.get_part_by_tex("Zn").get_edge_center(UP),
                                   balanced_zinc_and_acid.get_part_by_tex("H^+").get_edge_center(UP), -PI / 2)
            elec = [Dot(color=ELECTRON_COLOR).move_to(balanced_zinc_and_acid.get_part_by_tex("Zn").get_edge_center(UP))
                    for _ in
                    range(0, 6)]
            self.play(
                AnimationGroup(
                    AnimationGroup(
                        *[Succession(FadeIn(e, rate_func=rate_functions.ease_in_expo),
                                     MoveAlongPath(e, arc, rate_func=linear),
                                     FadeOut(e, rate_func=rate_functions.ease_out_expo)) for e in elec],
                        lag_ratio=0.1
                    ),
                    lag_ratio=0.75,
                    run_time=tracker.duration
                )
            )
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Les atomes de zinc ont alors perdu 2 éléctrons, on les note Zn 2+") as tracker:
            self.play(TransformMatchingTex(balanced_zinc_and_acid, step1_zinc_and_acid), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Les atomes d'hydrogène vont alors s'associer pour former du di-hydrogène noté H2") as tracker:
            self.play(TransformMatchingTex(step1_zinc_and_acid, step2_zinc_and_acid), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"À ce stade, on a vu des éléctrons qui bougent, ce qui est la définition de l'éléctricité."
                     r"Le problème, c'est qu'on aimerait que ces éléctrons passent par un fil"
        ) as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=r"Reprennons notre formule d'avant la réaction") as tracker:
            self.play(AnimationGroup(FadeOut(step2_zinc_and_acid, rate_func=linear),
                                     FadeIn(balanced_zinc_and_acid, rate_func=linear), lag_ratio=1),
                      run_time=tracker.duration, rate_func=linear)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"L'astuce, c'est de donner aux cations de l'hydrogène des éléctrons plus facile à arracher que ceux du zinc") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Le cuivre, noté Cu, est parfait pour ce rôle et n'importe quelle pièce de 5 centimes en contient.") as tracker:
            self.play(TransformMatchingTex(balanced_zinc_and_acid, balanced_zinc_acid_copper))
            self.remove(balanced_zinc_acid_copper)
            self.add(zinc_acid_copper)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"L'hydrogène va alors prendre des électrons au cuivre") as tracker:
            arc = ArcBetweenPoints(zinc_acid_copper.get_part_by_tex("Cu").get_edge_center(UP),
                                   zinc_acid_copper.get_part_by_tex("H^+").get_edge_center(UP))
            elec = [Dot(color=ELECTRON_COLOR).move_to(zinc_acid_copper.get_part_by_tex("Cu").get_edge_center(UP))
                    for _ in
                    range(0, 6)]
            self.play(
                AnimationGroup(
                    AnimationGroup(
                        *[Succession(FadeIn(e, rate_func=rate_functions.ease_in_expo),
                                     MoveAlongPath(e, arc, rate_func=linear),
                                     FadeOut(e, rate_func=rate_functions.ease_out_expo)) for e in elec],
                        lag_ratio=0.1
                    ),
                    lag_ratio=0.75,
                    run_time=tracker.duration
                )
            )
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Cela va produire du di-hydrogène, comme avant") as tracker:
            self.play(TransformMatchingTex(zinc_acid_copper, step1_zinc_acid_copper), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Et le cuivre va se transformer en cations") as tracker:
            self.play(TransformMatchingTex(step1_zinc_acid_copper, step2_zinc_acid_copper), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Mais le reste d'acide vas toujours chercher les cations de zinc") as tracker:
            self.remove(step2_zinc_acid_copper)
            self.add(step2bis_zinc_acid_copper)
            self.play(TransformMatchingTex(step2bis_zinc_acid_copper, step3_zinc_acid_copper), run_time=tracker.duration)
            self.remove(step3_zinc_acid_copper)
            self.add(step4_zinc_acid_copper)
        self.next_section(skip_animations=section_done)
        zinc_charged = step4_zinc_acid_copper.get_part_by_tex("Zn").get_edge_center(DOWN)
        with self.myVoiceOver(
                text=r"Ça a pour effet de laisser des electrons derrière") as tracker:
            elec = VGroup(*[Dot(color=ELECTRON_COLOR).move_to(zinc_charged).shift(LEFT * 0.2)
                            for _ in
                            range(0, 6)]).arrange(buff=0.01, center=False)
            self.play(FadeIn(elec), run_time=tracker.duration / 2)
            self.play(FadeOut(elec), run_time=tracker.duration / 2)
        cable = ArcBetweenPoints(zinc_charged + (DOWN*0.1),
                                 step4_zinc_acid_copper.get_part_by_tex("Cu").get_edge_center(DOWN) + (DOWN*0.1), color=COPPER)
        with self.myVoiceOver(
                text=r"C'est là qu'on peut mettre un fil entre le zinc et le cuivre") as tracker:
            self.play(FadeIn(cable), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Les éléctrons peuvent alors facilement rejoindre les cations de cuivre") as tracker:
            elec = [Dot(color=ELECTRON_COLOR).move_to(zinc_charged)
                    for _ in
                    range(0, 6)]
            self.play(
                AnimationGroup(
                    AnimationGroup(
                        *[Succession(FadeIn(e, rate_func=rate_functions.ease_in_expo),
                                     MoveAlongPath(e, cable, rate_func=linear),
                                     FadeOut(e, rate_func=rate_functions.ease_out_expo)) for e in elec],
                        lag_ratio=0.1
                    ),
                    lag_ratio=0.75,
                    run_time=tracker.duration
                )
            )
        self.next_section(skip_animations=False)
        with self.myVoiceOver(
                text=r"Les cations de cuivre vont alors redevenir du cuivre") as tracker:
            self.remove(step4_zinc_acid_copper)
            self.add(step5_zinc_acid_copper)
            self.play(TransformMatchingTex(step5_zinc_acid_copper, final_eq), run_time=tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(
                text=r"Et comme on a des électrons qui passent dans notre cable, on a de l'éléctricité") as tracker:
            self.play(Indicate(cable,scale_factor=1), run_time=tracker.duration)
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
