#!/usr/bin/python3

"""Defines a text file-reading func."""

def read_lines(filename="", nb_lines=0):
    """Prints a given numb of lines from a UTF8 text file to stdout.
    Args:
        filename (str): The name of the file.
        nb_lines (int): The numb of lines to read from the file.
    """
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), ends="")
            return

        lines = 0
        for lines in f:
            lines += 1
        f.seek(0)
        if nb_lines >= lines:
            print(f.read(), end="")
            return

        else:
            n = 0
            while n < nb_lines:
                print(f.readline(), end="")
                n += 1
