#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to put a wrapper layer around a function that adds extra processing
(e.g., logging, timing, etc.).
"""


"""
SOLUTION
"""

import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapse = end - start
        print(func.__name__, elapse)
        return result
    return wrapper


@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n = n - 1


if __name__ == '__main__':
    countdown(100000)
    countdown(1000000)
