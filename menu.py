import sys
import time as t
from threading import Thread
import random
import game
import server
import client

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
    menu_options()
    make_header("Thanks for playing!")
    return

def menu_options():
    playing = True
    while playing:
        make_header("Welcome to <game>!")
        print("You have the following options:\n" + "[" + color("G", "S") + "]ingle player\n1[" + color("G", "v") + "]s1\n["  + color("G", "T") + "]ournament")
        choice = input("Please make your " + color("G", "choice: "))

        if choice == "S" or choice == "s":
            AI_vs()
            break

        elif choice == "V" or choice == "v":
            while True:
                print("Do you wish to play [" + color("G", "L") + "]ocal or [" + color("G", "O") + "]nline?\n[" + color("R", "R") + "]eturn to previous options")
                choice = input("Please make your " + color("G", "choice: "))

                if choice == "L" or choice == "l":
                    local_vs()
                    playing = False
                    break

                elif choice == "O" or choice == "o":
                    online_vs()
                    playing = False
                    break

                elif choice == "R" or choice == "r":
                    break

                else: print("Invalid choice, try again")

        elif choice == "T" or choice == "t":
            while True:
                print("Do you wish to play [" + color("G", "L") + "]ocal or [" + color("G", "O") + "]nline?\n[" + color("R", "R") + "]eturn to previous options")
                choice = input("Please make your " + color("G", "choice: "))

                if choice == "L" or choice == "l":
                    local_tour_play()
                    playing = False
                    break

                elif choice == "O" or choice == "o":
                    online_tour_play()
                    player = False
                    break

                elif choice == "R" or choice == "r":
                    break

                else: print("Invalid choice, try again")

        else: print("Invalid choice, try again")

    return

def AI_vs():
    result = game.vs_AI()
    make_header(result)

def local_vs():
    result = game.local_vs("Player 1", "Player 2")
    make_header(result)

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
        winner = game.local_vs("player_1", "player_2")
        make_header(winner)
        # tour.post_result(game, winner)

    make_header("Winner is: Player_1!")

def online_vs():
    while True:
        choice = input("Do you wish to act as server? [" + color("G", "Y") + "]es [" + color("R", "N") + "]no ")
        if choice == "Y" or choice == "y":
            s = server.Server()

            t.sleep(0.2)                              # client is sometimes quicker than server to start
            client_thread = Thread(target=run_client_single) # Starts thread to run client simultaneously as server
            client_thread.daemon = True               # Thread will not block if not properly shut down(E.g server crashes)
            client_thread.start()

            s.accept_clients(2)
            players = s.get_player_list()
            winner = s.relay_game(players)
            while client_thread.isAlive():            # Delay execution until thread is finished
                t.sleep(0.1)
            s.teardown()
            return

        elif choice == "N" or choice == "n":
            c = client.Client("Client Player")
            tmp = c.receive() # SYNC
            result = game.online_vs("Client player", c)
            make_header(result)
            c.teardown()
            return

    return

def online_tour_play():
    make_header("Tournament play!")

    while True:
        choice = input("Do you wish to act as server? [" + color("G", "Y") + "]es [" + color("R", "N") + "]no ")
        if choice == "Y" or choice == "y":
            players = []

            while True:
                choice = input("How many players? [" + color("G", "3-8") + "] ")
                if type(int(choice)) == int:
                    choice = int(choice)
                    if choice > 2 and choice < 9:
                        break

            s = server.Server()

            t.sleep(0.2)                                   # client is sometimes quicker than server to start
            client_thread = Thread(target=run_client_tour) # Starts thread to run client simultaneously as server
            client_thread.daemon = True                    # Thread will not block if not properly shut down(E.g server crashes)
            client_thread.start()

            s.accept_clients(choice)
            player_list = s.get_player_list()

            final = []
            match = []
            i = 0
            while i < 6:
                if i < 4:
                    match.append(player_list[i])
                    match.append(player_list[i+1])
                else:
                    match = final
                winner = s.relay_game(match)
                final.append(winner)
                match = []
                i += 2

            while client_thread.isAlive():                # Delay execution until thread is finished
                t.sleep(0.1)
            s.teardown()
            return

        else:
            i = random.randrange(1000)
            name = str(i)
            c = client.Client(name)

            while True:
                tmp = c.receive() # SYNC
                result = game.online_vs(name, c)
                make_header(result + " You advance to the next round!")


def run_client_single():
    c = client.Client("Server player")
    tmp = c.receive() # SYNC
    result = game.online_vs("Server player", c)
    make_header(result)
    c.teardown()
    return # Return to kill the thread that spawned this function.

def run_client_tour():
    i = random.randrange(1000)
    name = str(i)
    c = client.Client(name)

    while True:
        tmp = c.receive() # SYNC
        result = game.online_vs(name, c)
        make_header(result + " You advance to the next round!")

# Only silly stuff below
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
