import sys, time

class tc:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    ENDTC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    #animation()
    menu_options()
    return

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

def menu_options():
    while True:
        make_header("Welcome to <game>!")
        print("You have the following options:\n" + "[" + color("G", "S") + "]ingle player\n1[" + color("G", "v") + "]s1\n["  + color("G", "T") + "]ournament")
        choice = input("Please make your " + color("G", "choice: "))

        if choice == "S" or choice == "s":
            print("Launch game platform here")

        elif choice == "V" or choice == "v":
            while True:
                print("Do you wish to play [" + color("G", "L") + "]ocal or [" + color("G", "O") + "]nline?\n[" + color("R", "R") + "]eturn to previous options")
                choice = input("Please make your " + color("G", "choice: "))

                if choice == "L" or choice == "l":
                    print("Launch game platform here")

                elif choice == "O" or choice == "o":
                    print("Find remote game platform here")

                elif choice == "R" or choice == "r":
                    break

                else: print("Invalid choice, try again")

        elif choice == "T" or choice == "t":
            while True:
                print("Do you wish to play [" + color("G", "L") + "]ocal or [" + color("G", "O") + "]nline?\n[" + color("R", "R") + "]eturn to previous options")
                choice = input("Please make your " + color("G", "choice: "))

                if choice == "L" or choice == "l":
                    print("Launch game platform here")

                elif choice == "O" or choice == "o":
                    print("Find remote game platform here")

                elif choice == "R" or choice == "r":
                    break

                else: print("Invalid choice, try again")

        else: print("Invalid choice, try again")

    return

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


if __name__ == '__main__':
    main()
