# -*- encoding:utf-8 -*-

import struct


s = b'ABCD1234'
print(s)

struct_str = struct.unpack('>BBBBBBBB', s)
print(struct_str)

struct_str = struct.unpack('>HHHH', s)
print(struct_str)

struct_str = struct.unpack('>LL', s)
print(struct_str)

struct_str = struct.unpack('>8s', s)
print(struct_str)

struct_str = struct.unpack('>BBHL', s)
print(struct_str)
