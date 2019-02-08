import random

class Tournament:
    tournament_depth = 0 # Numbers of game iteration.
    winner_state = 0 # Flag that indicate if the tournament is finish or not.
    winner_list = []  # Lists in list with the wining players from each game iteration.
    winner_list_temp = [] # List with the wining players from the active game iteration.

    # Initialize the tournament class, with a list of players as input.
    # To get the opponents do as follows: tournament1 = Tournament(player_list), opponents = tournament1.opponent_list
    def __init__(self, player_list):
        if (len(player_list) > 3) & (len(player_list) > 8):
            raise Exception("Error: It has to be between 3 - 8 players!")
        self.waiting_players = player_list.copy() # List with the current players in the tournament
        self.start_player_list = player_list.copy() # List with all players
        player_list_copy = player_list.copy()
        if ((len(player_list) % 2) == 0) | (len(player_list) == 3):
            self.opponents_queue = make_opponents(player_list_copy)  # List with the current opponents
            self.all_opponents = [self.opponents_queue.copy()]
            self.opponents = self.opponents_queue.pop(0)
            self.waiting_players.remove(self.opponents[0])
            self.waiting_players.remove(self.opponents[1])
            for i in range(len(self.opponents_queue)):
                self.waiting_players.remove(self.opponents_queue[i][0])
                self.waiting_players.remove(self.opponents_queue[i][1])
        else:
            player1 = random.choice(self.waiting_players)
            self.waiting_players.remove(player1)
            player2 = random.choice(self.waiting_players)
            self.waiting_players.remove(player2)
            self.opponents = [player1, player2]
            self.opponents_queue = []
            self.all_opponents = [self.opponents.copy()]

    # Update the variable opponents and adds the winner to the winner list. If the opponents_list is empty, the function calls update_opponents_list to update
    # the opponents_list. If the current_player_list becomes equal to 1 and the winner_list becomes equal to 1 the
    # winner_state flags changes and a empty list is set to the variable opponents
    def next_game(self, winner):
        self.winner_list_temp.append(winner)
        if not self.opponents_queue:
            self.winner_list.append(self.winner_list_temp)
            self.opponents_queue = update_opponents(self.winner_list_temp, self.waiting_players)
            if len(self.waiting_players) % 2 == 1:
                self.waiting_players.remove(self.opponents[1])
            opponents_list_copy = self.opponents_queue.copy()
            self.all_opponents.append(opponents_list_copy)
            self.tournament_depth += 1
            self.winner_list_temp = []
        if self.winner_list:
            if len(self.winner_list[self.tournament_depth - 1]) == 3:
                player1 = self.winner_list[self.tournament_depth - 1][0]
                player2 = self.winner_list[self.tournament_depth - 1][1]
                self.waiting_players.append(self.winner_list[self.tournament_depth - 1][-1])
                self.opponents_queue = [[player1, player2]]
            elif ((len(self.winner_list[self.tournament_depth - 1]) == 1) & (len(self.start_player_list) == 3)) | \
                    ((len(self.winner_list[self.tournament_depth - 1]) == 2) & (len(self.winner_list_temp) == 0)) | \
                    ((len(self.winner_list[self.tournament_depth - 1]) == 1) & (len(self.winner_list_temp) == 0) &
                         (len(self.all_opponents[self.tournament_depth]) != 2) & (len(self.all_opponents[self.tournament_depth]) != 3)):
                self.winner_list.append([winner])
                self.winner_state = 1
                self.opponents = []
                return ()
        self.opponents = self.opponents_queue[0]
        self.opponents_queue.remove(self.opponents)

    #Prints the scoreboard
    def print_scoreboard(self):
        cases = len(self.start_player_list)

        opponent03 = "NaN"
        opponent04 = "NaN"
        opponent05 = "NaN"
        opponent06 = "NaN"
        opponent07 = "NaN"
        opponent08 = "NaN"
        opponent09 = "NaN"
        opponent10 = "NaN"
        opponent11 = "NaN"
        opponent12 = "NaN"
        opponent13 = "NaN"
        opponent14 = "NaN"
        opponent15 = "NaN"
        opponent16 = "NaN"
        winner = "NaN"
        if cases == 3:
            print(self.all_opponents)
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            if len(self.all_opponents) == 2:
                opponent03 = self.all_opponents[1][0][0]
                opponent04 = self.all_opponents[1][0][1]
            if len(self.winner_list) == 2:
                winner = self.winner_list[1][0]

            print(opponent01, " ---|")
            print("                |---", opponent03, "---|")
            print(opponent02, " ---|                      |---", winner)
            print("                    ", opponent04, "---|")


        if cases == 4:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            opponent03 = self.all_opponents[0][1][0]
            opponent04 = self.all_opponents[0][1][1]
            if self.winner_list_temp:
                if len(self.winner_list_temp) == 1:
                    opponent05 = self.winner_list_temp[0]
                if len(self.winner_list) == 1:
                    winner = self.winner_list[1][0]
            if len(self.winner_list) == 2:
                opponent05 = self.winner_list[0][0]
                opponent06 = self.winner_list[0][1]
            if self.winner_state == 1:
                winner = self.winner_list[1][0]

            print(opponent01, " ---|")
            print("                |---", opponent05, "---|")
            print(opponent02, " ---|                      |")
            print("                                       |---", winner)
            print(opponent03, " ---|                      |")
            print("                |---", opponent06, "---|")
            print(opponent04, " ---|")

        if cases == 5:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            if len(self.all_opponents) == 2:
                print(self.opponents)
                print(self.opponents_queue)
                opponent03 = self.winner_list[0]
                opponent04 = self.waiting_players[0]
                opponent05 = self.opponents[0]
                opponent06 = self.opponents[1]
                opponent07 = self.opponents_queue[0][1]
                opponent08 = self.opponents_queue[0][0]
            if len(self.all_opponents) == 3:
                opponent01 = self.all_opponents[0][0][0]
                opponent02 = self.all_opponents[0][0][1]
                opponent03 = self.all_opponents[1][0][0]
                opponent04 = self.all_opponents[1][0][1]
                opponent05 = self.all_opponents[1][1][0]
                opponent06 = self.all_opponents[1][1][1]
                opponent07 = self.all_opponents[1][2][0]
                opponent08 = self.all_opponents[1][2][1]
                opponent09 = self.all_opponents[2][0][0]
                opponent10 = self.all_opponents[2][0][1]
            if len(self.all_opponents) == 4:
                opponent11 = self.opponents[0]
                opponent12 = self.opponents[1]
            if len(self.winner_list) == 4:
                winner = self.winner_list[3][0]

            print(opponent01, "---|")
            print("               |---", opponent03, "---|")
            print(opponent02, "---|                      |-------------------------", opponent11, " ---|")
            print("                   ", opponent04, "---|                                             |")
            print("                                                                                    |")
            print("                   ", opponent05, "---|                                             |---", winner)
            print("                                      |---", opponent09, "---|                      |")
            print("                   ", opponent06, "---|                      |                      |")
            print("                                                             |---", opponent12, "---|")
            print("                   ", opponent07, "---|                      |                      ")
            print("                                      |---", opponent10, "---|")
            print("                   ", opponent08, "---|")

        if cases == 6:
            opponent01 = self.all_opponents[0][0]
            opponent02 = self.all_opponents[0][1]
            opponent03 = self.all_opponents[0][0]
            opponent04 = self.all_opponents[0][1]
            opponent05 = self.all_opponents[0][0]
            opponent06 = self.all_opponents[0][1]
            if len(self.all_opponents) == 2:
                opponent07 = self.all_opponents[1][0][0]
                opponent08 = self.all_opponents[1][0][1]
            if len(self.all_opponents) == 3:
                opponent09 = self.all_opponents[2][0][0]
                opponent10 = self.all_opponents[2][0][1]
            if len(self.winner_list) == 3:
                winner = self.winner_list[2][0]


            print("", opponent01, "---|")
            print("                   |--------------------------", opponent09, "---|")
            print("", opponent02, "---|                                             |")
            print("                                                                 |")
            print("", opponent03, "---|                                             |---", winner)
            print("                   |---", opponent07, "---|                      |")
            print("", opponent04, "---|                      |                      |")
            print("                                          |---", opponent10, "---|")
            print("", opponent05, "---|                      |")
            print("                   |---", opponent08, "---|")
            print("", opponent06, "---|")

        if cases == 7:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            if len(self.all_opponents) == 2:
                opponent03 = self.all_opponents[1][0][0]
                opponent04 = self.all_opponents[1][0][1]
                opponent05 = self.all_opponents[1][1][0]
                opponent06 = self.all_opponents[1][1][1]
                opponent07 = self.all_opponents[1][2][0]
                opponent08 = self.all_opponents[1][2][1]
                opponent09 = self.all_opponents[1][3][0]
                opponent10 = self.all_opponents[1][3][1]
            if len(self.all_opponents) == 3:
                opponent11 = self.all_opponents[2][0][0]
                opponent12 = self.all_opponents[2][0][1]
                opponent13 = self.all_opponents[2][1][0]
                opponent14 = self.all_opponents[2][1][1]
            if len(self.all_opponents) == 4:
                opponent15 = self.all_opponents[3][0][0]
                opponent16 = self.all_opponents[3][0][1]
            if len(self.winner_list) == 4:
                winner = self.winner_list[3][0]

            print("", opponent01, "---|")
            print("                   |---", opponent03, "---|")
            print("", opponent02, "---|                      |---", opponent11, "---|")
            print("                       ", opponent04, "---|                      |")
            print("                                                                 |---", opponent15, "---|")
            print("                       ", opponent05, "---|                      |                      |")
            print("                                          |---", opponent12, "---|                      |")
            print("                       ", opponent06, "---|                                             |")
            print("                                                                                        |---", winner)
            print("                       ", opponent07, "---|                                             |")
            print("                                          |---", opponent13, "---|                      |")
            print("                       ", opponent08, "---|                      |                      |")
            print("                                                                 |---", opponent16, "---|")
            print("                       ", opponent09, "---|                      |")
            print("                                          |---", opponent14, "---|")
            print("                       ", opponent10, "---|")

        if cases == 8:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            opponent03 = self.all_opponents[0][1][0]
            opponent04 = self.all_opponents[0][1][1]
            opponent05 = self.all_opponents[0][2][0]
            opponent06 = self.all_opponents[0][2][1]
            opponent07 = self.all_opponents[0][3][0]
            opponent08 = self.all_opponents[0][3][1]
            if len(self.all_opponents) == 2:
                opponent09 = self.all_opponents[1][0][0]
                opponent10 = self.all_opponents[1][0][1]
                opponent11 = self.all_opponents[1][1][0]
                opponent12 = self.all_opponents[1][1][1]
            if len(self.all_opponents) == 3:
                opponent13 = self.all_opponents[2][0][0]
                opponent14 = self.all_opponents[2][0][1]
            if len(self.winner_list) == 3:
                winner = self.winner_list[2][0]

            print("", opponent01, "---|")
            print("                   |---", opponent09, "---|")
            print("", opponent02, "---|                      |")
            print("                                          |---", opponent13, "---|")
            print("", opponent03, "---|                      |                      |")
            print("                   |---", opponent10, "---|                      |")
            print("", opponent04, "---|                                             |")
            print("                                                                 |---", winner)
            print("", opponent05, "---|                                             |")
            print("                   |---", opponent11, "---|                      |")
            print("", opponent06, "---|                      |                      |")
            print("                                          |---", opponent14, "---|")
            print("", opponent07, "---|                      |")
            print("                   |---", opponent12, "---|")
            print("", opponent08, "---|")

