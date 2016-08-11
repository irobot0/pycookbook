#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to perform matrix and linear algebra operations, such as matrix
multiplication, finding determinants, solving linear equations, and so on.
"""


"""
SOLUTION
"""

import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)

# Return transpose
print(m.T)

# Return inverse
print(m.I)

# Create a vector and multiply
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)

import numpy.linalg

# Determinant
print(numpy.linalg.det(m))

# Eigenvalues
print(numpy.linalg.eigvals(m))

# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
print(x)

print(m * x)
print(v)
