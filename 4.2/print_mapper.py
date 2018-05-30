#!/usr/bin/env python3

import sys

(date_time, user_id, site) = (0, '', '')

for line in sys.stdin:
    (date_time, user_id, site) = line.strip().split('\t')
    print(site)
