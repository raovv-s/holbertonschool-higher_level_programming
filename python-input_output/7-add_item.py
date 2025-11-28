#!/usr/bin/python3
"""load add save"""
import json
save_to_json_file = __import__(5-save_to_json_file).save_to_json_file
load_from_json_file = __import__(6-load_from_json_file).load_from_json_file
try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    obj = []
save_to_json_file(obj, filename)
