#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

Instead of iterating over a file by lines, you want to iterate over a collection
of fixed- sized records or chunks.
"""


"""
SOLUTION
"""

from functools import partial

RECORD_SIZE = 1

with open('somefile.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    bindata = bytearray()
    textresult = []
    for r in records:
        bindata = bindata + r
    textresult = bindata.decode('utf-8')
    print(textresult)
