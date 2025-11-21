#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d = len(my_list)
    if not my_list:
        return None
    for i in range(0,d):
        if my_list[i] % 2 != 0:
            print("{:d} {:s} divisible by 2".format(my_list[i], "is not"))
        else:
            print("{:d} {:s} divisible by 2".format(my_list[i], "is"))

