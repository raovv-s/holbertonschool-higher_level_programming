#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k, v in a_dictionary.items():
        s = a_dictionary[k]
        print("{}: {}".format(k, s))
