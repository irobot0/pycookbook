#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have code that uses a while loop to iteratively process data because it
involves a function or some kind of unusual test condition that doesn’t fall
into the usual iteration pattern.
"""


"""
SOLUTION
"""

import sys

f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), b''):
    n = sys.stdout.write(chunk)
