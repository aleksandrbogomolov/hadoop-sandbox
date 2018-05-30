#!/usr/bin/env python3

import sys

for line in sys.stdin:
    (line_id, doc_id, count) = line.strip().split('\t')
    print('%s\t%s;%s;%i' % (line_id, doc_id, count, 1))
