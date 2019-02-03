import random
import client
import time as t

def vs_AI():
    return "A game against AI has been played!"

def local_vs(player_1, player_2):
    outcome = random.randrange(2)
    if outcome == 1:
        return player_1 + " has won!"
    else: return player_2 + " has won!"

def online_vs(nick, c):
    c.send("ACK")
    tmp = c.receive()
    print(nick, "initial receive:", tmp)
    if tmp == "FIRST":
        game_state = [0, 0]
        starting_player = True
    else:
        game_state = tmp
        starting_player = False
    i = 0
    score = 0
    win_limit = 20

    while i < 100:
        if game_state[0] > win_limit:
            if not starting_player:
                return "You've lost!"

        if game_state[1] > win_limit:
            if starting_player:
                return "You've lost!"

        score += random.randrange(5)
        if starting_player: game_state[0] += score
        else: game_state[1] += score

        if game_state[0] > win_limit:
            if starting_player:
                c.send(["WIN", game_state])
                return "You've won!"

        if game_state[1] > win_limit:
            if not starting_player:
                c.send(["WIN", game_state])
                return "You've won!"

        print(nick, "sent", game_state)
        c.send(game_state)
        game_state = c.receive()
        print(nick, "received", game_state)
        t.sleep(0.1)
        score = 0
        i += 1

