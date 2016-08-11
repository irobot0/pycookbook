#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to create or test for the floating-point values of infinity, negative
infinity, or NaN (not a number).
"""


"""
SOLUTION
"""

a = float('inf')
b = float('-inf')
c = float('nan')

print(a)
print(b)
print(c)

import math

math.isinf(a)
math.isnan(c)


"""
DISCUSSION
"""

a = float('inf')
print(a + 45)
print(a * 10)
print(10 / a)

a = float('inf')
print(a/a)
b = float('-inf')
print(a + b)

c = float('nan')
print(c + 23)
print(c / 2)
print(c * 2)
math.sqrt(c)

c = float('nan')
d = float('nan')
print(c == d)
print(c is d)
