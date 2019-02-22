from game_engine.game import Game
from game_engine.player_human import PlayerHuman
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_medium import PlayerMediumAI
from game_engine.player_ai_hard import PlayerHardAI
from random import choice


class Play:
    """
    The Play class
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 14/02/2019
    """

    def __init__(self):
        """
        The Play class constructor
        """
        self.game = Game()  # initiates a Game class instance
        self.players = []  # a list for players to be added to when initialised
        self.current_player = None  # initiates current player during game play
        self.selected_piece = None  # initiates current selected piece

    def play_selection(self, pce=None):
        """
        The selecting of a piece part of a game turn and
        swapping of current player after a piece is selected
        :param pce: the piece being selected for placing on the board
        """
        if isinstance(self.current_player, PlayerHuman):
            self.selected_piece = self.current_player.choose_piece(pce)

            if self.selected_piece:
                self.selected_piece = self.game.pieces.pop(self.selected_piece)
        else:
            self.selected_piece = self.game.pieces.pop(self.current_player.
                                                       choose_piece())
        if self.selected_piece:
            self.current_player = self.change_player()  # swaps player turn
        return self.selected_piece

    def play_placement(self, y=None, x=None):
        """
        The placing of a selected piece on the board part of a game turn
        :param y: the board row position the piece is being placed for human
        :param x: the board column position the piece is being placed for human
        """
        if isinstance(self.current_player, PlayerHuman):
            return self.current_player.place_piece(self.selected_piece, y, x)
        else:
            self.current_player.place_piece(self.selected_piece)  # place piece

    def play_auto(self):
        """
        Where the game turns are played automatically until game won or drawn
        :return: the winning player if game won, or None if game drawn
        """
        while True:
            self.play_selection()  # current player selects a piece, play swaps
            self.play_placement()  # new current player places piece on board

            if self.game.has_won_game(self.selected_piece):  # if game is won
                return self.current_player.name  # returns game winner name
            elif not self.game.has_next_play():  # checks if play turns remain
                return None  # returns no game winner

    def init_players(self, mod, dif=0, p_one="Player One", p_two="Player Two"):
        """
        Initializes the two players for the game dependent on game mode
        :param mod: the game mode being played; human vs human, AI vs AI, ...
        :param dif: the difficulty being played when playing AI
        :param p_one: the name for player one; default: Player One
        :param p_two: the name for player two; default: Player Two
        """
        if mod == 1:  # if human player vs human player
            self.players = [PlayerHuman(self.game, p_one),
                            PlayerHuman(self.game, p_two)]
        elif mod == 2:  # if human player vs AI player
            if dif == 1:  # if easy difficulty AI
                self.players = [PlayerHuman(self.game, p_one),
                                PlayerEasyAI(self.game, p_two)]
            elif dif == 2:  # if medium difficulty AI
                self.players = [PlayerHuman(self.game, p_one),
                                PlayerMediumAI(self.game, p_two)]
            else:  # if hard difficulty AI
                self.players = [PlayerHuman(self.game, p_one),
                                PlayerHardAI(self.game, p_two)]
        else:  # if AI player vs AI player
            if dif == 1:  # if easy difficulty AI
                self.players = [PlayerEasyAI(self.game, p_one),
                                PlayerEasyAI(self.game, p_two)]

            elif dif == 2:  # if medium difficulty AI
                self.players = [PlayerMediumAI(self.game, p_one),
                                PlayerMediumAI(self.game, p_two)]
            else:  # if hard difficulty AI
                self.players = [PlayerHardAI(self.game, p_one),
                                PlayerHardAI(self.game, p_two)]
        self.current_player = choice(self.players)  # random starting player

    def change_player(self):
        """
        Toggles player selection for when the game play turn changes
        :return: the new selected player for the current game play turn
        """
        return self.players[abs(self.players.index(self.current_player) - 1)]
