#!/usr/bin/python3
"""write method"""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, "w", encoding="utf-8") as m:
        d = text 
        return m.write(d)
