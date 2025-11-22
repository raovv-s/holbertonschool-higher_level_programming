#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = a_dictionary.keys()
    values = a_dictionary.values()
    nvalues = list(map(lambda x: x*2 , values))
    print("{}: {}".format(keys, nvalues))
    