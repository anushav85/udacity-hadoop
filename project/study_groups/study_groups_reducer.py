#!/usr/bin/python

import sys

old_key = None
users = list()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_user = data_mapped

    if old_key is not None and old_key != this_key:
        print("{0}\t{1}".format(old_key, "\t".join(users)))
        users = list()

    old_key = this_key
    users.append(this_user)

if old_key is not None:
    print("{0}\t{1}".format(old_key, "\t".join(users)))
