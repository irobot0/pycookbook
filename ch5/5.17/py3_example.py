#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to write raw bytes to a file opened in text mode.
"""


"""
SOLUTION
"""

import sys
sys.stdout.buffer.write(b'Hello\n')
