#!/usr/bin/python3

"""Defines a class student."""

class student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self_age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student.
        If attrs is a list of a str, represents only those attrs included in the list.
        Args:
            attrs (list): (optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == atr for ele in attrs)):
            return (k:getattr(self, k) for k in attr if hasattr(self, k))
        return self.__dict__
