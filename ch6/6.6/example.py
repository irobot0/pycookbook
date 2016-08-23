#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to read an XML document, make changes to it, and then write it back
out as XML.
"""


"""
SOLUTION
"""

from xml.etree.ElementTree import parse
from xml.etree.ElementTree import Element

doc = parse('pred.xml')
root = doc.getroot()
print(root)

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>...</nm>
elem_nm = root.find('nm')
index_elem_nm = root.getchildren().index(elem_nm)
print(index_elem_nm)

e = Element('spam')
e.text = 'This is a test'
root.insert(index_elem_nm+1, e)

# Write back to a file
doc.write('newpred.xml', xml_declaration=True)
