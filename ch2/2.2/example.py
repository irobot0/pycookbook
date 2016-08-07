#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You need to check the start or end of a string for specific text patterns, such
as filename extensions, URL schemes, and so on.
"""


"""
SOLUTION
"""

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

import os
filename = os.listdir('.')
print(filename)
print([name for name in filename if name.endswith(('.py', '.txt', ))])
print(any(name.endswith('.py') for name in filename))

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# Both str.startswith() and str.endswith() expect their first args to be str,
# unicode, or tuple, not list
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# url.startswith(choices)
url.startswith(tuple(choices))


"""
DISCUSSION
"""

filename = 'spam.txt'
print(filename[-4:] == '.txt')

url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))
