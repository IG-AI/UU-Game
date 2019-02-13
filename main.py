#!/usr/bin/env python3

import sys
import time as t
import random
import game, peer
import graphics as g
import tournament2 as tour


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
        print("You have the following options:\n" + "[" + g.color("G", "S") + "]ingle player\n1[" + g.color("G", "v")\
              + "]s1\n["  + g.color("G", "T") + "]ournament\n[" + g.color("R", "Q") + "]uit ")
        choice = input("Please make your " + g.color("G", "choice: "))

        # Single player game
        if choice == "S" or choice == "s":
            AI_vs()
            break

        # 1 vs 1 game
        elif choice == "V" or choice == "v":
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


def AI_vs():
    """
    Sig:    None
    Pre:    None
    Post:   A game played against a computer controlled player
    """
    result = game.local_vs(["Player 1", "NPC"], [True, False])
    g.make_header(result + " has won!")


def local_vs():
    """
    Sig:    None
    Pre:    None
    Post:   A game played between between two humans
    """
    result = game.local_vs(["Player 1", "Player 2"], [True, True])
    g.make_header(result + " has won!")


def online_vs():
    """
    Sig:    None
    Pre:    None
    Post:   A game played between against a remote player
    """
    while True:
        choice = input("Do you wish to act as server? [" + g.color("G", "Y") + "]es [" \
                       + g.color("R", "N") + "]no\n[" + g.color("R", "Q") + "]uit ")
        if choice == "Y" or choice == "y":
            # Create peer which will act as server
            c = peer.Peer(True)
            c.accept_client()
            # Name, peer, Human = True, Server = True
            win = game.online_vs("Player 1", c, True, True)
            if win:
                g.make_header("You've won!")
            else: g.make_header("You've lost!")
            c.teardown()
            break

        elif choice == "N" or choice == "n":
            # Create peer which will act as client
            c = peer.Peer(False)
            c.connect_to_server()
            # Name, peer, Human = True, Server = False
            win = game.online_vs("Player 2", c, True, False)
            if win:
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
    player_list = [] # Strings of names
    human_dict = {}  # Booleans. Key = player. True = Human, False = NPC

    # Determine players
    g.make_header("Tournament play!")
    while True:
        choice = input("How many players? [" + g.color("G", "3-8") + "] ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice > 2 and choice < 9:
                break

    # Determine names and human/computer controlled
    for player in range(choice):
        name = input("Name player " + str(player+1) + ": ")
        while True:
            human = input("Is this a human player? [" + g.color("G", "Y") + "/" + g.color("R", "N") + "]")
            if human == "Y" or human == "y":
                human = True
                break
            if human == "n" or human == "n":
                human = False
                break

        player_list.append(name)
        human_dict[name] = human

    # Play tournament
    t = tour.Tournament(player_list)
    while True:
        g.make_header("Tournament Standings")
        print(t.get_bracket())
        match = t.get_next_game()
        if match == "END":
            break
        else:
            players = match.get_players()
            g.make_header("Up next: " + players[0] + " vs " + players[1])
            humans = [human_dict[players[0]], human_dict[players[1]]]
            winner = game.local_vs(players, humans)
            t.set_winner(match, winner)
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
        choice = input("Do you wish to act as server? [" + g.color("G", "Y") + "]es ["\
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
    """
    # Setup
    c = peer.Peer(True)
    c.accept_client()
    plist, hdict = decide_online_tour_players(c)
    print("Waiting for remote list of players...")
    remote_plist = c.receive()
    t = tour.Tournament(plist + remote_plist)
    data = {}                      # Dictionary containing various data needed by remote peer
    data["instruction"] = None     # Instructions in the form of strings
    data["player"] = None          # Player or players to play next game
    data["tour"] = t.get_bracket() # String representing current tournament bracket
    c.send(data)                   # Send initial tournament bracket
    c.receive()                    # Receive acknowledgement, to sync with remote

    while True:
        g.make_header("Tournament Standings")
        print(t.get_bracket())
        data["tour"] = t.get_bracket()
        match = t.get_next_game()  # Get and check if there are more games to be played
        if match == "END":
            data["instruction"] = "COMPLETE"
            data["player"] = winner
            c.send(data)
            g.make_header(winner + " Has won the tournament!")
            c.teardown()
            sys.exit()

        else:
            players = match.get_players()
            g.make_header("Up next: " + players[0] + " vs " + players[1])
            if players[0] in plist and players[1] in plist:       # If both players are local
                # Local game
                data["instruction"] = "WAIT"
                c.send(data)
                humans = [hdict[players[0]], hdict[players[1]]]
                winner = game.local_vs(players, humans)
                t.set_winner(match, winner)
                g.make_header(winner + " has advanced to the next round!")

            elif players[0] in plist and players[1] not in plist: # If one player is remote
                # Cross play game
                data["instruction"] = "XPLAY"
                data["player"] = players[1]
                c.send(data)
                winner = game.online_vs(players[0], c, hdict[players[0]], True)
                if winner:
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")
                else:
                    winner = players[1]
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")

            elif players[0] not in plist and players[1] in plist: # If one player is remote
                # Cross play game
                data["instruction"] = "XPLAY"
                data["player"] = players[0]
                c.send(data)
                winner = game.online_vs(players[1], c, hdict[players[1]], True)
                if winner:
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")
                else:
                    winner = players[0]
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")

            elif players[0] not in plist and players[1] not in plist: # If both players are remote
                # Remote game
                data["instruction"] = "PLAY"
                data["player"] = players
                print("Waiting for remote game to conclude...")
                c.send(data)
                winner = c.receive()
                t.set_winner(match, winner)
                g.make_header(winner + " has advanced to the next round!")
            else:
                raise Exception("Cant find player")


def client_side_tournament():
    """
    Sig:    None
    Pre:    None
    Post:   A tournament played between local, and remote players. And termination of program
    """
    # Setup
    c = peer.Peer(False)
    c.connect_to_server()
    player_list, human_dict = decide_online_tour_players(c)
    c.send(player_list)                # Full player list needed by server in order to set up tournament
    data = c.receive()                 # Receive initial tournament bracket
    c.send("ACK")                      # Sync with remote

    while True:
        data = c.receive()             # Get instructions
        g.make_header("Tournament Standings")
        print(data["tour"])
        if data["instruction"] == "WAIT":
            # Remote game
            print("Waiting for remote game to conclude...")
            continue

        elif data["instruction"] == "XPLAY":
            # Cross play game
            print("Starting online game...")
            winner = game.online_vs(data["player"], c, human_dict[data["player"]], False)
            if winner:
                g.make_header(winner + " has advanced to the next round!")
            else:
                g.make_header("Remote player advanced to the next round!")

        elif data["instruction"] == "PLAY":
            # Local game
            humans = [human_dict[data["player"][0]], human_dict[data["player"][1]]]
            winner = game.local_vs(data["player"], humans)
            g.make_header(winner + " has advanced to the next round!")
            c.send(winner)
            print("Sent", winner)

        elif data["instruction"] == "COMPLETE":
            g.make_header(data["player"] + " has won the tournament!")
            c.teardown()
            sys.exit()

        else:
            raise Exception("Invalid instructions recived from server:", data["instruction"])


def decide_online_tour_players(c):
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
        decide_online_tour_players(c, server)


    player_list = [] # Strings of names
    human_dict = {}  # Booleans. Key = player. True = Human, False = NPC
    # Determine names and human/computer controlled
    for player in range(choice):
        name = input("Name player " + str(player+1) + ": ")
        while True:
            human = input("Is this a human player? [" + g.color("G", "Y") + "/" + g.color("R", "N") + "]")
            if human == "Y" or human == "y":
                human = True
                break
            if human == "n" or human == "n":
                human = False
                break

        player_list.append(name)
        human_dict[name] = human

    return player_list, human_dict


if __name__ == '__main__':
    main()
