#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to initialize parts of a class definition once at the time a class is
defined, not when instances are created.
"""


"""
DISCUSSION
"""


import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) == len(cls._fields):
            return super().__new__(cls, args)
        else:
            raise ValueError('{} arguments required'.format(len(cls._fields)))


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']


if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s[0])
    print(s.name)
    print(s.shares * s.price)
    # s.shares = 23
