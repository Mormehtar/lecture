import pytest
from attributes import Attributes
from unittest.mock import Mock


def test_attributes_exists():
    Attributes(
        constitution=10,
        agility=10,
        perception=10,
        strength=10,
    )


def test_get_max_hp():
    Attributes.get_max_hp


@pytest.mark.parametrize(
    ("const", "max_hp"),
    (
        (5, 50),
        (10, 100),
    )
)
def test_get_max_hp_returns_hp(const, max_hp):
    attrs = Attributes(
        constitution=const,
        agility=10,
        perception=10,
        strength=10,
    )
    assert attrs.get_max_hp() == max_hp


def test_generate_attrs():
    attrs = Attributes.generate_attributes()
    assert attrs


def test_attrs_generated_with_predictable_values():
    rnd = Mock()
    rnd.randint.return_value = 42
    attrs = Attributes.generate_attributes(rnd)
    assert attrs.strength == 42
