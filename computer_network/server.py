# -*- encoding:utf-8 -*-


import json
import socket

from operating_system.pool import ThreadPool as tp
from operating_system.task import AsyncTask
from computer_network.processor.net.parser import IPParser
from computer_network.processor.tran.parser import UDPParser, TCPParser


class ProcessTask(AsyncTask):
    def __init__(self, packet, *args, **kwargs):
        self.packet = packet
        super(ProcessTask, self).__init__(func=self.process, *args, **kwargs)

    def process(self):
        headers = {
            'network_header': None,
            'transport_header': None
        }
        ip_header = IPParser.ip_parse(self.packet)
        headers['network_header'] = ip_header
        if ip_header['protocol'] == 17:
            udp_header = UDPParser.parse(self.packet)
            headers['transport_header'] = udp_header
        elif ip_header['protocol'] == 6:
            tcp_header = TCPParser.parse(self.packet)
            headers['transport_header'] = tcp_header
        return headers


class Server:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        ip = '192.168.1.4'
        port = 6667
        self.sock.bind((ip, port))
        self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        self.pool = tp(10)
        self.pool.start()

    def loop_server(self):
        while True:
            packet, addr = self.sock.recvfrom(65535)
            task = ProcessTask(packet)
            self.pool.put(task)
            result = task.get_result()
            result = json.dumps(result, indent=4)
            print(result)


if __name__ == '__main__':
    server = Server()
    server.loop_server()
