#! -*- encoding:utf-8 -*-

from DoubleLinkedList import DoubleLinkedList, Node


class FIFOCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = dict()
        self.double_linked_list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key not in self.map:
            return -1
        value = self.map[key].value
        return value

    def put(self, key, value):
        if key in self.map:
            node = self.map.get(key)
            self.double_linked_list.remove(node)
            node.value = value
            self.double_linked_list.append(node)
        else:
            if self.size == self.capacity:
                node = self.double_linked_list.pop()
                del self.map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.map[key] = node
            self.double_linked_list.append(node)
            self.size += 1

    def print(self):
        self.double_linked_list.print()


if __name__ == '__main__':
    ff = FIFOCache(2)
    ff.put(1, 1)
    ff.print()
    ff.put(2, 2)
    ff.print()
    print(ff.get(1))
    ff.put(3, 3)
    ff.print()
    print(ff.get(2))
    ff.print()
    ff.put(4, 4)
    ff.print()
    print(ff.get(1))



