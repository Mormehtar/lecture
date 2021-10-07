from random import Random


class Attributes(object):
    def __init__(
        self, constitution: int, agility: int, perception: int, strength: int,
    ):
        self.constitution = constitution
        self.agility = agility
        self.perception = perception
        self.strength = strength

    def get_max_hp(self):
        return self.constitution * 10

    @classmethod
    def generate_attributes(cls, rnd: Random = None):
        if rnd is None:
            rnd = Random()
        return Attributes(
            constitution=rnd.randint(1, 10),
            agility=rnd.randint(1, 10),
            perception=rnd.randint(1, 10),
            strength=rnd.randint(1, 10),
        )

    def __str__(self):
        return (
            f"const: {self.constitution}, agl: {self.agility}, "
            f"perc: {self.perception}, str: {self.strength}"
        )

    def get_dict(self):
        return self.__dict__.copy()

    def get_copy(self):
        return Attributes(**self.get_dict())
