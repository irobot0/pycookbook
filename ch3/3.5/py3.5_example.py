#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You have a byte string and you need to unpack it into an integer value.
Alternatively, you need to convert a large integer back into a byte string.
"""


"""
SOLUTION
"""

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))


"""
DISCUSSION
"""

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

import struct

hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

x = 523 ** 23
print(x)
print(x.bit_length())

nbytes, rem = divmod(x.bit_length(), 8)

if rem != 0:
    nbytes = nbytes + 1

print(x.to_bytes(nbytes, 'little'))
