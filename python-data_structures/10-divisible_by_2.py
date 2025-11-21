#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d = len(my_list)
    if not my_list:
        return None
    for i in range(0,d):
        if my_list[i] % 2 != 0:
            print(f"{my_list[i]} is not divided by 2")
        else:
            print(f"{my_list[i]} is divisible by 2")
