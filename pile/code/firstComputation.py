from manim import *
from manim.__main__ import main
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

from FakeTraker import FakeTracker

section_done = False


class ChemicalReaction(VoiceoverScene):

    def myVoiceOver(self, text, duration=1):
        if section_done:
            return FakeTracker(duration)
        else:
            return self.voiceover(text)

    def construct(self):
        self.next_section(skip_animations=section_done)
        service = GTTSService(lang="fr") if section_done else RecorderService()
        self.set_speech_service(service)
        self.next_section(skip_animations=False)
        with self.myVoiceOver(text=
                              r"Une boussole, ça suit le champ magnétique terrestre"
                              r"Un champ manétique, ça se mesure en Teslas"
                              r"Le champ magnétique terrestre, en France, fait environ 5 * 10-5 Teslas"
                              r"Si on applique un champ magnétique B perpendiculaire au champ terrestre et suffisament fort, on devrait voir la boussole bouger"
                              r"Le mouvement de l'aiguille devrait être propotionnel à rapport entre le champ créé et le champ terrestre"
                              r"On peut calculer l'angle dont va se déplacer l'aiguille avec la formule alpha = 90 * B / (B + 5*10-5)"
                              r"Si on applique un champ magnétique égal au champ terrestre, alors l'aiguille devrait bouger de 45 degrées"
                              r"De 1 degré pour un champ 100 fois plus faible"
                              r"De presque 90 degré pour un champ 100 fois plus fort"
                              r"Si on arrive à exprimer la relation entre notre champ magnétique et le nombre d'éléctrons qui se déplacent (c'est à dire l'intensité) alors on aura un ampèremetre"
                              r"La formule du champ magnétique d'un fil traversé par un courant est B=mu0 I / 2 PI r"
                              r"Mu 0 est une constante de la perméabilité magnétique du vide et vaut 4 PI 10-7"
                              r"r est la distance entre le fil et le point qu'on mesure. Notre boussole devrais être à environ 1 cm soit 10-2 m"
                              r"En simplifiant, on obtient B = 2I 10-5"
                              r"Sauf qu'une patate s'est pas très puissant et que l'intensité qu'on en tirera sera de l'ordre du dixeme de milli-ampère, soit 10-4 ampères"
                              r"On obtient alors un champ magnétique de l'ordre de 2 10-9 Teslas ce qui est bien trop faible pour notre boussole"
                              r"Il va falloir augmenter notre champ magnétique en créant une bobine"
                              r"Le champ magnétique d'une bobine suit la formule suivante : B = K mu 0 N / L I"
                              r"Mu 0 est la même constant qu'auparavant qui vaut 4 PI 10-7"
                              r"L est la longuer de la bobine, pour nous éviter trop de travail, une bobine de 1 cm devrait suffir"
                              r"Il nous reste alors deux inconnue sur lequelles nous avons la main"
                              r"K, qui est la permeabilité relative du matériau que nous allons mettre au centre de la bobine"
                              r"Le fer a une permeabilité fort mais diminue très vite si le fer n'est pas pur. Nous utiliserons donc un clou en fer pour notre bobine et un K = 100 dans nos calculs"
                              r"N est le nombre de tours de la bobine. C'est ce que nous voulons calculer."
                              r"Partons du principe que notre patate nous donne 10-4 ampères"
                              r"Notre objectif est de produire un champ magnétique égal à celui du champ terrestre"
                              r"Si on simplifie nos calculs, on obtiens 5 10-5 = 4 PI 10 -7 N"
                              r"Soit 5 10-5 // 4 PI 10 -7 = N"
                              r"Ce qui donne environ N = 40"
                              r"Pour être tranquilles, je te propose de prendre de la marge et de faire 100 tours"
                              ) as tracker:
            self.wait(tracker.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__], prog_name='invoked-command')
