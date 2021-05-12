#!/usr/bin/python3
"""returns deserialized JSON string"""


def from_json_string(my_str):
    """returns deserialized JSON string"""

    import json

    j = json.loads(my_str)
    return j
