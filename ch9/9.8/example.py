#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to define a decorator inside a class definition and apply it to other
functions or methods.
"""


"""
DISCUSSION
"""

from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


# As an instance method
a = A()


@a.decorator1
def spam():
    pass


# As a class method
@A.decorator2
def grok():
    pass


"""
DISCUSSION
"""


class Person:
    # Create a property instance]
    first_name = property()

    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str):
            self._first_name = value
        else:
            raise TypeError('Expected a string')


class B(A):
    @A.decorator2
    def bar(self):
        pass
