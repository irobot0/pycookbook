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

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        else:
            # Set the arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

            # Set the additional arguments (if any)
            try:
                # for Python 3
                extra_args = kwargs.keys() - self._fields
            except TypeError:
                # for Python 2
                extra_args = self.diff(kwargs.keys(), self._fields)

            for name in extra_args:
                setattr(self, name, kwargs.pop(name))

            if kwargs:
                raise TypeError('Duplicate value for {}'.format(','.join(kwargs)))

    def diff(self, first, second):
        # using set(b) to ensure the algorithm is O(nlogn) instead of O(n^2)
        second = set(second)
        return [item for item in first if item not in second]


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


# Example use
if __name__ == '__main__':
    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
