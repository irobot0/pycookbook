#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have a collection of sorted sequences and you want to iterate over a sorted
sequence of them all merged together.
"""


"""
SOLUTION
"""

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)
