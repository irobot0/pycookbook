#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to iterate over a sequence, but would like to keep track of which
element of the sequence is currently being processed.
"""


"""
SOLUTION
"""

my_list = ['a', 'b', 'c']

for index, value in enumerate(my_list):
    print(index, value)

for index, value in enumerate(my_list, 1):
    print(index, value)


def parse_date(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


from collections import defaultdict

word_summary = defaultdict(list)
with open('example.py', 'r') as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(index)


"""
DISCUSSION
"""

data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

for n, (x, y) in enumerate(data):
    print(n, (x, y))
