#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

A decorator has been applied to a function, but you want to “undo” it, gaining
access to the original unwrapped function.
"""


"""
DISCUSSION
"""

from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(add(2, 3))
    print('')
    print(add.__wrapped__(2, 3))
