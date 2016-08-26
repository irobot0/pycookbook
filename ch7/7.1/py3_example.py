#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to write a function that accepts any number of input arguments.
"""


"""
SOLUTION
"""

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2, 3, 4))


import html

def make_element(name, value, **attrs):
    keyvals = [ '%s=%s' % item for item in attrs.items() ]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element

# Example
# Create '<item size="large" quantity="6">Albatross</item>'
elem_1 = make_element('item', 'Albatross', size='large', quantity=6)
print(elem_1)

# Creates '<p>&lt;spam&gt;</p>'
elem_2 = make_element('p', '<spam>')
print(elem_2)

def anyargs(*args, **kwargs):
    print(args)     # A tuple
    print(kwargs)   # A dict


"""
DISCUSSION
"""

def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass
