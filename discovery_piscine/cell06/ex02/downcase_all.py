#!/usr/bin/env python

import sys

def downcase_it(word):
    return word.lower()

if len(sys.argv) < 2:
    print("none")
else:
    i = 1
    while i < len(sys.argv):
        print(downcase_it(sys.argv[i]))
        i = i + 1