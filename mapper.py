#!/usr/bin/env python3

import sys

for line in sys.stdin:
    dict = {}
    for word in line.strip().split(' '):
        if word:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

    for k, v in dict.items():
        print(str(k) + '\t' + str(v))
