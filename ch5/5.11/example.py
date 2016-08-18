#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to manipulate pathnames in order to find the base filename, directory
name, absolute path, and so on.
"""


"""
SOLUTION
"""

import os

path = '/Users/Lawrence/Public/data.csv'

# Get the last component of the path
print(os.path.basename(path))

# Get the directory name
print(os.path.dirname(path))

# Join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))

# Expand the user's home directory
path = '~/Public/data.csv'
print(os.path.expanduser(path))

# Split the file extension
print(os.path.splitext(path))
