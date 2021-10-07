from .base import BaseStatus


class Lame(BaseStatus):
    NAME = "Lame"

    def modify_attrs(self, attrs):
        attrs.agility //= 2
        return attrs
