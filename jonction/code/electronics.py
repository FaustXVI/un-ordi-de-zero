from typing import Sequence

from manim import *

section_done = False

flat_map = lambda f, xs: (y for ys in xs for y in f(ys))


class Electronic(VGroup):
    def __init__(self):
        super().__init__()

    def entry_point(self):
        return self.submobjects[0].get_start()

    def exit_point(self):
        return self.submobjects[-1].get_end()

    def connect(self, other_electronic):
        start = self.exit_point()
        finish = other_electronic.entry_point()
        if (abs(finish[0]) > abs(start[0])):
            midpoint = [finish[0], start[1], 0]
        else:
            midpoint = [start[0], finish[1], 0]

        return VGroup(Cable(start, midpoint), Cable(midpoint, finish))

    def energize(self, dot):
        raise NotImplementedError("Todo : implement energize")


class Contact(Electronic):
    def __init__(self, position):
        super().__init__()
        self.dot = Dot(position).set_opacity(0)
        self.add(self.dot)

    def entry_point(self):
        return self.dot.get_center()

    def exit_point(self):
        return self.dot.get_center()

class Cable(Line):

    def __init__(self, start=LEFT, end=RIGHT, buff=0, path_arc=None, **kwargs):
        super().__init__(start, end, buff, path_arc, **kwargs)

    def energize(self, dot):
        return MoveAlongPath(dot, self, rate_func=linear, run_time=self.get_length() / 2)


class Resistance(Electronic):
    def __init__(self):
        super().__init__()
        n = 9
        step = 2 / n

        self.pts = [LEFT, LEFT / 2,
                    *[LEFT / 2 * (1 - i * step) + (DOWN / 4 if i % 2 == 0 else UP / 4) for i in
                      range(1, round(n / 2) + 1)],
                    *[RIGHT / 2 * (1 - (round(n / 2) - i) * step) + (UP / 4 if i % 2 == 0 else DOWN / 4) for i in
                      range(0, round(n / 2))],
                    RIGHT / 2, RIGHT]
        self.lines = [Line(a, b) for a, b in zip(self.pts, self.pts[1:])]
        self.add(*self.lines)

    def energize(self, dot):
        return Succession(*[
            MoveAlongPath(dot, line, rate_func=linear) for line in self.submobjects
        ])


class Switch(Electronic):
    def __init__(self):
        super().__init__()
        self.closed = False
        self.moving_line = Line(LEFT / 2, RIGHT / 2).rotate(-PI / 12, about_point=LEFT / 2)
        self.add(Line(LEFT, LEFT / 2), Dot().move_to(LEFT / 2).scale(1 / 3), self.moving_line,
                 Dot().move_to(RIGHT / 2).scale(1 / 3), Line(RIGHT / 2, RIGHT))

    def energize(self, dot):
        if not self.closed:
            raise RuntimeError("Trying to energize an open circuit")
        return Succession(*[
            MoveAlongPath(dot, line, rate_func=linear) for line in self.submobjects if isinstance(line, Line)
        ])

    def rotate(self, angle: float, axis: np.ndarray = OUT, about_point: Sequence[float] | None = None, **kwargs):
        if about_point is None:
            about_point = Line(self.submobjects[0].get_start(), self.submobjects[-1].get_end()).get_center()
        return super().rotate(angle, axis, about_point, **kwargs)

    def close(self):
        if not self.closed:
            self.moving_line.rotate(PI / 12, about_point=self.moving_line.get_start())
            self.closed = True

    def open(self):
        if self.closed:
            self.moving_line.rotate(-PI / 12, about_point=self.moving_line.get_start())
            self.closed = False


class Battery(Electronic):
    def __init__(self):
        super().__init__()
        self.add(Line(LEFT, LEFT / 6),
                 Line((LEFT / 6) + UP / 2, (LEFT / 6) + DOWN / 2),
                 Line((RIGHT / 6) + (UP / 4), (RIGHT / 6) + (DOWN / 4)),
                 MathTex("+").shift((LEFT / 3) + (UP / 3)).scale(0.75),
                 MathTex("-").shift((RIGHT / 3) + (UP / 3)).scale(0.75),
                 Line(RIGHT / 6, RIGHT),
                 )

    def energize(self, dot):
        dot.set_opacity(0).move_to(self.submobjects[-1].get_start())
        return Succession(dot.animate(rate_func=linear).set_opacity(1),
                          MoveAlongPath(dot, self.submobjects[-1], rate_func=linear))

    def consume(self, dot):
        return Succession(MoveAlongPath(dot, self.submobjects[0], rate_func=linear),
                          dot.animate(rate_func=linear).set_opacity(0).move_to(self.submobjects[0].get_end()))


class Mesurement(Electronic):
    def __init__(self, letter):
        super().__init__()
        self.circle = Circle(color=WHITE, radius=1 / 2).rotate(PI)
        self.letter = Tex(letter)
        self.entry = Line(LEFT * self.circle.radius * 2, LEFT * self.circle.radius)
        self.exit = Line(RIGHT * self.circle.radius, RIGHT * self.circle.radius * 2)
        self.add(self.entry, self.circle, self.letter, self.exit)

    def rotate(self, angle: float, axis: np.ndarray = OUT, about_point: Sequence[float] | None = None, **kwargs):
        r = super().rotate(angle, axis, about_point, **kwargs)
        r.letter.rotate(-angle)
        return r

    def energize(self, dot):
        color = self.get_color()
        return Succession(
            MoveAlongPath(dot, self.submobjects[0], rate_func=linear),
            AnimationGroup(dot.animate(run_time=0).set_opacity(0)),
            AnimationGroup(
                self.circle.animate(rate_func=linear).set_color(dot.get_color()),
                self.letter.animate(rate_func=linear).set_color(dot.get_color())),
            AnimationGroup(self.circle.animate(rate_func=linear).set_color(color),
                           self.letter.animate(rate_func=linear).set_color(color),
                           ),
            AnimationGroup(dot.animate(run_time=0).set_opacity(1)),
            MoveAlongPath(dot, self.submobjects[-1], rate_func=linear)
        )


class Ameter(Mesurement):
    def __init__(self):
        super().__init__("A")


class Voltmeter(Mesurement):
    def __init__(self):
        super().__init__("V")


class Ohmmeter(Mesurement):
    def __init__(self):
        super().__init__(r"$\Omega$")


class Circuit(VGroup):

    def __init__(self, battery, *vmobjects, **kwargs):
        super().__init__(battery, *vmobjects, **kwargs)
        self.battery = battery

    def run_electron(self):
        electron = Dot(color=YELLOW)
        return Succession(*[o.energize(electron) for o in self.submobjects], self.battery.consume(electron))


class Junction(Electronic):
    def __init__(self, *branches):
        super().__init__()
        self.start = Contact(center_of_mass([branch.entry_point() for branch in branches]))
        self.stop = Contact(center_of_mass([branch.exit_point() for branch in branches]))
        self.add(self.start, *flat_map(lambda b: [self.start.connect(b),b,b.connect(self.stop)], branches), self.stop)

    def entry_point(self):
        return self.start.entry_point()

    def exit_point(self):
        return self.stop.exit_point()


class Branch(Electronic):
    def __init__(self, *vmobjects):
        super().__init__()
        self.add(*vmobjects)

    def entry_point(self):
        return self.submobjects[0].entry_point()

    def exit_point(self):
        return self.submobjects[-1].exit_point()
