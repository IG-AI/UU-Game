import random
from communication_platform import graphics as g

class Tournament:
    """
    A class which makes and controls a tournament. It makes opponents from a player list given as a input.
    The first two opponents are added to a list and the rest of the paired opponents gets added to a queue.
    Unpaired players are added to a waiting list.

    Methods
    -------
    next_game(self, winner)
        Retrieves the next opponents from opponents_queue and returns it. It also adds the winners to winner_list_temp.
        If the opponents_queue is empty, its gets updated with new opponents based on the winners and waiting players
        and winner_list_temp gets appended to winner_list and then gets zeroed.
    print_scoreboard(self)
        Formats a string of the tournament bracket and returns it
    """

    def __init__(self, player_list):
        """
        Initialize the tournament class, with a list of players as input.
        To get the opponents do as follows:
        tournament1 = Tournament(player_list), opponents = tournament1.opponents_queue

        Attributes
        ----------
        tournament_depth : int
            Numbers of game iterations.
        winner_state : boolean
            Flag that indicate if the game is done.
        winner_list : list
            Lists in list with the winning players from each game iteration.
        winner_list_temp : list
            List with the wining players from the active game iteration.
        waiting_players : list
            List with the current players in the tournament.
        start_player_list : list
            List with all players.
        opponents_queue : list of lists
            List with the current opponents, represented by lists with two opponents.
        all_opponents : list of lists of lists
            A list with all opponents, represented by lists for each game iteration
            with lists of opponents for each game.
        opponents : list
            List with active opponents
        self.waiting_players: list
            List of players who haven't been paired with any opponents.

        Parameters
        ----------
        player_list : list
            list of players participating in the current tournament in the form of strings.

        Raises
        ------
        Exception
            If the numbers of players aren't between 3 to 8 players, Exception is raised because the tournament
            isn't built to handle that amount of players.
        Exception
            If the player_list input doesn't contains only strings, Exception is raised because player_list should
            contains the names of the players in the form of strings.
        """

        self.tournament_depth = 0
        self.winner_state = 0
        self.winner_list = []
        self.winner_list_temp = []

        if (len(player_list) < 3) | (len(player_list) > 8):
            raise Exception("Error: It has to be between 3 - 8 players!")
        if not all(isinstance(s, str) for s in player_list):
            raise Exception("Error: The player names has to be in the form of a string!")
        self.waiting_players = player_list.copy()
        self.start_player_list = player_list.copy()
        player_list_copy = player_list.copy()
        if ((len(player_list) % 2) == 0) | (len(player_list) == 3):
            self.opponents_queue = make_opponents(player_list_copy)
            self.all_opponents = [self.opponents_queue.copy()]
            self.opponents = self.opponents_queue.pop(0)
            self.waiting_players.remove(self.opponents[0])
            self.waiting_players.remove(self.opponents[1])
            for i in range(len(self.opponents_queue)):
                self.waiting_players.remove(self.opponents_queue[i][0])
                self.waiting_players.remove(self.opponents_queue[i][1])
        else:
            self.opponents_queue = make_opponents(player_list_copy)
            self.all_opponents = [self.opponents_queue.copy()]
            self.opponents = self.opponents_queue.pop(0)
            self.waiting_players.remove(self.opponents[0])
            self.waiting_players.remove(self.opponents[1])


    def next_game(self, winner):
        """
        Retrieves the next opponents from opponents_queue and returns it. It also adds the winners to winner_list_temp.
        If the opponents_queue are empty, its gets updated with new opponents based on the winners and waiting players
        with the help from the method update_opponents and winner_list_temp gets appended to winner_list and then gets
        zeroed.

        Parameters
        ----------
        winner : string
            The name of the current games winner
        """
        self.winner_list_temp.append(winner)
        if not self.opponents_queue:
            self.winner_list.append(self.winner_list_temp)
            self.opponents_queue = update_opponents(self.winner_list_temp, self.waiting_players)
            self.tournament_depth += 1
            self.winner_list_temp = []
            if self.winner_list:
                if ((len(self.start_player_list) == 3) & (self.tournament_depth == 2)) | \
                        ((len(self.start_player_list) == 4) & (self.tournament_depth == 2)) | \
                        ((len(self.start_player_list) == 5) & (self.tournament_depth == 3)) | \
                        ((len(self.start_player_list) == 6) & (self.tournament_depth == 3)) | \
                        ((len(self.start_player_list) == 7) & (self.tournament_depth == 4)) | \
                        ((len(self.start_player_list) == 8) & (self.tournament_depth == 3)):
                    self.winner_state = 1
                    self.opponents = []
                    return ()
                if len(self.winner_list[self.tournament_depth - 1]) == 3:
                    player1 = self.winner_list[self.tournament_depth - 1][0]
                    player2 = self.winner_list[self.tournament_depth - 1][1]
                    self.waiting_players.append(self.winner_list[self.tournament_depth - 1][-1])
                    self.opponents_queue = [[player1, player2]]
                if (len(self.winner_list[self.tournament_depth - 1]) == 1) & (len(self.winner_list) == 2) & (len(self.start_player_list) != 4):
                    player1 = self.winner_list[self.tournament_depth - 1][0]
                    player2 = self.winner_list[0][2]
                    self.opponents_queue = [[player1, player2]]
                if (len(self.waiting_players) % 2 == 1) & (len(self.start_player_list) == 3):
                    self.waiting_players.remove(self.opponents[0])
                if (len(self.waiting_players) == 2) & (len(self.start_player_list) == 5):
                    self.waiting_players.remove(self.opponents_queue[1][0])
                    self.waiting_players.remove(self.opponents_queue[1][1])
                self.all_opponents.append(self.opponents_queue.copy())
        self.opponents = self.opponents_queue[0]
        self.opponents_queue.remove(self.opponents)


    def get_scoreboard(self):
        """
        Formats a string of the tournament bracket and returns it.
        """
        cases = len(self.start_player_list)
        anti_pad = 9

        opponent03 = g.color("O", "N/A")
        opponent04 = g.color("O", "N/A")
        opponent05 = g.color("O", "N/A")
        opponent06 = g.color("O", "N/A")
        opponent07 = g.color("O", "N/A")
        opponent08 = g.color("O", "N/A")
        opponent09 = g.color("O", "N/A")
        opponent10 = g.color("O", "N/A")
        opponent11 = g.color("O", "N/A")
        opponent12 = g.color("O", "N/A")
        opponent13 = g.color("O", "N/A")
        opponent14 = g.color("O", "N/A")
        winner = g.color("O", "N/A")

        display = "\n"

        # Game with 3 players
        if cases == 3:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            if len(self.all_opponents) == 2:
                opponent03 = self.all_opponents[1][0][0]
                opponent04 = self.all_opponents[1][0][1]
                if len(self.winner_list) == 2:
                    winner = self.winner_list[1][0]

            opp_list = [opponent01, opponent02, opponent03, opponent04]
            opp_len_list = []
            for opp in opp_list:
                opp_len_list.append(len(opp) - anti_pad)

            first_game = opp_len_list[0:2]
            max_string = max(first_game)
            string_size1 = opp_len_list[0]
            padding1 = "".ljust((int(max_string-string_size1)), '-')
            string_size2 = max(opp_len_list[0], opp_len_list[1])
            padding2 = "".ljust(string_size2, ' ')
            string_size3 = opp_len_list[1]
            padding3 = "".ljust((int(max_string)-string_size3), '-')
            string_size4 = len(padding2+"|---")
            padding4 = "".ljust(string_size4, ' ')
            string_size6 = max(opp_len_list[2], opp_len_list[3]) - opp_len_list[2]
            padding6 = "".ljust(string_size6, '-')
            string_size7 = max(opp_len_list[2], opp_len_list[3]) - opp_len_list[3]
            padding7 = "".ljust(string_size7, '-')
            string_size5 = len(padding4+opponent04+padding7) - len(opponent02+padding3) - 1
            padding5 = "".ljust(string_size5, ' ')

            display += opponent01+padding1+"|"+"\n"
            display += padding2+"|---"+opponent03+padding6+"|"+"\n"
            display += opponent02+padding3+"|"+padding5+"|---"+winner+"\n"
            display += padding4+opponent04+padding7+"|"+"\n"

        # Game with 4 players
        if cases == 4:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            opponent03 = self.all_opponents[0][1][0]
            opponent04 = self.all_opponents[0][1][1]
            if len(self.winner_list_temp) == 1:
                    opponent05 = self.winner_list_temp[0]
            if len(self.winner_list) >= 1:
                opponent05 = self.winner_list[0][0]
                opponent06 = self.winner_list[0][1]
            if self.winner_state == 1:
                winner = self.winner_list[1][0]

            opp_list = [opponent01, opponent02, opponent03, opponent04, opponent05, opponent06]
            opp_len_list = []
            for opp in opp_list:
                opp_len_list.append(len(opp) - anti_pad)

            first_game = opp_len_list[0:4]
            max_string = max(first_game)
            string_size1 = opp_len_list[0]
            padding1 = "".ljust(int(max_string-string_size1), '-')
            string_size2 = max_string
            padding2 = "".ljust(string_size2, ' ')
            string_size3 = opp_len_list[1]
            padding3 = "".ljust(int(max_string-string_size3), '-')
            string_size5 = opp_len_list[2]
            padding5 = "".ljust(int(max_string-string_size5), '-')
            string_size6 = max_string
            padding6 = "".ljust(string_size6, ' ')
            string_size7 = opp_len_list[3]
            padding7 = "".ljust(int(max_string-string_size7), '-')
            string_size8 = max(opp_len_list[4], opp_len_list[5]) - opp_len_list[4]
            padding8 = "".ljust(string_size8, '-')
            string_size9 = max(opp_len_list[4], opp_len_list[5]) - opp_len_list[5]
            padding9 = "".ljust(string_size9, '-')
            string_size4 = max(len(""+padding2+opponent05+"|---"+padding8+"|"), (len(""+padding6+opponent06+"|---"+padding9+"|")))-1-anti_pad
            padding4 = "".ljust(string_size4, ' ')
            string_size10 = len(padding4) - (len(""+padding3+"|")+opp_len_list[1])
            padding10 = "".ljust(string_size10, ' ')
            string_size11 = len(padding4) - (len(""+padding5+"|")+opp_len_list[2])
            padding11 = "".ljust(string_size11, ' ')

            display += opponent01+padding1+"|"+"\n"
            display += padding2+"|---"+opponent05+padding8+"|"+"\n"
            display += opponent02+padding3+"|"+padding10+"|"+"\n"
            display += padding4+"|---"+winner+"\n"
            display += opponent03+padding5+"|"+padding11+"|"+"\n"
            display += padding6+"|---"+opponent06+padding9+"|"+"\n"
            display += opponent04+padding7+"|"+"\n"

        # Game with 5 players
        if cases == 5:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            if len(self.all_opponents) >= 2:
                opponent03 = self.all_opponents[1][0][0]
                opponent04 = self.all_opponents[1][0][1]
                opponent05 = self.all_opponents[1][1][0]
                opponent06 = self.all_opponents[1][1][1]
                if len(self.winner_list_temp) == 1:
                    opponent07 = self.winner_list_temp[0]
                if len(self.winner_list) >= 2:
                    opponent07 = self.winner_list[1][0]
                    opponent08 = self.winner_list[1][1]
                if len(self.winner_list) == 3:
                    winner = self.winner_list[2][0]

            opp_list = [opponent01, opponent02, opponent03, opponent04, opponent05, opponent06, opponent07, opponent08]
            opp_len_list = []
            for opp in opp_list:
                opp_len_list.append(len(opp) - anti_pad)

            first_game = opp_len_list[0:4]
            max_string = max(first_game)
            string_size1 = opp_len_list[0]
            padding1 = "".ljust(int(max_string-string_size1), '-')
            string_size2 = max_string
            padding2 = "".ljust(string_size2, ' ')
            string_size3 = opp_len_list[1]
            padding3 = "".ljust(int(max_string-string_size3), '-')
            string_size4 = max(len(""+opponent01+padding1), len(""+opponent02+padding3)) -5
            padding4 = "".ljust(string_size4, ' ')
            string_size5 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5])
            padding5 = "".ljust((string_size5 - opp_len_list[2]), '-')
            string_size7 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5])
            padding7 = "".ljust((string_size7 - opp_len_list[3]), '-')
            string_size8 = len(""+padding2+"|---")
            padding8 = "".ljust(string_size8, ' ')
            string_size6 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5]) + 3
            padding6 = "".ljust(string_size6, ' ')
            string_size9 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5]) - opp_len_list[4]
            padding9 = "".ljust(string_size9, '-')
            string_size10 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5]) - opp_len_list[5]
            padding10 = "".ljust(string_size10, '-')
            string_size11 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5]) + len(padding4)
            padding11 = "".ljust(string_size11, ' ')
            string_size12 = max(opp_len_list[6], opp_len_list[7]) - opp_len_list[6]
            padding12 = "".ljust(string_size12, '-')
            string_size13 = max(opp_len_list[6], opp_len_list[7]) - opp_len_list[7]
            padding13 = "".ljust(string_size13, '-')
            string_size14 = max(opp_len_list[6], opp_len_list[7]) + 3
            padding14 = "".ljust(string_size14, ' ')
            string_size15 = max(opp_len_list[6], opp_len_list[7]) + 3
            padding15 = "".ljust(string_size15, ' ')
            string_size16 = opp_len_list[7] + len(padding11+"|---") + len(padding13)
            padding16 = "".ljust(string_size16, ' ')

            display += opponent01+padding1+"|"+"\n"
            display += padding2+"|---"+opponent03+padding5+"|"+"\n"
            display += opponent02+padding3+"|"+padding6+"|---"+opponent07+padding12+"|"+"\n"
            display += padding4+opponent04+padding7+"|"+padding14+"|"+"\n"
            display += padding16+"|---"+winner+"\n"
            display += padding8+opponent05+padding9+"|"+padding15+"|"+"\n"
            display += padding11+"|---"+opponent08+padding13+"|"+"\n"
            display += padding8+opponent06+padding10+"|"+"\n"

        # Game with 6 players
        if cases == 6:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            opponent03 = self.all_opponents[0][1][0]
            opponent04 = self.all_opponents[0][1][1]
            opponent05 = self.all_opponents[0][2][0]
            opponent06 = self.all_opponents[0][2][1]
            if len(self.winner_list_temp) >= 1:
                opponent07 = self.winner_list_temp[0]
                if len(self.winner_list_temp) >= 2:
                    opponent08 = self.winner_list_temp[1]
            if len(self.winner_list) >= 1:
                opponent07 = self.winner_list[0][0]
                opponent08 = self.winner_list[0][1]
                opponent09 = self.winner_list[0][2]
            if len(self.all_opponents) >= 3:
                opponent10 = self.all_opponents[2][0][0]
            if len(self.winner_list) == 3:
                winner = self.winner_list[2][0]

            opp_list = [opponent01, opponent02, opponent03, opponent04, opponent05, opponent06, opponent07, opponent08, opponent09, opponent10]
            opp_len_list = []
            for opp in opp_list:
                opp_len_list.append(len(opp) - anti_pad)

            first_game = opp_len_list[0:6]
            max_string = max(first_game)
            string_size1 = opp_len_list[0]
            padding1 = "".ljust(int(max_string-string_size1), '-')
            string_size2 = opp_len_list[1]
            padding2 = "".ljust(int(max_string-string_size2), '-')
            string_size3 = opp_len_list[2]
            padding3 = "".ljust(int(max_string-string_size3), '-')
            string_size4 = opp_len_list[3]
            padding4 = "".ljust(int(max_string-string_size4), '-')
            string_size5 = opp_len_list[4]
            padding5 = "".ljust(int(max_string-string_size5), '-')
            string_size6 = opp_len_list[5]
            padding6 = "".ljust(int(max_string-string_size6), '-')
            string_size7 = max_string
            padding7 = "".ljust(string_size7, ' ')
            string_size8 = max(opp_len_list[6], opp_len_list[7], opp_len_list[8]) - opp_len_list[6]
            padding8 = "".ljust(string_size8, '-')
            string_size9 = max(opp_len_list[6], opp_len_list[7], opp_len_list[8]) - opp_len_list[7]
            padding9 = "".ljust(string_size9, '-')
            string_size10 = max(opp_len_list[6], opp_len_list[7], opp_len_list[8]) - opp_len_list[8]
            padding10 = "".ljust(string_size10, '-')
            string_size12 = max(opp_len_list[0], opp_len_list[1], opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5]) + max(opp_len_list[6], opp_len_list[7], opp_len_list[8], opp_len_list[9]) + 4
            padding12 = "".ljust(string_size12, ' ')
            string_size14 = max(opp_len_list[6], opp_len_list[7], opp_len_list[8]) + 3
            padding14 = "".ljust(string_size14, ' ')
            string_size15 = len(""+padding12+"|---"+opponent10) - len(""+padding7+"|---"+opponent09)
            padding15 = "".ljust(string_size15, '-')
            string_size16 = len(padding7+"|---"+opponent09+padding15) - len(opponent05+padding5+"|")
            padding16 = "".ljust(string_size16, ' ')
            string_size17 = max(opp_len_list[0], opp_len_list[1], opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5]) + max(opp_len_list[6], opp_len_list[7], opp_len_list[8]) + opp_len_list[9] + 8
            padding17 = "".ljust(string_size17, ' ')
            string_size18 = max(opp_len_list[0], opp_len_list[1], opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5]) + max(opp_len_list[6], opp_len_list[7], opp_len_list[8]) + opp_len_list[9] - 5
            padding18 = "".ljust(string_size18, ' ')
            string_size19 = opp_len_list[9] + 3
            padding19 = "".ljust(string_size19, ' ')

            display += opponent01+padding1+"|"+"\n"
            display += padding7+"|---"+opponent07+padding8+"|"+"\n"
            display += opponent02+padding2+"|"+padding14+"|"+"\n"
            display += padding12+"|---"+opponent10+"|"+"\n"
            display += opponent03+padding3+"|"+padding14+"|"+padding19+"|"+"\n"
            display += padding7+"|---"+opponent08+padding9+"|"+padding19+"|"+"\n"
            display += opponent04+padding4+"|"+padding18+"|---"+winner+"\n"
            display += padding17+"|"+"\n"
            display += opponent05+padding5+"|"+padding16+"|"+"\n"
            display += padding7+"|---"+opponent09+padding15+"|"+"\n"
            display += opponent06+padding6+"|"+"\n"

        # Game with 7 players
        if cases == 7:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            if len(self.all_opponents) >= 2:

                opponent03 = self.all_opponents[1][0][0]
                opponent04 = self.all_opponents[1][0][1]
                opponent05 = self.all_opponents[1][1][0]
                opponent06 = self.all_opponents[1][1][1]
                opponent07 = self.all_opponents[1][2][0]
                opponent08 = self.all_opponents[1][2][1]
                if len(self.winner_list_temp) >= 1:
                    opponent09 = self.winner_list_temp[0]
                    if len(self.winner_list_temp) >= 2:
                        opponent10 = self.winner_list_temp[1]
            if len(self.winner_list) >= 2:
                opponent09 = self.winner_list[1][0]
                opponent10 = self.winner_list[1][1]
                opponent11 = self.winner_list[1][2]
            if len(self.all_opponents) >= 4:
                opponent12 = self.all_opponents[3][0][0]
            if len(self.winner_list) == 4:
                winner = self.winner_list[3][0]

            opp_list = [opponent01, opponent02, opponent03, opponent04, opponent05, opponent06, opponent07, opponent08, opponent09, opponent10, opponent11, opponent12]
            opp_len_list = []
            for opp in opp_list:
                opp_len_list.append(len(opp) - anti_pad)

            string_size1 = max(opp_len_list[0], opp_len_list[1]) - opp_len_list[0]
            padding1 = "".ljust(string_size1, '-')
            string_size2 = max(opp_len_list[0], opp_len_list[1]) - opp_len_list[1]
            padding2 = "".ljust(string_size2, '-')
            string_size3 = max(opp_len_list[0], opp_len_list[1])
            padding3 = "".ljust(string_size3, ' ')
            string_size4 = max(opp_len_list[0], opp_len_list[1]) + 4
            padding4 = "".ljust(string_size4, ' ')
            string_size5 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) - opp_len_list[2]
            padding5 = "".ljust(string_size5, '-')
            string_size6 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) - opp_len_list[3]
            padding6 = "".ljust(string_size6, '-')
            string_size7 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) - opp_len_list[4]
            padding7 = "".ljust(string_size7, '-')
            string_size8 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) - opp_len_list[5]
            padding8 = "".ljust(string_size8, '-')
            string_size9 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) - opp_len_list[6]
            padding9 = "".ljust(string_size9, '-')
            string_size10 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) - opp_len_list[7]
            padding10 = "".ljust(string_size10, '-')
            string_size11 = max(opp_len_list[10], opp_len_list[11]) - opp_len_list[11] - 4
            padding11 = "".ljust(string_size11, ' ')
            string_size12 = max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) + 3
            padding12 = "".ljust(string_size12, ' ')
            string_size13 = max(opp_len_list[8], opp_len_list[9], opp_len_list[10]) - opp_len_list[8]
            padding13 = "".ljust(string_size13, '-')
            string_size14 = max(opp_len_list[8], opp_len_list[9]) - opp_len_list[9]
            padding14 = "".ljust(string_size14, '-')
            string_size15 = max(opp_len_list[8], opp_len_list[9], opp_len_list[10], opp_len_list[11]) + 3
            padding15 = "".ljust(string_size15, ' ')
            string_size16 = len(padding4) + max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7])
            padding16 = "".ljust(string_size16, ' ')
            string_size17 = opp_len_list[11] + 3
            padding17 = "".ljust(string_size17, ' ')
            string_size20 = max(opp_len_list[8], opp_len_list[9], opp_len_list[10]) + opp_len_list[11] + 4 - opp_len_list[10]
            padding20 = "".ljust(string_size20, '-')
            string_size21 = opp_len_list[8] + len(padding13) + max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) + max(opp_len_list[0], opp_len_list[1]) + 8
            padding21 = "".ljust(string_size21, ' ')
            string_size18 = max(opp_len_list[8], opp_len_list[9]) + opp_len_list[11] + 7
            padding18 = "".ljust(string_size18, ' ')
            string_size19 = max(opp_len_list[0], opp_len_list[1]) + max(opp_len_list[2], opp_len_list[3], opp_len_list[4], opp_len_list[5], opp_len_list[6], opp_len_list[7]) + max(opp_len_list[8], opp_len_list[9], opp_len_list[10])  + opp_len_list[11] + 12
            padding19 = "".ljust(string_size19, ' ')

            display += opponent01+padding1+"|"+"\n"
            display += padding3+"|---"+opponent03+padding5+"|"+"\n"
            display += opponent02+padding2+"|"+padding12+"|---"+opponent09+padding13+"|"+"\n"
            display += padding4+opponent04+padding6+"|"+padding15+"|"+"\n"
            display += padding21+"|---"+opponent12+padding11+"|"+"\n"
            display += padding4+opponent05+padding7+"|"+padding15+"|"+padding17+"|"+"\n"
            display += padding16+"|---"+opponent10+padding14+"|"+padding17+"|"+"\n"
            display += padding4+opponent06+padding8+"|"+padding18+"|---"+winner+"\n"
            display += padding19+"|"+"\n"
            display += padding4+opponent07+padding9+"|"+padding18+"|"+"\n"
            display += padding16+"|---"+opponent11+padding20+"|"+"\n"
            display += padding4+opponent08+padding10+"|"+"\n"

        # Game with 8 players
        if cases == 8:
            opponent01 = self.all_opponents[0][0][0]
            opponent02 = self.all_opponents[0][0][1]
            opponent03 = self.all_opponents[0][1][0]
            opponent04 = self.all_opponents[0][1][1]
            opponent05 = self.all_opponents[0][2][0]
            opponent06 = self.all_opponents[0][2][1]
            opponent07 = self.all_opponents[0][3][0]
            opponent08 = self.all_opponents[0][3][1]
            if len(self.all_opponents) == 1:
                if len(self.winner_list_temp) >= 1:
                    opponent09 = self.winner_list_temp[0]
                    if len(self.winner_list_temp) >= 2:
                        opponent10 = self.winner_list_temp[1]
                        if len(self.winner_list_temp) >= 3:
                            opponent11 = self.winner_list_temp[2]
            if len(self.all_opponents) >= 2:
                opponent09 = self.all_opponents[1][0][0]
                opponent10 = self.all_opponents[1][0][1]
                opponent11 = self.all_opponents[1][1][0]
                opponent12 = self.all_opponents[1][1][1]
                if len(self.winner_list_temp) >= 1:
                    opponent13 = self.winner_list_temp[0]
            if len(self.all_opponents) >= 3:
                opponent13 = self.all_opponents[2][0][0]
                opponent14 = self.all_opponents[2][0][1]
            if len(self.winner_list) == 3:
                winner = self.winner_list[2][0]

            opp_list = [opponent01, opponent02, opponent03, opponent04, opponent05, opponent06, opponent07, opponent08, opponent09, opponent10, opponent11, opponent12, opponent13, opponent14]
            opp_len_list = []
            for opp in opp_list:
                opp_len_list.append(len(opp) - anti_pad)

            first_game = opp_len_list[0:8]
            max_string = max(first_game)
            string_size1 = max_string - opp_len_list[0]
            padding1 = "".ljust(int(string_size1), '-')
            string_size2 = opp_len_list[1]
            padding2 = "".ljust(int(max_string-string_size2), '-')
            string_size3 = opp_len_list[2]
            padding3 = "".ljust(int(max_string-string_size3), '-')
            string_size4 = opp_len_list[3]
            padding4 = "".ljust(int(max_string-string_size4), '-')
            string_size5 = opp_len_list[4]
            padding5 = "".ljust(int(max_string-string_size5), '-')
            string_size6 = opp_len_list[5]
            padding6 = "".ljust(int(max_string-string_size6), '-')
            string_size7 = opp_len_list[6]
            padding7 = "".ljust(int(max_string-string_size7), '-')
            string_size8 = opp_len_list[7]
            padding8 = "".ljust(int(max_string-string_size8), '-')
            string_size9 = max_string
            padding9 = "".ljust(string_size9, ' ')
            string_size10 = max(opp_len_list[8], opp_len_list[9], opp_len_list[10], opp_len_list[11]) - opp_len_list[8]
            padding10 = "".ljust(string_size10, '-')
            string_size11 = max(opp_len_list[8], opp_len_list[9], opp_len_list[10], opp_len_list[11]) - opp_len_list[9]
            padding11 = "".ljust(string_size11, '-')
            string_size12 = max(opp_len_list[8], opp_len_list[9], opp_len_list[10], opp_len_list[11]) - opp_len_list[10]
            padding12 = "".ljust(string_size12, '-')
            string_size13 = max(opp_len_list[8], opp_len_list[9], opp_len_list[10], opp_len_list[11]) - opp_len_list[11]
            padding13 = "".ljust(string_size13, '-')
            string_size14 = len(padding9+"|---"+opponent09+padding10) - len(opponent02+padding2) - 1
            padding14 = "".ljust(string_size14, ' ')
            string_size15 = max_string + max(opp_len_list[8], opp_len_list[9], opp_len_list[10], opp_len_list[11]) + 4
            padding15 = "".ljust(string_size15, ' ')
            string_size16 = max(opp_len_list[12], opp_len_list[13]) - opp_len_list[12]
            padding16 = "".ljust(string_size16, '-')
            string_size17 = max(opp_len_list[12], opp_len_list[13]) - opp_len_list[13]
            padding17 = "".ljust(string_size17, '-')
            string_size18 = max(opp_len_list[12], opp_len_list[13]) + 3
            padding18 = "".ljust(string_size18, ' ')
            string_size19 = len(padding15+"|---"+opponent14+padding17) - len(opponent08+padding8) - 1
            padding19 = "".ljust(string_size19, ' ')
            string_size20 = max_string + max(opp_len_list[8], opp_len_list[9], opp_len_list[10], opp_len_list[11]) + max(opp_len_list[12], opp_len_list[13]) + 8
            padding20 = "".ljust(string_size20, ' ')

            display += opponent01+padding1+"|"+"\n"
            display += padding9+"|---"+opponent09+padding10+"|"+"\n"
            display += opponent02+padding2+"|"+padding14+"|"+"\n"
            display += padding15+"|---"+opponent13+padding16+"|"+"\n"
            display += opponent03+padding3+"|"+padding14+"|"+padding18+"|"+"\n"
            display += padding9+"|---"+opponent10+padding11+"|"+padding18+"|"+"\n"
            display += opponent04+padding4+"|"+padding19+"|"+"\n"
            display += padding20+"|---"+winner+"\n"
            display += opponent05+padding5+"|"+padding19+"|"+"\n"
            display += padding9+"|---"+opponent11+padding12+"|"+padding18+"|"+"\n"
            display += opponent06+padding6+"|"+padding14+"|"+padding18+"|"+"\n"
            display += padding15+"|---"+opponent14+padding17+"|"+"\n"
            display += opponent07+padding7+"|"+padding14+"|"+"\n"
            display += padding9+"|---"+opponent12+padding13+"|"+"\n"
            display += opponent08+padding8+"|"+"\n"

        return display

