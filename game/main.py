from typing import TYPE_CHECKING

from random import randint
from fighter import Fighter
from attributes import Attributes
from outputs.console import ConsoleOutput

if TYPE_CHECKING:
    from outputs.base import BaseOutput


class Main(object):
    def __init__(self, output: "BaseOutput"):
        self.output = output
        self.fighters = [
            Fighter("Fighter1", Attributes.generate(), self.output),
            Fighter("Fighter2", Attributes.generate(), self.output),
            Fighter("Fighter3", Attributes.generate(), self.output),
        ]

    @classmethod
    def alive_fighters(cls, fighters):
        return filter(lambda x: x.hp > 0, fighters)

    def run(self):
        for fighter in self.fighters:
            self.output.declare_fighter(fighter)

        round_number = 1

        alive_fighters = tuple(self.alive_fighters(self.fighters))

        while len(alive_fighters) > 1:
            self.output.declare_round(round_number)
            for i, fighter in enumerate(alive_fighters):
                target = randint(1, len(alive_fighters) - 1)
                if target == i:
                    target = 0
                fighter.attack(alive_fighters[target])

            alive_fighters = tuple(self.alive_fighters(alive_fighters))
            for fighter in alive_fighters:
                fighter.tick()
            round_number += 1

        for fighter in self.fighters:
            self.output.declare_fighter(fighter)


if __name__ == "__main__":
    Main(ConsoleOutput()).run()
