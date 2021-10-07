from status.base import BaseStatus


class Bleed(BaseStatus):
    def tick(self, fighter):
        super(Bleed, self).tick(fighter)
        fighter.apply_damage(10, "bleed")
