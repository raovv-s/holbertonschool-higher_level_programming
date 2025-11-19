#!/usr/bin/python3
def no_c(my_string):
    d = len(my_string)
    for i in range(0,d):
        if my_string[i] == "c" or my_string[i] == "C":
            my_string.remove(i)
    print(my_string)