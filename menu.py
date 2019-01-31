import sys, time
import game

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
    choice = menu_options()
    return



def menu_options():
    while True:
        make_header("Welcome to <game>!")
        print("You have the following options:\n" + "[" + color("G", "S") + "]ingle player\n1[" + color("G", "v") + "]s1\n["  + color("G", "T") + "]ournament")
        choice = input("Please make your " + color("G", "choice: "))

        if choice == "S" or choice == "s":
            game.vs_AI()
            continue

        elif choice == "V" or choice == "v":
            while True:
                print("Do you wish to play [" + color("G", "L") + "]ocal or [" + color("G", "O") + "]nline?\n[" + color("R", "R") + "]eturn to previous options")
                choice = input("Please make your " + color("G", "choice: "))

                if choice == "L" or choice == "l":
                    game.vs_player()
                    break

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
                    local_tour_play()
                    break

                elif choice == "O" or choice == "o":
                    print("Find remote game platform here")

                elif choice == "R" or choice == "r":
                    break

                else: print("Invalid choice, try again")

        else: print("Invalid choice, try again")

    return

def local_tour_play():
    players = []

    make_header("Tournament play!")
    while True:
        choice = input("How many players? [" + color("G", "3-8") + "] ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice > 2 and choice < 9:
                break

    print("Name your players!")
    #for i in range(choice):
    #    name = input("Player nr " + str(i) + ": ")
    #    players.append(name)

    # Shortcut for testing
    players = ['ErikO', 'Daniel', 'Nicole', 'ErikL', 'Davide', 'Sam', 'Kevin', 'Viktor']
    for i in range(8-choice):
        del players[-1]

    # Hur jag tänkt, ungefär, att det kan funka:
    # import tournament
    # tour = tournament.create_tournament(players)
    nr_games = 6 # or tour.nr_games
    for i in range(nr_games):
        # tour.show_tournament_board()
        # game = tour.get_next_game()
        # (player_1, player_2) = tour.get_players(game)
        winner = game.vs_player("player_1", "player_2")
        # tour.post_result(game, winner)

    make_header("Winner is: Player_1!")

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

if __name__ == '__main__':
    main()
