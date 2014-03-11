#!/usr/bin/python

import sys

count_total = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_count = data_mapped

    if this_key == "fantastic":
        count_total += int(this_count)

print("Total: {0}".format(count_total))