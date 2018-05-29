#!/usr/bin/env python3

import sys

(last_key, sum) = ('', 0)

for line in sys.stdin:
    (key, value) = line.strip().split('\t')
    if last_key and last_key != key:
        print(last_key + '\t' + str(sum))
        (last_key, sum) = (key, int(value))
    else:
        (last_key, sum) = (key, sum + int(value))

if last_key:
    print(last_key + '\t' + str(sum))
