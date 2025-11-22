#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    s = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            s += 1
    except (ValueError, TypeError):
        pass
    print()

    return s