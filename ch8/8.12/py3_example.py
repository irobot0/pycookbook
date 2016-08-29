#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to define a class that serves as an interface or abstract base class
from which you can perform type checking and ensure that certain methods are
implemented in subclasses.
"""


"""
DISCUSSION
"""

from abc import ABCMeta
from abc import abstractmethod


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


import io

# Register the built-in I/O classes as supporting out interface
IStream.register(io.IOBase)

# Open a normal file and type check
f = open('foo.txt')
print(isinstance(f, IStream))   # Returns True


class A(metaclass=ABCMeta):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


import collections


x = [1, 2, 3]

# Check if x is a sequence
if isinstance(x, collections.Sequence):
    print('{} is a sequence'.format(x))


x = (1, 2, 3)

# Check if x is iterable
if isinstance(x, collections.Iterable):
    print('{} is a iterable'.format(x))


x = (1, 2, 3)

# Check if x has a size
if isinstance(x, collections.Sized):
    print('{} has a size'.format(x))


x = {
    'name'      : 'Jim',
    'age'       : 18,
    'gender'    : 'male'
}

# Check if x is a mapping
if isinstance(x, collections.Mapping):
    print('{} is a mapping'.format(x))


from decimal import Decimal
import numbers

x = Decimal('3.4')
print(isinstance(x, numbers.Real))
