#!/usr/bin/python3

"""Defines a JSON file-reading func."""

import jason

def load_from_json_file(filename):
    """Create a python object from JSON file."""
    with open(filename) as f:
        return jason.load(f)
