import sys
import time as t
from threading import Thread
import random
import game, server, client, peer
import graphics as g


def main():
    menu_options()
    g.make_header("Thanks for playing!")
    return

def menu_options():
    playing = True
    while playing:
        g.make_header("Welcome to <game>!")
        print("You have the following options:\n" + "[" + g.color("G", "S") + "]ingle player\n1[" + g.color("G", "v") + "]s1\n["  + g.color("G", "T") + "]ournament")
        choice = input("Please make your " + g.color("G", "choice: "))

        if choice == "S" or choice == "s":
            AI_vs()
            break

        elif choice == "V" or choice == "v":
            while True:
                print("Do you wish to play [" + g.color("G", "L") + "]ocal or [" + g.color("G", "O") + "]nline?\n[" + g.color("R", "R") + "]eturn to previous options")
                choice = input("Please make your " + g.color("G", "choice: "))

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
                print("Do you wish to play [" + g.color("G", "L") + "]ocal or [" + g.color("G", "O") + "]nline?\n[" + g.color("R", "R") + "]eturn to previous options")
                choice = input("Please make your " + g.color("G", "choice: "))

                if choice == "L" or choice == "l":
                    local_tour_play()
                    playing = False
                    break

                elif choice == "O" or choice == "o":
                    online_tour_play()
                    playing = False
                    break

                elif choice == "R" or choice == "r":
                    break

                else: print("Invalid choice, try again")

        else: print("Invalid choice, try again")

    return

def AI_vs():
    result = game.local_vs("Player 1", "AI", [True, False])
    g.make_header(result + " has won!")

def local_vs():
    result = game.local_vs("Player 1", "Player 2", [True, True])
    g.make_header(result + " has won!")

def local_tour_play():
    players = []

    g.make_header("Tournament play!")
    while True:
        choice = input("How many players? [" + g.color("G", "3-8") + "] ")
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

    nr_games = 6 # or tour.nr_games
    for i in range(nr_games):
        winner = game.local_vs("player_1", "player_2")
        g.make_header(winner)

    g.make_header("Winner is: Player_1!")

def online_vs():
    while True:
        choice = input("Do you wish to act as server? [" + g.color("G", "Y") + "]es [" + g.color("R", "N") + "]no ")
        if choice == "Y" or choice == "y":
            c = peer.Peer(True)
            c.accept_client()
            win = game.online_vs("Player 1", c, True, True)
            if win:
                print("You've won!")
            else: print("Loose")
            c.teardown()
            break

        elif choice == "N" or choice == "n":
            c = peer.Peer(False)
            c.connect_to_server()
            win = game.online_vs("Player 2", c, True, False)
            if win:
                print("You've won!")
            else: print("Loose")
            c.teardown()
            break

def online_tour_play():
    g.make_header("Tournament play!")

    while True:
        choice = input("Do you wish to act as server? [" + g.color("G", "Y") + "]es [" + g.color("R", "N") + "]no ")
        if choice == "Y" or choice == "y":
            c = peer.Peer(True)
            c.accept_client()
            plist, hlist = decide_online_tour_players(c)
            print("Waiting for remote list of players...")
            lists = c.receive()
            remote_plist = lists[0]
            remote_hlist = lists[1]
            return

        elif choice == "N" or choice == "n":
            c = peer.Peer(False)
            c.connect_to_server()
            player_list, human_list = decide_online_tour_players(c)
            c.send((player_list, human_list))
            return


def decide_online_tour_players(c):
    while True:
        choice = input("How many players on this computer? [" + g.color("G", "1-7") + "](maximum 8 total) ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice >= 1 and choice <= 7:
                break

    c.send(choice)
    print("Confirming number of players...")
    remote_choice = c.receive()
    if remote_choice + choice > 8:
        print("Your total is over 8. Try again")
        decide_online_tour_players(c, server)


    player_list = []
    human_list = []
    for player in range(choice):
        name = input("Name player " + str(player+1) + ": ")
        while True:
            human = input("Is this a human player? [" + g.color("G", "Y") + "/" + g.color("R", "N") + "]")
            if human == "Y" or choice == "y":
                human = True
                break
            if human == "n" or choice == "n":
                human = False
                break

        player_list.append(name)
        human_list.append(human)

    return player_list, human_list


if __name__ == '__main__':
    main()
