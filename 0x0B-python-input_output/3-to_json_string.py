#!/usr/bin/python3

"""Defines a string-to-JSON func."""

import json

def to_json_string(my_obj):
    """Defines the JSON representation of a string obj."""
    return json.dumps(my_obj)
