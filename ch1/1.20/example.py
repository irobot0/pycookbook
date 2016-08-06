#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You have multiple dictionaries or mappings that you want to logically combine
into a single mapping to perform certain operations, such as looking up values
or checking for the existence of keys.
"""


"""
SOLUTION
"""

a = { 'x' : 1, 'z' : 3 }
b = { 'y' : 2, 'z' : 4 }

try:
    from collections import ChainMap
except ImportError:
    from chainmap import ChainMap

c = ChainMap(a, b)
print(c['x'])   # Output 1 (from a)
print(c['y'])   # Output 2 (from b)
print(c['z'])   # Output 3 (from a)


"""
DISCUSSION
"""

print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 10
del c['x']
print(a)

# Mutation always affect the fist mapping listed, while there is no entry of
# key 'y' in dictionary a
# del c['y']

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# Discard last mapping
values = values.parents
values['x']
# Discard last mapping
values = values.parents
values['x']
print(values)

# Merging dictionaries together using the update() method.
a = { 'x' : 1, 'z' : 3 }
b = { 'y' : 2, 'z' : 4 }
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 13
merged['x']

# Using ChainMap to avoid inconsistency.
a = { 'x' : 1, 'z' : 3 }
b = { 'y' : 2, 'z' : 4 }
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])
