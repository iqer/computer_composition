# -*- encoding:utf-8 -*-


import socket


def client(i):
    s = socket.socket()
    s.connect(('127.0.0.1', 6666))
    print('client % s receive: %s' % (i, s.recv(1024)))
    s.close()


if __name__ == '__main__':
    for i in range(10):
        client(i)

