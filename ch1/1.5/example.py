#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to implement a queue that sorts items by a given priority and always
returns the item with the highest priority on each pop operation.
"""


"""
SOLUTION
"""

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index = self._index + 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':

    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


    """
    DISCUSSION
    """

    # instances of Item class can not be ordered
    # a = Item('foo')
    # b = Item('bar')
    # print(a < b)

    # the (priority, item) tuples are comparable as long as the priorities are
    # different.
    a = (1, Item('foo'))
    b = (5, Item('bar'))
    print(a < b)
    # c = (1, Item('grok'))
    # print(a < c)

    # introduce the extra index to solve the comparison problem
    a = (1, 0, Item('foo'))
    b = (5, 1, Item('bar'))
    c = (1, 2, Item('grok'))
    print(a < b)
    print(a < c)
