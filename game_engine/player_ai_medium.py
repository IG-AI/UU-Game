from game_engine.player_ai import PlayerAI
from random import choice


class PlayerMediumAI(PlayerAI):
    """
    The Medium difficulty AI class
    Author(s):      Gustav From; Adam Ross
    Last-edit-date: 13/02/19
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    def choose_piece(self):
        """
        Method for medium difficulty AI piece choosing. Implements get_best()
        Implements either easy or hard AI algorithms by random 50/50 selection
        :return: the selected piece for placing on the board
        """
        return self.get_best(dict({str(pce): self.select_best_sim_count(self.
                hard(self.game.pieces[pce]), True, self.game.pieces[pce]) for
                pce in self.game.pieces}.items()), True) if choice([True,
                False]) else self.get_best(dict({str(pce): self.
                select_best_sim_count(self.easy(self.game.pieces[pce]), False,
                self.game.pieces[pce]) for pce in self.game.pieces}.items()),
                False)

    def place_piece(self, pce):
        """
        Method for medium difficulty AI piece placing on board
        Implements either easy or hard AI algorithms by random 50/50 selection
        :param pce the piece selected for placing on board
        """
        y, x = self.select_best_sim_count(self.hard(pce), True, pce)[0] if \
            choice([True, False]) else \
            self.select_best_sim_count(self.easy(pce), False, pce)[0]
        self.game.board[y][x] = pce  # sets the selected piece to a board pos
