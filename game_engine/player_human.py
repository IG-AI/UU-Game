from game_engine.player_abstract import Player


class PlayerHuman(Player):
    """
    The human player class
    Author(s):      Adam Ross
    Last-edit-date: 14/02/2019
    """

    def __init__(self, game, name):
        """
        The PlayerHuman class constructor
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    def choose_piece(self, pce=None):
        """
        Selects and validates a piece for the other player to place on board
        :param pce: the piece being selected for placing on the board
        :return: either the validated piece, or None to confirm invalidity
        """
        return pce if pce in self.game.pieces.keys() else None

    def place_piece(self, pce, y=None, x=None):
        """
        Selects and validates a game board cell for placing a selected piece
        :param pce: the piece selected for placing on the board
        :param y: the row position of the board the piece is being placed
        :param x: the column position of the board the piece is being placed
        :return: either True if valid placement, or False to confirm invalidity
        """
        try:
            if y and x and self.game.is_cell_empty(int(y), int(x)):
                self.game.board[int(y)][int(x)] = pce
                return True
            return False
        except:
            return False
