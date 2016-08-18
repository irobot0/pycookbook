#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to create a temporary file or directory for use when your program
executes. Afterward, you possibly want the file or directory to be destroyed.
"""


"""
SOLUTION
"""

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/Write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
# Temporary file is destroyed

f = TemporaryFile('w+t')
# Use the temporary file

f.close()
# File is destroyed


from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
# File automatically destroyed

with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory
# Directory and all contents destroyed


"""
DISCUSSION
"""

import tempfile
print(tempfile.mkstemp())
print(tempfile.mkdtemp())

print(tempfile.gettempdir())
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
print(f.name)
