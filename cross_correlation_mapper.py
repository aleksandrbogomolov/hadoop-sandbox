#!/usr/bin/env python3

import sys

for line in sys.stdin:
    splits = line.strip().split(' ')
    for i in splits:
        for j in splits:
            if i != j:
                print('%s,%s\t1' % (i, j))
