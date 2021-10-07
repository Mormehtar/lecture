from random import random
from typing import TYPE_CHECKING

from status.lame import Lame
from status.bleed import Bleed

if TYPE_CHECKING:
    from attributes import Attributes
    from outputs.base import BaseOutput


class Fighter(object):
    def __init__(self, name: str, attributes: "Attributes", output: "BaseOutput"):
        self.output = output
        self.name = name
        self.attributes = attributes
        self.hp = self.attributes.get_max_hp()
        self.statuses = dict()

    def apply_damage(self, quantity, reason):
        self.hp -= quantity
        self.output.declare_hp_loss(self, quantity, reason)
        if self.hp <= 0:
            self.output.declare_death(self, reason)

    def set_status(self, status):
        if status.get_name() in self.statuses.keys():
            self.statuses[status.get_name()].extend(status)
        else:
            self.statuses[status.get_name()] = status

    def tick(self):
        for status in self.statuses.values():
            status.tick(self)
        statuses_to_drop = tuple(
            status.get_name()
            for status in self.statuses.values()
            if status.is_dropped()
        )
        for status in statuses_to_drop:
            self.output.declare_status_dropped(
                self,
                self.statuses.pop(status)
            )

    def get_attrs_modified_by_statuses(self):
        attrs_copy = self.attributes.get_copy()
        for status in self.statuses.values():
            attrs_copy = status.modify_attrs(attrs_copy)
        return attrs_copy

    def __str__(self):
        return f"Fighter {self.name} with attrs {self.attributes}. {self.hp} hp left and hes statuses {self.statuses}."

    def attack(self, target: "Fighter"):
        self.output.declare_attack(self, target)

        my_attrs = self.get_attrs_modified_by_statuses()
        target_attrs = target.get_attrs_modified_by_statuses()

        hit_probability = my_attrs.perception / (my_attrs.perception + target_attrs.agility)
        hit = random() > hit_probability
        self.output.declare_hit_probability(hit_probability)
        if hit:
            self.output.declare_hit()
            self.apply_damage(self.attributes.strength, "attack")
            if random() < 0.2:
                if random() > 0.5:
                    target.set_status(Lame(turns=2))
                else:
                    target.set_status(Bleed(turns=2))
            self.output.declare_fighter(target)
        else:
            self.output.declare_miss(self, target)
