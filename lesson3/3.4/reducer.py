#!/usr/bin/python

import sys

hits_total = 0
old_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_hit = data_mapped

    if old_key and old_key != this_key:
        print("{0}\t{1}".format(old_key, hits_total))
        old_Key = this_key
        hits_total = 0

    old_Key = this_key
    hits_total += float(this_hit)

if old_key is not None:
    print("{0}\t{1}".format(old_key, hits_total))