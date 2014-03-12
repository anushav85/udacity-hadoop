#!/usr/bin/python

import sys
import time

week_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, hour, store, item, cost, payment = data
        week_day_name = week_day[time.strptime(date, "%Y-%m-%d").tm_wday]

        print("{0}\t{1}".format(week_day_name, cost))