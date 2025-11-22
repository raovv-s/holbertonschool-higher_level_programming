#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    s = 0
    new_list = []
    length = len(my_list_1)
    for i in range(length):
        try:
            s = my_list_1[i] / my_list_2[i]
            new_list.append(s)
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")

    return new_list
