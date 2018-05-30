#!/usr/bin/env python3

import sys

union_dict = {}

for line in sys.stdin:
    (k, v) = line.strip().split('\t')
    if k not in union_dict:
        union_dict[k] = v
    else:
        union_dict[k] = union_dict[k] + v

for k, v in union_dict.items():
    if len(v) == 1 and v[0] == 'A':
        print(k)
