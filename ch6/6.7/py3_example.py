#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to parse an XML document, but it’s using XML namespaces.
"""


"""
SOLUTION
"""

from xml.etree.ElementTree import parse


class XMLNamespace:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


doc = parse('sample.xml')

ns = XMLNamespace(html='http://www.w3.org/1999/xhtml')

e = doc.find(ns('content/{html}html'))
print(e)

text = doc.findtext(ns('content/{html}html/{html}head/{html}title'))
print(text)


"""
DISCUSSION
"""

from xml.etree.ElementTree import iterparse

for event, element in iterparse('sample.xml', ('end', 'start-ns', 'end-ns')):
    print(event, element)
