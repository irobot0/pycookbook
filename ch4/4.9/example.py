#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to iterate over all of the possible combinations or permutations of a
collection of items.
"""


"""
SOLUTION
"""

items = ['a', 'b', 'c']

from itertools import permutations

for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)


from itertools import combinations
from itertools import combinations_with_replacement

for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

for c in combinations(items, 1):
    print(c)

for c in combinations_with_replacement(items, 3):
    print(c)
