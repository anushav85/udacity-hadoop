#!/usr/bin/python

import sys
popular_hits = 0
popular_file = None
count_hits = 0
old_file = None

for line in sys.stdin:
    this_file = line.strip()
    if old_file is not None and this_file != old_file:
        if count_hits > popular_hits:
            popular_file = this_file
            popular_hits = count_hits
        count_hits = 0

    count_hits += 1
    old_file = this_file

print("{0} {1}".format(popular_file, popular_hits))
