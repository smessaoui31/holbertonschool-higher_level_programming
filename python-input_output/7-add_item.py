#!/usr/bin/python3
"""
Adds all arguments to a list and saves it in add_item.json.
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
