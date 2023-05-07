import math
import operator
from itertools import accumulate

from manim import *
from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Electron(Dot):

    def __init__(self, **kwargs):
        super().__init__(color=YELLOW_E, **kwargs)


class ElectronMovement(MyScene, ZoomedScene):

    def __init__(self):
        super().__init__(recording=False)
        ZoomedScene.__init__(
            self,
            zoomed_display_height=1,
            zoomed_display_width=2,
        )

    def construct(self):
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        frame.set_color(WHITE)
        frame.width = 2
        zoomed_display_frame = zoomed_display.display_frame
        zoomed_display_frame.set_color(WHITE)
        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))
        nb_electrons_visible = 20
        self.camera.frame_height = nb_electrons_visible * (self.camera.frame_height / self.camera.frame_width)
        self.camera.frame_width = nb_electrons_visible
        electrons = VGroup(*[Electron(radius=1 / 2) for i in range(30)]).arrange(buff=0)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Comme expliqué avant, les éléctrons se poussent les uns les autres, un peut comme des billes mises les unes derrière les autres.""") as timer:
            self.play(Create(electrons), run_time=timer.duration)
        with self.my_voiceover(
                """Du coup, quand on ajoute une bille à gauche, ça pousse toutes les billes et en fait sortir une à droite""") as timer:
            electron_move_duration = timer.duration
            self.play(electrons.animate.shift(RIGHT), rate_functions=linear, run_time=electron_move_duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Si on se s'interesse juste à une partie de notre circuit""") as timer:
            self.play(Create(frame), run_time=timer.duration / 2)
            self.activate_zooming(False)
            self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, run_time=timer.duration / 2)
        with self.my_voiceover(
                """On peut faire exactement la même observation""") as timer:
            self.play(electrons.animate.shift(RIGHT), rate_functions=linear, run_time=electron_move_duration)
        with self.my_voiceover(
                """Et ce, où que l'on se place dans le circuit""") as timer:
            self.play(frame.animate.shift(4 * LEFT), run_time=timer.duration)
            self.play(electrons.animate.shift(RIGHT), rate_functions=linear, run_time=electron_move_duration)
        with self.my_voiceover(
                """Et quel que soit la longueur du circuit que l'on regarde""") as timer:
            self.play(frame.animate.scale([2, 1, 0]), zoomed_display.animate.scale([2, 1, 0]), run_time=timer.duration)
            self.play(electrons.animate.shift(RIGHT), rate_functions=linear, run_time=electron_move_duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Dit autrement, en tout point du circuit""") as timer:
            self.play(frame.animate.scale([1 / 4, 1, 0]).shift(7.5 * RIGHT),
                      zoomed_display.animate.scale([1 / 4, 1, 0]),
                      run_time=timer.duration)
        with self.my_voiceover(
                """Toute intensité qui entre doit également resortir""") as timer:
            self.play(electrons.animate.shift(RIGHT), rate_functions=linear, run_time=electron_move_duration)
        with self.my_voiceover(
                """C'est la première loi de Kirchoff qu'on appele également la loi des nœuds""") as timer:
            self.play(FadeOut(electrons), run_time=timer.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
