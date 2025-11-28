#!/usr/bin/python3
"""READ UTF-8"""


def read_file(filename=""):
    """open with using "with" """

    with open("filename.txt", "r", encoding="utf-8") as m:
        s = m.read()
        print(s)

