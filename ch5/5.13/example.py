#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to get a list of the files contained in a directory on the filesystem.
"""


"""
SOLUTION
"""

PUBLIC_DIR = '/Users/Lawrence/Public'

import os

names = os.listdir(PUBLIC_DIR)
print(names)

import os.path

# Get all regular files
names = [name for name in os.listdir(PUBLIC_DIR)
         if os.path.isfile(os.path.join(PUBLIC_DIR, name))]
print(names)

# Get all dirs
dirnames = [name for name in os.listdir(PUBLIC_DIR)
            if os.path.isdir(os.path.join(PUBLIC_DIR, name))]
print(dirnames)

pyfiles = [name for name in os.listdir(PUBLIC_DIR)
           if name.endswith('.py')]
print(pyfiles)

import glob
pyfiles = glob.glob(PUBLIC_DIR + '/*.py')
print(pyfiles)

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir(PUBLIC_DIR)
           if fnmatch(name, '*.py')]
print(pyfiles)


"""
DISCUSSION
"""

# Example of getting a directory listing

pyfiles = glob.glob(PUBLIC_DIR + '/*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]

for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
