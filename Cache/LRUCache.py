#! -*- encoding:utf-8 -*-

from DoubleLinkedList import DoubleLinkedList, Node


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = dict()
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.list.remove_node(node)
            self.list.append_front(node)
            return node.value
        return -1

    def put(self, key, value):
        node = Node(key, value)
        if key in self.map:
            old_node = self.map.pop(key)
            self.map[key] = node
            self.list.remove_node(old_node)
            self.list.append_front(node)
        else:
            if self.size == self.capacity:
                old_node = self.list.remove_node()
                self.map.pop(old_node.key)
                self.size -= 1
            self.map[key] = node
            self.list.append_front(node)
            self.size += 1

    def print(self):
        self.list.print()


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.print()
    lru.put(2, 2)
    lru.print()
    print(lru.get(1))
    lru.print()
    lru.put(3, 3)
    lru.print()
    print(lru.get(4))
