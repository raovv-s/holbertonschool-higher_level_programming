#!/usr/bin/python3
"""load from json"""
import json


def load_from_json_file(filename):
    """load function"""

    with open(filename, "r", encoding="utf-8") as m:
        return json.load(f)
