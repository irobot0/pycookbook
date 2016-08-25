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


class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<', '>', '!', '@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset = offset + struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


if __name__ == '__main__':
    f = open('polys.bin', 'rb')
    phead = PolyHeader.from_file(f)
    print(phead.file_code == 0x1234)
    print('min_x={}'.format(phead.min_x))
    print('min_y={}'.format(phead.min_y))
    print('max_x={}'.format(phead.max_x))
    print('max_y={}'.format(phead.max_y))
    print('num_polys={}'.format(phead.num_polys))
