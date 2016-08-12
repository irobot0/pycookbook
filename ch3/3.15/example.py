#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

Your application receives temporal data in string format, but you want to
convert those strings into datetime objects in order to perform nonstring
operations on them.
"""


"""
SOLUTION
"""

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)


"""
DISCUSSION
"""

print(z)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
