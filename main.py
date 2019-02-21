#!/usr/bin/env python3

import sys
#import time as t
import random
import game, peer
import graphics as g
import tournament as tour


def main():
    """
    Sig:    None
    Pre:    None
    Post:   A played game or tournament in the case of user choosing so, and termination of program
    """
    menu_options()
    g.make_header("Thanks for playing!")

def menu_options():
    """
    Sig:    None
    Pre:    None
    Post:   A played game or tournament in the case of user choosing so, and termination of program
    """
    playing = True
    while playing:
        g.make_header("Welcome to <game>!")
        print("You have the following options:\n 1[" + g.color("G", "v")\
              + "]s1\n["  + g.color("G", "T") + "]ournament\n[" + g.color("R", "Q") + "]uit ")
        choice = input("Please make your " + g.color("G", "choice: "))

        # 1 vs 1 game
        if choice == "V" or choice == "v":
            while True:
                print("Do you wish to play [" + g.color("G", "L") + "]ocal or [" + g.color("G", "O") + "]nline?\n["\
                      + g.color("R", "R") + "]eturn to previous options\n[" + g.color("R", "Q") + "]uit ")
                choice = input("Please make your " + g.color("G", "choice: "))

                # Local game
                if choice == "L" or choice == "l":
                    local_vs()
                    playing = False
                    break

                # Online game
                elif choice == "O" or choice == "o":
                    online_vs()
                    playing = False
                    break

                elif choice == "R" or choice == "r":
                    break

                elif choice == "Q" or choice == "q":
                    sys.exit()

                else: print("Invalid choice, try again")

        # Tournament game
        elif choice == "T" or choice == "t":
            while True:
                print("Do you wish to play [" + g.color("G", "L") + "]ocal or [" + g.color("G", "O") + "]nline?\n["\
                      + g.color("R", "R") + "]eturn to previous options\n[" + g.color("R", "Q") + "]uit ")
                choice = input("Please make your " + g.color("G", "choice: "))

                # Local tournament
                if choice == "L" or choice == "l":
                    local_tour_play()
                    playing = False
                    break

                # Online tournament
                elif choice == "O" or choice == "o":
                    online_tour_play()
                    playing = False
                    break

                elif choice == "R" or choice == "r":
                    break

                elif choice == "Q" or choice == "q":
                    sys.exit()

                else: print("Invalid choice, try again")

        elif choice == "Q" or choice == "q":
            sys.exit()

        else: print("Invalid choice, try again")


def local_vs():
    """
    Sig:    None
    Pre:    None
    Post:   A game played between between two players
    """
    players, humans = get_local_names()
    while True:
        result = game.local_vs(players, humans)
        if result != "DRAW":
            break
        else:
            g.make_header("Game draw! Replay game")
    g.make_header(result + " has won!")


def online_vs():
    """
    Sig:    None
    Pre:    None
    Post:   A game played between against a remote player
    """
    while True:
        name, human = get_online_name()
        choice = input("Are you the first to start the game? [" + g.color("G", "Y") + "]es [" \
                       + g.color("R", "N") + "]no\n[" + g.color("R", "Q") + "]uit ")
        if choice == "Y" or choice == "y":
            # Create peer which will act as server
            c = peer.Peer(True)
            c.accept_client()
            while True:
                # Name, peer, Human, Server
                win = game.online_vs(name, c, human, True)
                if win != "DRAW":
                    break
                else:
                    g.make_header("Game draw! Replay game")
            if win == name:
                g.make_header("You've won!")
            else: g.make_header("You've lost!")
            c.teardown()
            break

        elif choice == "N" or choice == "n":
            # Create peer which will act as client
            c = peer.Peer(False)
            c.connect_to_server()
            while True:
                # Name, peer, Human, Server
                win = game.online_vs(name, c, human, False)
                if win != "DRAW":
                    break
                else:
                    g.make_header("Game draw! Replay game")
            # Name, peer, Human = True, Server = False
            if win == name:
                g.make_header("You've won!")
            else: g.make_header("You've lost!")
            c.teardown()
            break

        elif choice == "Q" or choice == "q":
            sys.exit()

        else: print("Invalid choice, try again")


