#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to wrap functions with a decorator, but the result is going to be a
callable instance. You need your decorator to work both inside and outside class
definitions.
"""


"""
DISCUSSION
"""

import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls = self.ncalls + 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


print(add(2, 3))
print(add(4, 5))
print(add.ncalls)

s = Spam()
print(s.bar(1))
print(s.bar(2))
print(s.bar(3))
print(s.bar.ncalls)
print('')


"""
DISCUSSION
"""

s = Spam()

def grok(self, x):
    pass

print(grok.__get__(s, Spam))
print('')


def profiled2(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls = ncalls + 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# Example
@profiled2
def add(x, y):
    return x + y

print(add(2, 3))
print(add(4, 5))
print(add.ncalls())
