#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You need to split a string into fields, but the delimiters (and spacing around
them) aren’t consistent throughout the string.
"""


"""
SOLUTION
"""

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))


"""
DISCUSSION
"""

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# Reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values, delimiters)))

print(re.split(r'(?:,|;|\s)\s*', line))
