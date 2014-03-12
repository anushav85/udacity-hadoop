#!/usr/bin/python

import sys

N = 10
tags = dict()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    tag, occurrences = data_mapped

    if tag in tags:
        tags[tag] += int(occurrences)
    else:
        tags[tag] = int(occurrences)

tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)[0:N]

for t in tags:
    print('{0}\t{1}'.format(t[0], t[1]))
