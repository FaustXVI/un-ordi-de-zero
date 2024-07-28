import itertools
from typing import Sequence

from manim import *


def without_none(tab):
    return filter(lambda e: e is not None, tab)


class Electronic(VGroup):
    component_number = 0

    @staticmethod
    def reset_component_counter():
        Electronic.component_number = 0

    def __init__(self, *vmobjects, id=None, **kwargs):
        super().__init__(**kwargs)
        self.add(*vmobjects)
        self.id = id if id is not None else Electronic.component_number
        Electronic.component_number = Electronic.component_number - 1

    def get_id(self):
        return self.id

    def entry_point(self):
        return self.submobjects[0].get_start()

    def exit_point(self):
        return self.submobjects[-1].get_end()

    def cables_and_contacts(self):
        cables = [o for o in self.submobjects if isinstance(o, Cable) or isinstance(o, Contact)] + [
            o.cables_and_contacts() for o in self.submobjects if isinstance(o, Electronic)]
        return list(itertools.chain(*without_none(cables)))

    def components(self):
        cables = [o.components() for o in self.submobjects if isinstance(o, Electronic)]
        return list(itertools.chain(*without_none(cables)))

    def connect(self, other_electronic):
        start = self.exit_point()
        finish = other_electronic.entry_point()
        finish_x = finish[0]
        start_x = start[0]
        finish_y = finish[1]
        start_y = start[1]
        if finish_x > start_x:
            if finish_y > start_y:
                midpoint = [start_x, finish_y, 0]
            else:
                midpoint = [finish_x, start_y, 0]
        else:
            if finish_y > start_y:
                midpoint = [start_x, finish_y, 0]
            else:
                midpoint = [finish_x, start_y, 0]

        c1 = Cable(start, midpoint)
        c2 = Cable(midpoint, finish)
        cables = [*filter(lambda c: c.get_length() > 0, [c1, c2])]

        if len(cables) > 0:
            return Component(*cables)
        else:
            return None

    def energize(self, dot):
        raise NotImplementedError("Todo : implement energize")


class Component(Electronic):
    def __init__(self, *vmobjects, **kwargs):
        super().__init__(Contact(vmobjects[0].get_start()), *vmobjects, Contact(vmobjects[-1].get_end()), **kwargs)

    def components(self):
        return [self]

    def energize(self, electron):
        return Succession(*without_none([o.energize(electron) for o in self.submobjects]),
                              rate_func=linear)


class Branch(Electronic):
    def __init__(self, *vmobjects, auto_align=True, **kwargs):
        super().__init__(**kwargs)
        components = [*without_none(vmobjects)]
        if auto_align:
            components = [components[0],
                          *[o2.shift(o.exit_point() - o2.entry_point()) for (o, o2) in
                            zip(components, components[1:])]]
        connected = [[*without_none([o, o.connect(o2)])] for (o, o2) in zip(components, components[1:])]
        self.add(*list(itertools.chain(*connected)), *components[-1:])

    def entry_point(self):
        return self.submobjects[0].entry_point()

    def exit_point(self):
        return self.submobjects[-1].exit_point()

    def energize(self, electron):
        return Succession(*without_none([o.energize(electron) for o in self.submobjects]),
                          rate_func=linear)

    @override_animation(Create)
    def _create_override(self, **kwargs):
        return Succession(*[Create(o) for o in self.submobjects], **kwargs)


class Circuit(Branch):

    def __init__(self, battery, *vmobjects, **kwargs):
        super().__init__(battery, *vmobjects, **kwargs)
        cable = vmobjects[-1].connect(battery)
        if cable is not None:
            self.add(cable)
        self.battery = battery

    def run_electron(self):
        electron = Dot(color=YELLOW)
        return Succession(
            Create(electron),
            self.energize(electron),
                          self.battery.consume(electron),
            rate_func=linear)


class Contact(Electronic):
    def __init__(self, position=ORIGIN):
        super().__init__()
        self.dot = Dot(position).set_opacity(0)
        self.add(self.dot)

    def get_end(self):
        return self.dot.get_center()

    def get_start(self):
        return self.dot.get_center()

    def entry_point(self):
        return self.dot.get_center()

    def exit_point(self):
        return self.dot.get_center()

    def energize(self, electron):
        pass

    @override_animation(Create)
    def _create_override(self):
        return Wait(0)


