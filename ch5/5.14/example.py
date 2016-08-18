#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to perform file I/O operations using raw filenames that have not been
decoded or encoded according to the default filename encoding.
"""


"""
SOLUTION
"""

import sys

print(sys.getfilesystemencoding())

# Write a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
import os
print(os.listdir('.'))

# Directory listing (raw)
print(os.listdir(b'.'))    # Note: byte string

# Open a file with raw filename
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())
