#!/usr/bin/env python3

import sys

for line in sys.stdin:
    (key, categories) = line.strip().split('\t')

    for c in categories.strip().split(','):
        print('%s,%s\t1' % (key, c))
