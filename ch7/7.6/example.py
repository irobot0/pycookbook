#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to supply a short callback function for use with an operation such as
sort(), but you don’t want to write a separate one-line function using the def
statement. Instead, you’d like a shortcut that allows you to specify the
function “in line.”
"""


"""
SOLUTION
"""

add = lambda x, y: x + y
print(add(2, 3))
print(add('hello', 'world'))

def add2(x, y):
    return x + y

print(add2(2, 3))

names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
sorted_names = sorted(names, key=lambda name:name.split()[-1].lower())
print(sorted_names)
