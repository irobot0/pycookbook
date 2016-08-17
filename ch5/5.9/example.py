#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to read binary data directly into a mutable buffer without any
intermediate copying. Perhaps you want to mutate the data in-place and write it
back out to a file.
"""


"""
SOLUTION
"""

import os

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# Write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)

buf[0:5] = b'Hallo'
print(buf)

with open('newsample.bin', 'wb') as f:
    f.write(buf)


"""
DISCUSSION
"""

record_size = 32 # Size of each record (adjust value)

buf = bytearray(record_size)
with open('sample.bin', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the contents of buf
        # ...

print(buf)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)
