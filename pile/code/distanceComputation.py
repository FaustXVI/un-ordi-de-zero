from abc import ABC

from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

from FakeTraker import FakeTracker

recording = True


def my_frac(d, n):
    return [r"{", r"{", *d, r"}", r"\over", r"{", *n, r"}", r"}"]


class K_Correction(VoiceoverScene, ABC):

    def my_voiceover(self, text, duration=1):
        if recording:
            return self.voiceover(text)
        else:
            return FakeTracker(duration)

    def construct(self):
        self.set_speech_service(RecorderService(device_index=12))
        with self.my_voiceover(text=
                               """
                               Quand on s'éloigne d'une bobine, le champ diminue de manière inversement proporstionnel au carré de la distance relative au rayon.
                               Ce qu'on peut écrire Bp = Bb / R2
                               Ou Bp est la valeur du champ au point qui nous interresse
                               Bb est la valeur du champ au centre de notre bobine
                               R est la distance relative au rayon entre la bobine et le point qui nous interresse.
                               Le terme distance relative au rayon veut dire qu'au lieu de compter la distance en unité absolue comme des cm, on va utiliser comme unité le rayon de la bobine.
                               Notre clou fait 2,5 mm de rayon
                               Notre boussolle se trouve, après mesure, à 30 mm de notre bobine
                               Donc R = 30 / 2.5 
                               Ce qui est égal à 12 et qui veut dire que notre champ est 144 fois plus faible que prévu.
                               Si on veut voir quelquechose avec notre situation actuelle, il va falloir faire 144 fois plus de tours soit prêt de 6 000 tours.
                               Avant d'en arriver là, je te propose d'être optimiste car on a un clou en fer et on calcul avec k = 1. Or k = 1 c'est l'équivalant d'avoir de l'air au centre de notre bobine.
                               On sait que k est inférieur à 100 mais il est peut-être égale à 1 non plus. Commence par faire une bobine de 1 000 tours et si ça marche pas monte à 6 000.
                               """
                               ) as tracker:
          self.wait(tracker.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
