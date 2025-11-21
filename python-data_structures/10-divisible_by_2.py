#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d = len(my_list)
    if not my_list:
        return None
    for i in range(0,d):
        if my_list[i] % 2 != 0:
            print("{:d} {:s} is not divisible by 2".format(my_list[i], "is"))
        else:
            print("{:d} {:s} is divisible by 2".format(my_list[i], "is"))

