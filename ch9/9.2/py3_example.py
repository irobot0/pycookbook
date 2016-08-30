#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’ve written a decorator, but when you apply it to a function, important
metadata such as the name, doc string, annotations, and calling signature are
lost.
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
def countdown(n:int):
    '''
    Counts down
    '''
    original_n = n
    while n > 0:
        n = n - 1
    print('Finished counting down {}'.format(original_n))


if __name__ == '__main__':
    countdown(100000)
    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)

    countdown.__wrapped__(100000)

    from inspect import signature
    print(signature(countdown))
