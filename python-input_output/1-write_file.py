#!/usr/bin/python3
"""write method"""


def write_file(filename="", text=""):
    with open(filename, w, encoding="utf-8") as m:
        d = text 
        m.write(d)
        