import sys
import random
import client
import time as t

def local_vs(player_1, player_2, humans):
    if humans[0]:
        tmp = "tmp" # Make player 1 NPC
    elif humans[1]:
        tmp = "tmp" # Make player 2 NPC

    outcome = random.randrange(2)
    if outcome == 1:
        return player_1
    else: return player_2

def online_vs(nick, c, human, server):
    starting_player = None
    if not human:
        tmp = "tmp" # Make this player NPC

    # Decide starting player
    if server:
        i = random.randint(0,1)
        if i == 1:
            starting_player = True
            c.send("WAIT")
        else:
            starting_player = False
            c.send("START")
    else:
        ack = c.receive()
        if ack == "WAIT":
            starting_player = False
            game_state = c.receive()
        else:
            starting_player = False
            game_state = [0, 0]

    if server and starting_player:
        game_state = [0, 0]
    elif server and not starting_player:
        game_state = c.receive()

    # Simulate game
    i = 0
    score = 0
    win_limit = 30

    while i < 100:
        if game_state[0] > win_limit:
            if not starting_player:
                return False

        if game_state[1] > win_limit:
            if starting_player:
                return False

        score += random.randint(1,5)
        side = random.randint(0,1)
        game_state[side] += score

        if game_state[0] > win_limit:
            if starting_player:
                c.send(game_state)
                return True

        if game_state[1] > win_limit:
            if not starting_player:
                c.send(game_state)
                return True

        print(nick, "sent", game_state)
        c.send(game_state)
        game_state = c.receive()
        print(nick, "received", game_state)
        t.sleep(0.1)
        score = 0
        i += 1
