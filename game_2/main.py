from typing import TYPE_CHECKING
from fighter import Fighter
from attributes import Attributes
from output_managers.console import ConsoleOutputManager


if TYPE_CHECKING:
    from output_managers.base import BaseOutputManager


class Main(object):
    def __init__(self, output_manager: "BaseOutputManager"):
        self.output_manager = output_manager
        self.fighter1 = Fighter(
            "Fighter1",
            Attributes.generate_attributes(),
            output_manager=output_manager,
        )
        self.fighter2 = Fighter(
            "Fighter2",
            Attributes.generate_attributes(),
            output_manager=output_manager,
        )

    def run(self):
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            self.fighter1.attack(self.fighter2)
            self.fighter2.attack(self.fighter1)

        self.output_manager.declare_fighter(self.fighter1)
        self.output_manager.declare_fighter(self.fighter2)


if __name__ == "__main__":
    Main(ConsoleOutputManager()).run()
