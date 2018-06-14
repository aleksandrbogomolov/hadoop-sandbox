#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    (key, page_rank, dest) = line.strip().split('\t')
    print(line.strip())

    dest = re.sub(r'[{}]', '', dest)
    dest = dest.split(',')
    for d in dest:
        print('%s\t%.3f\t{}' % (d, float(page_rank) / len(dest)))