def make_opponents(player_list):
    player_list_copy = player_list.copy()
    opponents_list = []
    player_number = len(player_list_copy)
    for i in range(int(player_number / 2)):
        player1 = random.choice(player_list_copy)
        player_list_copy.remove(player1)
        player2 = random.choice(player_list_copy)
        player_list_copy.remove(player2)
        opponents = [player1, player2]
        opponents_list.append(opponents)
    return opponents_list

def update_opponents(winner_list, waiting_players):
    opponents_list = []
    winner_list_copy = winner_list.copy()
    player_number = len(winner_list)
    if player_number % 2 == 0:
        for i in range(int(player_number / 2)):
            player1 = winner_list_copy[0]
            winner_list_copy.remove(player1)
            player2 = winner_list_copy[0]
            winner_list_copy.remove(player2)
            opponents = [player1, player2]
            opponents_list.append(opponents)
    else:
        if (len(winner_list_copy) == 1) & (len(waiting_players) != 5):
            player1 = winner_list[0]
            player2 = waiting_players[0]
            waiting_players.remove(player2)
            new_opponent = [player1, player2]
            opponents_list = make_opponents(waiting_players)
            opponents_list.insert(0, new_opponent)
        elif len(waiting_players) == 5:
            player1 = winner_list[0]
            player2 = waiting_players[0]
            waiting_players.remove(player2)
            opponents_list =[[player1, player2]]
            for i in range(int(len(waiting_players)/2)):
                player1 = waiting_players[0]
                player2 = waiting_players[1]
                waiting_players.remove(player1)
                waiting_players.remove(player2)
                opponents_list.append([player1, player2])
        else:
            player2 = random.choice(winner_list_copy)
            winner_list_copy.remove(player2)
            opponents_list = make_opponents(winner_list_copy)
    opponents_list
    return opponents_list

if __name__ == "__main__":
    Tournament([1,2,3,4,5,6,7])
