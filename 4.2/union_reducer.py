#!/usr/bin/env python3

import sys

union_dict = {}

for line in sys.stdin:
    (k, v) = line.strip().split('\t')
    if k not in union_dict:
        union_dict[k] = 1

for k, v in union_dict.items():
    print(k)
