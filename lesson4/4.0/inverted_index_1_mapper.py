#!/usr/bin/python

import csv
import sys
import re
import unidecode

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

regex = re.compile(r"(\bfantastic\b)")

for line in reader:
    res = regex.findall(line[4])
    if len(res) > 0:
        print("{0}\t{1}".format(res[0], len(res)))

