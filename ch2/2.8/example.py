#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You’re trying to match a block of text using a regular expression, but you need
the match to span multiple lines.
"""


"""
SOLUTION
"""

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */
        '''
print(comment.findall(text1))
print(comment.findall(text2))

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))


"""
DISCUSSION
"""

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
