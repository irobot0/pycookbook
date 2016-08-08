#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to strip unwanted characters, such as whitespace, from the beginning,
end, or middle of a text string.
"""


"""
SOLUTION
"""

# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))


"""
DISCUSSION
"""

s = '  hello      world  \n'
s = s.strip()
print(s)
print(s.replace(' ', ''))

import re
print(re.sub('\s+', ' ', s))

filename = 'example.py'
with open(filename) as f:
    lines = (line.rstrip() for line in f)
    for line in lines:
        print(line)
