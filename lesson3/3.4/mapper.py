#!/usr/bin/python

import sys
import re

regex = re.compile('"GET (.*) HTTP/1.0"')

for line in sys.stdin:
    res = regex.findall(line)
    if len(res) > 0:
        print("{0}\t1".format(res))