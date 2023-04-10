import operator
from itertools import accumulate
from typing import Sequence

from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Electronic(VGroup):
    def __init__(self):
        super().__init__()

    def entry_point(self):
        return self.submobjects[0].get_start()

    def exit_point(self):
        return self.submobjects[-1].get_end()

    def connect(self, other_electronic):
        return Cable(self.exit_point(), other_electronic.entry_point())

    def energize(self, dot):
        raise NotImplementedError("Todo : implement energize")


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
        self.add(Line(LEFT, LEFT / 2),
                 Line(LEFT / 2 + (UP / 4), LEFT / 2 + (DOWN / 4)),
                 Line((LEFT * 1 / 6) + UP / 2, (LEFT * 1 / 6) + DOWN / 2),
                 Line((RIGHT * 1 / 6) + (UP / 4), (RIGHT * 1 / 6) + (DOWN / 4)),
                 Line((RIGHT + UP) / 2, (RIGHT + DOWN) / 2),
                 Line(RIGHT / 2, RIGHT))

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


config.background_color = WHITE

Mobject.set_default(color=BLACK)
Dot.set_default(color=BLACK)
Arc.set_default(color=BLACK, stroke_color=BLACK)


class Electronics(MyScene):

    def __init__(self):
        super().__init__(recording=True)

    def construct(self):
        battery = Battery().shift(UP)
        amter = Ameter().shift(DOWN).rotate(-PI)
        resistance = Resistance().rotate(-PI / 2).shift(RIGHT)
        switch = Switch()
        switch.rotate(PI / 2).shift(LEFT)
        circuit = Circuit(battery, battery.connect(resistance), resistance, resistance.connect(amter), amter,
                          amter.connect(switch), switch, switch.connect(battery)).scale(2.5)
        switch.open()
        self.play(Create(circuit))
        self.play(switch.animate.close())
        # self.play(AnimationGroup(*[circuit.run_electron() for i in range(20)], lag_ratio=0.1, run_time=10))
        self.play(switch.animate.open())
        self.wait()


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
