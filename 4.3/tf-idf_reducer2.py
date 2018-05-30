#!/usr/bin/env python3

import sys

tf_dict = {}
raw_line = []

for line in sys.stdin:
    (line_id, tf_count) = line.strip().split('\t')
    if line_id not in tf_dict:
        tf_dict[line_id] = 1
    else:
        tf_dict[line_id] = int(tf_dict[line_id]) + 1
    raw_line.append(line)

for raw_str in raw_line:
    (key, values) = raw_str.strip().split('\t')
    (doc_id, tf, count) = values.strip().split(';')
    print('%s#%s\t%s\t%s' % (key, doc_id, tf, tf_dict[key]))
