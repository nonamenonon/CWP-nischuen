#!/usr/bin/env python

import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = len(re.findall(re.escape(keyword), text))
    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()