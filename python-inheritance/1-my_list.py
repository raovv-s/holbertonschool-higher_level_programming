#!/usr/bin/python3
""" class Mylist with arg list """


class MyList(list):
    """function which sortslist's elements"""

    def print_sorted(self):
        """prints sorted list elements"""

        print(sorted(self))
