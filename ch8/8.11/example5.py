#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You are writing a lot of classes that serve as data structures, but you are
getting tired of writing highly repetitive and boilerplate __init__() functions.
"""


"""
DISCUSSION
"""


class Structure:
    # Class variable that specifies expected fields
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        else:
            # Set the arguments (alternate)
            self.__dict__.update(zip(self._fields, args))
