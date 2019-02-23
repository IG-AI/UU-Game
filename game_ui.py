import sys
import time

from game_engine.play import Play
from game_engine.player_human import PlayerHuman

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
            print("Starting player")
            c.send(False)
            time.sleep(0.2)
            winner = run_online_game(driver, c, True)
        else:
            print("Not starting player, True")
            c.send(True)
            time.sleep(0.2)
            print("Sending game")
            c.send(driver)
            print("Waiting for game")
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
        print("Running as starting player")
        dispay(driver)
        print("\nCurrent = " + driver.current_player.name)
        driver = give_piece(driver)
        c.send(driver)
        print("Waiting for remote to play...")
        driver = c.receive()

    while type(driver) != str:
        dispay(driver)
        print("\nCurrent = " + driver.current_player.name)
        driver = place_piece(driver)
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
        print("selected piece " + driver.selected_piece)

    return driver

def place_piece(driver):
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

    return driver

def check_win(driver):
    if driver.game.has_won_game(driver.selected_piece):   # Won game
        display_gameboard(driver)
        print("\nGame won by: " + driver.current_player.name)
        return driver.current_player.name
    elif not driver.game.has_next_play():                 # Draw
        display_gameboard(driver)
        print("Game draw! Replay game")
        return False
    else:
        return False

def run_online_game2(driver, c):
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
        c.send(driver.current_player.name)
        return driver.current_player.name
    elif not driver.game.has_next_play():                 # Draw
        display_gameboard(driver)
        print("Game draw! Replay game")
        return False
    else:
        print("Sent game")
        c.send(driver)
        print("Waiting for remote game")
        driver_or_winner = c.receive()
        if type(driver_or_winner) != str:
            return run_online_game2(driver_or_winner, c)
        else:
            return driver


def dispay(driver):
    display_pieces(driver)
    display_gameboard(driver)

def display_pieces(driver):
    print("\nGame pieces available:")
    print(list(driver.game.pieces.items())[:int((len(driver.game.pieces) + 1) / 2)])

    if len(driver.game.pieces) > 1:
        print(list(driver.game.pieces.items())[int((len(driver.game.pieces) + 1) / 2):])

def display_gameboard(driver):
    print("\nGame board status:")
    print(*(row for row in driver.game.board), sep="\n")

if __name__ == '__main__':
    sys.exit()