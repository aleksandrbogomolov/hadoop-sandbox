#!/usr/bin/env python3

import sys

selection_id = 'user10'
(date_time, user_id, site) = (0, '', '')

for line in sys.stdin:
    (date_time, user_id, site) = line.strip().split('\t')
    if selection_id == user_id:
        print(line.strip())
