# -*- encoding:utf-8 -*-

import time
from operating_system import task, pool


class SimpleTask(task.Task):
    def __init__(self, callable):
        super(SimpleTask, self).__init__(callable)


def process():
    time.sleep(1)
    print('This is a SimpleTask callable function 1.')
    time.sleep(1)
    print('This is a SimpleTask callable function 2.')


def test():
    test_pool = pool.ThreadPool()
    test_pool.start()

    for i in range(10):
        simple_task = SimpleTask(process)
        test_pool.put(simple_task)


def async_test():
    test_pool = pool.ThreadPool()
    test_pool.start()

    def async_process():
        num = 0
        for j in range(100):
            num += j
        return num

    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        result = async_task.get_result()
        print('Get result: %s' % result)


def async_test2():
    test_pool = pool.ThreadPool()
    test_pool.start()

    def async_process():
        num = 0
        for j in range(100):
            num += j
        time.sleep(5)
        return num

    for i in range(1):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        print('Get result at %s' % time.time())
        result = async_task.get_result()
        print('Get result at %s : %s' % (time.time(), result))


def async_test3():
    test_pool = pool.ThreadPool()
    test_pool.start()

    def async_process():
        num = 0
        for j in range(100):
            num += j
        return num

    for i in range(1):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        print('Get result at %s' % time.time())
        time.sleep(5)
        result = async_task.get_result()
        print('Get result at %s : %s' % (time.time(), result))


if __name__ == '__main__':
    # test()
    # async_test()
    # async_test2()
    async_test3()
