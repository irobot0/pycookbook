#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to define a function or method where one or more of the arguments are
optional and have a default value.
"""


"""
SOLUTION
"""

def spam1(a, b=42):
    print(a, b)

spam1(1)
spam1(1, 2)

# Using a list as a default value
def spam2(a, b=None):
    if b is None:
        b = []
    print(a, b)

spam2(1)
spam2(1, 2)

_no_value = object()

def spam3(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print(a, b)

spam3(1)
spam3(1, 2)
spam3(1, None)


"""
DISCUSSION
"""

x = 42
def spam4(a, b=x):
    print(a, b)

spam4(1)
x = 23
spam4(1)


def spam5(a, b=[]):
    print(b)
    return b

x = spam5(1)
print(x)
x.append(99)
x.append('Yow!')
print(x)
spam5(1)


def spam6(a, b=None):
    if not b:       # NO! Use 'b is None' instead
        b = []
    print(a, b)

spam6(1)
x = []
spam6(1, x)         # Silent error. x value overwritten by default
spam6(1, 0)         # Silent error. 0 ignored
spam6(1, '')        # Silent error. '' ignored
