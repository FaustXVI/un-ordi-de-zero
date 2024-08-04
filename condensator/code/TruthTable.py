import functools
import math
import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = True
recording = False

frame_factor = 3
config.frame_width = 16 * frame_factor
config.frame_height = 9 * frame_factor
atomSize = 5
MAX_DISTANCE_EFFECT = 5
EFFECT_INTENSITY = 100
# timeBetweenFrames = 0.5
timeBetweenFrames = 0.08
SPEED_UP = 1


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
            return 0
        distance = closestDistance(neighbour, currentAtom, poolOfAtoms)
        return distance - 1

    def oppositeStateAttractionWeight(currentAtom, neighbour, poolOfAtoms):
        if len(poolOfAtoms) == 0 or (len(poolOfAtoms) == 1 and poolOfAtoms[0].position == currentAtom.position):
            return 0
        distance = closestDistance(neighbour, currentAtom, poolOfAtoms)
        return MAX_DISTANCE_EFFECT - (distance - 1)

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
        return EFFECT_INTENSITY ** min(MAX_DISTANCE_EFFECT, max(0, exponent))

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
    return ([drawAtoms(atoms) for atoms in steps], steps[-1])


def constructLeftSide(distance=0):
    return [*(createLeftBattery(distance)), *(createLeftCable(distance)), *(createLeftPlate(distance))]


def createLeftPlate(distance):
    return createRectangle((-3 - distance, -5), (-1 - distance, 5))


def countNegativesInLeftPlate(distance, atoms):
    return countStateInRectangle((-3 - distance, -5), (-1 - distance, 5), atoms, AtomState.NEGATIVE)


def createLeftCable(distance):
    return createRectangle((-10 - distance, -1), (-4 - distance, 1))


def createDisconnectedLeftCable(distance):
    return createRectangle((-9 - distance, -1), (-3 - distance, 1))


def createLeftBattery(distance):
    return createRectangle((-15 - distance, -3), (-11 - distance, 3), AtomState.NEGATIVE)


def constructRightSide(distance=0):
    return [*(createRightBattery(distance)), *(createRightCable(distance)), *(createRightPlate(distance))]


def createRightPlate(distance):
    return createRectangle((1 + distance, -5), (3 + distance, 5))


def createRightCable(distance):
    return createRectangle((4 + distance, -1), (10 + distance, 1))


def createRightBattery(distance):
    return createRectangle((11 + distance, -3), (15 + distance, 3), AtomState.POSITIVE)


def constructCircuit(distance=0):
    return [*constructLeftSide(distance), *constructRightSide(distance)]


class TruthTable(MyScene):

    def __init__(self):
        super().__init__(recording=recording)

    def playSimulation(self, circuit, duration):
        nbFrames = math.ceil(duration / timeBetweenFrames)
        (drawings, lastState) = simulate(circuit, nbFrames)
        for (i, drawing) in enumerate(drawings):
            if (i % SPEED_UP == 0):
                self.clear()
                self.add(drawing)
                self.wait(timeBetweenFrames)
        return lastState

    def construct(self):
        self.next_section(skip_animations=section_done)
        leftBattery = createLeftBattery(3)
        leftBatteryDrawing = drawAtoms(leftBattery)
        with self.my_voiceover(r"""TODO""") as timer:
            self.play(FadeIn(leftBatteryDrawing), run_time=timer.duration)
        self.next_section(skip_animations=section_done)
        circuit = constructCircuit(MAX_DISTANCE_EFFECT)
        with self.my_voiceover(
                r"""TODO""", duration=10) as timer:
            finalState = self.playSimulation(circuit, timer.duration)
        negativeInLeftPlate = countNegativesInLeftPlate(MAX_DISTANCE_EFFECT, finalState)
        with self.my_voiceover(f"""On a {negativeInLeftPlate}""") as timer:
            self.wait(timer.duration)
        # circuit = constructCircuit()
        # with self.my_voiceover(
        #         r"""TODO""", duration=10) as timer:
        #     self.playSimulation(circuit, timer.duration)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
