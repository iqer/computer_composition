# -*- encoding:utf-8 -*-

import threading
import time


class ThreadSafeException(Exception):
    pass


class ThreadSafeQueue:

    def __init__(self, max_size=0):
        self.max_size = max_size
        self.queue = list()
        self.lock = threading.Lock()
        self.condition = threading.Condition()

    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    def put(self, item):
        if self.max_size != 0 and self.size() > self.max_size:
            return ThreadSafeException()
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
                self.condition.acquire()
                self.condition.wait(timeout=timeout)
                self.condition.release()
            else:
                return None

        self.lock.acquire()
        item = None
        if len(self.queue) > 0:
            item = self.queue.pop()
        self.lock.release()
        return item

    def get(self, index):
        self.lock.acquire()
        item = self.queue[index]
        self.lock.release()
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
            time.sleep(1)
            print('获取到的元素为: %s' % item)

    thread1 = threading.Thread(target=produce)
    thread2 = threading.Thread(target=consumer)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
