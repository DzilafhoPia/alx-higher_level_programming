#!/usr/bin/python3
""""Defines a text file line-counting func."""

def number_of_lines(filename=""):
    """Returns the numb of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1

    return