def local_tour_play():
    """
    Sig:    None
    Pre:    None
    Post:   A tournament played between local players. And termination of program
    """
    g.make_header("Tournament play!")

    # Determine players
    player_list, human_dict = decide_offline_tour_players()

    # Play tournament
    t = tour.Tournament(player_list)
    while True:
        g.make_header("Tournament Standings")
        print(t.get_scoreboard())
        end = t.winner_state
        players = t.opponents
        if end == 1: # Last game already played
            break
        else:
            g.make_header("Up next: " + players[0] + " vs " + players[1])
            humans = [human_dict[players[0]], human_dict[players[1]]]
            while True:
                winner = game.local_vs(players, humans)
                if winner != "DRAW":
                    break
                else:
                    g.make_header("Draw game! Replaying game")
            t.next_game(winner) # Set winner of current game
            g.make_header(winner + " has advanced to the next round!")

    g.make_header(winner + " has won the tournament!")
    sys.exit()


def online_tour_play():
    """
    Sig:    None
    Pre:    None
    Post:   A tournament played between local, and remote players. And/or termination of program
    """
    g.make_header("Tournament play!")

    while True:
        choice = input("Are you the first to start the game? [" + g.color("G", "Y") + "]es ["\
                       + g.color("R", "N") + "]no\n[" + g.color("R", "Q") + "]uit ")
        if choice == "Y" or choice == "y":
            server_side_tournament()

        elif choice == "N" or choice == "n":
            client_side_tournament()

        elif choice == "Q" or choice == "q":
            sys.exit()

        else: print("Invalid choice, try again")

def server_side_tournament():
    """
    Sig:    None
    Pre:    None
    Post:   A tournament played between local, and remote players. And termination of program

    Notes
    -----
    If multiple messages are sent in a row without being received, they will be concatenated in the pipeline \
    and the receiving end will be unable to process the message. Therefor it is sometime needed to send \
    junk messages to sync the clients
    """
    # Setup
    c = peer.Peer(True)
    c.accept_client()
    player_list, human_dict = decide_online_tour_players(c, False)
    print("Waiting for remote list of players...")

    # Sync player lists
    remote_player_list = c.receive()
    player_list = player_list + remote_player_list
    c.send(player_list)
    remote_human_dict = c.receive()
    human_dict.update(remote_human_dict)
    c.send(human_dict)
    c.receive()                         # Block needed here to ensure clients are synced

    # Create tournament and setup instructions
    t = tour.Tournament(player_list)
    data = {}                           # Dictionary containing various data needed by remote peer
    data["instruction"] = None          # Instructions in the form of strings
    data["players"] = None              # players to play next game
    data["tour"] = t.get_scoreboard()   # String representing current tournament bracket
    c.send(data)                        # Send initial tournament bracket
    winner = ""

    while True:
        g.make_header("Tournament Standings")
        data["tour"] = t.get_scoreboard()
        print(data["tour"])
        end = t.winner_state
        players = t.opponents
        winners = []

        # Completed tournament
        if end == 1:
            data["instruction"] = "COMPLETE"
            data["player"] = winner
            c.send(data)
            g.make_header(winner + " Has won the tournament!")
            c.teardown()
            sys.exit()

        else:
            # Setup game
            g.make_header("Up next: Local " + players[0] + " vs remote " + players[1])
            data["players"] = players
            data["instruction"] = "PLAY"
            c.send(data)

            while True:
                winner = game.online_vs(players[0], c, human_dict[players[0]], True)
                if winner != "DRAW":
                    break
                else:
                    g.make_header("Game draw! Replay game")

            if winner == players[0]: # If local player won
                winners.append(winner)
                g.make_header(winner + " has advanced to the next round!")
            else:                    # If remote player won
                winner = players[1] 
                winners.append(winner)
                g.make_header(winner + " has advanced to the next round!")

        t.next_game(winner)

def client_side_tournament():
    """
    Sig:    None
    Pre:    None
    Post:   A tournament played between local, and remote players. And termination of program
    """
    # Setup
    c = peer.Peer(False)
    c.connect_to_server()
    player_list, human_dict = decide_online_tour_players(c, True)

    # Sync player lists
    c.send(player_list)
    player_list = c.receive()
    c.send(human_dict)
    human_dict = c.receive()
    c.send("ACK")                      # Sync with remote
    data = c.receive()                 # Get initial tournament bracket

    while True:
        g.make_header("Tournament Standings")
        print(data["tour"])

        # End tournament
        if data["instruction"] == "COMPLETE":
            g.make_header(data["player"] + " has won the tournament!")
            c.teardown()
            sys.exit()

        elif data["instruction"] == "PLAY":
            players = data["players"]
            g.make_header("Up next: Local " + players[1] + " vs remote " + players[0])
            while True:
                winner = game.online_vs(players[1], c, human_dict[players[1]], False)
                if winner != "DRAW":
                    break
                else:
                    g.make_header("Game draw! Replay game")

            if winner == players[1]: # If local player won
                g.make_header(winner + " has advanced to the next round!")
            else:                    # If remote player won
                g.make_header(players[0] + " has advanced to the next round!")

        data = c.receive()

