import functools
import random

from manim.__main__ import main
from MyScene import MyScene, my_frac
import locale
from electronics import *

# locale.setlocale(locale.LC_ALL, 'fr_FR')

section_done = False
recording = False

atomsPerUnit = 3
atomSize = 5


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
                  ], ).scale(0.33)


def getX(position):
    return position[0]


def getY(position):
    return position[1]


class Atom:
    def __init__(self, position, state):
        self.position = position
        self.state = state

    def distance(self, atom):
        return max(abs(getX(self.position) - getX(atom.position)) , abs(getY(self.position) - getY(atom.position)))

    def isNeigbour(self, atom):
        return self.distance(atom) <= 1


def createRectangle(start, stop):
    (startx, starty) = start
    (stopx, stopy) = stop
    return [Atom((x, y, 0), AtomState.NEUTRAL) for x in
            range(startx, (stopx + 1)) for y in
            range(starty, (stopy + 1))]


def computeNextAtoms(atoms):
    newAtoms = [Atom(a.position, a.state) for a in atoms]

    for index, atom in enumerate(atoms):
        if atom.state == AtomState.NEGATIVE:
            possiblePositions = [(n.position, i) for i, n in enumerate(atoms) if n.isNeigbour(atom)]
            (newPosition, newIndex) = random.choice(possiblePositions)
            if newPosition != atom.position:
                newAtoms[index].state = newAtoms[newIndex].state
                newAtoms[newIndex].state = atom.state
    return newAtoms


class TruthTable(MyScene):

    def __init__(self):
        super().__init__(recording=recording)

    def construct(self):
        self.next_section(skip_animations=section_done)
        r1 = createRectangle((-2, -2), (2, 0))
        r1[0].state = AtomState.NEGATIVE
        atoms = drawAtoms(r1)
        self.add(atoms)
        self.wait(0.08)
        steps = functools.reduce(lambda acc, _: [*acc, computeNextAtoms(acc[-1])], range(1, 50), [r1])
        drawings = [drawAtoms(atoms) for atoms in steps]
        with self.my_voiceover(
                r"""TODO""") as timer:
            for drawing in drawings:
                self.clear()
                self.add(drawing)
                self.wait(0.08)


if __name__ == "__main__":
    main(["-pql",
          # "--disable_caching",
          __file__,
          # "--write_all",
          ], prog_name='invoked-command')
