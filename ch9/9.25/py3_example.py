#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to know in detail what your code is doing under the covers by
disassembling it into lower-level byte code used by the interpreter.
"""


"""
SOLUTION
"""

import opcode


def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i = i + 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i+1]*256 + extended_arg
            extended_arg = 0
            i = i + 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
            else:
                oparg = None
            yield (op, oparg)


# Example
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n = n - 1
    print('Blastoff!')


for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)
