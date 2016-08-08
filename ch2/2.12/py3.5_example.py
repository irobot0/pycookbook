#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web
page and you’d like to clean it up somehow.
"""


"""
SOLUTION
"""

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None    # Delete
}

a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)
result = b.translate(cmb_chrs)
print(result)

digitmap = { c : ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd' }

print(len(digitmap))

# Arabic digits
x = '\u0661\u0662\u0663'
x.translate(digitmap)

print(a)
b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')


"""
DISCUSSION
"""

def clean_space(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s