def make_opponents(player_list):
    """
    Makes and returns the opponents_queue for the first game iteration in the form of a list with the names of the
    players in the form of strings.

    Parameters
    ----------
    player_list : list
        A list with all the players in the tournament in the form of strings.
    """
    player_list_copy = player_list.copy()
    opponents_list = []
    player_number = len(player_list_copy)
    if (player_number % 2 == 0) | (player_number == 3):
        for i in range(int(player_number / 2)):
            player1 = random.choice(player_list_copy)
            player_list_copy.remove(player1)
            player2 = random.choice(player_list_copy)
            player_list_copy.remove(player2)
            opponents = [player1, player2]
            opponents_list.append(opponents)
    else:
        player1 = random.choice(player_list_copy)
        player_list_copy.remove(player1)
        player2 = random.choice(player_list_copy)
        player_list_copy.remove(player2)
        opponents_list = [[player1, player2]]
    return opponents_list

def update_opponents(winner_list, waiting_players):
    """
    Returns a updated opponents_queue with the new opponents for the current game iteration in the form of a list with
    the names of the players in the form of strings.

    Parameters
    ----------
    winner_list : list
        A list with the winners of the current game iteration in the form of strings.
    waiting_players : list
        A list with unpaired players (players who aren't in the opponents_queue).
    """
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
        if (len(winner_list_copy) == 1) & (len(waiting_players) != 5) & (len(waiting_players) != 0):
            player1 = winner_list[0]
            player2 = waiting_players[0]
            waiting_players.remove(player2)
            new_opponent = [player1, player2]
            opponents_list = make_opponents(waiting_players)
            opponents_list.insert(0, new_opponent)
        elif len(waiting_players) == 5:
            player1 = winner_list[0]
            player2 = random.choice(waiting_players)
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
    return opponents_list

if __name__ == "__main__":
    Tournament(["Pettersson", "Undran", "Ola", "Mr.X", "Bumbi-Bu", "Pelle", "Gerald"])
