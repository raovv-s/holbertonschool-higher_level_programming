#!/usr/bin/python3
"""function with a argument"""


def append_write(filename="", text=""):
    """a argument with "with" """
    with open(filename, "a", encoding="utf-8") as m:
        d = text 
        return m.write(d)
