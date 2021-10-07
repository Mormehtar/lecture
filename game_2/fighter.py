from typing import Optional, TYPE_CHECKING, Dict
from random import Random
from attributes import Attributes
from statuses.base import BaseStatus
from statuses.lame import Lame
from statuses.feeble import Feeble


if TYPE_CHECKING:
    from output_managers.base import BaseOutputManager


class Fighter(object):
    def __init__(
        self,
        name: str,
        attributes: Attributes,
        output_manager: "BaseOutputManager",
        rnd: Optional[Random] = None,
    ):
        self.rnd = Random() if rnd is None else rnd
        self.name = name
        self.attributes = attributes
        self.hp = self.attributes.get_max_hp()
        self.output_manager = output_manager
        self.statuses: Dict[str, BaseStatus] = {}

    def set_status(self, status: BaseStatus):
        self.statuses[status.NAME] = status

    def get_attrs_modified_by_statuses(self) -> Attributes:
        attrs_copy = self.attributes.get_copy()
        for status in self.statuses.values():
            attrs_copy = status.modify_attrs(attrs_copy)
        return attrs_copy

    def attack(self, target: "Fighter"):
        self.output_manager.declare_attack(attacker=self, target=target)
        my_modified_attrs = self.get_attrs_modified_by_statuses()
        target_modified_attrs = target.get_attrs_modified_by_statuses()

        hit_chance = (
            my_modified_attrs.perception /
            (target_modified_attrs.agility + my_modified_attrs.perception)
        )
        self.output_manager.declare_hit_chance(self, target, hit_chance)
        if self.rnd.random() < hit_chance:
            if self.rnd.random() < 0.2:
                if self.rnd.random() > 0.5:
                    target.set_status(Feeble())
                else:
                    target.set_status(Lame())

            self.output_manager.declare_hit(self, target)
            target.hp -= my_modified_attrs.strength
        else:
            self.output_manager.declare_miss(self, target)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} with attrs {self.attributes} has {self.hp} hp."
