#!/usr/bin/python3
"""adds args to a list and saves as JSON file"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    args_list = load_from_json_file("add_item.json")
except:
    args_list = []
for i in range(1, len(sys.argv)):
    args_list.append(sys.argv[i])
save_to_json_file(args_list, "add_item.json")
