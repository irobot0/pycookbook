#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to write a decorator that adds an extra argument to the calling
signature of the wrapped function. However, the added argument can’t interfere
with the existing calling conventions of the function.
"""


"""
DISCUSSION & DESCUSSION
"""

from functools import wraps
import inspect


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')
    else:
        @wraps(func)
        def wrapper(*args, debug=False, **kwargs):
            if debug:
                print('Calling', func.__name__)
            return func(*args, **kwargs)
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        params.append(inspect.Parameter('debug',
                                        inspect.Parameter.KEYWORD_ONLY,
                                        default=False))
        wrapper.__signature__ = sig.replace(parameters=params)
        return wrapper


@optional_debug
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(inspect.signature(add))
    print(add(2, 3))
