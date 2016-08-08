#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to replace HTML or XML entities such as &entity; or &#code; with their
corresponding text. Alternatively, you need to produce text, but escape certain
characters (e.g., <, >, or &).
"""


"""
SOLUTION
"""

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
