#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to read or write data in a file with gzip or bz2 compression.
"""


"""
SOLUTION
"""

import gzip
import bz2


# gzip

with gzip.open('somefile.gz', 'wt') as f:
    text = 'Hello World!'
    f.write(text)

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
    print(text)


# bz2

with bz2.open('somefile2.gz', 'wt') as f:
    text = 'Goodbye World!'
    f.write(text)

with bz2.open('somefile2.gz', 'rt') as f:
    text = f.read()
    print(text)


"""
DISCUSSION
"""

with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    text = 'Hello Again!'
    f.write(text)

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
    print(text)

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
    print(text)
