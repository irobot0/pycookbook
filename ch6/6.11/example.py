#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to read or write data encoded as a binary array of uniform structures
into Python tuples.
"""


"""
SOLUTION
"""

from struct import Struct


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)

    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)

    print('')

    with open('data.b', 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        print(rec)

    print('')


    """
    DISCUSSION
    """

    from collections import namedtuple

    Record = namedtuple('Record', ['kind', 'x', 'y'])

    with open('data.b', 'rb') as f:
        records = (Record(*r) for r in read_records('<idd', f))
        for r in records:
            print(r.kind, r.x, r.y)

    print('')

    import numpy as np

    f = open('data.b', 'rb')
    records = np.fromfile(f, dtype='<i, <d, <d')
    print(records)
    print(records[0])
    print(records[1])
