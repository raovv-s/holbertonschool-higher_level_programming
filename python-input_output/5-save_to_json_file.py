#!/usr/bin/python3
"""saving json to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function where it happens"""

    with open(filename, "w", encoding="utf-8") as m:
        json.dump(my_obj, m)
