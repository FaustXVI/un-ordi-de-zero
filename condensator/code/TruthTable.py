import functools
import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False
recording = False

frame_factor = 3
config.frame_width = 16 * frame_factor
config.frame_height = 9 * frame_factor
atomSize = 5
MAX_DISTANCE_EFFECT = 5
EFFECT_INTENSITY = 5
timeBetweenFrames = 0.08


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


def createRectangle(start, stop):
    (startx, starty) = start
    (stopx, stopy) = stop
    return [Atom((x, y, 0), AtomState.NEUTRAL) for x in
            range(startx, (stopx + 1)) for y in
            range(starty, (stopy + 1))]


def flat_map(f, xs):
    ys = []
    for x in xs:
        ys.extend(f(x))
    return ys


def repeatByWeight(e):
    (p, i, n) = e
    return [(p, i) for _ in range(0, n)]


def computeNextAtoms(atoms):
    newAtoms = [Atom(a.position, a.state) for a in atoms]
    negativeAtoms = [Atom(a.position, a.state) for a in atoms if a.state == AtomState.NEGATIVE]
    positiveAtoms = [Atom(a.position, a.state) for a in atoms if a.state == AtomState.POSITIVE]

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
    for index, atom in enumerate(atoms):
        if atom.state != AtomState.NEUTRAL:
            # print("for", atom.position)
            weightPosition = [(n.position, i, attractionWeight(atom, n)) for i, n in enumerate(atoms) if
                              n.isNeigbour(atom) and (n.state == AtomState.NEUTRAL or n == atom)]
            possiblePositions = flat_map(repeatByWeight, weightPosition)
            (newPosition, newIndex) = random.choice(possiblePositions)
            newAtoms[index].state = newAtoms[newIndex].state
            newAtoms[newIndex].state = atom.state
    return newAtoms


def simulate(circuit, nbFrames):
    steps = functools.reduce(lambda acc, _: [*acc, computeNextAtoms(acc[-1])], range(1, nbFrames), [circuit])
    return [drawAtoms(atoms) for atoms in steps]


class TruthTable(MyScene):

    def __init__(self):
        super().__init__(recording=recording)

    def playSimulation(self, drawings, timer):
        for drawing in drawings:
            self.clear()
            self.add(drawing)
            self.wait(timeBetweenFrames)

    def construct(self):
        self.next_section(skip_animations=section_done)
        r1 = createRectangle((-5, -5), (-1, 5))
        r2 = createRectangle((1, -5), (5, 5))
        r1[0].state = AtomState.NEGATIVE
        r2[-1].state = AtomState.POSITIVE
        circuit = [*r1, *r2]
        simulation = simulate(circuit, 10)
        with self.my_voiceover(
                r"""TODO""") as timer:
            self.playSimulation(simulation, timer)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
