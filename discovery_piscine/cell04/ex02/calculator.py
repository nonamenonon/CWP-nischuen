#!/usr/bin/env python

def main():
    first = float(input("Give me the first number: "))
    second = float(input("Give me the second number: "))
    print("Thank you!")
    print(f"{first} + {second} = {first + second}")
    print(f"{first} - {second} = {first - second}")
    print(f"{first} / {second} = {first / second}")
    print(f"{first} * {second} = {first * second}")

if __name__ == "__main__":
    main()