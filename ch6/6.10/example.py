#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to decode or encode binary data using Base64 encoding.
"""


"""
SOLUTION
"""

# Some byte data
s = b'hello'

import base64

# Encode as base64
a = base64.b64encode(s)
print(a)

# Decode from base64
b = base64.b64decode(a)
print(b)


"""
DISCUSSION
"""

a = base64.b64encode(s).decode('ascii')
print(a)
