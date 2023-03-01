from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

# config.disable_caching = True

section_done = False

COPPER = ORANGE
ELECTRON_COLOR = YELLOW


class Radiate(Animation):

    def __init__(self, mobject: Mobject, scale=2, **kwargs) -> None:
        self.radiation = mobject.copy()
        self.scale = scale
        self.original_width = mobject.get_stroke_width()
        super().__init__(self.radiation, **kwargs)

    def interpolate_mobject(self, alpha: float) -> None:
        alpha = self.rate_func(alpha)
        self.mobject.set_stroke_width(self.original_width + self.original_width * self.scale * alpha) \
            .set_opacity(1 - alpha)

    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
        scene.remove(self.mobject)


class ElectroMagnetism(VoiceoverScene):

    def construct(self):
        self.next_section(skip_animations=section_done)
        service = GTTSService(lang="fr") if section_done else RecorderService()
        self.set_speech_service(service)

        self.next_section(skip_animations=section_done)
        screen = FullScreenRectangle()
        electrons = [Dot(color=ELECTRON_COLOR).set_opacity(0).to_edge(LEFT, buff=-1) for _ in range(0, 100)]
        visibleElectrons = [e.copy().set_opacity(1) for e in electrons]
        cable = Line(start=screen.get_edge_center(LEFT), end=screen.get_edge_center(RIGHT), color=COPPER, buff=-1,
                     stroke_width=100,
                     stroke_opacity=0.9
                     )
        self.add(cable)
        self.add(turn_animation_into_updater(AnimationGroup(
            *[electron.animate(rate_func=linear, run_time=5).to_edge(RIGHT, buff=-1) for electron in electrons],
            lag_ratio=0.1,
            rate_func=linear
        ), cycle=False))
        electrons_opacity = ValueTracker(1)
        self.add(
            always_redraw(lambda: VGroup(
                *[ve.move_to(e.get_center()).set_opacity(electrons_opacity.get_value()) for ve, e in
                  zip(visibleElectrons, electrons)])))
        with self.myVoiceOver(
                text=r"Comme je te l'ai dis, l'éléctricité, c'est des éléctrons qui se déplacent."
                     r"Imagine un moment que les éléctrons sont des bateaux et que le fil est un canal.") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=r"Quand un bateau se déplace, il laisse derrière lui un sillage.") as tracker:
            self.wait(1)
            sillages = [
                Elbow(angle=-PI / 4, width=0.8, stroke_color=COPPER, stroke_opacity=0.9).move_to(electron.get_center())
                for electron in electrons]
            self.add(always_redraw(lambda: VGroup(*[
                elbow.move_to(electron.get_center()).shift(LEFT * electron.width) for elbow, electron in
                zip(sillages, electrons)
            ])))
            self.play(AnimationGroup(*[FadeIn(sillage) for sillage in sillages]), run_time=3)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=r"Si on se place sur le côté du canal, on peut voir des vagues duent au sillages."
                                   r"Plus on voit de vagues plus en on déduis qu'il y a beaucoup de bateaux qui passent") as tracker:
            self.wait(tracker.duration)
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=r"D'ailleurs, on a même pas besoin de voir les bateaux pour savoir qu'ils sont là."
                                   r"Les vagues nous suffisent.") as tracker:
            self.play(electrons_opacity.animate(rate_func=linear, run_time=tracker.duration).set_value(0))
        self.next_section(skip_animations=section_done)
        with self.myVoiceOver(text=r"Le plan d'eau, c'est léquivalant de ce qu'on appele le champ magnétique."
                                   r"Dit autrement, si on vois un champ magnétique changer, on peut en déduire qu'il y a de l'électricité pas loin."
                                   r"La bonne nouvelle, c'est qu'un champ magnétique, ça s'observe facilement grâce à une boussole") as tracker:
            self.wait(tracker.duration + 1)

    def myVoiceOver(self, text):
        # if not self.skip_animations:
            return self.voiceover(text)
        # else:
        # return FakeTracker()


if __name__ == "__main__":
    main(["-pqm",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
