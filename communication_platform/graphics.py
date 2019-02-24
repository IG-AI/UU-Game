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
    BGPURPLE= '\033[45m'
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
    width = 75
    title = color("P", title)
    color_count = repr(title).count("\\")

    #print(repr(title))
    # Re-color text if tc.ENDTC is present in string
    if color_count > 2:
        last_found = 0
        for i in range(color_count-2):
            last_found = repr(title).find("\\x1b[0m", last_found)
            if last_found < len(repr(title)) - 20: # Dont overwrite last tc.ENDTC
                title = title[:last_found-3] + tc.PURPLE + title[last_found-3:]
                #print(last_found)
            last_found += 5
    #print(repr(title))
    
    color_count = repr(title).count("\\")
    #print(color_count)

    for i in range(width):
        header += "-"
    header += "\n|"
    
    # "".format does not allow variable inside of "", therefore this is needed
    if color_count == 4:
        header += "{:^91}".format(title) + "|\n"

    elif color_count == 5:
        header += "{:^96}".format(title) + "|\n"

    elif color_count == 6:
        header += "{:^100}".format(title) + "|\n"

    elif color_count == 7:
        header += "{:^105}".format(title) + "|\n"

    elif color_count == 8:
        header += "{:^110}".format(title) + "|\n"

    else:
        header += "{:^82}".format(title) + "|\n"

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

    elif color == "Y":
        return tc.YELLOW + text + tc.ENDTC

    elif color == "BP":
        return tc.BGPURPLE + text + tc.ENDTC

    elif color == "BP_START":
        return tc.BGPURPLE + text

    elif color == "BP_STOP":
        return text + tc.ENDTC

    else:
        return text
