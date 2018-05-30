#!/usr/bin/env python3

import sys

union_a = {}
union_b = {}

for line in sys.stdin:
    (union_id, value) = line.strip().split('\t')
    (k, v) = value.strip().split(':')
    if k == 'query':
        if union_id not in union_a:
            union_a[union_id] = [v]
        else:
            union_a[union_id].append(v)
    elif k == 'url':
        if union_id not in union_b:
            union_b[union_id] = [v]
        else:
            union_b[union_id].append(v)

for u_id, queries in union_a.items():
    if u_id in union_b:
        for item in queries:
            for urls in union_b[u_id]:
                print('%s\t%s\t%s' % (u_id, item, urls))
