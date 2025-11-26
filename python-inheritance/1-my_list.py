#!/usr/bin/python3 
""" class Mylist with arg list """

class Mylist(list):
    """ function which sorts list's elements"""

    def print_sorted(self):
        print(sorted(self))
