#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to redirect the output of the print() function to a file.
"""


"""
SOLUTION
"""

print('ACME', 50, 91.5)

print('ACME', 50, 91.5, sep=',')

print('ACME', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')

print('')

"""
DISCUSSION
"""

print(','.join(('ACME', '50', '91.5')))

row = ('ACME', 50, 91.5)

print(','.join(str(x) for x in row))

print(*row, sep=',')
