#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to crunch through large datasets and generate summaries or other kinds
of statistics.
"""


"""
SOLUTION

NOTICE: Before running the code below, make sure that you have the pandas
package installed (via 'sudo pip install pandas' in the terminal).
"""

import pandas


# read a CSV file, skipping last line
rats = pandas.read_csv('rats.csv', skip_footer=1)
print(rats)

# Investigate range of values for a certain field
print(rats['Current Activity'].unique())

# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
len(crew_dispatched)

# Find 10 most rat-infested ZIP codes in Chicago
print(crew_dispatched['ZIP Code'].value_counts()[:10])

# Group by completion data
dates = crew_dispatched.groupby('Completion Date')
print(len(dates))

# Determine counts on each day
date_counts = dates.size()
print(date_counts[0:10])

# Sort the counts
date_counts.sort()
print(date_counts[-10:])
