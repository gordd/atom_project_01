#!/usr/bin/python3
user_input = input("Enter a number: ")

try:
    val = int(user_input)
    print("Input is an integer number. Number =", val)
except ValueError:
    try:
        val = float(user_input)
        print("Input is a float  number. Number =", val)
    except ValueError:
        if len(user_input) == 0:
            print("Input is just an empty line.")
        else:
            print("Input is a string =", user_input)
