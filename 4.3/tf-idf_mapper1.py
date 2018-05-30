#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    raw_words = re.split('\W+', line.strip())
    pattern = re.compile('\w+')
    for word in raw_words[1:]:
        if pattern.match(word):
            print('%s#%s\t%i' % (word, raw_words[0], 1))
