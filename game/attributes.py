from random import randint


class Attributes(object):
    def __init__(self, constitution, perception, agility, strength):
        self.constitution = constitution
        self.perception = perception
        self.agility = agility
        self.strength = strength

    def get_max_hp(self):
        return self.constitution * 10

    def __str__(self):
        return f"con: {self.constitution}, per: {self.perception}, agi: {self.agility}, str: {self.strength}"

    @classmethod
    def generate(cls):
        return Attributes(
            randint(1, 10),
            randint(1, 10),
            randint(1, 10),
            randint(1, 10),
        )

    def get_dict(self):
        return {
            "constitution": self.constitution,
            "perception": self.perception,
            "agility": self.agility,
            "strength": self.strength,
        }

    def get_copy(self):
        return Attributes(**self.get_dict())
