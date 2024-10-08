import functools
import math
import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

recording = True
section_done = True and not recording
finalOnly = True

frame_factor = 3
config.frame_width = 16 * frame_factor
config.frame_height = 9 * frame_factor
# config.frame_rate = 30
atomSize = 5
MAX_DISTANCE_EFFECT = 4
EFFECT_INTENSITY = 100
SLOWMO_FACTOR = 10
plateSize = 8
defaultBatterySize = 5


class AtomState(Enum):
    NEUTRAL = 1
    POSITIVE = 2
    NEGATIVE = 3


def colorByState(state):
    if state == AtomState.POSITIVE:
        return RED_D
    if state == AtomState.NEGATIVE:
        return BLUE_D
    return YELLOW_D


def drawAtoms(atoms):
    return VGroup(*[
        Dot(color=colorByState(atom.state)).scale(atomSize).move_to(ORIGIN + atom.position) for atom in atoms
    ],
                  *[
                      Text("-").scale(atomSize * 0.33).move_to(ORIGIN + atom.position) for atom in atoms if
                      atom.state == AtomState.NEGATIVE
                  ],
                  *[
                      Text("+").scale(atomSize * 0.33).move_to(ORIGIN + atom.position) for atom in atoms if
                      atom.state == AtomState.POSITIVE
                  ], )


def getX(position):
    return position[0]


def getY(position):
    return position[1]


class Atom:
    def __init__(self, position, state):
        self.position = position
        self.state = state

    def distance(self, atom):
        return max(abs(getX(self.position) - getX(atom.position)), abs(getY(self.position) - getY(atom.position)))

    def isNeigbour(self, atom):
        return self.distance(atom) <= 1


def createRectangle(start, stop, state=AtomState.NEUTRAL):
    (startx, starty) = start
    (stopx, stopy) = stop
    return [Atom((x, y, 0), state) for x in
            range(startx, (stopx + 1)) for y in
            range(starty, (stopy + 1))]


def countStateInRectangle(start, stop, atoms, state):
    (startx, starty) = start
    (stopx, stopy) = stop
    positions = [(x, y, 0) for x in range(startx, (stopx + 1)) for y in range(starty, (stopy + 1))]
    return sum([1 for a in atoms if a.state == state and (a.position in positions)])


def computeNextAtoms(atoms):
    random.shuffle(atoms)
    newAtoms = []
    negativeAtoms = []
    positiveAtoms = []
    neutralAtoms = []
    nonNeutralAtoms = []
    for i, a in enumerate(atoms):
        newAtoms.append(Atom(a.position, a.state))
        if (a.state == AtomState.NEGATIVE):
            negativeAtoms.append(a)
        if (a.state == AtomState.POSITIVE):
            positiveAtoms.append(a)
        if (a.state == AtomState.NEUTRAL):
            neutralAtoms.append((i, a))
        else:
            nonNeutralAtoms.append((i, a))

    def closestDistance(nextPosition, currentAtom, poolOfAtoms):
        result = min([nextPosition.distance(n) for n in poolOfAtoms if n.position != currentAtom.position])
        return result

    def sameStateAttractionWeight(currentAtom, neighbour, poolOfAtoms):
        if len(poolOfAtoms) == 0 or (len(poolOfAtoms) == 1 and poolOfAtoms[0].position == currentAtom.position):
            return MAX_DISTANCE_EFFECT ** 2
        distance = closestDistance(neighbour, currentAtom, poolOfAtoms)
        return min(MAX_DISTANCE_EFFECT, max(0, distance)) ** 2

    def oppositeStateAttractionWeight(currentAtom, neighbour, poolOfAtoms):
        if len(poolOfAtoms) == 0 or (len(poolOfAtoms) == 1 and poolOfAtoms[0].position == currentAtom.position):
            return 0
        distance = closestDistance(neighbour, currentAtom, poolOfAtoms)
        return (MAX_DISTANCE_EFFECT - min(MAX_DISTANCE_EFFECT, max(0, distance))) ** 2

    def attractionWeight(currentAtom, neighbour):
        assert currentAtom.state != AtomState.NEUTRAL
        if currentAtom.state == AtomState.NEGATIVE:
            same = negativeAtoms
            opposites = positiveAtoms
        else:
            same = positiveAtoms
            opposites = negativeAtoms
        exponent = (sameStateAttractionWeight(currentAtom, neighbour, same)
                    + oppositeStateAttractionWeight(currentAtom, neighbour, opposites))
        # print(exponent, neighbour.position)
        return EFFECT_INTENSITY ** exponent

    # print("next frame")
    for index, atom in nonNeutralAtoms:
        # print("for", atom.position)
        positions = [(atom.position, index)]
        weights = [attractionWeight(atom, atom)]
        for i, n in neutralAtoms:
            if n.isNeigbour(atom):
                positions.append((n.position, i))
                weights.append(attractionWeight(atom, n))
        (newPosition, newIndex) = random.choices(positions, weights)[0]
        newAtoms[index].state = newAtoms[newIndex].state
        newAtoms[newIndex].state = atom.state
    return newAtoms


