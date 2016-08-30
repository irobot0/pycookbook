#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

When creating instances of a class, you want to return a cached reference to a
previous instance created with the same arguments (if any).
"""


"""
SOLUTION
"""

import logging

a = logging.getLogger('foo')
b = logging.getLogger('bar')

print(a is b)

c = logging.getLogger('foo')

print(a is c)
print('')


# The class in question
class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
import weakref

_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name in _spam_cache:
        s = _spam_cache[name]
    else:
        s = Spam(name)
        _spam_cache[name] = s
    return s

a = get_spam('foo')
b = get_spam('bar')
print(a is b)

c = get_spam('foo')
print(a is c)
print('')


"""
DISCUSSION
"""

a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')

print(list(_spam_cache))
del a
del c
print(list(_spam_cache))
del b
print(list(_spam_cache))
