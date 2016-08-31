#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’ve written a function or method that uses *args and **kwargs, so that it
can be general purpose, but you would also like to check the passed arguments
to see if they match a specific function calling signature.
"""


"""
SOLUTION
"""

from inspect import Signature
from inspect import Parameter

# Make a signature for a func(x, y=42, *, z=None)
params = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
           Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
           Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]

sig = Signature(params)
print(sig)
print('')


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)

# Try various examples
func(1, 2, z=3)
func(1)
func(1, z=3)
func(y=2, x=1)
# func(1, 2, 3, 4)
# func(y=2)
# func(1, y=2, x=3)
print('')


def make_sig(*names):
    params = [ Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
               for name in names ]
    return Signature(params)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


# Example use

class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


import inspect

print(inspect.signature(Stock))
s1 = Stock('ACME', 100, 490.1)
# s2 = Stock('ACME', 100)
# s3 = Stock('ACME', 100, 490.1, shares=50)
print('')


"""
DISCUSSION
"""

def make_sig2(*names):
    params = [ Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
               for name in names ]
    return Signature(params)


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)


class Structure2(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


# Example
class Stock2(Structure2):
    _fields = ['name', 'shares', 'price']


class Point2(Structure2):
    _fields = ['x', 'y']


print(inspect.signature(Stock2))
print(inspect.signature(Point2))
