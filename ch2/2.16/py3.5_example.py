#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You have long strings that you want to reformat so that they fill a
user-specified number of columns.
"""


"""
SOLUTION
"""

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))


"""
DISCUSSION
"""
import os
print(os.get_terminal_size().columns)
