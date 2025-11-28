#!/usr/bin/python3
"""load add save"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    obj = []

items.extend(argv[1:])

save_to_json_file(obj, filename)
