#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to create a new kind of instance attribute type with some extra
functionality, such as type checking.
"""


"""
SOLUTION
"""


# Descriptor attribute for an integer type-checked attribute
class Integer:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.name] = value
        else:
            raise TypeError('Expected an int')

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)      # Calls Point.x.__get__(p, Point)
p.y = 5         # Calls Point.y.__set__(p, 5)

# The following statement will cause exception in Python 3
# p.x = 2.3       # Calls Point.x.__set__(p, 2.3)


"""
DISCUSSION
"""

print(Point.x)      # Calls Point.x.__get__(None, Point)


# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, self.expected_type):
            instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attribute
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
