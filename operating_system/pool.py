# -*- encoding:utf-8 -*-


import threading
from operating_system.task import Task

class ProcessThread(threading.Thread):

    def __init__(self, task_queue, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.args = args
        self.kwargs = kwargs
        self.task_queue = task_queue
        self.dismiss_flag = threading.Event()

    def run(self):
        while True:
            if self.dismiss_flag.is_set():
                break
            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            result = task.callable(*task.args, **task.kwargs)

    def stop(self):
        self.dismiss()

    def dismiss(self):
        self.dismiss_flag.set()

