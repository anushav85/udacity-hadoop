#!/usr/bin/python

import sys
import time

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, hour, store, item, cost, payment = data

        if time.strptime(date, "%Y-%m-%d").tm_wday == 6:
            print("{0}\t{1}".format("sunday", cost))