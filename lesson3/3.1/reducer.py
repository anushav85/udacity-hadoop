#!/usr/bin/python

import sys

sales_total = 0
old_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_sale = data_mapped

    if old_key and old_key != this_key:
        print("{0}\t{1}".format(old_key, sales_total))
        old_key = this_key
        sales_total = 0

    old_key = this_key
    sales_total += float(this_sale)

if old_key is not None:
    print("{0}\t{1}".format(old_key, sales_total))