#!/usr/bin/python

import sys

old_key = None
question_len = 0
answer_len = 0
answer_num = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    this_key, this_type, this_value = data_mapped

    if old_key is not None and old_key != this_key:
        if answer_num > 0:
            answer_avg = answer_len / answer_num
        else:
            answer_avg = 0

        print("{0}\t{1}\t{2}".format(old_key, question_len, answer_avg))

        question_len = 0
        answer_len = 0
        answer_num = 0

    old_key = this_key

    if this_type == "Q":
        question_len = float(this_value)

    if this_type == "A":
        answer_len += float(this_value)
        answer_num += 1

if old_key is not None:
    answer_avg = answer_len / answer_num
    print("{0}\t{1}\t{2}".format(old_key, question_len, answer_avg))