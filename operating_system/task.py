# -*- encoding:utf-8 -*-

import uuid
import threading


class Task:

    def __init__(self, func, *args, **kwargs):
        self.callable = func
        self.args = args
        self.kwargs = kwargs
        self.id = uuid.uuid4()

    def __str__(self):
        return 'Task id: ' + str(self.id)


class AsyncTask(Task):

    def __init__(self, func, *args, **kwargs):
        self.result = None
        self.condition = threading.Condition()
        super().__init__(func, *args, **kwargs)

    def set_result(self, result):
        self.condition.acquire()
        self.result = result
        self.condition.notify()
        self.condition.release()

    def get_result(self):
        self.condition.acquire()
        if not self.result:
            self.condition.wait()
        result = self.result
        self.condition.release()
        return result


def my_function():
    print('This is a tes function.')


if __name__ == '__main__':
    task = Task(my_function)
    print(task)
    print(task.args)
    print(task.kwargs)
