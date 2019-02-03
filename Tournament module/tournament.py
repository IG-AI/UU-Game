import random

class Tournament:
    # Initialize the tournament class, with a list of players as input.
    # To get the opponents do as follows: tournament1 = Tournament(player_list), opponents = tournament1.opponent_list
    def __init__(self, player_list):
        self.current_player_list = player_list # List with the current players in the tournament
        self.start_player_list = player_list # List with all players
        self.winner_list = [] # Lists in list with the wining players from each game iteration
        self.opponents_list = choose_players_list(self.current_player_list) # List with the current opponents

    # Receives the winners in the form of a list from the client and updates the opponent_list with new opponents.
    # To get new opponents do as follows: tournament1.set_winner(winner_list), opponents = tournament1.opponent_list
    def update_opponents(self, winner_list):
        self.winner_list.append(winner_list)
        self.current_player_list = self.current_player_list + winner_list
        if len(self.current_player_list) <= 1:
            print('The winner is: ')
            print("Player ", self.current_player_list[0])
            print(' Congratulations!')
            self.opponents_list = [self.current_player_list]
            return ()
        self.opponents_list = choose_players_list(self.current_player_list)

# Helps the class to select two opponents and then update the opponent_list in the class.
def choose_two_players(player_list):
    opponents_list = []
    player1 = random.choice(player_list)
    player_list.remove(player1)
    player2 = random.choice(player_list)
    player_list.remove(player2)
    opponents = [player1, player2]
    opponents_list.append(opponents)
    return opponents_list

# Helps the class to select a list with opponents and then update the opponent_list in the class.
def choose_players_list(player_list):
    opponents_list = []
    player_number = len(player_list)
    if player_number % 2 == 0:
        for i in range(int(player_number / 2)):
            player1 = random.choice(player_list)
            player_list.remove(player1)
            player2 = random.choice(player_list)
            player_list.remove(player2)
            opponents = [player1, player2]
            opponents_list.append(opponents)
        return opponents_list
    else:
        player1 = random.choice(player_list)
        player_list.remove(player1)
        player2 = random.choice(player_list)
        player_list.remove(player2)
        opponents = [player1, player2]
        opponents_list.append(opponents)
        return opponents_list

if __name__ == "__main__":
    Tournament()