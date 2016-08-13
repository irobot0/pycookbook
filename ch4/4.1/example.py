#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to process items in an iterable, but for whatever reason, you can’t or
don’t want to use a for loop.
"""


"""
SOLUTION
"""

with open('example.py') as f:
    try:
        while True:
            line = next(f)
            print(line)
    except StopIteration:
        pass


with open('example.py') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line)


"""
DISCUSSION
"""

items = [1, 2, 3]

# Get the iterator
it = iter(items)

# Run the iterator
print(next(it))
print(next(it))
print(next(it))
print(next(it))
