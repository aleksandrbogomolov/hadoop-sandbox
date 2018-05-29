#!/usr/bin/env python3

import sys

dict = {}
dist_dict = {}

for line in sys.stdin:
    dist_key = line.strip().replace('\t', ',')
    if dist_key not in dist_dict:
        dist_dict[dist_key] = 1

for k, v in dist_dict.items():
    (i, c) = k.strip().split(',')
    if c in dict:
        dict[c] = dict[c] + 1
    else:
            dict[c] = 1

for k, v in dict.items():
    print('%s\t%i' % (k, v))
