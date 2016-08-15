#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to write data to a file, but only if it doesn’t already exist on the
filesystem.
"""


"""
SOLUTION
"""

# with open('somefile', 'wt') as f:
#     f.write('Hello\n')

with open('somefile', 'xt') as f:
    f.write('Hello\n')


"""
DISCUSSION
"""

import os

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')
