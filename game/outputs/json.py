from outputs.base import BaseOutput


class JSONOutput(BaseOutput):
    def __init__(self):
        self.output_buffer = []

    def get_events(self):
        result = self.output_buffer
        self.output_buffer = []
        return result

    def declare_fighter(self, fighter):
        self.output_buffer.append(
            {
                "event_type": "fighter_state",
                "fighter": fighter.name,
                "attributes": fighter.attributes.get_dict(),
                "hp": fighter.hp,
                "statuses": tuple(map(lambda x: x.get_dict(), fighter.statuses.values())),
            }
        )

    def declare_round(self, round_number):
        self.output_buffer.append(
            {
                "event_type": "new_round",
                "round_number": round_number,
            }
        )

    def declare_status_dropped(self, fighter, status):
        self.output_buffer.append(
            {
                "event_type": "status_dropped",
                "fighter": fighter.name,
                "status": status.get_name(),
            }
        )

    def declare_attack(self, attacker, target):
        self.output_buffer.append(
            {
                "event_type": "attack",
                "attacker": attacker.name,
                "target": target.name,
            }
        )

    def declare_hit_probability(self, probability):
        self.output_buffer.append(
            {
                "event_type": "hit_probability",
                "probability": probability,
            }
        )

    def declare_hit(self):
        self.output_buffer.append(
            {
                "event_type": "hit",
            }
        )

    def declare_hp_loss(self, fighter, loss, reason):
        self.output_buffer.append(
            {
                "event_type": "hp_loss",
                "fighter": fighter.name,
                "resulting_hp": fighter.hp,
                "hp_loss": loss,
                "reason": reason,
            }
        )

    def declare_death(self, fighter, reason):
        self.output_buffer.append(
            {
                "event_type": "death",
                "fighter": fighter.name,
                "reason": reason,
            }
        )

    def declare_miss(self, attacker, target):
        self.output_buffer.append(
            {
                "event_type": "miss",
                "attacker": attacker.name,
                "target": target.name,
            }
        )
