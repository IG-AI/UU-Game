from random import random

class Tournament:
    # Initialize the tournament class, with a list of players as input.
    # To get the opponents do as follows: tournament1 = Tournament(player_list), opponents = tournament1.opponent_list
    def __init__(self, player_list):
        self.player_list = player_list
        self.opponent_list = choose_players(self.player_list)

    # Receives the winners in the form of a list from the client and updates the opponent_list with new opponents.
    # To get new opponents do as follows: tournament1.set_winner(winner_list), opponents = tournament1.opponent_list
    def set_winner(self, winner_list):
        self.player_list = self.player_list + winner_list
        if len(self.player_list) <= 1:
            print('The winner is: ')
            print("Player ", self.player_list[0])
            print(' Congratulations!')
            return ()
        self.opponent_list = choose_players(self.player_list)

# Helps the class to select the opponents and then update the opponent_list in the class.
def choose_players(player_list):
    opponent_list = []
    player_number = len(player_list)
    if player_number % 2 == 0:
        for i in range(int(player_number / 2)):
            player1 = random.choice(player_list)
            player_list.remove(player1)
            player2 = random.choice(player_list)
            player_list.remove(player2)
            opponent = [player1, player2]
            opponent_list.append(opponent)
        return opponent_list
    else:
        player1 = random.choice(player_list)
        player_list.remove(player1)
        player2 = random.choice(player_list)
        player_list.remove(player2)
        opponent = [player1, player2]
        opponent_list.append(opponent)
        return opponent_list


