#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to iterate over items in an iterable, but the first few items aren’t of
interest and you just want to discard them.
"""


"""
SOLUTION
"""

with open('example.py') as f:
    for line in f:
        print(line)

from itertools import dropwhile
with open('example.py') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line)

from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]

for x in islice(items, 3, None):
    print(x)


"""
DISCUSSION
"""

with open('example.py') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    try:
        while line:
            # Replace with useful processing
            print(line)
            line = next(f)
    except StopIteration:
        pass

with open('example.py') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line)
