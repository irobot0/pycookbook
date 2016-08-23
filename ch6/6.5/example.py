#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to take the data in a Python dictionary and turn it into XML.
"""


"""
SOLUTION
"""

from xml.etree.ElementTree import Element


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key-value pairs into XML
    '''
    elem = Element(tag)
    for key, value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem

s = {
    'name'      : 'GOOG',
    'shares'    : 100,
    'price'     : 490.1
}

e = dict_to_xml('stock', s)
print(e)


from xml.etree.ElementTree import tostring

print(tostring(e))

e.set('_id', '1234')
print(tostring(e))


"""
DISCUSSION
"""

from xml.sax.saxutils import escape
from xml.sax.saxutils import unescape
escaped_val = escape('<spam>')
print(escaped_val)
unescaped_val = unescape(escaped_val)
print(unescaped_val)
