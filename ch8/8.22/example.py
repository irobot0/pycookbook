#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

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

import types


class Node(object):
    pass


class NodeVisitor(object):
    def visit(self, node):
        stack = [ node ]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self, node):
        methodname = 'visit_' + type(node).__name__
        method = getattr(self, methodname, None)
        if method is None:
            method = self.generic_visit
        return method(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


# A sample visitor class that evaluate expressions
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        # print('Add:', node)
        # lhs = yield node.left
        # print('left=', lhs)
        # rhs = yield node.right
        # print('right=', rhs)
        # yield lhs + rhs
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield -(yield node.operand)


if __name__ == '__main__':
    # Representation of 1 + 2 * (3 - 4) / 5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)

    e = Evaluator()
    result = e.visit(t4)
    print(result)
    print('')

    a = Number(0)
    for n in range(1, 100000):
        a = Add(a, Number(n))
    e = Evaluator()
    result = e.visit(a)
    print(result)
