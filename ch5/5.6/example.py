#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to feed a text or binary string to code that’s been written to operate
on file- like objects instead.
"""


"""
SOLUTION
"""

from io import StringIO
from io import BytesIO

s = StringIO()
s.write('Hello World\n')

print('This is a test', file=s)

# Get all of the data written so far
print(s.getvalue())

# Wrap a file interface around an existing string
s = StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

# Handling binary data with io.BytesIO
s = BytesIO()
s.write(b'binary data')
print(s.getvalue())
