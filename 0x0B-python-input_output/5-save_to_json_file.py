#!/usr/bin/python3
"""writes an object to a text file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """Text file to JSON"""

    with open(filename, "w") as outfile:
        outfile.write(json.dumps(my_obj))
