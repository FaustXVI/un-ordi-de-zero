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


def createAnimationForNextStep(previousAtoms, newAtoms):
    return AnimationGroup(FadeOut(previousAtoms), FadeIn(newAtoms))


def getX(position):
    return position[0]


def getY(position):
    return position[1]


class Atom:
    def __init__(self, position, state):
        self.position = position
        self.state = state

    def closeTo(self, atom):
        return ((abs(getX(self.position) - getX(atom.position)) <= 1 and getY(self.position) == getY(
            atom.position)) or
                (abs(getY(self.position) - getY(atom.position)) <= 1 and getX(self.position) == getX(
                    atom.position)))


def createRectangle(start, stop):
    (startx, starty) = start
    (stopx, stopy) = stop
    return [Atom((x, y, 0), AtomState.NEUTRAL) for x in
            range(startx, (stopx + 1)) for y in
            range(starty, (stopy + 1))]


def computeNextAtoms(atoms):
    newAtoms = []
    for atom in atoms:
        if atom.position not in [a.position for a in newAtoms]:
            currentState = atom.state
            if currentState == AtomState.NEGATIVE:
                neighbours = [n for n in atoms if
                              n.closeTo(atom) and (n.position not in [a.position for a in newAtoms])]
                newStatePosition = random.choice(neighbours)
                if newStatePosition.position == atom.position:
                    newAtoms.append(Atom(atom.position, atom.state))
                else:
                    newAtoms.append(Atom(atom.position, newStatePosition.state))
                    newAtoms.append(Atom(newStatePosition.position, atom.state))
    return [*newAtoms, *[n for n in atoms if n.position not in [a.position for a in newAtoms]]]


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
        animations = [createAnimationForNextStep(p, n) for (p, n) in zip(drawings, drawings[1:])]
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
