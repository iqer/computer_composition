# -*- encoding:utf-8 -*-

import time
from threading import Lock, Condition, Thread


class ThreadSafeQueueException(Exception):
    pass


class ThreadSafeQueue:

    def __init__(self, max_size=0):
        self.max_size = max_size
        self.queue = list()
        self.lock = Lock()
        self.condition = Condition()

    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    def put(self, item):
        if self.max_size == 0:
            return ThreadSafeQueueException()
        if self.size() == self.max_size:
            self.condition.wait()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    def pop(self, block=False, timeout=0):
        if self.size() == 0:
            if block:
                time.sleep(timeout)
        if self.size() == 0:
            return None
        self.lock.acquire()
        item = self.queue.pop()
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()
        return item

    def get(self, index, block=False, timeout=0):
        if self.max_size == 0:
            return ThreadSafeQueueException()
        if self.size() == 0:
            if block:
                time.sleep(timeout)
        if self.size() == 0:
            return None
        self.lock.acquire()
        item = self.queue[index]
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()
        return item


if __name__ == '__main__':
    queue = ThreadSafeQueue(100)

    def produce():
        while True:
            queue.put(1)
            time.sleep(2)

    def consumer():
        while True:
            item = queue.pop(block=True, timeout=2)
            print('消费者获取到: %s' % item)
            time.sleep(1)
    thread1 = Thread(target=produce)
    thread2 = Thread(target=consumer)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
