#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to perform common text operations (e.g., stripping, searching, and
replacement) on byte strings.
"""


"""
SOLUTION
"""

data = b'Hello World'
print(data[0:5])

print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = b'FOO:BAR,SPAM'
import re
print(re.split(b'[:,]', data))  # Notice: pattern as bytes


"""
DISCUSSION
"""

a = 'Hello World'
print(a[0])
print(a[1])
b = b'Hello World'
print(b[0])
print(b[1])

s = b'Hello World'
print(s)
print(s.decode('ascii'))

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing
import os
print(os.listdir('.'))
print(os.listdir(b'.'))
