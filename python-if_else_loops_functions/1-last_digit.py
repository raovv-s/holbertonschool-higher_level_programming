#!/usr/bin/python3
import random

number_str = str(number)
last_digit = number_str[-1]

print(f"Last digit of {number} is {last_digit}", end='')

if int(last_digit) > 5:
    print(" and is greater than 5")
elif last_digit == '0':
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")

