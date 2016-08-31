#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to change the way in which instances are created in order to implement
singletons, caching, or other similar features.

"""


"""
SOLUTION
"""


class Spam:
    def __init__(self, name):
        self.name = name

a = Spam('Guido')
b = Spam('Diana')


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly.")


# Example
class Spam2(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam2.grok')

Spam2.grok(42)
# s = Spam2()
print('')


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam3(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam3')

a = Spam3()
b = Spam3()
print(a is b)
c = Spam3()
print(a is c)
print('')


import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
        return obj


# Example
class Spam4(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam4({!r})'.format(name))
        self.name = name

a = Spam4('Guido')
b = Spam4('Diana')
c = Spam4('Guido')
print(a is b)
print(a is c)
print('')


"""
DISCUSSION
"""


class _Spam5:
    def __init__(self):
        print('Creating Spam5')

_spam_instance = None


def Spam5():
    global _spam_instance
    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam5()
        return _spam_instance


a = Spam5()
b = Spam5()
c = Spam5()
print(a is b)
print(a is c)
