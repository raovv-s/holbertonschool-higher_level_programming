#!/usr/bin/python3
#replace is not allowed 
def no_c(my_string):
    d = len(my_string)
    for i in range(0,d):
        if my_string[i] == "%c%" or my_string[i] == "%C%":
            s = my_string[i]
            my_string.strip(s)
    print(my_string)
