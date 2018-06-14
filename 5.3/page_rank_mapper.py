#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    (key, page_rank, dest) = line.split('\t')
    print(line)

    dest = dest[1:-1].split(',')
    for d in dest:
        print('%s\t%.3f\t{}' % (d, float(page_rank) / len(dest)))
