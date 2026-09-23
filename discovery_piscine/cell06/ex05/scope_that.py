#!/usr/bin/env python

def add_one(number):
    number = number + 1
    print("Inside the method, the number is now " + str(number))

my_number = 5
print("Before calling the method: " + str(my_number))
add_one(my_number)
print("After calling the method: " + str(my_number))