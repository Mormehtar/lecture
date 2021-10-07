from outputs.base import BaseOutput


class ConsoleOutput(BaseOutput):
    def declare_fighter(self, fighter):
        print(fighter)

    def declare_round(self, round_number):
        print("*" * 40)
        print(f"ROUND NUMBER {round_number}")

    def declare_status_dropped(self, fighter, status):
        print(f"{fighter.name} dropped status {status.get_name()}")

    def declare_attack(self, attacker, target):
        print(f"{attacker.name} attack {target.name}")

    def declare_hit_probability(self, probability):
        probability = int(probability * 100 + 0.5)
        print(f"Hit probability is {probability}%")

    def declare_hit(self):
        print("Target hit!")

    def declare_hp_loss(self, fighter, loss, reason):
        print(f"Fighter {fighter} lost {loss} hp due to {reason}")

    def declare_death(self, fighter, reason):
        print(f"Fighter {fighter} died due to {reason}")

    def declare_miss(self, attacker, target):
        print(f"Fighter {attacker.name} missed {target.name}")
