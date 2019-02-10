#!/usr/bin/env python3

class tc:
    """
    A class to hold shorthands for different color formats
    """
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    ENDTC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def make_header(title):
    """
    Sig:    string ==> string
    Pre:    string is shorter than 48
    Post:   string formatted as a pretty header

    Example:
             make_header("header!") ==>
             --------------------------------------------------
             |                     header!                    |
             --------------------------------------------------

    """
    header = ""
    width = 50
    color_length = 9
    if len(title) % 2 == 0: tmp = len(title) / 2
    else: tmp = (len(title) - 1) / 2
    difference = int(24 - tmp)
    title = color("P", title)

    for i in range(width):
        header += "-"
    header += "\n|"

    for i in range(difference):
        header += " "
    header += title
    while len(header) < width * 2 + color_length:
        header += " "
    header += "|\n"

    for i in range(width):
        header += "-"

    print(header)

def color(color, text):
    """
    Sig:    string, string ==> string
    Pre:    color is "G", "P", or "R"
    Post:   string in the color indicated by variable color

    Example:
             color("G", "text") ==> "<green>text"
             color("P", "text") ==> "<purple>text"
    """
    if color == "G":
        return tc.GREEN + text + tc.ENDTC

    elif color == "P":
        return tc.PURPLE + text + tc.ENDTC

    elif color == "R":
        return tc.RED + text + tc.ENDTC

    else:
        return text
