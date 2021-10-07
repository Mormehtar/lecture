from typing import Hashable, Generic, TypeVar
from logging import getLogger


logger = getLogger(__name__)


class Node(object):
    def __init__(self, data, prev_=None, next_=None):
        self._data = data
        self._prev = prev_
        self._next = next_

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, eq_func):
        pointer = self.head
        while pointer is not None:
            if eq_func(pointer._data):
                return pointer
            pointer = pointer._next
        raise KeyError(f"Nothing found!")

    def append(self, data):
        new_node = Node(data, prev_=self.tail)
        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail._next = new_node
        self.tail = new_node

    def delete(self, node):
        if node._prev is not None:
            node._prev._next = node._next
        else:
            self.head = node._next
        if node._next is not None:
            node._next._prev = node._prev
        else:
            self.tail = node._next


KT = TypeVar("KT", bound=Hashable)
VT = TypeVar("VT")


class HashMap(Generic[KT, VT]):
    def __init__(self, volume: int = 1000, collision_manager=LinkedList):
        self.volume = volume
        self.table = tuple(collision_manager() for _ in range(volume))

    @classmethod
    def get_search_func(cls, key: KT):
        def search_func(data: tuple[KT, VT]) -> bool:
            return data[0] == key
        return search_func

    def get(self, key: KT, default: VT = None) -> VT:
        bucket = self._get_bucket(key)
        try:
            node = bucket.find(self.get_search_func(key))
            return node.data[1]
        except KeyError:
            return default

    def set(self, key, value):
        bucket = self._get_bucket(key)
        try:
            existing_item = bucket.find(self.get_search_func(key))
            existing_item.data = (key, value)
        except KeyError:
            bucket.append((key, value))

    def delete(self, key):
        bucket = self._get_bucket(key)
        existing_item = bucket.find(self.get_search_func(key))
        bucket.delete(existing_item)

    def pop(self, key, default=None):
        bucket = self._get_bucket(key)
        try:
            existing_item = bucket.find(self.get_search_func(key))
            bucket.delete(existing_item)
            return existing_item.data[1]
        except KeyError:
            return default

    def _get_bucket(self, key: KT):
        hash_value = hash(key) % self.volume
        bucket: LinkedList = self.table[hash_value]
        return bucket
