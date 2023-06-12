#!/usr/bin/python3
"""Defines a func that adds attr to obj."""


def add_attribute(obj, att, value):
    """Add a new attr to an obj if possible.

    Args:
        obj (any): The object to add an attr to.
        att (str): The name of the attr to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
