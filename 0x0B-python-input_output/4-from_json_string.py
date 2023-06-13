#!/usr/bin/python3

"""Defines a JSON-to-object func."""

import json

def from_json_string(my_str):
    """Returns the python object representation of a JSON str."""
    return json.loads(my_str)
