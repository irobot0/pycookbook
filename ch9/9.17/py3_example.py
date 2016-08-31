#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

Your program consists of a large class hierarchy and you would like to enforce
certain kinds of coding conventions (or perform diagnostics) to help maintain
programmer sanity.
"""


"""
SOLUTION
"""

from inspect import signature
import logging


class MatchSignatureMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        super_classes = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            else:
                # Get the previous definition (if any) and compare the signatures
                prev_def = getattr(super_classes, name, None)
                if prev_def is not None:
                    prev_sig = signature(prev_def)
                    val_sig = signature(value)
                    if prev_sig != val_sig:
                        logging.warning(
                            'Signature mismatch in {}. {} != {}'.format(value.__qualname__,
                                                                        prev_sig,
                                                                        val_sig))


# Example
class Root(metaclass=MatchSignatureMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass


def spam(self, x, *, z):
    pass


# Class with redefined methods, but slightly different signatures
class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass
