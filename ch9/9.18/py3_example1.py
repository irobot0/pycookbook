#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’re writing code that ultimately needs to create a new class object. You’ve
thought about emitting emit class source code to a string and using a function
such as exec() to evaluate it, but you’d prefer a more elegant solution.
"""


"""
SOLUTION
"""

# Example of making a class manually from parts

# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__'  : __init__,
    'cost'      : cost,
}


# Make a class
import types
import abc

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

Stock2 = types.new_class('Stock2',
                         (),
                         {
                            'metaclass' : abc.ABCMeta
                         },
                         lambda ns: ns.update(cls_dict))
Stock2.__module__ = __name__


if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s.cost())
    print('')

    print(Stock2)
    print(type(Stock2))
