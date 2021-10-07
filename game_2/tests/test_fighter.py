from fighter import Fighter
from attributes import Attributes


def test_fighter_can_be_created():
    Fighter("Dummy", Attributes.generate_attributes())


def test_attack_exists():
    f = Fighter("Dummy", Attributes.generate_attributes())
    assert f.attack


def test_attack_costs_10_hp():
    attacker = Fighter("Dummy", Attributes.generate_attributes())
    target = Fighter("Dummy2", Attributes.generate_attributes())
    attacker.attack(target)
    assert target.hp == 90


def test_is_alive_exists():
    f = Fighter("Dummy", Attributes.generate_attributes())
    assert f.is_alive


def test_is_alive_returns_true_for_alive():
    f = Fighter("Dummy", Attributes.generate_attributes())
    assert f.is_alive()


def test_is_alive_returns_false_for_dead():
    f = Fighter("Dummy", Attributes.generate_attributes())
    f.hp = 0
    assert f.is_alive() is False


def test_is_alive_returns_false_for_negative_hp():
    f = Fighter("Dummy", Attributes.generate_attributes())
    f.hp = -1
    assert f.is_alive() is False
