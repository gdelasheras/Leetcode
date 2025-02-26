"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

T: O(1) every operation.
S: O(c) c is the capacity of the cache.
"""

from utils.linked_list import create_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Diccionario para acceso O(1)

        # Nodos centinelas para facilitar la manipulación de la lista doblemente enlazada
        self.oldest = ListNode()  # Nodo menos reciente
        self.newest = ListNode()  # Nodo más reciente
        self.oldest.next = self.newest
        self.newest.prev = self.oldest

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_least_recently_used()

            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _remove_least_recently_used(self):
        lru_node = self.oldest.next
        self._remove_node(lru_node)
        del self.cache[lru_node.key]

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _add_to_front(self, node):
        node.prev = self.newest.prev
        node.next = self.newest
        self.newest.prev.next = node
        self.newest.prev = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


def test_lru_cache():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1
    lru_cache.put(4, 4)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4
    assert lru_cache.get(2) == -1
    assert lru_cache.get(5) == -1
    lru_cache.put(6, 6)
    assert lru_cache.get(3) == -1
