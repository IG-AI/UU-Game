import sys
import random
import client
import time as t

def local_vs(players, humans):
    """
    Simulates a local game.
    players : array
        List of strings, which represents the players
    humans : array
        List of booleans, representing whether players are human or NPC
    """
    if humans[0]:
        tmp = "tmp" # Make player 1 NPC
    elif humans[1]:
        tmp = "tmp" # Make player 2 NPC

    outcome = random.randrange(2)
    print("Simulating local game...")
    t.sleep(2)
    if outcome == 1:
        return players[0]
    else: return players[1]

def online_vs(nick, c, human, server):
    """
    Simulates an online game
    nick : string
        String representing local player's name
    c : Peer
        Class Peer, connection with remote player
    human : Boolean
        True = Human player, False = NPC player
    server : Boolean
        Whether this player acts as server or not. Needed in order to properly synchronize peers

    Notes
    -----
    The order of these events must be strictly kept in order for the connections to remain properly \
    synchronized. This order is:

    Server:
    Determine whether starting or not, and send this to client
    Wait for acknowledgement
    Wait for gamestate if not first, otherwise determine first gamestate
    REPEAT HERE
    determine if remote player has won, return if true
    update game state
    check if local player has won, send game state if true and return
    send game state
    receive remote game state
    loop from REPEAT HERE

    client:
    receive whether starting or not
    send acknowledgement
    wait for gamestate if not first, otherwise determine first gamestate
    REPEAT HERE
    determine if remote player has won, return if true
    update game state
    check if local player has won, send game state if true and return
    send game state
    receive remote game state
    loop from REPEAT HERE
    """
    starting_player = None
    if not human:
        tmp = "tmp" # Make this player NPC

    t.sleep(2)
    # Decide starting player
    if server:
        i = random.randint(0,1)
        if i == 1:
            starting_player = True
            c.send("WAIT")
            c.receive()
        else:
            starting_player = False
            c.send("START")
            c.receive()
    else:
        ack = c.receive()
        if ack == "WAIT":
            starting_player = False
            c.send("ACK")
            game_state = c.receive()
        else:
            starting_player = True
            c.send("ACK")
            game_state = [0, 0]

    if server and starting_player:
        game_state = [0, 0]
    elif server and not starting_player:
        print("Waiting to receive first gamestate")
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
                return nick

        if game_state[1] > win_limit:
            if not starting_player:
                c.send(game_state)
                return nick

        print(nick, "sent", game_state)
        c.send(game_state)
        game_state = c.receive()
        print(nick, "received", game_state)
        t.sleep(0.1)
        score = 0
        i += 1
