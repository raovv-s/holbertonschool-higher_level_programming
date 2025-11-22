#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        value = a_dictionary[k]
        print("{}: {}".format(k, value))
