#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to return multiple values from a function.
"""


"""
SOLUTION
"""

def myfun():
    return 1, 2, 3

a, b, c = myfun()

print(a)
print(b)
print(c)


"""
DISCUSSION
"""

a = (1, 2)
print(a)

b = 1, 2
print(b)

x = myfun()
print(x)
