#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’ve learned about function argument annotations and you have a thought that
you might be able to use them to implement multiple-dispatch (method
overloading) based on types. However, you’re not quite sure what’s involved (or
if it’s even a good idea).
"""


"""
SOLUTION
"""

import inspect
import types


class MultiMethod:
    '''
    Represents a single multimethod.
    '''
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, method):
        '''
        Register a new method as a multimethod.
        '''
        sig = inspect.signature(method)

        # Build a type signature from the method's annotations.
        types = []
        for name, param in sig.parameters.items():
            if name == 'self':
                continue
            if param.annotation is inspect.Parameter.empty:
                raise TypeError(
                    'Argument {} must be annotated with a type'.format(name)
                )
            if not isinstance(param.annotation, type):
                raise TypeError(
                    'Argument {} annotation must be a type'.format(name)
                )
            if param.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = method
            types.append(param.annotation)
        self._methods[tuple(types)] = method

    def __call__(self, *args):
        '''
        Call a method based on type signature of the arguments.
        '''
        types = tuple(type(arg) for arg in args[1:])
        method = self._methods.get(types, None)
        if method is None:
            raise TypeError('No matching method for types {}'.format(types))
        else:
            return method(*args)

    def __get__(self, instance, cls):
        '''
        Descriptor method needed to make calls work in a class.
        '''
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


class MultiDict(dict):
    '''
    Special dictionary to build multimethods in a metaclass.
    '''
    def __setitem__(self, key, value):
        if key in self:
            # If key already exists, it must be a multimethod or callable.
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mval = MultiMethod(key)
                mval.register(current_value)
                mval.register(value)
                super().__setitem__(key, value)
        else:
            super().__setitem__(key, value)


class MultipleMeta(type):
    '''
    Metaclass that allows multiple dispatch of methods.
    '''
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()


class Spam(metaclass=MultipleMeta):

    def bar(self, x:int, y:int):
        print('Bar 1:', x, y)

    def bar(self, s:str, n:int = 0):
        print('Bar 2:', s, n)


# Example: overloaded __init__
import time

class Date(metaclass=MultipleMeta):
    def __init__(self, year:int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)


if __name__ == '__main__':
    s = Spam()
    s.bar(2, 3)
    s.bar('hello')
    s.bar('hello', 5)
    try:
        s.bar(2, 'hello')
    except TypeError as e:
        print(e)

    # Overloaded __init__
    d = Date(2012, 12, 21)
    print(d.year, d.month, d.day)
    # Get today's date
    e = Date()
    print(e.year, e.month, e.day)
