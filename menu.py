#!/usr/bin/env python3

import sys
import time as t
import random
import game, server, client, peer
import graphics as g
import tournament as tour


def main():
    menu_options()
    g.make_header("Thanks for playing!")

def menu_options():
    playing = True
    while playing:
        g.make_header("Welcome to <game>!")
        print("You have the following options:\n" + "[" + g.color("G", "S") + "]ingle player\n1[" + g.color("G", "v")\
              + "]s1\n["  + g.color("G", "T") + "]ournament\n[" + g.color("R", "Q") + "]uit ")
        choice = input("Please make your " + g.color("G", "choice: "))

        if choice == "S" or choice == "s":
            AI_vs()
            break

        elif choice == "V" or choice == "v":
            while True:
                print("Do you wish to play [" + g.color("G", "L") + "]ocal or [" + g.color("G", "O") + "]nline?\n["\
                      + g.color("R", "R") + "]eturn to previous options\n[" + g.color("R", "Q") + "]uit ")
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

                elif choice == "Q" or choice == "q":
                    sys.exit()

                else: print("Invalid choice, try again")

        elif choice == "T" or choice == "t":
            while True:
                print("Do you wish to play [" + g.color("G", "L") + "]ocal or [" + g.color("G", "O") + "]nline?\n["\
                      + g.color("R", "R") + "]eturn to previous options\n[" + g.color("R", "Q") + "]uit ")
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

                elif choice == "Q" or choice == "q":
                    sys.exit()

                else: print("Invalid choice, try again")

        elif choice == "Q" or choice == "q":
            sys.exit()

        else: print("Invalid choice, try again")


def AI_vs():
    result = game.local_vs(["Player 1", "NPC"], [True, False])
    g.make_header(result + " has won!")


def local_vs():
    result = game.local_vs(["Player 1", "Player 2"], [True, True])
    g.make_header(result + " has won!")


def online_vs():
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
    player_list = []
    human_dict = {}

    g.make_header("Tournament play!")
    while True:
        choice = input("How many players? [" + g.color("G", "3-8") + "] ")
        if type(int(choice)) == int:
            choice = int(choice)
            if choice > 2 and choice < 9:
                break

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

    # Shortcut for testing
    '''
    plist = ['ErikO', 'Daniel', 'Nicole', 'ErikL', 'Davide', 'Sam', 'Kevin', 'Viktor']
    hlist = [True, True, False, True, False, False, True, False]
    for i in range(choice):
        player_list.append(plist[i])
        human_dict[player_list[i]] = hlist[i]
    '''

    t = tour.Tournament(player_list)
    while True:
        g.make_header("Tournament Standings")
        print(t.get_bracket())
        match = t.get_next_game()
        if match == "END":
            break
        else:
            players = match.get_players()
            humans = [human_dict[players[0]], human_dict[players[1]]]
            winner = game.local_vs(players, humans)
            t.set_winner(match, winner)
            g.make_header(winner + " has advanced to the next round!")

    g.make_header(winner + " has won the tournament!")
    sys.exit()


def online_tour_play():
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
    # Setup
    c = peer.Peer(True)
    c.accept_client()
    plist, hdict = decide_online_tour_players(c, False, True)
    print("Waiting for remote list of players...")
    remote_plist = c.receive()
    t = tour.Tournament(plist + remote_plist)
    # Dict sent to client-side containing instructions
    data = {}
    data["instruction"] = None
    data["player"] = None
    data["tour"] = t.get_bracket()
    c.send(data)
    print("Sent", data)
    c.receive()
    print("Recieved ACK")

    while True:
        g.make_header("Tournament Standings")
        print(t.get_bracket())
        data["tour"] = t.get_bracket()
        match = t.get_next_game()
        if match == "END":
            data["instruction"] = "COMPLETE"
            data["player"] = winner
            c.send(data)
            g.make_header(winner + " Has won the tournament!")
            c.teardown()
            sys.exit()

        else:
            players = match.get_players()
            print("Up next:", players)
            if players[0] in plist and players[1] in plist:
                # Local game
                data["instruction"] = "WAIT"
                c.send(data)
                print("Sent", data)
                humans = [hdict[players[0]], hdict[players[1]]]
                winner = game.local_vs(players, humans)
                t.set_winner(match, winner)
                g.make_header(winner + " has advanced to the next round!")

            elif players[0] in plist and players[1] not in plist:
                # Cross play game
                data["instruction"] = "XPLAY"
                data["player"] = players[1]
                c.send(data)
                print("Sent", data)
                winner = game.online_vs(players[0], c, hdict[players[0]], True)
                if winner:
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")
                else:
                    winner = players[1]
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")

            elif players[0] not in plist and players[1] in plist:
                # Cross play game
                data["instruction"] = "XPLAY"
                data["player"] = players[0]
                c.send(data)
                print("Sent", data)
                winner = game.online_vs(players[1], c, hdict[players[1]], True)
                if winner:
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")
                else:
                    winner = players[0]
                    t.set_winner(match, winner)
                    g.make_header(winner + " has advanced to the next round!")

            elif players[0] not in plist and players[1] not in plist:
                # Remote game
                data["instruction"] = "PLAY"
                data["player"] = players
                print("Waiting for remote game to conclude...")
                c.send(data)
                print("Sent", data)
                winner = c.receive()
                t.set_winner(match, winner)
                g.make_header(winner + " has advanced to the next round!")
            else:
                raise Exception("Cant find player")


def client_side_tournament():
    # Setup
    c = peer.Peer(False)
    c.connect_to_server()
    player_list, human_dict = decide_online_tour_players(c, False, False)
    c.send(player_list)
    data = c.receive()
    print("Recieved", data)
    c.send("ACK")
    print("Sent ACK")

    while True:
        print("Waiting to receive")
        data = c.receive()
        print("Recieved:", data)
        g.make_header("Tournament Standings")
        print(data["tour"])
        if data["instruction"] == "WAIT":
            print("Waiting for remote game to conclude...")
            continue

        elif data["instruction"] == "XPLAY":
            print("Starting online game...")
            winner = game.online_vs(data["player"], c, human_dict[data["player"]], False)
            if winner:
                g.make_header(winner + " has advanced to the next round!")

        elif data["instruction"] == "PLAY":
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


def decide_online_tour_players(c, debug, first):
    if debug:
        if first:
            player_list = ["ErikS", "JohanS", "ViktorS"]
            human_dict = {}
            for name in player_list:
                human_dict[name] = True

            return player_list, human_dict
        else:
            player_list = ["DanielC", "DavideC", "SamC", "PizzaC", "NicoleC"]
            human_dict = {}
            for name in player_list:
                human_dict[name] = True

            return player_list, human_dict

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
    human_dict = {}
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
