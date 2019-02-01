import random
import client
import time as t

def vs_AI():
    print("A game against AI has been played!")

def local_vs(player_1, player_2):
    outcome = random.randrange(2)
    print("A game between two players has been played! Player:", outcome, "won!")
    if outcome == 1:
        return player_1
    else: return player_2

def online_vs(nick, starting_player):
    c = client.Client(nick)
    game_state = [0, 0]
    i = 0
    score = 0
    if not starting_player:
        print(nick, "initial receive:")
        game_state = c.receive()
        print(game_state)
    while i < 20:
        score += random.randrange(5)

        if starting_player: game_state[0] += score
        else: game_state[1] += score

        print(nick, "sent", game_state)
        c.send(game_state)
        game_state = c.receive()
        print(nick, "received", game_state)
        t.sleep(0.1)
        score = 0
        i += 1

