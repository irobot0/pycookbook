#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’ve written a function, but would like to attach some additional information
to the arguments so that others know more about how a function is supposed to be
used.
"""


"""
SOLUTION
"""

def add(x:int, y:int) -> int:
    return x + y

print(help(add))


"""
DISCUSSION
"""

print(add.__annotations__)
