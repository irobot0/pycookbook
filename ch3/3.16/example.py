#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in
Chicago. At what local time did your friend in Bangalore, India, have to show
up to attend?
"""


"""
SOLUTION
"""

from datetime import datetime, timedelta
import pytz
# from pytz import timezone
# from pytz import utc
# from pytz import country_timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the date for Chicago
central = pytz.timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(pytz.timezone('Asia/Kolkata'))
print(bang_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)

from datetime import timedelta
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)


"""
DISCUSSION
"""

print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

print(pytz.country_timezones['IN'])
