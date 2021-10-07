from .base import BaseStatus


class Feeble(BaseStatus):
    NAME = "Feeble"

    def modify_attrs(self, attrs):
        attrs.strength //= 2
        return attrs
