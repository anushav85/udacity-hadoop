#!/usr/bin/python

import sys
import csv
from dateutil.parser import parse

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():  # skip header
            continue

        author_id = line[3]
        added_at = parse(line[8])

        print("{0}\t{1}".format(author_id, added_at.hour))
