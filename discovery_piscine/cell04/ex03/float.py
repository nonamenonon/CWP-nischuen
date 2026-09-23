#!/usr/bin/env python

def main():
    number = float(input("Give me a number: "))
    if number == int(number):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

if __name__ == "__main__":
    main()