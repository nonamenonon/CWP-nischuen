#!/usr/bin/env python

print("Enter a number")
number = int(input())

i = 0
while i <= 9:
    print(str(i) + " x " + str(number) + " = " + str(i * number))
    i = i + 1