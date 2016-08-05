#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You have two dictionaries and want to find out what they might have in common
(same keys, same values, etc.)
"""


"""
SOLUTION
"""

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# Find keys in common
print(a.viewkeys() & b.viewkeys()) # set(['x', 'y'])

# Find keys in a that are not in b
print(a.viewkeys() - b.viewkeys()) # set(['z'])

# Find (key, value) pairs in common
print(a.viewitems() & b.viewitems()) # set([('y', 2)])

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.viewkeys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
print(c)
