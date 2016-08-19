#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to read or write data encoded as a CSV file.
"""


"""
SOLUTION
"""

import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Process row
        print(row)


from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # Process row
        print(row.Symbol, row.Price, row.Date,
              row.Time, row.Change, row.Volume)


headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
    ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
]

with open('stocks2.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
    print(f_csv)


headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    {
        'Symbol'    :   'AA',
        'Price'     :   39.48,
        'Date'      :   '6/11/2007',
        'Time'      :   '9:36am',
        'Change'    :   -0.18,
        'Volume'    :   181800
    },
    {
        'Symbol'    :   'AIG',
        'Price'     :   71.38,
        'Date'      :   '6/11/2007',
        'Time'      :   '9:36am',
        'Change'    :   -0.15,
        'Volume'    :   195500
    },
    {
        'Symbol'    :   'AXP',
        'Price'     :   62.58,
        'Date'      :   '6/11/2007',
        'Time'      :   '9:36am',
        'Change'    :   -0.46,
        'Volume'    :   935000
    },
]

with open('stocks3.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
    print(f_csv)


"""
DISCUSSION
"""

# import re
# with open('stocks4.csv') as f:
#     f_csv = csv.reader(f)
#     headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
#     Rows = namedtuple('Row', headers)
#     for r in f_csv:
#         row = Row(*r)
#         # Process row
#         pass


col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

print('Reading as dicts with type conversion')
field_types = [
    ('Price', float),
    ('Change', float),
    ('Volume', int)
]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        # Now each row becomes a dict
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)
