#!/usr/bin/python

import sys

count_total = 0

res = list()

for line in sys.stdin:
    key = line.strip().split("\t")
    if len(key) != 1:
        continue

    res.append(int(key[0]))

res = sorted(res)

print(res)