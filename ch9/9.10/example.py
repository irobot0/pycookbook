#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to apply a decorator to a class or static method.
"""


"""
DISCUSSION
"""

import time
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapse = end - start
        print(elapse)
        return result
    return wrapper


# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n = n - 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n = n - 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n = n - 1

if __name__ == '__main__':
    s = Spam()
    s.instance_method(1000000)
    Spam.class_method(1000000)
    Spam.static_method(1000000)
