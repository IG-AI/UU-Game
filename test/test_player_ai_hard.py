from unittest import TestCase

from game_engine.play import Play
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_hard import PlayerHardAI
from game_engine.game import Game
from random import choice


class TestPlayerAIHardClass(TestCase):
    """
    Tests the PlayerHardAI class
    Author(s): Adam Ross; Laurin Kerle
    Date: 17/02/19
    """

    def test_player_ai_hard(self):
        """
        Tests PlayerHardAI class instance
        """
        test = PlayerHardAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerHardAI))

    # def test_choose_piece(self):
    #     """
    #     Tests choose_piece() method in the PlayerHardAI class
    #     """
    #     test = PlayerHardAI(Game(), "Test")
    #     test.game.board = [['0000', '1000', '0001', '0101'],
    #                         [None, '0010', '0111', None],
    #                         ['1001', None, '0100', '1111'],
    #                         ['1011', '0110', None, '1110']]
    #     test.game.pieces = {'3': '0011', '10': '1010',
    #                         '12': '1100', '13': '1101'}
    #     self.assertEqual('12', test.choose_piece())

    def test_place_piece(self):
        """
        Tests choose_piece() method in the PlayerHardAI class
        """
        test = PlayerHardAI(Game(), "Test")
        test.game.board = [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]
        test.game.pieces = {'10': '1010', '12': '1100', '13': '1101'}
        test.place_piece('1010')
        self.assertTrue(test.game.board
                          == [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', '1010', '1111', '1011'],
                           ['0100', '0110', '0011', '1110']] and
                            test.game.has_won_game('1010'))

    def test_player_ai_hard_play(self):
        """
        Test HardAI for average wins against itself being <= 10%
        """
        average = 0

        for i in range(100):
            test = Play()
            test.players = [PlayerHardAI(test.game, "Player One"),
                            PlayerHardAI(test.game, "Player Two")]
            test.current_player = choice(test.players)

            if test.play_auto() and test.current_player == "Player One":
                average += 1
        self.assertTrue(average <= 10)

    def test_player_ai_hard_vs_ai_easy_play(self):
        """
        Test HardAI for average wins against EasyAI being >= 95%
        """
        average, p_one, p_two = 0, "Player One", "Player Two"

        for i in range(100):
            test = Play()
            test.players = [PlayerHardAI(test.game, p_one),
                            PlayerEasyAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto() and test.current_player == p_one:
                average += 1
        self.assertTrue(average >= 95)
