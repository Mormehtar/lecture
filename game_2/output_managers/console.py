from .base import BaseOutputManager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fighter import Fighter


class ConsoleOutputManager(BaseOutputManager):
    def declare_attack(self, attacker: "Fighter", target: "Fighter"):
        print(f"{attacker.name} attacks {target.name}")

    def declare_hit_chance(
        self,
        attacker: "Fighter",
        target: "Fighter",
        chance: float
    ):
        print(f"Hit chance {chance}")

    def declare_hit(self, attacker: "Fighter", target: "Fighter"):
        print("Hit!")

    def declare_miss(self, attacker: "Fighter", target: "Fighter"):
        print("Miss!")

    def declare_fighter(self, fighter: "Fighter"):
        print(fighter)
