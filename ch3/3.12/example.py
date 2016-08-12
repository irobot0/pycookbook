#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have code that needs to perform simple time conversions, like days to
seconds, hours to minutes, and so on.
"""


"""
SOLUTION
"""

from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
print((a - b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)


"""
DISCUSSION
"""

a = datetime(2012, 9, 23)
from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))

# Time between two dates
b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d)
print(d.months)
print(d.days)
