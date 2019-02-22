from game_engine.player_ai import PlayerAI


class PlayerEasyAI(PlayerAI):
    """
    The easy difficulty AI class
    Author(s): Pelle Ingvast, Maxime Gaide, Adam Ross
    Last-edit-date: 17/02/19
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the game instance
        :param name: the name of the player
        """
        super().__init__(game, name)

    def choose_piece(self):
        """
        Method for easy difficulty AI piece choosing
        :return: the selected piece for placing on the board
        """
        return self.get_best(dict({str(pce): self.select_best_sim_count(self.
                hard(self.game.pieces[pce]), True, self.game.pieces[pce]) for
                pce in self.game.pieces}.items()), True)

    def place_piece(self, pce):
        """
        Method for easy difficulty AI piece placing on board
        :param pce the piece selected for placing on board
        """
        y, x = self.select_best_sim_count(self.easy(pce), False, pce)[0]
        self.game.board[y][x] = pce
