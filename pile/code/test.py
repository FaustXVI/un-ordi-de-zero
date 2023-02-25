from manim import *
from manim.__main__ import main


class Element(VGroup):
    def __init__(self, color: str, name: MathTex, radius: float | None = None):
        self.shell = Circle(radius, color)
        self.shell.set_fill(color, 0.5)
        self.element_name = name
        super().__init__(self.shell, name)


class Ionize(Animation):

    def __init__(self, mobject: Element, new_element: Element, **kwargs) -> None:
        super().__init__(mobject, **kwargs)
        self.change_shell = Transform(mobject.shell, new_element.shell)
        self.change_text = TransformMatchingTex(mobject.element_name, new_element.element_name)

    def begin(self) -> None:
        self.change_shell.begin()
        self.change_text.begin()

    def interpolate(self, alpha: float) -> None:
        self.change_shell.interpolate(alpha)
        self.change_text.interpolate(alpha)


class SurroundingCircle(Circle):
    def __init__(self, content: VMobject, **kwargs):
        super().__init__(radius=max(content.width, content.height), **kwargs)
        self.move_to(content.get_center())


class CreateCircle(Scene):
    def construct(self):
        zn = Element(GRAY_BROWN, MathTex("Zn"))
        # circle = always_redraw(lambda: SurroundingCircle(zn))
        zn2Plus = Element(RED, MathTex("Zn","^{2+}"))
        self.add(zn)
        # self.play(Create(zn))
        self.play(Ionize(zn, zn2Plus))
        self.wait()


if __name__ == "__main__":
    main(["-pql", __file__], prog_name='invoked-command')
