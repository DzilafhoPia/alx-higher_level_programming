#!/usr/bin/python3

"""Defines a python class-to-JSON func."""

def class_to_json(obj):
    """Return the dictionary representation of a simple data struct."""
    return obj.__dict__
