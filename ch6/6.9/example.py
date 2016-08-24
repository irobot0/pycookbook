#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to decode a string of hexadecimal digits into a byte string or encode
a byte string as hex.
"""


"""
SOLUTION
"""

# Initial byte string
s = b'hello'

# Encode as hex
import binascii
h = binascii.b2a_hex(s)
print(h)

# Decode back to bytes
b = binascii.a2b_hex(h)
print(b)

# The same functionality in module base64
import base64
h = base64.b16encode(s)
print(h)

b = base64.b16decode(h)
print(b)


"""
DISCUSSION
"""

h = base64.b16encode(s)
print(h)
print(h.decode('ascii'))
