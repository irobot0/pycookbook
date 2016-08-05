#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to eliminate the duplicate values in a sequence, but preserve the order
of the remaining items.
"""


"""
SOLUTION FOR HASHABLE ELEMENTS
"""

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    print(list(dedupe(a)))
