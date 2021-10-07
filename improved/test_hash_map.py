import pytest
from .hash_map import HashMap


def test_set():
    m = HashMap()
    m.set(3, 42)


def test_get():
    m = HashMap()
    assert m.get(3) is None


def test_get_after_set():
    m = HashMap()
    m.set(3, 42)
    assert m.get(3) == 42


def test_get_after_set_for_strings():
    m = HashMap()
    m.set("blah", 42)
    assert m.get("blah") == 42


def test_delete():
    m = HashMap()
    assert m.pop(3) is None


def test_delete_after_set():
    m = HashMap()
    m.set(3, 42)
    assert m.pop(3) == 42
    assert m.get(3) is None


def test_set_overwrite():
    m = HashMap()
    m.set(3, 42)
    m.set(3, 100500)
    assert m.get(3) == 100500


def test_test_get_after_set_with_big_key():
    m = HashMap()
    m.set(1_000_000_003, 42)
    assert m.get(1_000_000_003) == 42


def test_collision_with_set():
    m = HashMap(volume=1)
    m.set(42, 42)
    m.set(84, 100500)
    assert m.get(42) == 42
    assert m.get(84) == 100500


def test_collision_delete_from_middle():
    m = HashMap(volume=1)
    m.set(42, 42)
    m.set(84, 100500)
    m.set(168, 13)
    m.delete(84)
    assert m.get(42) == 42
    assert m.get(84) is None
    assert m.get(168) == 13


def test_collision_delete_from_beginning():
    m = HashMap(volume=1)
    m.set(42, 42)
    m.set(84, 100500)
    m.delete(42)
    assert m.get(42) is None
    assert m.get(84) == 100500


def test_collision_delete_from_end():
    m = HashMap(volume=1)
    m.set(42, 42)
    m.set(84, 100500)
    m.delete(84)
    assert m.get(42) == 42
    assert m.get(84) is None
