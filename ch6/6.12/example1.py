#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to read complicated binary-encoded data that contains a collection of
nested and/or variable-sized records. Such data might include images, video,
shapefiles, and so on.
"""


"""
SOLUTION
"""

import struct


class StructField:
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format,
                                   instance._buffer,
                                   self.offset)
            if len(r) == 1:
                return r[0]
            else:
                return r


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


if __name__ == '__main__':
    f = open('polys.bin', 'rb')
    data = f.read()
    phead = PolyHeader(data)
    print(phead.file_code == 0x1234)
    print('min_x={}'.format(phead.min_x))
    print('min_y={}'.format(phead.min_y))
    print('max_x={}'.format(phead.max_x))
    print('max_y={}'.format(phead.max_y))
    print('num_polys={}'.format(phead.num_polys))
