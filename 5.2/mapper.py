#!/usr/bin/env python3

import sys
import re

inf = 'INF'

for line in sys.stdin:
    (key, dist, dest) = line.strip().split('\t')
    dest = re.sub(r'[{}]', '', dest)
    print('%s\t%s\t{%s}' % (key, dist, dest))
    dist = int(dist) + 1 if dist != inf else inf
    for s in [s for s in dest.split(',') if s != '']:
            print('%s\t%s\t{}' % (s, str(dist)))
