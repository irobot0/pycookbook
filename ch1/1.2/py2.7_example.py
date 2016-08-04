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
    # index of the last item: -1
    first, middle, last = grades[0], grades[1:-1], grades[-1]
    return avg(middle)

items = [10, 8, 7, 1, 9, 5, 10, 3]
print(drop_first_last(items))

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, phone_numbers = record[0], record[1], record[2:]
print(name)
print(email)
print(phone_numbers)

sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
trailing, current = sales_record[:-1], sales_record[-1]


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

for record in records:
    tag = record[0]
    args = record[1:]
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
items = line.split(':')
uname, fields, homedir, sh = items[0], items[:-2], items[-2], items[-1]
print(uname)
print(fields)
print(homedir)
print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, _, date_record = record[0], record[1:-1], record[-1]
_, year = date_record[:-1], date_record[-1]
print(name)
print(year)

items = [1, 10, 7, 4, 5, 9]
head, tail = items[0], items[1:]
print(head)
print(tail)

def sum(items):
    head, tail = items[0], items[1:]
    return head + sum(tail) if tail else head

print(sum(items))
