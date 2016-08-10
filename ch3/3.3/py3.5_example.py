#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You need to format a number for output, controlling the number of digits,
alignment, inclusion of a thousands separator, and other details.
"""


"""
SOLUTION
"""

x = 1234.56789

# Two decimal places of accuracy
print(format(x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))

# Left justified
print(format(x, '<10.1f'))

# Centered
print(format(x, '^10.1f'))

# Inclusion of thousands separator
print(format(x, ','))
print(format(x, '0,.1f'))

# Scientific notation
print(format(x, 'e'))
print(format(x, '0.2E'))

print('THe value is {:0,.2f}'.format(x))


"""
DISCUSSION
"""

print(x)
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

swap_separators = {
    ord('.') : ',',
    ord(',') : '.'
}

print(format(x, ',').translate(swap_separators))

print('%0.2f' % x)
print('%10.1f' % x)
print('%-10.1f' % x)
