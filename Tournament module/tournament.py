import random

class Tournament:
    winner_state = 0 # Flag that indicate if the tournament is finish or not.

    # Initialize the tournament class, with a list of players as input.
    # To get the opponents do as follows: tournament1 = Tournament(player_list), opponents = tournament1.opponent_list
    def __init__(self, player_list):
        self.current_player_list = player_list # List with the current players in the tournament
        self.start_player_list = player_list # List with all players
        self.winner_list = [] # Lists in list with the wining players from each game iteration
        copy_player_list = player_list.copy()
        self.opponents_list = make_opponents_list(copy_player_list)  # List with the current opponents
        self.opponents = self.opponents_list.pop(0)
        self.current_player_list.remove(self.opponents[0])
        self.current_player_list.remove(self.opponents[1])

    # Update the variable opponents. If the opponents_list is empty, the functions calls make_opponents_list to update
    # the opponents_list. If the current_player_list becomes equal to 1 and the winner_list becomes equal to 1 the
    # winner_state flags changes and a empty list is set to the variable opponents
    def get_opponents(self, winner):
        winner_list = [winner]
        if winner_list != []:
            self.winner_list.append(winner)
        if not self.opponents_list:
            self.current_player_list = self.current_player_list + self.winner_list
            self.opponents_list = make_opponents_list(self.winner_list)
        if len(self.current_player_list) == 1 & len(self.winner_list) == 1:
            self.winner_state = 1
            self.opponents = []
            return ()
        self.current_player_list.remove(self.opponents_list[0][0])
        self.current_player_list.remove(self.opponents_list[0][1])
        self.opponents = self.opponents_list.pop(0)

# Helps the class to make the opponents_list
def make_opponents_list(player_list):
    opponents_list = []
    player_number = len(player_list)
    for i in range(int(player_number / 2)):
        player1 = random.choice(player_list)
        player_list.remove(player1)
        player2 = random.choice(player_list)
        player_list.remove(player2)
        opponents = [player1, player2]
        opponents_list.append(opponents)
    return opponents_list

if __name__ == "__main__":
    Tournament()