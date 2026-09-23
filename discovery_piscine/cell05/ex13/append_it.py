#!/usr/bin/env python

import sys

def main():
    params = sys.argv[1:]
    if len(params) == 0:
        print("none")
        return
    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")

if __name__ == "__main__":
    main()