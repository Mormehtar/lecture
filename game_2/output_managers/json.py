from .base import BaseOutputManager
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from fighter import Fighter


class JSONOutputManager(BaseOutputManager):
    def __init__(self):
        self.buffer = []

    def declare_attack(self, attacker: "Fighter", target: "Fighter"):
        self.buffer.append({
            "event_type": "attack",
            "attacker": attacker.name,
            "target": target.name,
        })

    def declare_hit_chance(
        self,
        attacker: "Fighter",
        target: "Fighter",
        chance: float
    ):
        self.buffer.append({
            "event_type": "hit_chance",
            "attacker": attacker.name,
            "target": target.name,
            "chance_percents": int(chance * 100 + 0.5),
        })

    def declare_hit(self, attacker: "Fighter", target: "Fighter"):
        self.buffer.append({
            "event_type": "hit",
            "attacker": attacker.name,
            "target": target.name,
        })

    def declare_miss(self, attacker: "Fighter", target: "Fighter"):
        self.buffer.append({
            "event_type": "miss",
            "attacker": attacker.name,
            "target": target.name,
        })

    def declare_fighter(self, fighter: "Fighter"):
        self.buffer.append({
            "event_type": "fighter",
            "fighter": fighter.name,
            "hp": fighter.hp,
            "attributes": fighter.attributes.get_dict(),
        })
