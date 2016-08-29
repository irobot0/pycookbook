#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement a custom class that mimics the behavior of a common
built-in container type, such as a list or dictionary. However, you’re not
entirely sure what methods need to be implemented to do it.
"""


"""
DISCUSSION
"""

import collections
import bisect


class SortedItems(collections.Sequence):

    def __init__(self, initial=None):
        if initial is None:
            self._items = []
        else:
            self._items = sorted(initial)

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(list(items))
print(items[0])
print(items[-1])
print(items.add(2))
print(items.add(-10))
print(list(items))
print(items[1:4])
print(3 in items)
print(len(items))

for n in items:
    print(n)

print('')


"""
DISCUSSION
"""

items = SortedItems()

print(isinstance(items, collections.Iterable))
print(isinstance(items, collections.Sequence))
print(isinstance(items, collections.Container))
print(isinstance(items, collections.Sized))
print(isinstance(items, collections.Mapping))
print('')


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        if initial is None:
            self._items = []
        else:
            self._items = list(initial)

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting: ', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting: ', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting: ', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting: ', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Length')
        return len(self._items)


a = Items([1, 2, 3])
print(len(a))
print('')
a.append(4)
a.append(2)
print('')
a.count(2)
print('')
a.remove(3)
