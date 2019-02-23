import sys
import time

from game_engine.play import Play
from game_engine.player_human import PlayerHuman
from communication_platform import graphics as g

def local(players, humans):
    driver = Play()

    if not humans[0] and not humans[1]:
        driver.init_players(3, 2, players[0], players[1])

    elif humans[0] and not humans[1]:
        driver.init_players(2, 2, players[0], players[1])

    elif not humans[0] and humans[1]:
        driver.init_players(2, 2, players[1], players[0])

    elif humans[0] and humans[1]:
        driver.init_players(1, 2, players[0], players[1])

    else:
        print("Invalid configuration of players", players, humans)
        raise(Exception)

    winner = run_local_game(driver)
    if winner:
        return winner
    else:
        return local(players, humans)

def online(players, humans, c, server):
    if server:
        driver = Play()
        if not humans[0] and not humans[1]:
            driver.init_players(3, 2, players[0], players[1])

        elif humans[0] and not humans[1]:
            driver.init_players(2, 2, players[0], players[1])

        elif not humans[0] and humans[1]:
            driver.init_players(2, 2, players[1], players[0])

        elif humans[0] and humans[1]:
            driver.init_players(1, 2, players[0], players[1])
            
        else:
            print("Invalid configuration of players", players, humans)
            raise(Exception)

        if driver.current_player.name == players[0]: # If starting player
            c.send(False)
            time.sleep(0.2)
            winner = run_online_game(driver, c, True)
        else:
            c.send(True)
            time.sleep(0.2)
            c.send(driver)
            print("Waiting for remote to start game...")
            driver = c.receive()
            winner = run_online_game(driver, c, False)

        return winner

    else:
        print("Waiting for remote to start game...")
        starting = c.receive()
        driver = c.receive()
        winner = run_online_game(driver, c, starting)
        return winner

    return "DRAW"

def run_local_game(driver):
    display_pieces(driver)
    display_gameboard(driver)

    # Give piece
    if isinstance(driver.current_player, PlayerHuman):    # If human
        while True:
            pce = input("\nPlayer " + driver.current_player.name + " select a piece [0-15]: ")

            if driver.play_selection(pce):
                break
    else:                                                 # If AI
        print("\nPlayer "+ driver.current_player.name + " selecting a piece")
        driver.play_selection()

    # Place piece
    if isinstance(driver.current_player, PlayerHuman):    # If human
        print("\nPlayer " + driver.current_player.name + ", place piece: " + driver.selected_piece)
        while True:
            try:
                y, x = input("\nEnter row and column [row] [column]: ").\
                    split()

                if driver.play_placement(y, x):
                    break
                print("\nInvalid! Try again. Example input: 0 0")
            except:
                continue
    else:                                                 # If AI
        print("\nPlayer " + driver.current_player.name + " placing piece: " + driver.selected_piece)
        driver.play_placement()

    # Determine game status
    if driver.game.has_won_game(driver.selected_piece):   # Won game
        display_gameboard(driver)
        print("\nGame won by: " + driver.current_player.name)
        return driver.current_player.name
    elif not driver.game.has_next_play():                 # Draw
        display_gameboard(driver)
        print("Game draw! Replay game")
        return False
    else:
        return run_local_game(driver)

def run_online_game(driver, c, starting):
    if starting:
        dispay(driver)
        driver = give_piece(driver)
        c.send(driver)
        driver = c.receive()

    while type(driver) != str:
        dispay(driver)
        driver = place_piece(driver)
        display_gameboard(driver)
        win = check_win(driver)
        if win:
            c.send(win)
            break
        driver = give_piece(driver)
        time.sleep(0.2)
        c.send(driver)
        print("Waiting for remote to play...")
        driver = c.receive()

    return win

def give_piece(driver):
    if isinstance(driver.current_player, PlayerHuman):    # If human
        while True:
            pce = input("\nPlayer " + driver.current_player.name + " select a piece [0-15]: ")

            if driver.play_selection(pce):
                break
    else:                                                 # If AI
        print("\nPlayer "+ driver.current_player.name)
        driver.play_selection()
        print("selected piece " + g.color("G", driver.selected_piece))

    return driver

def place_piece(driver):
    if isinstance(driver.current_player, PlayerHuman):    # If human
        print("\nPlayer " + driver.current_player.name + ", place piece: "\
            + g.color("G", driver.selected_piece))
        while True:
            try:
                y, x = input("\nEnter row and column [row] [column]: ").\
                    split()

                if driver.play_placement(y, x):
                    break
                print("\nInvalid! Try again. Example input: 0 0")
            except:
                continue
    else:                                                 # If AI
        print("\nPlayer " + driver.current_player.name + " placing piece: "\
            + g.color("G", driver.selected_piece))
        driver.play_placement()

    return driver

def check_win(driver):
    if driver.game.has_won_game(driver.selected_piece):   # Won game
        return driver.current_player.name
    elif not driver.game.has_next_play():                 # Draw
        display_gameboard(driver)
        print("Game draw! Replay game")
        return False
    else:
        return False

def dispay(driver):
    display_pieces(driver)
    display_gameboard(driver)

def display_pieces(driver):
    pieces = list(driver.game.pieces.items())
    switch = False
    print("\n")
    output = ""
    for pce in pieces:
        output += "{:>20}".format("[" + g.color("G", pce[0]) + "]: " + pce[1] + " ")
        if switch:
            print(output)
            output = ""
            switch = False
        else:
            switch = True
    print(output)

def display_gameboard(driver):
    i = 0
    print("\n [" + g.color("G", "0") + "]  [" + g.color("G", "1") + \
        "]  [" + g.color("G", "2") + "]  [" + g.color("G", "3") + "] ")
    for row in driver.game.board:
        output = ""
        for piece in row:
            if piece:
                output += piece + " "
            else:
                output += "____ "
        output += " [" + g.color("G", str(i)) + "]"
        i += 1
        print(output)


if __name__ == '__main__':
    sys.exit()