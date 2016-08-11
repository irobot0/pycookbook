#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

Your code for interacting with the latest web authentication scheme has
encountered a singularity and your only solution is to go around it in the
complex plane. Or maybe you just need to perform some calculations using complex
numbers.
"""


"""
SOLUTION
"""

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

print(a.real)
print(a.imag)
print(a.conjugate())

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

import cmath
cmath.sin(a)
cmath.cos(a)
cmath.exp(a)


"""
DISCUSSION

Notice: Please ensure you have the numpy module install (sudo pip install numpy)
before running the following codes.
"""

import numpy as np

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)

print(a + 2)
print(np.sin(a))

print(cmath.sqrt(-1))
