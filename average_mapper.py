#!/usr/bin/env python3

import sys

for line in sys.stdin:
    if line:
        (k, v) = line.strip().split('\t')
        print(k + '\t' + v)
