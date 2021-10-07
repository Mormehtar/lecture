from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from attributes import Attributes


class StatusException(Exception):
    pass


class WrongInitialisation(StatusException):
    pass


class StatusesAreNotCompatible(StatusException):
    pass


class BaseStatus(object):
    def __init__(self, turns=None, infinite=False, **kvargs):
        self.turns = turns
        self.infinite = infinite
        if self.turns is None and not self.infinite:
            raise WrongInitialisation("No turns for finite status!")

    def get_name(self):
        return self.__class__.__name__

    def get_dict(self):
        result = {"name": self.get_name()}
        if not self.infinite:
            result["turns"] = self.turns
        return result

    def __str__(self):
        if self.infinite:
            return self.get_name()
        else:
            return f"{self.get_name()} for {self.turns} turns"

    def __repr__(self):
        return str(self)

    def extend(self, status: "BaseStatus"):
        if self.get_name() != status.get_name():
            raise StatusesAreNotCompatible(f"{self.get_name()} is not compatible with {status.get_name()}")
        if self.infinite or status.infinite:
            self.infinite = True
        else:
            self.turns += status.turns

    def tick(self, fighter):
        if not self.infinite:
            self.turns -= 1

    def is_dropped(self):
        return not self.infinite and self.turns == 0

    def modify_attrs(self, attributes: "Attributes"):
        return attributes
