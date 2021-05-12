#!/usr/bin/python3
"""returns a JSON version of an object"""


def to_json_string(my_obj):
    """returns a JSON version of an object"""

    import json

    j = json.dumps(my_obj)
    return j
