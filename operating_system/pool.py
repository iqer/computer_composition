# -*- encoding:utf-8 -*-

import psutil
import threading
from operating_system.task import Task
from operating_system.ThreadSafeQueue import ThreadSafeQueue


class ProcessThread(threading.Thread):

    def __init__(self, task_queue, *args, **kwargs):
        threading.Thread.__init__(self)
        self.task_queue = task_queue
        self.dismiss_flag = threading.Event()
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while True:
            if self.dismiss_flag.is_set():
                break
            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            result = task.callable(*task.args, **task.kwargs)

    def dismiss(self):
        self.dismiss_flag.set()

    def stop(self):
        self.dismiss()


class ThreadPool:

    def __init__(self, size=0):
        if not size:
            size = psutil.cpu_count() * 2
        self.task_queue = ThreadSafeQueue(size)
        self.pool = ThreadSafeQueue()
        for i in range(size):
            self.pool.put(ProcessThread(self.task_queue))

    def start(self):
        for i in range(self.size()):
            thread = self.pool.get(i)
            thread.start()

    def join(self):
        for i in range(self.size()):
            thread = self.pool.get(i)
            thread.stop()

    def put(self, item):
        if not isinstance(item, Task):
            raise TaskTypeError()
        self.task_queue.put(item)

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    def size(self):
        return self.pool.size()


class TaskTypeError(Exception):
    pass
