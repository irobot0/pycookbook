#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to add or change the Unicode encoding of an already open file without
closing it first.
"""


"""
SOLUTION
"""

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

import sys
print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)


"""
DISCUSSION
"""

f = open('sample.txt', 'w')
print(f)
print(f.buffer)
print(f.buffer.raw)

f = io.TextIOWrapper(f.buffer, encoding='latin-1')
print(f)

f = open('sample.txt', 'w')
print(f)
b = f.detach()
print(b)
f = io.TextIOWrapper(b, encoding='latin-1')
print(f)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                              errors='xmlcharrefreplace')
print('Jalape\u00f1o')
