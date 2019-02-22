from unittest import TestCase
from game_engine.play import Play
from game_engine.game import Game
from game_engine.player_ai_medium import PlayerMediumAI
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_hard import PlayerHardAI
from random import choice


class TestPlayerAIEasyClass(TestCase):
    """
    Tests the PlayerEasyAI class
    Author(s): Adam Ross
    Last-edit-date: 17/02/19
    """

    def test_player_ai_medium(self):
        """
        Tests PlayerEasyAI class instance
        """
        test = PlayerEasyAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerEasyAI))

    def test_choose_piece(self):
        """
        Tests choose_piece() method in the PlayerEasyAI class
        """
        test = PlayerEasyAI(Game(), "Test")
        test.game.board = [['0000', '1000', '0001', '0101'],
                            [None, '0010', '0111', None],
                            ['1001', None, '0100', '1111'],
                            ['1011', '0110', None, '1110']]
        test.game.pieces = {'3': '0011', '10': '1010',
                            '12': '1100', '13': '1101'}
        self.assertEqual('3', test.choose_piece())

    def test_place_piece(self):
        """
        Tests choose_piece() method in the PlayerEasyAI class
        """
        test = PlayerEasyAI(Game(), "Test")
        test.game.board = [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]
        test.game.pieces = {'10': '1010', '12': '1100', '13': '1101'}
        test.place_piece('1010')
        self.assertTrue((test.game.board == [[None, '1000', '0001', '0101'],
                           ['1010', '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']] or test.game.board
                          == [['1010', '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]) and not
                          test.game.has_won_game('1010'))

    def test_player_ai_easy_vs_ai_medium_play(self):
        """
        Tests average EasyAI player wins against MediumAI player <= 15%
        Is usually below 10% win rate, but can by chance be just above 10%
        """
        p_one, p_two, wins = "Player One", "Player Two", 0
        samples = 100  # the number of samples of won games in each test

        for i in range(samples):
            test = Play()
            test.players = [PlayerEasyAI(test.game, p_one),
                            PlayerMediumAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto() and test.current_player.name == p_one:
                wins += 1
        self.assertTrue((wins / samples * 100) <= 10)

    def test_player_ai_easy_vs_ai_hard_play(self):
        """
        Tests average EasyAI player wins against HardAI player <= 5%
        Theoretically, should never win against the hard (minimax) AI
        """
        p_one, p_two, wins = "Player One", "Player Two", 0
        samples = 100  # the number of samples of won games in each test

        for i in range(samples):
            test = Play()
            test.players = [PlayerEasyAI(test.game, p_one),
                            PlayerHardAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto() and test.current_player.name == p_two:
                wins += 1
        self.assertTrue(((samples - wins) / samples * 100) <= 5)
