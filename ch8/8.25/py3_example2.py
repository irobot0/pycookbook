#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

When creating instances of a class, you want to return a cached reference to a
previous instance created with the same arguments (if any).
"""


"""
DISCUSSION
"""

# Note: This code doesn't quite work
import weakref

class Spam:

    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


if __name__ == '__main__':
    s = Spam('Dave')
    t = Spam('Dave')
    print(s is t)
