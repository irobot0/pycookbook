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
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        else:
            # Set all of the positional arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

            # Set the remaining keyword arguments
            for name in self._fields[len(args):]:
                setattr(self, name, kwargs.pop(name))

            # Check for any remaining unknown arguments
            if len(kwargs) != 0:
                raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


# Example use
if __name__ == '__main__':
    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)
