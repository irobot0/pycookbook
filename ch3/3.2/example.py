#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You need to perform accurate calculations with decimal numbers, and don’t want
the small errors that naturally occur with floats.
"""


"""
SOLUTION
"""

a = 4.2
b = 2.1
print(a + b)
print(a + b == 6.3)

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print(a + b == Decimal('6.3'))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / 6)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)


"""
DISCUSSION
"""

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))

import math
print(math.fsum(nums))