class Junction(Electronic):
    def __init__(self, *branches, draw_delay=0):
        super().__init__()
        branches = [branches[0], *[o2.next_to(o, DOWN) for (o, o2) in zip(branches, branches[1:])]]
        self.start = Contact(center_of_mass([branch.entry_point() for branch in branches]))
        self.stop = Contact(center_of_mass([branch.exit_point() for branch in branches]))
        self.branches = [Electronic(self.start.connect(b), b, b.connect(self.stop)) for b in branches]
        self.add(self.start, *self.branches, self.stop)
        self.draw_delay = draw_delay

    @override_animation(Create)
    def _create_override(self, **kwargs):
        kwargs["lag_ratio"] = self.draw_delay
        return AnimationGroup(*[Create(o) for o in self.branches], **kwargs)

    def entry_point(self):
        return self.start.entry_point()

    def exit_point(self):
        return self.stop.exit_point()

    def energize(self, electron):
        def energizeBranch(branch):
            e = electron.copy()
            return Succession(*[
                AnimationGroup(e.animate(run_time=0).set_opacity(1)),
                branch.energize(e),
                AnimationGroup(e.animate(run_time=0).set_opacity(0)),
            ], rate_func=linear)

        anims = [energizeBranch(o) for o in self.branches]
        return Succession(*[
            AnimationGroup(electron.animate(run_time=0).set_opacity(0)),
            AnimationGroup(*anims),
            AnimationGroup(electron.animate(run_time=0).set_opacity(1))
        ], rate_func=linear)


class Cable(Line, Electronic):

    def __init__(self, start=LEFT, end=RIGHT, buff=0, path_arc=None, **kwargs):
        super().__init__(start, end, buff, path_arc, **kwargs)
        self.start = start
        self.end = end

    def energize(self, dot):
        return MoveAlongPath(dot, self, rate_func=linear, run_time=self.get_length() / 2)

    def entry_point(self):
        return self.start

    def exit_point(self):
        return self.end


class Resistance(Component):
    def __init__(self, id=None,**kwargs):
        n = 9
        step = 2 / n

        self.pts = [LEFT, LEFT / 2,
                    *[LEFT / 2 * (1 - i * step) + (DOWN / 4 if i % 2 == 0 else UP / 4) for i in
                      range(1, round(n / 2) + 1)],
                    *[RIGHT / 2 * (1 - (round(n / 2) - i) * step) + (UP / 4 if i % 2 == 0 else DOWN / 4) for i in
                      range(0, round(n / 2))],
                    RIGHT / 2, RIGHT]
        self.lines = [Line(a, b, **kwargs) for a, b in zip(self.pts, self.pts[1:])]
        super().__init__(*self.lines, id=id,**kwargs)

    def energize(self, dot):
        return Succession(*[
            MoveAlongPath(dot, line, rate_func=linear) for line in self.lines
        ], rate_func=linear)


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
        ], rate_func=linear)

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


class Battery(Component):
    def __init__(self):
        self.components = [Line(LEFT, LEFT / 6),
                      Line((LEFT / 6) + UP / 4, (LEFT / 6) + DOWN / 4),
                      Line((RIGHT / 6) + (UP / 2), (RIGHT / 6) + (DOWN / 2)),
                      MathTex("-").shift((LEFT / 3) + (UP / 3)).scale(0.75),
                      MathTex("+").shift((RIGHT / 3) + (UP / 3)).scale(0.75),
                      Line(RIGHT / 6, RIGHT),
                      ]
        super().__init__(*self.components)

    def energize(self, dot):
        dot.set_opacity(0).move_to(self.components[-1].get_start())
        return Succession(dot.animate(rate_func=linear).set_opacity(1),
                          MoveAlongPath(dot, self.components[-1], rate_func=linear),
                          rate_func=linear)

    def consume(self, dot):
        return Succession(
            MoveAlongPath(dot, self.components[0], rate_func=linear),
                          dot.animate(rate_func=linear).set_opacity(0).move_to(self.components[0].get_end()),
                          rate_func=linear)


class Mesurement(Component):
    def __init__(self, letter):
        self.circle = Circle(color=WHITE, radius=1 / 2).rotate(PI)
        self.letter = Tex(letter)
        self.entry = Line(LEFT * self.circle.radius * 2, LEFT * self.circle.radius)
        self.exit = Line(RIGHT * self.circle.radius, RIGHT * self.circle.radius * 2)
        components = [self.entry, self.circle, self.letter, self.exit]
        super().__init__(*components)

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
            MoveAlongPath(dot, self.submobjects[-1], rate_func=linear),
            rate_func=linear
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


def transformCircuitById(start, finish):
    start_comps = start.components()
    finish_comps = finish.components()
    matched = [(o, [*filter(lambda o2: o2.get_id() == o.get_id(), finish_comps)]) for o in start_comps]
    matched_finished = [(o, [*filter(lambda o2: o2.get_id() == o.get_id(), start_comps)]) for o in finish_comps]
    transformed = [Transform(o, o2[0], replace_mobject_with_target_in_scene=True) for (o, o2) in
                   filter(lambda p: len(p[1]) > 0, matched)]
    unmatched_start = [o for (o, o2) in filter(lambda p: len(p[1]) == 0, matched)]
    unmatched_finish = [o for (o, o2) in filter(lambda p: len(p[1]) == 0, matched_finished)]
    return Succession(
        Uncreate(VGroup(*unmatched_start, *(start.cables_and_contacts()))),
        AnimationGroup(*transformed),
        Create(VGroup(*unmatched_finish, *(finish.cables_and_contacts())))
    )
