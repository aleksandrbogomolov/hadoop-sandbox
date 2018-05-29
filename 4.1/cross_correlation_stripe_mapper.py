#!/usr/bin/env python3

import sys

for line in sys.stdin:
    splits = line.strip().split(' ')
    for i in splits:
        dict = {}
        for j in splits:
            if i != j:
                if j in dict:
                    dict[j] = dict[j] + 1
                else:
                    dict[j] = 1
        
        print('%s\t%s' % (i, ','.join(['%s:%i' % (k, v) for k, v in dict.items()])))
