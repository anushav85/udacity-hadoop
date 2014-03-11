#!/usr/bin/python

import sys
count = 0

for line in sys.stdin:
    data_mapped = line.strip()
    if data_mapped == "10.99.99.186":
        count += 1

print(count)
