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
    ORANGE = '\033[33m'
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

    # Re-color text if tc.ENDTC is present in string
    if color_count > 2:
        last_found = 0
        for i in range(color_count-2):
            last_found = repr(title).find("\\x1b[0m", last_found)
            if last_found < len(repr(title)) - 20: # Dont overwrite last tc.ENDTC
                title = title[:last_found-3] + tc.PURPLE + title[last_found-3:]
            last_found += 5
    
    color_count = repr(title).count("\\")

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

def make_rules():
    example_board = color("G", "0") + "001 0010 1100 1000\n"
    example_board += "____ " + color("G", "0") + "100 0111 ____\n"
    example_board += "____ 1111 " + color("G", "0") + "110 1010\n"
    example_board += "____ 0011 ____ " + color("G", "0") + "000\n"

    output = color("P", "UU-Game") + " is a game similar to " + color("P", "4-in-a-row")
    output += ". The difference being that each \npiece has unique characteristics."
    output += " Each piece is a set of 4 binary numbers.\nTo get 4 in a row, "
    output += "the binary number at a given index has to be the same\nacross the whole row.\n"
    print(output)
    input("[" + color("G", "Enter") + "] to continue")

    output = "\nxamples:\n\n"
    example_board = "____ 0010 ____ 1111\n"
    example_board += "00"+color("G", "0")+"0 11"+color("G", "0")+"0 10"+color("G", "0")+"1 11"+color("G", "0")+"1\n"
    example_board += "____ 0110 ____ 0011\n"
    example_board += "1110 1011 ____ 0100\n"
    output += example_board + "\n"

    example_board = color("G", "0") + "001 0010 1100 1000\n"
    example_board += "____ " + color("G", "0") + "100 0111 ____\n"
    example_board += "____ 1111 " + color("G", "0") + "110 1010\n"
    example_board += "____ 0011 ____ " + color("G", "0") + "000\n"
    output += example_board + "\n"

    example_board =  "1"+color("G", "1")+"11 0000 0101 1000\n"
    example_board += "0"+color("G", "1")+"10 ____ ____ ____\n"
    example_board += "0"+color("G", "1")+"00 1100 0001 ____\n"
    example_board += "0"+color("G", "1")+"11 ____ ____ ____\n"
    output += example_board
    print(output)
    input("[" + color("G", "Enter") + "] to continue")

    output = "\nGames are played in turn. One player will choose a piece for the opposing\nplayer"
    output += " who will then place the chosen piece on the board. This player then\nin turn "
    output += "chooses the next piece for the opponent. This is repeated until\nsomeone has "
    output += "achieved 4 in a row\n"
    print(output)
    input("[" + color("G", "Enter") + "] to continue")

    output = "\nPieces are chosen from a list, by entering the corresponding number.\n"
    output += "Given the list of pieces:\n"
    pieces = "["+color("G","0")+"]: 0000 ["+color("G","1")+"]: 0001\n"
    pieces += "["+color("G","2")+"]: 0010 ["+color("G","3")+"]: 0011\n"
    pieces += "["+color("G","4")+"]: 0100 ["+color("G","5")+"]: 0101\n"
    output += pieces
    output += "\nAnd choosing " + color("G", "2") + " will result in piece: " + color("G", "0010") + " being chosen\n"
    print(output)
    input("[" + color("G", "Enter") + "] to continue")

    output = "\nPieces are placed by entering two numbers. The first corresponding to the row,\n"
    output += "and the second corresponding to the column. Given a board of:\n\n"
    board = " ["+color("G", "0")+"]  ["+color("G", "1")+"]  ["+color("G", "2")+"]  ["+color("G", "3")+"]\n"
    board += "____ ____ ____ ____  ["+color("G", "0")+"]\n"
    board += "____ ____ ____ ____  ["+color("G", "1")+"]\n"
    board += "____ ____ ____ ____  ["+color("G", "2")+"]\n"
    board += "____ ____ ____ ____  ["+color("G", "3")+"]\n"
    output += board
    output += "\nAnd choosing "+color("G", "1 2")+" will result in:\n\n"
    board = " ["+color("G", "0")+"]  ["+color("G", "1")+"]  ["+color("G", "2")+"]  ["+color("G", "3")+"]\n"
    board += "____ ____ ____ ____  ["+color("G", "0")+"]\n"
    board += "____ ____ "+color("G", "0010")+" ____  ["+color("G", "1")+"]\n"
    board += "____ ____ ____ ____  ["+color("G", "2")+"]\n"
    board += "____ ____ ____ ____  ["+color("G", "3")+"]\n"
    output += board
    print(output)
    input("[" + color("G", "Enter") + "] to continue")

    output = color("B", "\nHuman players")+" are colored "+color("B", "blue")+", AI players are colored "
    output += color("R", "red")+", "+color("Y", "yellow")+" or, "+color("G", "green")+"\ndepending on "
    output += "their difficulty level.\n"
    print(output)
    input("[" + color("G", "Enter") + "] to start the game!")
    print("\n")

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

    elif color == "B":
        return tc.BLUE + text + tc.ENDTC

    elif color == "O":
        return tc.ORANGE + text + tc.ENDTC

    elif color == "BP":
        return tc.BGPURPLE + text + tc.ENDTC

    elif color == "BP_START":
        return tc.BGPURPLE + text

    elif color == "BP_STOP":
        return text + tc.ENDTC

    else:
        return text
