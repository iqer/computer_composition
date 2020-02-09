# -*_ enconding:utf-8 -*_


import struct
import socket


class IPParser:
    pass

    @classmethod
    def ip_head_parse(cls, ip_header):
        """
        1.ip version ip头长度 服务类型 16位总长度
        2.16位标识符 3位标记位 3位片偏移
        3.8位TTL 8位协议 16位ip头校验和
        4.32位源ip
        5.目的ip
        :param ip_header:
        :return:
        """
        # 1
        line1 = struct.unpack('>BBH', ip_header[:4])
        ip_version = line1[0] >> 4
        iph_length = line1[0] & 15
        pkg_length = line1[2]
        # 3
        line3 = struct.unpack('>BBH', ip_header[8:12])
        TTL = line3[0]
        protocol = line3[1]
        iph_checksum = line3[2]
        # 4
        line4 = struct.unpack('>4s', ip_header[12:16])
        src_ip = socket.inet_ntoa(line4[0])
        line5 = struct.unpack('>4s', ip_header[16:20])
        dst_ip = socket.inet_ntoa(line5[0])
        return {
            'ip_version': ip_version,
            'iph_length': iph_length,
            'packet_length': pkg_length,
            'TTL': TTL,
            'protocol': protocol,
            'iph_checksum': iph_checksum,
            'src_ip': src_ip,
            'dst_ip': dst_ip
        }

    @classmethod
    def ip_parse(cls, packet):
        ip_header = packet[:20]
        return cls.ip_head_parse(ip_header)
