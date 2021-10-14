#!/usr/bin/python3
"""returns an object represented by JSON string"""

import json


def from_json_string(my_str):
    """Takes object and returns JSON string"""

    return json.loads(my_str)
