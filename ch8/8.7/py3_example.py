#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to invoke a method in a parent class in place of a method that has been
overridden in a subclass.
"""


"""
SOLUTION
"""


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()      # Call parent's spam()


class A2:
    def __init__(self):
        self.x = 0


class B2(A2):
    def __init__(self):
        super().__init__()
        self.y = 1


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)    # Call original __setattr__
        else:
            setattr(self._obj, name, value)


"""
DISCUSSION
"""

class Base:
    def __init__(self):
        print('Base.__init__')


class A3(Base):
    def __init__(self):
        Base.__init__(self)
        print('A3.__init__')


class Base2:
    def __init__(self):
        print('Base2.__init__')


class A4(Base2):
    def __init__(self):
        Base2.__init__(self)
        print('A4.__init__')

class B4(Base2):
    def __init__(self):
        Base2.__init__(self)
        print('B4.__init__')


class C4(A4, B4):
    def __init__(self):
        A4.__init__(self)
        B4.__init__(self)
        print('C4.__init__')

c = C4()
print('')


class Base3:
    def __init__(self):
        print('Base3.__init__')


class A5(Base3):
    def __init__(self):
        super().__init__()
        print('A5.__init__')

class B5(Base3):
    def __init__(self):
        super().__init__()
        print('B5.__init__')


class C5(A5, B5):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C5.__init__')


c = C5()
print(C5.__mro__)
print('')


class A6:
    def spam(self):
        print('A.spam')
        super().spam()

a = A6()
# a.spam()
print('')


class B6:
    def spam(self):
        print('B.spam')


class C6(A6, B6):
    pass

c = C6()
c.spam()
print(C6.mro)
print('')
