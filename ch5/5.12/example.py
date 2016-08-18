#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to test whether or not a file or directory exists.
"""


"""
SOLUTION
"""

import os

print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))

# Is a regular file
print(os.path.isfile('/etc/passwd'))

# Is a directory
print(os.path.isdir('/etc/passwd'))

# Is a symbolic link
print(os.path.islink('/usr/local/bin/python3'))

# Get the file linked to
print(os.path.realpath('/usr/local/bin/python3'))

print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))

import time
print(time.ctime(os.path.getmtime('/etc/passwd')))
