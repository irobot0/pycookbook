#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You are building custom objects on which you would like to support iteration,
but would like an easy way to implement the iterator protocol.
"""


"""
SOLUTION
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for child in self:
            for grandchild in child.depth_first():
                yield grandchild

    # # For Python 3.3 and above
    # def depth_first(self):
    #     yield self
    #     for c in self:
    #         yield from c.depth_first()


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    # Output Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
