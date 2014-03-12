#!/usr/bin/python

import csv
import sys
import re
import unidecode

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

regex = re.compile(r"(\bfantastically\b)")

for line in reader:
    res = regex.findall(line[4], re.IGNORECASE)
    if len(res) > 0:
        print("{0}".format(line[0]))

