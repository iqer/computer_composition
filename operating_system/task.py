# -*- encoding:utf-8 -*-

import uuid


class Task:

    def __init__(self, func, *args, **kwargs):
        self.callable = func
        self.args = args
        self.kwargs = kwargs
        self.id = uuid.uuid4()

    def __str__(self):
        return 'Task id: ' + str(self.id)


def my_function():
    print('This is a tes function.')


if __name__ == '__main__':
    task = Task(my_function)
    print(task)
    print(task.args)
    print(task.kwargs)
