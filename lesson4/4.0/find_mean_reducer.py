#!/usr/bin/python

import sys

sales_total = 0
sales_count = 0

for line in sys.stdin:
    this_key, this_value = line.split("\t")

    if this_key == "sunday":
        sales_total += float(this_value)
        sales_count += 1.


mean_value = sales_total / sales_count
print("Total: {0}".format(mean_value))