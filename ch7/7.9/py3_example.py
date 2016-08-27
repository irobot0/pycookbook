#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have a class that only defines a single method besides __init__(). However,
to simplify your code, you would much rather just have a simple function.
"""


"""
SOLUTION
"""

from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

# Example use. Download stock data from Yahoo.
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))
    
print('')


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

# Example use
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))
