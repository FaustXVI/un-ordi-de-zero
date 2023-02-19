from manim import *
import numpy as np

class Element(VGroup):
    def __init__(self,color: str, name: str, radius: float | None = None):
        self.shell = Circle(radius,color)
        self.shell.set_fill(color,0.5)
        super().__init__(self.shell, MathTex(name))

class ZincIon(Element):
    def __init__(self):
        super().__init__(BLUE,"Zn^{2+}")

class Electron(Element):
    def __init__(self):
        super().__init__(YELLOW_D,"e^{-}",0.33)

class ZincIonGroup(VGroup):

    def __init__(self):
        self.zincIon = ZincIon()
        self.e1 = Electron()
        self.e1.next_to(self.zincIon,RIGHT).shift(UP/2)
        self.e2 = Electron()
        self.e2.next_to(self.zincIon,RIGHT).shift(DOWN/2)
        super().__init__(self.zincIon,self.e1,self.e2)

class Zinc(Element):
    def __init__(self):
        super().__init__(BLUE,"Zn")

    def to_ion(self) -> (ZincIonGroup,Animation):
        group = ZincIonGroup()
        return (group,AnimationGroup(Transform(self,group.zincIon),GrowFromCenter(group.e1),GrowFromCenter(group.e2)))

class CreateCircle(Scene):
    def construct(self):
        z = Zinc()
        self.play(Create(z))
        self.wait()
        (zi,a) = z.to_ion()
        self.play(a)
        self.wait()

