#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to redirect the output of the print() function to a file.
"""


"""
SOLUTION
"""

with open('sample.txt', 'wt') as f:
    print('Hello World!', file=f)