def get_local_names():
    """
    Sig:    None
    Pre:    None
    Post:   List of names, and list of booleans corresponding to whether player is human or NPC
    """
    players = []
    humans = []

    for i in range(2):
        name = input("Name player " + str(i+1) + ": ")
        while True:
            human = input("Is this a human player? [" + g.color("G", "Y") + "/" + g.color("R", "N") + "]")
            if human == "Y" or human == "y":
                human = True
                break
            if human == "n" or human == "n":
                human = False
                break
        players.append(name)
        humans.append(human)

    return players, humans

def get_online_name():
    """
    Sig:    None
    Pre:    None
    Post:   Name, and boolean corresponding to whether player is human or NPC
    """
    name = input("Input your name: ")
    while True:
        human = input("Are you a human player? [" + g.color("G", "Y") + "/" + g.color("R", "N") + "]")
        if human == "Y" or human == "y":
            human = True
            break
        if human == "n" or human == "n":
            human = False
            break

    return name, human

def decide_offline_tour_players():
    player_list = [] # Strings of names
    human_dict = {}  # Booleans. Key = player. True = Human, False = NPC
    # Decide nr players
    while True:
        choice = input("How many players? [" + g.color("G", "3-8") + "] ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice > 2 and choice < 9:
                break
    nr_players = choice

    # Decide nr AI players
    while True:
        choice = input("How many AI players? [" + g.color("G", "0-" + str(nr_players)) + "] ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice <= nr_players:
                break
    nr_ai = choice

    # Name human players
    for player in range(nr_players-nr_ai):
        name = input("Name player" + str(player+1) + ": ")
        player_list.append(name)
        human_dict[name] = True

    # Name AI players
    names = ["SKYNET", "MAX HEADROOM", "WATSON", "DEEP THOUGHT", "J.A.R.V.I.S.", "R2D2", "MU-TH-UR 6000", "TÄNKANDE AUGUST"]
    for nr in range(nr_ai):
        name = names[nr]
        player_list.append(name)
        human_dict[name] = False

    return player_list, human_dict

def decide_online_tour_players(c, remote):
    """
    Sig:    Peer ==> array, dictionary
    Pre:    Peer is connected to another peer
    Post:   Array containing list of players on this side of connection, dictionary containing whether \
            players are human or computer controlled
    """
    # Determine number of players
    while True:
        choice = input("How many players on this computer? [" + g.color("G", "1-7") + "](maximum 8 total) ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice >= 1 and choice <= 7:
                break

    # Send number of players and ensure remote and local don't exceed 8
    c.send(choice)
    print("Confirming number of players...")
    remote_choice = c.receive()
    if remote_choice + choice > 8:
        print("Your total is over 8. Try again")
        decide_online_tour_players(c, remote)

    nr_players = choice
    player_list = [] # Strings of names
    human_dict = {}  # Booleans. Key = player. True = Human, False = NPC
    # Determine names and human/computer controlled
    while True:
        choice = input("How many AI players? [" + g.color("G", "0-" + str(nr_players)) + "] ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice <= nr_players:
                break
    nr_ai = choice

    # Name human players
    for player in range(nr_players-nr_ai):
        name = input("Name player" + str(player+1) + ": ")
        player_list.append(name)
        human_dict[name] = True

    # Name AI players
    names = ["SKYNET", "MAX HEADROOM", "WATSON", "DEEP THOUGHT", "J.A.R.V.I.S.", "R2D2", "MU-TH-UR 6000", "TÄNKANDE AUGUST"]
    for nr in range(nr_ai):
        # This is to ensure that server/client dont create players with the same name
        if remote:
            name = names[nr]            
        else:
            name = names[nr+4]
        player_list.append(name)
        human_dict[name] = False

    return player_list, human_dict


if __name__ == '__main__':
    main()