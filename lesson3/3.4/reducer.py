#!/usr/bin/python

import sys
count = 0

for line in sys.stdin:
    data_mapped = line.strip()
    if data_mapped == "/assets/js/the-associates.js":
        count += 1
print(count)
