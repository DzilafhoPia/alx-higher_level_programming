#!/usr/bin/python3

"""Defines a JSON file-writing func."""
import json

def save_to_json_file(my_obj, filename):
    """Writes object to text file using JSON representation."""
    with open(filename, "w") as f:
        jason.dump(my_obj, f)
