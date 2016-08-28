#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’d like to define a read-only attribute as a property that only gets computed
on access. However, once accessed, you’d like the value to be cached and not
recomputed on each access.
"""


"""
SOLUTION
"""


class lazyproperty:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)
print('')


"""
DISCUSSION
"""

c = Circle(4.0)

# Get instance variables
print(vars(c))

# Compute area and observe variables afterward
print(c.area)
print(vars(c))

# Notice access doesn't invoke property anymore
print(c.area)

# Delete the variable and see property trigger again
del c.area
print(vars(c))
print(c.area)

print(c.area)
c.area = 25
print(c.area)
print('')


def lazyproperty2(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


class Circle2:

    def __init__(self, radius):
        self.radius = radius

    @lazyproperty2
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty2
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle2(4.0)
print(c.area)
print(c.area)
c.area = 25
