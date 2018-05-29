#!/usr/bin/env python3

import sys

(last_key, sum, count) = ('', 0, 0)

for line in sys.stdin:
    (key, value) = line.strip().split('\t')
    (line_sum, line_count) = value.strip().split(';')
    if last_key and last_key != key:
        print('%s\t%s;%s' % (last_key, sum, count))
        (last_key, sum, count) = (key, line_sum, line_count)
    else:
        (last_key, sum, count) = (key, int(sum) + int(line_sum), int(count) + int(line_count))

if last_key:
    print('%s\t%s;%s' % (last_key, sum, count))
