#!/usr/bin/env python

import sys

def shrink(word):
    print(word[0:8])

def enlarge(word):
    result = word
    while len(result) < 8:
        result = result + "Z"
    print(result)

if len(sys.argv) < 2:
    print("none")
else:
    i = 1
    while i < len(sys.argv):
        word = sys.argv[i]
        if len(word) > 8:
            shrink(word)
        elif len(word) < 8:
            enlarge(word)
        else:
            print(word)
        i = i + 1