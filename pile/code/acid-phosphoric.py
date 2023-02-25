from abc import ABC

from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService


class Element(VGroup, ABC):
    def __init__(self, color: str, name: MathTex, radius: float | None = None):
        self.shell = Circle(radius, color)
        self.shell.set_fill(color, 0.5)
        self.name = name
        super().__init__(self.shell, name)


class HydrogeneIon(Element):
    def __init__(self):
        super().__init__(RED_A, MathTex("H", "^{+}"), 0.5)


class TriHydrogene(VGroup):
    def __init__(self):
        super().__init__()
        self.tri_h = Element(RED_A, MathTex("H_{3}^{+}"), 1)
        self.add(self.tri_h)

    def decompose(self, animate):
        hydrogens = [HydrogeneIon().move_to(self.get_center()) for _ in range(0, 3)]
        hydrogens[1].next_to(hydrogens[0], UP)
        hydrogens[2].next_to(hydrogens[0], DOWN)
        self.add(*hydrogens)
        animate(FadeOut(self.tri_h), *[FadeIn(h) for h in hydrogens])
        self.remove(self.tri_h)


class AcidRoot(Element):
    def __init__(self):
        super().__init__(GREEN_B, MathTex("PO", "_{4}", "^{3-}"), 1)


class AcidPhosphoric(VGroup):
    def __init__(self):
        super().__init__()
        self.acid_root = None
        self.tri_hydro = None
        self.acid = Element(GRAY_BROWN, MathTex("Acid phosphorique"), 2)
        self.add(self.acid)

    def decompose(self, animate) -> (TriHydrogene, AcidRoot):
        self.tri_hydro = TriHydrogene()
        self.tri_hydro.move_to(LEFT)
        self.add(self.tri_hydro)
        self.acid_root = AcidRoot()
        self.acid_root.move_to(RIGHT)
        self.add(self.acid_root)
        animate(FadeOut(self.acid), FadeIn(self.tri_hydro), FadeIn(self.acid_root))
        self.remove(self.acid)


class Electron(Element):
    def __init__(self):
        super().__init__(YELLOW_D, MathTex("e^{-}"), 0.33)


class Electrons(VGroup):
    def __init__(self, n: int):
        super().__init__()
        [self.add(Electron()) for _ in range(0, n)]


class Zinc(VGroup):
    def __init__(self):
        super().__init__()
        self.electrons = None
        self.zincIon = None
        self.zinc = Element(BLUE, MathTex("Zn"))
        self.add(self.zinc)

    def to_ion(self, animate):
        self.zincIon = Element(BLUE, MathTex("Zn", "^{2+}"))
        self.add(self.zincIon)
        self.electrons = Electrons(2)
        self.add(self.electrons)
        animate(Transform(self.zinc,self.zincIon),
                *[GrowFromCenter(e) for e in self.electrons],
                self.electrons[0].animate.next_to(self.zincIon, RIGHT).shift(UP / 2),
                self.electrons[1].animate.next_to(self.zincIon, RIGHT).shift(DOWN / 2)
                )
        self.remove(self.zinc)


section_done = True


class CreateCircle(VoiceoverScene):
    def construct(self):
        self.next_section(skip_animations=section_done)
        service = GTTSService(lang="fr") if section_done else RecorderService()
        self.set_speech_service(service)
        self.next_section(skip_animations=section_done)
        acid = self.create_acid()
        self.next_section()
        zinc = self.create_zinc()
        self.next_section(skip_animations=section_done)
        with self.voiceover(text="Les ions hydrogène de l'acide") as tracker:
            self.play(Indicate(acid.tri_hydro), run_time=tracker.duration)

        self.play(Indicate(zinc.electrons))
        self.next_section(skip_animations=section_done)
        zinc2 = zinc.copy()
        zinc3 = zinc.copy()
        acid2 = acid.copy()
        self.play(
            zinc2.animate.shift(UP * zinc.height * 1.1),
            zinc3.animate.shift(DOWN * zinc.height * 1.1),
            acid.animate.shift(DOWN * acid.height / 1.8),
            acid2.animate.shift(UP * acid.height / 1.8),
        )
        self.wait()

    def create_zinc(self):
        zinc = Zinc()
        self.play(FadeIn(zinc))
        self.wait()
        zinc.to_ion(self.play)
        self.wait()
        self.play(zinc.animate.move_to(LEFT * 2))
        return zinc

    def create_acid(self):
        acid = AcidPhosphoric()
        self.play(FadeIn(acid))
        self.wait()
        acid.decompose(self.play)
        self.wait()
        acid.tri_hydro.decompose(self.play)
        self.play(acid.animate.move_to(RIGHT * 5))
        self.wait()
        return acid


if __name__ == "__main__":
    main(["-pql", __file__], prog_name='invoked-command')
