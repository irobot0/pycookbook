#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to unpack N elements from an iterable, but the iterable may be longer
than N elements, causing a "too many values to unpack" exception.
"""


"""
SOLUTION
"""

def avg(items):
    return sum(items) / len(items)

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing, current = sales_record
print(trailing)
print(current)
trailing_avg = avg(trailing)
print(trailing_avg)


"""
DISCUSSION
"""

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
