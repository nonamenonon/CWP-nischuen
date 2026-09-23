#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    word = input("What was the parameter? ")
    if word == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()