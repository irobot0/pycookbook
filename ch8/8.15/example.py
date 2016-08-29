#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want an instance to delegate attribute access to an internally held instance
possibly as an alternative to inheritance or in order to implement a proxy.
"""


"""
DISCUSSION
"""


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


class A2:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B2:
    def __init__(self):
        self._a = A2()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        return getattr(self._a, name)

b = B2()
b.bar()     # Calls B.bar() (exists on B)
b.spam(42)  # Calls B.__getattr__('spam') and delegates to A.spam


# A proxy class that wraps around another object, but
# exposees its public attributes

class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr: ', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super(Proxy, self).__setattr__(name, value)
        else:
            print('setattr: ', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super(Proxy, self).__delattr__(name)
        else:
            print('delattr: ', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


# Create an instance
s = Spam(2)

# Create a proxy arount it
p = Proxy(s)

# Access the proxy
print(p.x)      # Outputs 2
p.bar(3)        # Outputs "Spam.bar: 2 3"
p.x = 37        # Changes s.x to 37


"""
DISCUSSION
"""

class A3:
    def spam(self, x):
        print('A3.spam')

    def foo(self):
        print('A3.foo')


class B3(A3):
    def spam(self, x):
        print('B3.spam')
        super().spam(x)

    def bar(self):
        print('B3.bar')


class A4:
    def spam(self, x):
        print('A4.spam', x)

    def foo(self):
        print('A4.foo')


class B4:
    def __init__(self):
        self._a = A4()

    def spam(self, x):
        print('B4.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B4.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)


class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    # Added special methods to support certian list operations
    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]


a = ListLike()
a.append(2)
a.insert(0, 1)
a.sort()
print(a)
print(len(a))
print(a[0])
