#! -*- encoding:utf-8 -*-


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = '{%s: %s}' % (self.key, self.value)
        return val

    def __repr__(self):
        val = '{%s: %s}' % (self.key, self.value)
        return val


class DoubleLinkedList:

    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def __add_head(self, node):
        if not self.head:
            self.head = self.tail = node
            self.head.next = self.head.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def __add_tail(self, node):
        if not self.tail:
            self.head = self.tail = node
            self.head.prev = self.head.next = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def __del_head(self):
        if not self.head:
            return
        node = self.head
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.tail = None
        return node

    def __remove(self, node):
        if not node:
            node = self.tail
        if node == self.head:
            return self.__del_head()
        elif node == self.tail:
            return self.__del_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node

    def append(self, node):
        return self.__add_tail(node)

    def append_front(self, node):
        return self.__add_head(node)

    def remove(self, node=None):
        return self.__remove(node)

    def pop(self):
        return self.__del_head()

    def print(self):
        p = self.head
        output = ''
        while p:
            output += '%s' % p
            p = p.next
            if p:
                output += '==>'
        output += '  size: %s' % self.size
        print(output)


if __name__ == '__main__':
    ll = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        node = Node(i, i)
        nodes.append(node)
    ll.append(nodes[0])
    ll.print()
    ll.append_front(nodes[1])
    ll.print()
    ll.append(nodes[2])
    ll.print()
    ll.pop()
    ll.print()
    ll.append_front(nodes[3])
    ll.print()
    ll.remove(nodes[0])
    ll.print()
    ll.remove()
    ll.print()