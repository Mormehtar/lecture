from typing import Hashable, Any, Callable, NamedTuple, TypeVar, Generic


class Node(object):
    def __init__(self, data, prev=None, next_=None):
        self.data = data
        self.next = next_
        self.prev = prev


class DoubleLinkedListException(Exception):
    pass


class NodeNotFound(DoubleLinkedListException):
    pass


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node(self, predicate):
        node = self.head
        while node is not None:
            if predicate(node.data):
                return node
            node = node.next
        raise NodeNotFound

    def update_or_append(self, predicate, data):
        try:
            node = self.find_node(predicate)
            node.data = data
        except NodeNotFound:
            self.append(data)

    def find_data(self, predicate):
        node = self.find_node(predicate)
        return node.data

    def append(self, data):
        new_node = Node(data, self.tail)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def delete(self, predicate):
        node = self.find_node(predicate)
        if self.head != node and self.tail != node:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            self.head.prev = None
        else:
            self.tail = node.prev
            self.tail.next = None


TKey = TypeVar("TKey", bound=Hashable)
TValue = TypeVar("TValue")


class HashTable(Generic[TKey, TValue]):

    class KeyValuePair(NamedTuple):
        key: TKey
        value: TValue

    def __init__(self, size: int = 1000):
        self.size = size
        self.buckets = [DoubleLinkedList() for _ in range(size)]

    def get(self, key: TKey, default=None) -> TValue:
        bucket = self._get_bucket(key)
        try:
            data = bucket.find_data(self._predicate(key))
            return data.value
        except NodeNotFound:
            return default

    def set(self, key: TKey, value: TValue):
        bucket = self._get_bucket(key)
        bucket.update_or_append(
            self._predicate(key),
            self.KeyValuePair(key, value),
        )

    def delete(self, key: TKey):
        try:
            bucket = self._get_bucket(key)
            bucket.delete(self._predicate(key))
        except NodeNotFound:
            raise KeyError(key)

    @classmethod
    def _predicate(cls, key: Hashable) -> Callable[[KeyValuePair], bool]:
        def real_predicate(data: HashTable.KeyValuePair) -> bool:
            return data.key == key
        return real_predicate

    def _get_bucket(self, key: TKey) -> DoubleLinkedList:
        hash_value = hash(key) % self.size
        bucket = self.buckets[hash_value]
        return bucket
