#!/usr/bin/env python
from checkmate import checkmate
from sys import argv


def main():
    board = """\
R...
.K..
..P.
....\
"""
    try:
        if len(argv) > 1:
            for arg in argv[1:]:
                checkmate(arg.replace("\\n", "\n"))
        else:
            checkmate(board)
    except Exception:
        print("Error")


if __name__ == "__main__":
    main()