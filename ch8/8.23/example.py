#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’re writing code that navigates through a deeply nested tree structure using
the visitor pattern, but it blows up due to exceeding the recursion limit.
You’d like to eliminate the recursion, but keep the programming style of the
visitor pattern.
"""


"""
SOLUTION
"""


import weakref


class Node(object):
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        if self._parent is None:
            return None
        else:
            return self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
del root
print(c1.parent)
print('')


"""
DISCUSSION
"""


# Class just to illustrate when deletion occurs.
class Data2(object):
    def __del__(self):
        print('Data2.__del__')


# Node class involving a cycle.
class Node2(object):
    def __init__(self):
        self.data = Data2()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data2()
del a       # Immediately deleted
a = Node2()
del a       # Immediately deleted
a = Node2()
a.add_child(Node2())
del a


import gc
gc.collect()    # Force collection
print('')


# Class just to illustrate when deletion occurs.
class Data3(object):
    def __del__(self):
        print('Data3.__del__')


# Node class involving a cycle.
class Node3(object):
    def __init__(self):
        self.data = Data3()
        self.parent = None
        self.children = []

    # NEVER DEFINE LIKE THIS.
    # Only here to illustrate pathological behavior.
    def __del__(self):
        del self.data
        del self.parent
        del self.children

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Node3()
a.add_child(Node3())
del a           # No message (not collected)
gc.collect()    # No message (not collected)
print('')


a = Node(2016)
a_ref = weakref.ref(a)
print(a_ref)

print(a_ref())
del a
print(a_ref())
