#!/usr/bin/env python

import sys

def main():
    params = sys.argv[1:]
    if len(params) == 0:
        print("none")
        return
    print(f"parameters: {len(params)}")
    for param in params:
        print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()