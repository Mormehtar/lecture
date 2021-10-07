from pytest import raises
from .first_approach import HashTable


def test_set():
    hash_map = HashTable()
    hash_map.set(3, 42)


def test_get():
    hash_map = HashTable()
    assert hash_map.get(3) is None


def test_get_data_after_set():
    hash_map = HashTable()
    hash_map.set(3, 42)
    assert hash_map.get(3) == 42


def test_delete():
    hash_map = HashTable()
    with raises(KeyError):
        hash_map.delete(3)


def test_should_not_return_deleted_value():
    hash_map = HashTable()
    hash_map.set(3, 42)
    hash_map.delete(3)
    assert hash_map.get(3) is None


def test_should_overwrite_by_key():
    hash_map = HashTable()
    hash_map.set(3, 42)
    hash_map.set(3, 100500)
    assert hash_map.get(3) == 100500


def test_big_key():
    hash_map = HashTable()
    hash_map.set(1_000_000_003, 42)
    assert hash_map.get(1_000_000_003) == 42


def test_collisions_do_not_overwrite():
    hash_map = HashTable(size=1)
    hash_map.set(42, 42)
    hash_map.set(84, 100500)
    assert hash_map.get(42) == 42
    assert hash_map.get(84) == 100500


def test_collision_with_delete_from_the_middle():
    hash_map = HashTable(size=1)
    hash_map.set(42, 42)
    hash_map.set(84, 100500)
    hash_map.set(168, 13)
    hash_map.delete(84)
    assert hash_map.get(42) == 42
    assert hash_map.get(84) is None
    assert hash_map.get(168) == 13


def test_collision_with_delete_from_the_begining():
    hash_map = HashTable(size=1)
    hash_map.set(42, 42)
    hash_map.set(84, 100500)
    hash_map.delete(42)
    assert hash_map.get(42) is None
    assert hash_map.get(84) == 100500


def test_collision_with_delete_from_the_end():
    hash_map = HashTable(size=1)
    hash_map.set(42, 42)
    hash_map.set(84, 100500)
    hash_map.delete(84)
    assert hash_map.get(42) == 42
    assert hash_map.get(84) is None


def test_strings():
    hash_map = HashTable()
    hash_map.set("blah", "blah! blah!")
    assert hash_map.get("blah") == "blah! blah!"
