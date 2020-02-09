# -*- encoding:utf-8 -*-


import socket


def server():

    s = socket.socket()

    host = '127.0.0.1'
    port = 6666
    s.bind((host, port))

    s.listen(5)

    while True:
        c, addr = s.accept()
        print('client addr:', addr)
        c.send(b'Message from server')
        c.close()


if __name__ == '__main__':
    server()
