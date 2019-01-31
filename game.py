import random

def vs_AI():
    print("A game against AI has been played!")

def vs_player(player_1, player_2):
    outcome = random.randrange(2)
    print("A game between two players has been played! Player:", outcome, "won!")
    if outcome == 1:
        return player_1
    else: return player_2
