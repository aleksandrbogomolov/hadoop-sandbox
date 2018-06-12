#!/usr/bin/env python3

import sys
import re

inf = 'INF'

for line in sys.stdin:
    (key, dist, dest) = line.strip().split('\t')
    dest = re.sub(r'[{}]', '', dest)
    dest = [int(s) for s in dest.split(',') if s != '']
    print(key, dist, dest)
    
