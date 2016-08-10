#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You need to convert or output integers represented by binary, octal, or
hexadecimal digits.
"""


"""
SOLUTION
"""

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

x = -1234
print(format(x, 'b'))
print(format(x, 'x'))

x = -1234
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))

print(int('4d2', 16))
print(int('10011010010', 2))


"""
DISCUSSION
"""

import os
os.chmod('example.py', 0o755)
