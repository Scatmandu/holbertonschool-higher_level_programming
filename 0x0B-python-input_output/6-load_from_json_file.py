#!/usr/bin/python3
"""creates object from JSON file"""


import json


def load_from_json_file(filename):
    """Creates object from JSON file"""

    with open(filename) as f:
        return json.loads(f.read())
