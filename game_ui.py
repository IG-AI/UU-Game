import sys

from game_engine.play import Play
from game_engine.player_human import PlayerHuman

def local(players, humans):
    print("GAME UI")
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

    winner = run_game(driver)
    if winner:
        return winner
    else:
        return local(players, humans)

def run_game(driver):
    display_pieces(driver)
    display_gameboard(driver)
    #print("\nPlayer " + driver.current_player.name)

    # Give piece
    if isinstance(driver.current_player, PlayerHuman):    # If human
        while True:
            pce = input("\nPlayer " + driver.current_player.name + " select a piece [0-15]: ")

            if driver.play_selection(pce):
                break
    else:                                                 # If AI
        print("\nPlayer "+ driver.current_player.name + " selecting a piece")
        driver.play_selection()

    if isinstance(driver.current_player, PlayerHuman): # If human
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

    if driver.game.has_won_game(driver.selected_piece):   # Won game
        display_gameboard(driver)
        print("\nGame won by: " + driver.current_player.name)
        return driver.current_player.name
    elif not driver.game.has_next_play():                 # Draw
        display_gameboard(driver)
        print("Game draw! Replay game")
        return False
    else:
        return run_game(driver)

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