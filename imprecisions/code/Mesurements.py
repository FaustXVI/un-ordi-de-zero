from manim import ORIGIN as origin, LEFT as left, PI as pi, UP as up, DOWN as down, RIGHT as right, DARK_BLUE
from manim.__main__ import main
from MyScene import MyScene
import locale
from electronics import *
from electronics import Circuit, Battery, Resistance, Ameter, Branch, Junction, Contact

locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False


class Mesurements(MyScene, MovingCameraScene):

    def __init__(self):
        super().__init__(recording=False)

    def construct(self):
        self.next_section(skip_animations=section_done)
        axis = NumberLine(x_range=[-15, 15], unit_size=1, include_ticks=False)
        axis10 = NumberLine(x_range=[-15, 15], unit_size=1, include_numbers=True)
        axis100 = NumberLine(x_range=[-150, 150], unit_size=0.1, numbers_with_elongated_ticks=range(-150, 150, 10))
        bigAxis = NumberLine(x_range=[-1000, 1000], include_ticks=False)
        with self.my_voiceover(
                """La différence entre un fil en théorie et un fil en pratique, c'est qu'en vrai, les fils ont une résistance.""") as timer:
            self.play(Create(axis, rate_func=linear), run_time=timer.duration)
        self.remove(axis)
        self.add(bigAxis)
        valueCoord = ORIGIN + 1.5 * RIGHT
        value = MathTex("1.5mA", color=GREEN).move_to(valueCoord + UP)
        valueLine = DashedLine(valueCoord + UP * 0.5, valueCoord + DOWN * 100, color=GREEN)
        with self.my_voiceover(
                """Pour notre exemple, imaginons qu'on veuille mesurer une valeur d'exactement $1.5mA$""") as timer:
            self.play(Create(VGroup(valueLine, value)), run_time=timer.duration)
        all_elem = VGroup(valueLine, value, bigAxis)
        frame = self.camera.frame
        frame.save_state()
        with self.my_voiceover(
                """Notre premier problème, c'est que cet axe est de longueur infinie.""") as timer:
            self.play(frame.animate.scale(4), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Nous devons donc commencer par définir sur quelle partie de cette axe nous allons regarder.""") as timer:
            self.play(frame.animate.shift(RIGHT * 10).scale(1 / 4), run_time=timer.duration)
        with self.my_voiceover(
                """La solution à ce problème est d'estimer une fourchette de la valeur que l'on veut mesurer.""") as timer:
            self.play(frame.animate.scale(4))
        with self.my_voiceover(
                """Par exemple, on sait que ce que l'on veut mesurer est entre $100\mu A$ et $10mA$.""") as timer:
            self.play(frame.animate.shift(LEFT * 15).scale(1 / 5), run_time=timer.duration)
        with self.my_voiceover(
                """C'est exactement ce que tu fais quand tu configure ton ampèremètre ou quand tu choisi d'utiliser un double décimètre plutôt qu'un mètre.""") as timer:
            self.play(frame.animate.move_to(RIGHT * 5), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        self.remove(bigAxis)
        self.add(axis)
        with self.my_voiceover(
                """On va alors découper notre axe en segments de longueur identique. """) as timer:
            self.play(Create(axis10), run_time=timer.duration)
        unit = Line(ORIGIN, RIGHT)
        with self.my_voiceover(
                """Si on divise notre morceau d'axe en 10 segments, chaque segment va représenter $1mA$.""") as timer:
            self.play(VGroup(unit, axis10.get_tick(0), axis10.get_tick(1)).animate(
                rate_func=rate_functions.there_and_back_with_pause).shift(UP * 2+RIGHT).scale(4), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """ Plus la longueur des segments sera petite, plus la résolution de notre mesure, c'est à dire le nombre de chiffres que nous pourrons lire, sera grande.""") as timer:
            self.play(Create(axis100), run_time=timer.duration)
        unit = Line(ORIGIN, RIGHT * 0.1)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                """Si on le divise en 100 segments, chaque segment représentera $100 \mu A$.""") as timer:
            self.play(VGroup(unit, axis100.get_tick(0), axis100.get_tick(1)).animate(
                rate_func=rate_functions.there_and_back_with_pause).shift(UP * 2).scale(4), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        accuracy_color = BLUE
        accuracy = Rectangle(height=1000, width=4, color=accuracy_color, fill_color=accuracy_color, fill_opacity=0.3,
                             stroke_width=0.1).move_to(RIGHT * 1.5)
        with self.my_voiceover(
                """L'exactitude de la mesure représente la proximité de notre mesure avec la valeur réelle.""") as timer:
            self.play(FadeIn(accuracy), run_time=timer.duration)
        with self.my_voiceover(
                """Dans notre exemple, une exactitude de $\pm 1\%$ veut dire que la mesure de $1.5 mA$ sera comprise entre $1.4 mA$ et $1.6 mA$.""") as timer:
            self.play(accuracy.animate.set(width=0.2), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        accuracy_value = MathTex(r"\pm 1\%", color=accuracy_color).move_to(accuracy).shift(UP * 2).scale(0.75)
        with self.my_voiceover(
                """D'après son manuel utilisateur, l'ampèremètre qu'on utilise a une précision de $\pm 1\%$.""") as timer:
            self.play(Create(accuracy_value), run_time=timer.duration)
        with self.my_voiceover(
                """Enfin, la précision nous indique à quelle point la mesure est reproductible.""") as timer:
            self.play(Wait(), run_time=timer.duration)
        self.next_section(skip_animations=False)
        first_mesurement = Arrow(color="#FF9226").rotate(PI / 2).next_to(RIGHT * 1.4, DOWN).shift(DOWN * 3)
        second_mesurement = first_mesurement.copy()
        third_mesurement = first_mesurement.copy().next_to(RIGHT * 1.6, DOWN).shift(DOWN * 3)
        fourth_mesurement = first_mesurement.copy().next_to(RIGHT * 1.5, DOWN).shift(DOWN * 3)
        self.add(first_mesurement)
        self.add(second_mesurement)
        with self.my_voiceover(
                """Dans notre exemple, si nous avons lu $1.4 mA$ la première fois et que notre mesure est précise""") as timer:
            self.play(first_mesurement.animate.shift(UP * 3), run_time=timer.duration)
        with self.my_voiceover(
                """si nous refaisons la mesure, nous lirons de nouveau $1.4 mA$.""") as timer:
            self.play(AnimationGroup(FadeOut(first_mesurement), second_mesurement.animate.shift(UP * 3)),
                      run_time=timer.duration)
        with self.my_voiceover(
                """A l'inverse, si notre mesure est imprécise, nous pourrions lire $1.6 mA$ ce qui reste dans notre fourchette d'exactitude, tout comme $1.5 mA$. """) as timer:
            self.play(AnimationGroup(FadeOut(second_mesurement), third_mesurement.animate.shift(UP * 3)),
                      run_time=timer.duration / 2)
            self.play(AnimationGroup(FadeOut(third_mesurement), fourth_mesurement.animate.shift(UP * 3)),
                      run_time=timer.duration / 2)
        self.next_section(skip_animations=False)
        self.wait(3)
        self.play(AnimationGroup(*[FadeOut(o) for o in self.mobjects]))


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
