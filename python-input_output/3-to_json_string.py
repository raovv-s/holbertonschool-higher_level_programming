#!/usr/bin/python3
import json
"""json.dump in using"""


def to_json_string(my_obj):
    """to json function"""

    jsobj = json.dumps(my_obj)
    return jsobj
