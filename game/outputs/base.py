from abc import ABC, abstractmethod


class BaseOutput(ABC):
    @abstractmethod
    def declare_fighter(self, fighter):
        raise NotImplementedError

    @abstractmethod
    def declare_round(self, round_number):
        raise NotImplementedError

    @abstractmethod
    def declare_status_dropped(self, fighter, status):
        raise NotImplementedError

    @abstractmethod
    def declare_attack(self, attacker, target):
        raise NotImplementedError

    @abstractmethod
    def declare_hit_probability(self, probability):
        raise NotImplementedError

    @abstractmethod
    def declare_hit(self):
        raise NotImplementedError

    @abstractmethod
    def declare_hp_loss(self, fighter, loss, reason):
        raise NotImplementedError

    @abstractmethod
    def declare_death(self, fighter, reason):
        raise NotImplementedError

    @abstractmethod
    def declare_miss(self, attacker, target):
        raise NotImplementedError
