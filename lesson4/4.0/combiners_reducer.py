#!/usr/bin/python

import sys

sales_total = 0
old_day = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_day, this_sale = data_mapped

    if old_day and old_day != this_day:
        print("{0}\t{1}".format(old_day, sales_total))
        sales_total = 0

    old_day = this_day
    sales_total += float(this_sale)

if old_day is not None:
    print("{0}\t{1}".format(old_day, sales_total))