def simulate(circuit, nbFrames):
    steps = functools.reduce(lambda acc, _: [*acc, computeNextAtoms(acc[-1])], range(1, nbFrames), [circuit])
    if recording or not finalOnly:
        return ([drawAtoms(atoms) for atoms in steps], steps[-1])
    else:
        return ([drawAtoms(steps[-1])], steps[-1])


def createLeftSide(distance=0, batterySize=defaultBatterySize):
    return [*(createLeftBattery(distance, batterySize)), *(createLeftCable(distance)), *(createLeftPlate(distance))]


def createLeftPlate(distance):
    return createRectangle((-3 - distance, -plateSize), (-1 - distance, plateSize))


def countNegativesInLeftSide(distance, atoms):
    return countStateInRectangle((-10 - distance, -plateSize), (-1 - distance, plateSize), atoms, AtomState.NEGATIVE)


def createLeftCable(distance):
    return createRectangle((-10 - distance, -1), (-4 - distance, 1))


def createLeftBattery(distance, batterySize=defaultBatterySize):
    return createRectangle((-10 - batterySize - distance, -math.floor(batterySize / 2)),
                           (-11 - distance, math.floor(batterySize / 2)), AtomState.NEGATIVE)


def createRightSide(distance=0, batterySize=defaultBatterySize):
    return [*(createRightBattery(distance, batterySize)), *(createRightCable(distance)), *(createRightPlate(distance))]


def createRightPlate(distance):
    return createRectangle((1 + distance, -plateSize), (3 + distance, plateSize))


def createRightCable(distance):
    return createRectangle((4 + distance, -1), (10 + distance, 1))


def countPositivesInRightSide(distance, atoms):
    return countStateInRectangle((1 + distance, -plateSize), (10 + distance, plateSize), atoms, AtomState.POSITIVE)


def createRightBattery(distance, batterySize=defaultBatterySize):
    return createRectangle((11 + distance, -math.floor(batterySize / 2)),
                           (10 + batterySize + distance, math.floor(batterySize / 2)), AtomState.POSITIVE)


def createCircuit(distance=0, batterySize=5):
    return [*createLeftSide(distance, batterySize), *createRightSide(distance, batterySize)]


