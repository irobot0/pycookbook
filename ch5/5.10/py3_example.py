#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to memory map a binary file into a mutable byte array, possibly for
random access to its contents or to make in-place modifications.
"""


"""
SOLUTION
"""

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])

# Reassign a slice
m[0:11] = b'Hello World'
m.close()

# Verify that changes were made
with open('data', 'rb') as f:
    print(f.read(11))

with memory_map('data') as m:
    print(len(m))
    print(m[0:10])

print(m.closed)


"""
DISCUSSION
"""

m = memory_map('data')

# Memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
