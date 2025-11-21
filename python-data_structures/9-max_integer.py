#!/usr/bin/python3
def max_integer(my_list=[]):
    d = len(my_list)
    c = 0
    for i in range(0,len(my_list)):
        if my_list[i] > c:
            c = my_list[i]
    print(f"Max: {a}")