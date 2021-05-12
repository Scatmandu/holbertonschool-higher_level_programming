#!/usr/bin/python3
"""writes an object to txt file using JSON representation"""


def save_to_json_file(my_obj, filename):
    """writes an object to txt file using JSON representation"""

    import json

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
