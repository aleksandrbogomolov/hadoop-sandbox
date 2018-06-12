#!/usr/bin/env python3

import sys
import re

inf = 'INF'
result_dict = {}

for line in sys.stdin:
    (key, dist, dest) = line.strip().split('\t')
    dest = re.sub(r'[{}]', '', dest)
    
    if key in result_dict:
        result_dict[key].append((dist, dest))
    else:
        result_dict[key] = [(dist, dest)]

for k, v in result_dict.items():
    (key, dist, dest) = (k, '', '')
    for i, j in v:
        if i != inf:
            if dist != inf and dist != '':
                dist = i if int(i) < int(dist) else dist
            else:
                dist = i
        elif i == inf and dist == '':
            dist = i
        dest = dest + j        
    print('%s\t%s\t{%s}' % (key, dist, dest))
