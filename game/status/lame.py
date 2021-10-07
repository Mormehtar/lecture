from status.base import BaseStatus


class Lame(BaseStatus):
    def modify_attrs(self, attributes):
        attributes.agility //= 2
        return attributes
