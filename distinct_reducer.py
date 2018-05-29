#!/usr/bin/env python3

import sys

dict = {}

for line in sys.stdin:
    (key, value) = line.strip().split('\t')
    if key:
        dict[key] = 1

if dict:
    for k, v in dict.items():
        print(k)
