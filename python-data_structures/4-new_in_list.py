#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list2 = my_list.copy()
    if len(my_list) < 0:
        return my_list[idx]
    else:
        if len(my_list) > 0:
            my_list2[idx] = element
            return my_list2
