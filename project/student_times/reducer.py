#!/usr/bin/python

import sys

old_key = None
hours = [0 for _ in range(24)]

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_hour = data_mapped

    if old_key is not None and old_key != this_key:
        max_hour_value = max(hours)

        for i, j in enumerate(hours):
            if j == max_hour_value:
                print("{0}\t{1}".format(old_key, i))

        hours = [0 for _ in range(24)]

    old_key = this_key

    hours[int(this_hour)] += 1

if old_key is not None:
    max_hour_value = max(hours)

    for i, j in enumerate(hours):
        if j == max_hour_value:
            print("{0}\t{1}".format(old_key, i))
