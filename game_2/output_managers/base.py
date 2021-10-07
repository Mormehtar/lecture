from typing import TYPE_CHECKING
from abc import ABC, abstractmethod


if TYPE_CHECKING:
    from fighter import Fighter


class BaseOutputManager(ABC):
    @abstractmethod
    def declare_attack(self, attacker: "Fighter", target: "Fighter"):
        raise NotImplementedError

    @abstractmethod
    def declare_hit_chance(
        self,
        attacker: "Fighter",
        target: "Fighter",
        chance: float
    ):
        raise NotImplementedError

    @abstractmethod
    def declare_hit(self, attacker: "Fighter", target: "Fighter"):
        raise NotImplementedError

    @abstractmethod
    def declare_miss(self, attacker: "Fighter", target: "Fighter"):
        raise NotImplementedError

    @abstractmethod
    def declare_fighter(self, fighter: "Fighter"):
        raise NotImplementedError
