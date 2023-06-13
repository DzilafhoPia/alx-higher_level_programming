#!/usr/bin/python3

"""Defines a str-to-JSON func."""

import json

def to_json_string(my_obj):
    """Returns the JSON representation of a str obj."""
    return json.dumps(my_obj)
