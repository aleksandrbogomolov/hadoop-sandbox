#!/usr/bin/env python3

import sys

tf_dict = {}
(line_id, count) = ('', 0)

for line in sys.stdin:
    (line_id, count) = line.strip().split('\t')
    if line_id not in tf_dict:
        tf_dict[line_id] = count
    else:
        tf_dict[line_id] = int(tf_dict[line_id]) + int(count)

for k, v in tf_dict.items():
    (key, doc_id) = k.strip().split('#')
    print('%s\t%s\t%s' % (key, doc_id, v))
