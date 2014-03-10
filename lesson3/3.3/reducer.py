#!/usr/bin/python

import sys

sales_total = 0
sales_count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_sale = data_mapped

    sales_total += float(this_sale)
    sales_count += 1

print("{0}\t{1}".format(sales_total, sales_count))
