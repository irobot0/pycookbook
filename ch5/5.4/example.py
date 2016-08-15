#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to read or write binary data, such as that found in images, sound
files, and so on.
"""


"""
SOLUTION
"""

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()
    print(data.decode('utf-8'))


"""
DISCUSSION
"""

# Text string
t = 'Hello World'
print(t[0])

for c in t:
    print(c)


# Byte string
b = b'Hello World'
print(b[0])

for c in b:
    print(c)

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    print(text)

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))


import array

nums = array.array('i', [1, 2, 3, 4])

with open('data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])

with open('data.bin', 'rb') as f:
    f.readinto(a)

print(a)
