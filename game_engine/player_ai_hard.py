from game_engine.player_abstract import Player
from game_engine.minimax import Minimax
from random import randint


class PlayerHardAI(Player):
    """
    The Hard difficulty AI class
    Author(s): Viktor Enzell, Laurin Kerle
    Last-edit-date: 10/02/2019
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the game instance
        :param name: the name of the player
        """
        super().__init__(game, name)
        self.chosen_piece = None  # the piece chosen by the Minimax algorithm

    def choose_piece(self):
        """
        Method for hard difficulty AI piece choosing
        :return: a random piece if it is the first round
        Otherwise a piece chosen by the Minimax algorithm
        """
        if len(self.game.pieces.keys()) > 12:  # limit has to be the same as for place_piece
            while True:
                random_piece = str(randint(0, 15))
                if random_piece in self.game.pieces.keys():  # validate selection
                    return random_piece
        return str(self.chosen_piece)

    def place_piece(self, selected_piece):
        """
        Method for hard difficulty AI piece placing on board.
        Selects where to place piece and saves piece chosen by Minimax algorithm
        :param selected_piece the piece selected for placing on board
        """
        # Place at random the first few draws
        if len(self.game.pieces) > 12:  # limit has to be the same as for choose_piece
            while True:
                x = randint(0, 3)
                y = randint(0, 3)
                if self.game.is_cell_empty(int(x), int(y)):
                    self.game.board[int(x)][int(y)] = selected_piece
                    break
        # if there is only one spot left
        elif len(self.game.pieces) == 0:
            spot = self.game.get_remaining_spots()[0]
            x = int(spot / 4)
            y = spot % 4
            if self.game.is_cell_empty(int(x), int(y)):
                self.game.board[int(x)][int(y)] = selected_piece
        else:
            # Search more steps forward towards the end of the game
            if len(self.game.pieces) > 7:
                depth = 1
            elif len(self.game.pieces) > 5:
                depth = 2
            elif len(self.game.pieces) > 4:
                depth = 3
            else:
                depth = 16

            minimax = Minimax(self.game, depth, int(selected_piece, 2))
            best_move = minimax.get_move()
            self.chosen_piece = best_move.passed_piece

            spot = best_move.spot
            x = int(spot / 4)
            y = spot % 4

            if self.game.is_cell_empty(int(x), int(y)):
                self.game.board[int(x)][int(y)] = selected_piece
