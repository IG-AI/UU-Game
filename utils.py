class tc:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    ENDTC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def make_header(title):
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
    if color == "G":
        return tc.GREEN + text + tc.ENDTC

    elif color == "P":
        return tc.PURPLE + text + tc.ENDTC

    elif color == "R":
        return tc.RED + text + tc.ENDTC

    else:
        return text

def animation():
    symbols = [':', ' ']
    i = 0
    while True:
        sys.stdout.write(symbols[i])
        sys.stdout.write("\b")
        sys.stdout.flush()
        time.sleep(0.2)
        if i == 0: i += 1
        else: i = 0
