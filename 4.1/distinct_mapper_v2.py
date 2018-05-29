#!/usr/bin/env python3

import sys

for line in sys.stdin:
    (key, value) = line.strip().split(',')
    print('%s\t%i' % (value, 1))
