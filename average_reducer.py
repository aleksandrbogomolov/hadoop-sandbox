#!/usr/bin/env python3

import sys

(last_key, sum, count) = ('', 0, 0)

for line in sys.stdin:
    (key, value) = line.strip().split('\t')
    if last_key and last_key != key:
        print(last_key + '\t' + str(int(sum / count)))
        (last_key, sum, count) = (key, int(value), 1)
    else:
        (last_key, sum, count) = (key, sum + int(value), count + 1)

if last_key:
    print(last_key + '\t' + str(int(sum / count)))
