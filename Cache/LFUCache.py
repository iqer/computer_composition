#! -*- encoding:utf-8 -*-

from DoubleLinkedList import DoubleLinkedList, Node


class LFUNode(Node):

    def __init__(self, key, value):
        self.freq = 0
        super(LFUNode, self).__init__(key, value)


class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = dict()
        self.freq_map = dict()

    def __update_freq(self, node):
        freq = node.freq
        if freq in self.freq_map:
            self.freq_map[freq].remove(node)
            if not self.freq_map[freq].head:
                del self.freq_map[freq]
        node.freq += 1
        if node.freq in self.freq_map:
            self.freq_map[node.freq].append(node)
        else:
            self.freq_map[node.freq] = DoubleLinkedList()
            self.freq_map[node.freq].append(node)

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.__update_freq(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.map:
            node = self.map.pop(key)
            node.value = value
            self.map[key] = node
            self.__update_freq(node)
        else:
            node = LFUNode(key, value)
            # node.freq = 1
            if self.size == self.capacity:
                min_freq = min(self.freq_map)
                self.freq_map[min_freq].pop()
                self.size -= 1
            self.map[key] = node
            self.__update_freq(node)
            self.size += 1

    def print(self):
        print('**************************')
        for k, v in self.freq_map.items():
            print('freq: %s' % k)
            v.print()
        print('**************************')
        print()


if __name__ == '__main__':
    lfu = LFUCache(4)
    lfu.put(1, 1)
    lfu.print()
    lfu.put(2, 2)
    lfu.print()
    print(lfu.get(2))
    lfu.print()
    print(lfu.get(2))
    lfu.print()
    lfu.put(3, 3)
    lfu.print()
    lfu.put(4, 4)
    lfu.print()
    lfu.put(5, 5)
    lfu.print()
    lfu.put(6, 6)
    lfu.print()
