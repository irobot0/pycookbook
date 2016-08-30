#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to write a decorator function that wraps a function, but has user
adjustable attributes that can be used to control the behavior of the decorator
at runtime.
"""


"""
DISCUSSION
"""

from functools import wraps
from functools import partial
import logging


# Utility decorator to attach a function as an attribute of object
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    else:
        setattr(obj, func.__name__, func)
        return func


def logged(level, name=None, message=None):
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


"""
DISCUSSION
"""

import time


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
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n = n - 1

@logged(logging.DEBUG)
@timethis
def countdown2(n):
    while n > 0:
        n = n - 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    add(2, 3)
    print('')

    # Change the log message.
    add.set_message('Add called')
    add(2, 3)
    print('')

    # Change the log level.
    add.set_level(logging.WARNING)
    add(2, 3)
    print('')

    # The accessor function can propagate across multiple level of decorators.
    countdown(1000000)
    countdown.set_level(logging.WARNING)
    countdown.set_message('Counting down to zero')
    countdown(1000000)
    print('')

    # The order of decorators does not affect the behavior of accessor
    # functions.
    countdown2(1000000)
    countdown2.set_level(logging.WARNING)
    countdown2.set_message('Counting down to zero')
    countdown2(1000000)