class TruthTable(MyScene):

    def __init__(self):
        super().__init__(recording=recording)

    def playSimulation(self, circuit, run_time, slow_factor=2):
        timeBetweenFrames = (1 / config.frame_rate) * slow_factor
        nbFrames = math.ceil(run_time / timeBetweenFrames)
        (drawings, lastState) = simulate(circuit, nbFrames)
        for (i, drawing) in enumerate(drawings):
            self.clear()
            self.add(drawing)
            self.wait(timeBetweenFrames)
        return lastState

    def construct(self):
        self.next_section(skip_animations=section_done)
        soloNeutral = drawAtoms(createRectangle((0, 0), (0, 0)))
        with self.my_voiceover(r"""Comme tu le sais, la matière est composé d'atomes. 
> Nous allons représenter chaque atome éléctriquement neutres par un point jaune.""") as timer:
            self.play(FadeIn(soloNeutral), run_time=timer.duration)
        soloNeg = drawAtoms(createRectangle((-1, 0), (-1, 0), AtomState.NEGATIVE))
        with self.my_voiceover(
                r"""Un atome qui a un surplus d'éléctron sera représenté par un point bleu avec un signe moins dedans, signifiant que l'atome a une change négative supplémentaire.""") as timer:
            self.play(FadeIn(soloNeg), run_time=timer.duration)
        soloPos = drawAtoms(createRectangle((1, 0), (1, 0), AtomState.POSITIVE))
        with self.my_voiceover(
                r"""Un atome qui a un déficite d'éléctron sera représenté par un point rouge avec un signe plus dedans, signifiant que l'atome a une change négative manquante qu'on peut voir comme une charge positive.""") as timer:
            self.play(FadeIn(soloPos), run_time=timer.duration)
        with self.my_voiceover(
                r"""Prenons un cas très simple :""") as timer:
            self.play(FadeOut(VGroup(soloPos, soloNeg, soloNeutral)), run_time=timer.duration)

        self.next_section(skip_animations=section_done)
        square1Neg = createRectangle((-3, -3), (3, 3))
        for a in square1Neg:
            if a.position == (0, 0, 0):
                a.state = AtomState.NEGATIVE
        with self.my_voiceover(
                r"""un carré de matière avec une seul charge négative.""") as timer:
            self.play(FadeIn(drawAtoms(square1Neg)), run_time=timer.duration)
        with self.my_voiceover(
                r"""L'éléctron peut se déplacer librement, on parle d'ailleurs d'éléctron libre. Pour simuler ça, les charges (négatives ou positivent) peuvent soit se déplacent de manière aléatoires sur un atome voisin ou soit rester sur place.""") as timer:
            self.clear()
            self.playSimulation(square1Neg, timer.duration, SLOWMO_FACTOR)
        with self.my_voiceover(
                r"""Pour savoir ce qu'il se passe quand on a deux charges, il faut s’intéresser à la loi de Coulomb.""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)

        self.next_section(skip_animations=section_done)

        with self.my_voiceover(
                r"""Elle nous nous dit que les signes opposés s'attirent""") as timer:
            start = drawAtoms([Atom((-3, 0, 0), AtomState.NEGATIVE), Atom((3, 0, 0), AtomState.POSITIVE)])
            stop = drawAtoms([Atom((-1, 0, 0), AtomState.NEGATIVE), Atom((1, 0, 0), AtomState.POSITIVE)])
            self.play(Transform(start, stop), run_time=timer.duration)
            self.clear()

        with self.my_voiceover(
                r"""et que les signes identiques se repoussent.""") as timer:
            start = drawAtoms([Atom((-1, 0, 0), AtomState.NEGATIVE), Atom((1, 0, 0), AtomState.NEGATIVE)])
            stop = drawAtoms([Atom((-3, 0, 0), AtomState.NEGATIVE), Atom((3, 0, 0), AtomState.NEGATIVE)])
            self.play(Transform(start, stop), run_time=timer.duration)
        with self.my_voiceover(r"""L'intensité de cette force est donnée par la formule :""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)

        self.next_section(skip_animations=False)
        coulomb = MathTex("k_0", *my_frac([r"|",r"q_1", r"\times", r"q_2",r"|"], ["r_{}", "^2"])).scale(frame_factor)
        with self.my_voiceover(
                r"""$k_0 \frac{|q_1 \times q_2|}{r^2}$""") as timer:
            self.play(Write(coulomb), run_time=timer.duration)
        with self.my_voiceover(
                r"""où k0 est une constante de l'univers""") as timer:
            self.play(Indicate(coulomb.get_part_by_tex("k_0")), run_time=timer.duration)
        with self.my_voiceover(
                r"""q1 et q2 sont les charges concernées""") as timer:
            self.play(Indicate(coulomb.get_part_by_tex("q_1")), Indicate(coulomb.get_part_by_tex("q_2")),
                      run_time=timer.duration)
        with self.my_voiceover(
                r""" r est la distance entre les deux charges""") as timer:
            self.play(Indicate(coulomb.get_part_by_tex("r_{}")), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                r"""Donc pour deux même charges, plus la distance est grandes moins la force est importante et ce, très vite""") as timer:
            self.wait(timer.duration)
        square2Neg = createRectangle((-3, -3), (3, 3))
        for a in square2Neg:
            if a.position == (-1, 0, 0) or a.position == (1, 0, 0):
                a.state = AtomState.NEGATIVE
        with self.my_voiceover(
                r"""Reprenons notre carré de matière, mais avec deux charges négatives cette fois si.""") as timer:
            self.play(Succession(FadeOut(coulomb), FadeIn(drawAtoms(square2Neg))), run_time=timer.duration)
        with self.my_voiceover(
                r"""Les charges de même signe se repoussent. Pour simuler ça, au moment du choix de la prochaine position de la charge, on favorise le choix des positions les plus éloignés des autres charges de même signe. On vois donc bien que les deux charges ne se rapprochent presque jamais.""") as timer:
            self.clear()
            self.playSimulation(square2Neg, timer.duration, SLOWMO_FACTOR)
        self.next_section(skip_animations=section_done)
        square1Pos1Neg = createRectangle((-3, -3), (3, 3))
        for a in square1Pos1Neg:
            if a.position == (-3, -3, 0):
                a.state = AtomState.POSITIVE
            if a.position == (3, 3, 0):
                a.state = AtomState.NEGATIVE
        with self.my_voiceover(
                r"""Si on recommence avec une charge négative et une charge positive.""") as timer:
            self.play(Succession(FadeOut(*self.mobjects), FadeIn(drawAtoms(square1Pos1Neg))), run_time=timer.duration)
        with self.my_voiceover(
                r"""Les charges de signe contraires s'attirent. Pour simuler ça, au moment du choix de la prochaine position de la charge, on favorise le choix des positions les plus proches des autres charges de signe opposés. On vois donc bien que les deux charges se rapprochent très vites et restent collées. En réalité, quand elles se rencontres, les deux charges s'annuleraient et notre carré finirait électriquement neutre.""") as timer:
            self.clear()
            self.playSimulation(square1Pos1Neg, timer.duration, SLOWMO_FACTOR)
        with self.my_voiceover(
                r"""Maintenant que les méchaniques de la simulation ont été vue, on va accèlerer les prochaines simulations pour avoir des résultats intéréssants plus rapidement.""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        leftBattery = createLeftBattery(3)
        with self.my_voiceover(
                r"""Prenons le coté négatif d'une pile. On peut le représenté comme étant une masse d'atomes négativement chargés.""") as timer:
            self.play(FadeIn(drawAtoms(leftBattery)), run_time=timer.duration)
        leftCable = createLeftCable(3)
        with self.my_voiceover(
                r"""et un fil électriquement neutre que nous mettons en contact avec le côté négatif de la pile.""") as timer:
            self.play(FadeIn(drawAtoms(leftCable)), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        batteryAndCableOnly = [*leftBattery, *leftCable]
        with self.my_voiceover(
                r"""On voit que les charges se répartissent rapidement dans la matière et que le fil contient maintenant des charges négatives. Les charges vont se répartir de manière égales dans la matière. On dit alors que le fil est à équipotentiel de la batterie. Si on enlève soudainement la pile et qu'on met sur pause.""",
                duration=10) as timer:
            self.clear()
            batteryAndCableOnlyFinal = self.playSimulation(batteryAndCableOnly, run_time=timer.duration)
        removedPositions = [y.position for y in leftBattery]
        batteryAndCableOnlyFinal = [a for a in batteryAndCableOnlyFinal if a.position not in removedPositions]
        self.clear()
        self.add(drawAtoms(batteryAndCableOnlyFinal))
        negOnLeft = countNegativesInLeftSide(3, batteryAndCableOnlyFinal)
        with self.my_voiceover(
                f"""On vois qu'il reste des charges négatives dans le fil ({negOnLeft} dans notre simulation).
 Et ça, c'est très intéressant pour nous car c'est une forme de stockage !""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover(
                f"""Le but maintenant, et d'augmenter le nombres de charges contenus dans notre dispositif quand on enlève la pile.""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)

        removedPositions = [*removedPositions, *[y.position for y in createRightBattery(3)]]
        with self.my_voiceover(
                r"""Pour commencer, il faut qu'on face la même chose de l'autre côté de la pile. Sinon on n'arrivera pas  à brancher notre condensateur à un circuit.""") as timer:
            self.play(FadeIn(
                drawAtoms([*createLeftBattery(3), *createLeftCable(3), *createRightCable(3), *createRightBattery(3)])), run_time=timer.duration)
        with self.my_voiceover(
                r"""Ensuite, la première avancées qu'on peut faire, c'est de se rendre compte que plus on a de matière, plus on a de place pour les charges. On peut donc mettre deux grandes plaques de chaque côté.""") as timer:
            self.play(FadeIn(drawAtoms([*createLeftPlate(3), *createRightPlate(3)])), run_time=timer.duration)
        circuitFar = createCircuit(3)
        with self.my_voiceover(
                r"""Si on lance notre simulation et qu'on la laisse tourner un petit moment … et qu'on enlève la pile d'un coup et qu'on met sur pause.""",
                duration=10) as timer:
            self.clear()
            circuitFarFinal = self.playSimulation(circuitFar, run_time=timer.duration)
        circuitFarFinal = [a for a in circuitFarFinal if a.position not in removedPositions]
        self.clear()
        self.add(drawAtoms(circuitFarFinal))
        negOnLeft2 = countNegativesInLeftSide(3, circuitFarFinal)
        posOnRight2 = countPositivesInRightSide(3, circuitFarFinal)
        print(
            f"""On obtient {negOnLeft2} charges négatives, ce qui est mieux que les {negOnLeft} d'avant. On a aussi {posOnRight2} charges positives.""")
        with self.my_voiceover(
                f"""On obtient {negOnLeft2} charges négatives, ce qui est mieux que les {negOnLeft} d'avant. On a aussi {posOnRight2} charges positives.""") as timer:
            self.wait(timer.duration)
        removedPositions = [*removedPositions, *[y.position for y in [*createRightCable(3), *createLeftCable(3)]]]
        circuitFarPlateOnlyFinal = [a for a in circuitFarFinal if a.position not in removedPositions]
        negOnLeft2 = countNegativesInLeftSide(3, circuitFarPlateOnlyFinal)
        posOnRight2 = countPositivesInRightSide(3, circuitFarPlateOnlyFinal)
        with self.my_voiceover(
                f"""en se concentrant que sur les plaques qui représente notre condensateur.""") as timer:
            self.play(FadeOut(*self.mobjects), FadeIn(drawAtoms(circuitFarPlateOnlyFinal)), run_time=timer.duration)
        print(f"""On obtient {negOnLeft2} charges négatives et {posOnRight2} charges positives.""")
        with self.my_voiceover(
                f"""On obtient {negOnLeft2} charges négatives et {posOnRight2} charges positives.""") as timer:
            self.wait(timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                f"""Si on se rappelle la loi de Coulomb, les opposés s'attirent mais l'intensité de cette force diminue avec le carrée de la distance.""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)
        circuit = createCircuit()
        removedPositions = [y.position for y in
                            [*createRightBattery(0), *createLeftBattery(0), *createRightCable(0), *createLeftCable(0)]]
        with self.my_voiceover(
                f"""Si on rapproche les deux plaques, les charges opposés seront plus proches et ça pourrait nous aider.""") as timer:
            self.play(FadeIn(drawAtoms(circuit)), run_time=timer.duration)
        with self.my_voiceover(
                r"""Aller, on laisse de nouveau tourner notre simulation pendant un petit moment … et on enlève la pile d'un coup.""",
                duration=10) as timer:
            self.clear()
            circuitFinal = self.playSimulation(circuit, run_time=timer.duration)
        circuitFinal = [a for a in circuitFinal if a.position not in removedPositions]
        self.clear()
        self.add(drawAtoms(circuitFinal))
        negOnLeft3 = countNegativesInLeftSide(0, circuitFinal)
        posOnRight3 = countPositivesInRightSide(0, circuitFinal)
        print(
            f"""On obtient {negOnLeft3} vs {negOnLeft2} vs {negOnLeft} charges négatives et {posOnRight3} vs {posOnRight2} charges positives.""")
        with self.my_voiceover(
                f"""On obtient {negOnLeft3} charges négatives et {posOnRight3} charges positives et on voit que les charges se concentrent à la surface des plaques.""") as timer:
            self.wait(timer.duration)
        self.next_section(skip_animations=section_done)
        with self.my_voiceover(
                f"""Cependant, il semblerait que l'on manque de charges. Jouons avec un dernier paramètre""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)
        bigCircuit = createCircuit(batterySize=defaultBatterySize + 2)
        removedPositions = [y.position for y in
                            [*createRightBattery(0, batterySize=defaultBatterySize + 2), *createRightCable(0),
                             *createLeftCable(0),
                             *createLeftBattery(0, batterySize=defaultBatterySize + 2)]]
        with self.my_voiceover(
                f"""si j'augmente le voltage en mettant une plus grosse pile.""") as timer:
            self.play(FadeIn(drawAtoms(bigCircuit)), run_time=timer.duration)
        with self.my_voiceover(
                r"""Qu'on fait tourner de nouveau notre simulation un peu … et qu'on enlève la pile.""",
                duration=10) as timer:
            self.clear()
            bigCircuitFinal = self.playSimulation(bigCircuit, run_time=timer.duration)
        bigCircuitFinal = [a for a in bigCircuitFinal if a.position not in removedPositions]
        self.clear()
        self.add(drawAtoms(bigCircuitFinal))
        negOnLeft4 = countNegativesInLeftSide(0, bigCircuitFinal)
        posOnRight4 = countPositivesInRightSide(0, bigCircuitFinal)
        print(
            f"""On obtient {negOnLeft4} vs {negOnLeft3} vs {negOnLeft2} vs {negOnLeft} charges négatives et {posOnRight4} vs {posOnRight3} vs {posOnRight2} charges positives.""")
        with self.my_voiceover(
                f"""On voit qu'on a que {negOnLeft4} charges négatives et {posOnRight4} charges positives.""") as timer:
            self.wait(timer.duration)
        with self.my_voiceover(
                f"""On viens donc de comprendre que :""") as timer:
            self.play(FadeOut(*self.mobjects), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        q = MathTex("Q").shift(LEFT * 3).scale(frame_factor)
        a = MathTex("A").shift(UP * 3).scale(frame_factor)
        d = MathTex("d").shift(DOWN * 3).scale(frame_factor)
        v = MathTex("V").shift(UP * 3 + RIGHT * 3).scale(frame_factor)
        qFormula = MathTex("Q", "=", r"\epsilon{}_0", r"\times", *my_frac("A", "d"), r"\times", "V").scale(frame_factor)
        qFormulaSplitReady = MathTex("Q", "=", r"\epsilon{}_0 \times", *my_frac("A", "d"), r"\times", "V").scale(
            frame_factor)
        cFormula = MathTex("C", "=", r"\epsilon{}_0 \times", *my_frac("A", "d")).scale(frame_factor)
        with self.my_voiceover(
                f"""Q, le nombre de charges contenus dans notre condensateur""") as timer:
            self.play(FadeIn(q), run_time=timer.duration)
        with self.my_voiceover(
                f"""augmente avec A, la surface de nos plaques.""") as timer:
            self.play(FadeIn(a), run_time=timer.duration)
        with self.my_voiceover(
                f"""diminue avec d, la distance entre nos plaques.""") as timer:
            self.play(FadeIn(d), run_time=timer.duration)
        with self.my_voiceover(
                f"""augmente avec V, le voltage de notre pile.""") as timer:
            self.play(FadeIn(v), run_time=timer.duration)
        with self.my_voiceover(
                f"""Et en effet, la formule du nombre de charges dans un condensateur est : Q = \epsilon_0 * A/d * V""") as timer:
            self.play(TransformMatchingTex(VGroup(q, a, d, v), qFormula), run_time=timer.duration)
        with self.my_voiceover(
                f"""\epsilon_0 étant une constante dépendante de la matière isolante contenue entre les deux plaques.""") as timer:
            self.play(Indicate(qFormula.get_part_by_tex(r"\epsilon{}_0")), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        self.clear()
        self.add(qFormulaSplitReady)
        with self.my_voiceover(
                f"""Pour un même voltage $V$ ce qui distingue une capacité d'une autre c'est donc \epsilon_0 * A/d$.""") as timer:
            self.play(Indicate(VGroup(
                qFormulaSplitReady.get_part_by_tex(r"\epsilon{}_0 \times"),
                qFormulaSplitReady.get_part_by_tex(r"A"),
                qFormulaSplitReady.get_part_by_tex(r"\over"),
                qFormulaSplitReady.get_part_by_tex(r"d"),
            )), run_time=timer.duration)
        with self.my_voiceover(
                f"""Cette valeur est donc caractéristique d'un condensateur et est noté C$.""") as timer:
            self.play(TransformMatchingTex(qFormulaSplitReady, cFormula), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        f = MathTex("F").shift(DOWN * 5).scale(frame_factor)
        faradFormula = MathTex("F", "=", *my_frac("C", "V")).shift(DOWN * 5).scale(frame_factor)
        with self.my_voiceover(
                f"""On l’appelle la capacitance et elle se mesure en Farad noté F""") as timer:
            self.play(FadeIn(f), run_time=timer.duration)
        with self.my_voiceover(
                f"""avec 1 Farad = 1 Coulomb par Volt""") as timer:
            self.play(TransformMatchingTex(f, faradFormula), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        symbol = Condensator().scale(frame_factor).shift(UP * 5)
        with self.my_voiceover(
                f"""Enfin, le symbole utilisé dans les schémas électroniques représentent exactement ce qu'on viens de simuler, à savoir deux plaques séparées par un gap.""") as timer:
            self.play(Create(symbol), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        self.play(FadeOut(*self.mobjects), run_time=3)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
