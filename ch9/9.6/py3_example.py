#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You would like to write a single decorator that can be used without arguments,
such as @decorator, or with optional arguments, such as @decorator(x,y,z).
However, there seems to be no straightforward way to do it due to differences
in calling conventions between simple decorators and decorators taking arguments.
"""


"""
DISCUSSION
"""

from functools import wraps
from functools import partial
import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    else:
        if name is not None:
            logname = name
        else:
            logname = func.__module__

        log = logging.getLogger(logname)

        if message is not None:
            logmsg = message
        else:
            logmsg = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper


# Example use
@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')
