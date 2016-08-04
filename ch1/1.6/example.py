#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to make a dictionary that maps keys to more than one value (a
so-called "multidict")
"""


"""
SOLUTION
"""

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)


"""
DISCUSSION
"""

pairs = [
    ['a', 1],
    ['a', 2],
    ['a', 3],
    ['b', 4],
    ['b', 5]
]

# messy code without using defaultdict
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# a cleaner solution using defaultdict
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)
