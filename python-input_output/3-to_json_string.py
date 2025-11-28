#!/usr/bin/python3
"""json.dump in using"""
import json


def to_json_string(my_obj):
    """to json function"""

    jsobj = json.dumps(my_obj)
    return jsobj
