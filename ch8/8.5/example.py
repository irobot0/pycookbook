#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to encapsulate “private” data on instances of a class, but are
concerned about Python’s lack of access control.
"""


"""
SOLUTION
"""


class A:
    def __init__(self):
        self._internal = 0      # An internal attribute
        self.public = 1         # a public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        '''
        An internal method
        '''
        pass


class B:
    def __init__(self):
        # Name mangling, this property will not be inherited by subclasses.
        self.__private = 0

    def __private_method(self):
        '''
        Name mangling, this method will not be inherited by subclasses
        '''
        pass

    def public_method(self):
        # Do something first ...
        self.__private_method()
        # Do something else ...


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1      # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass


"""
DISCUSSION
"""

lambda_ = 2.0   # Trailing _ to avoid clash with lambda keyword
