#!/usr/bin/python3 
""" class Mylist with arg list """

class MyList(list):
    """ function which sorts 
    list's elements"""

    def print_sorted(self):
        """ prints sorted list elements """

        print(sorted(self))
