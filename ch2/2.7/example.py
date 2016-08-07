#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You’re trying to match a text pattern using regular expressions, but it is
identifying the longest possible matches of a pattern. Instead, you would like
to change it to find the shortest possible match.
"""


"""
SOLUTION
"""

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
