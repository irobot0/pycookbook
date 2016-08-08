#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to combine many small strings together into a larger string.
"""


"""
SOLUTION
"""

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
c = 'I have no idea.'
print(a + ' ' + b)
print('{} {}'.format(a, b))
print(a + ' ' + b)

a = 'Hello' 'World'
print(a)


"""
DISCUSSION
"""

data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

print(a + ':' + b + ':' + c)    # ugly
print(':'.join([a, b, c]))      # still ugly
print(a, b, c, sep=':')         # better

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())

# for part in sample():
#     f.write(part)
#
# def combine(source, maxsize):
#     parts = []
#     size = 0
#     for part in source:
#         parts.append(part)
#         size = size + len(part)
#         if size > maxsize:
#             yield ''.join(parts)
#             parts = []
#             size = 0
#         yield ''.join(parts)
#
# for part in combine(sample(), 32768):
#     f.write(part)
