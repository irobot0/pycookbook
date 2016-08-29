#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You are writing a lot of classes that serve as data structures, but you are
getting tired of writing highly repetitive and boilerplate __init__() functions.
"""


"""
SOLUTION
"""


class Structure:

    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) == len(self._fields):
            # Set the arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)
        else:
            raise TypeError('Expected {} arguments'.format(len(self.__fields)))


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']


class Circle(Structure):
    _fields = ['radius']


# Example class definitions
if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)
    # s2 = Stock('ACME', 50)
