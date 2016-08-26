#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want a function to only accept certain arguments by keyword.
"""


"""
SOLUTION
"""

def recv(maxsize, *, block):
    '''
    Receives a message
    '''
    pass

recv(1024, block=True)

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        if clip > m:
            m = clip
    return m

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))


"""
DISCUSSION
"""

print(help(recv))
