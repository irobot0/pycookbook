#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to define a metaclass that allows class definitions to supply optional
arguments, possibly to control or configure aspects of processing during type
creation.
"""


"""
SOLUTION
"""


class MyMeta(type):

    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        super().__init__(name, bases, ns)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass
