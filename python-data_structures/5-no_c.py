#!/usr/bin/python3
#replace is not allowed 
def no_c(my_string):
    stringc = ""
    for i in my_string:
        if i != 'c' or i != 'C':
            stringc += i 
    print(stringc)
