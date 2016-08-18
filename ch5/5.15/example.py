#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

Your program received a directory listing, but when it tried to print the
filenames, it crashed with a UnicodeEncodeError exception and a cryptic message
about “surrogates not allowed.”
"""


"""
SOLUTION
"""

def bad_filename(filename):
    return repr(filename)[1:-1]

import os

files = os.listdir('.')

print(files)

for name in files:
    print(name)

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))

def bad_filename_improved(filename):
    temp = filename.encode(sys.getfilesystemencoding(),
                           errors='surrogateescape')
    return temp.decode('latin-1')

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename_improved(name))
