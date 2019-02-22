from unittest import TestCase
from game_engine.play import Play
from game_engine.game import Game
from game_engine.player_ai_medium import PlayerMediumAI
from game_engine.player_ai_hard import PlayerHardAI
from game_engine.player_ai_easy import PlayerEasyAI
from random import choice


class TestPlayerAIMediumClass(TestCase):
    """
    Tests the PlayerMediumAI class
    Author(s): Adam Ross; Gustav From
    Date: 17/02/19
    """

    def test_player_ai_medium(self):
        """
        Tests PlayerMediumAI class instance
        """
        test = PlayerMediumAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerMediumAI))

    def test_choose_piece(self):
        """
        Tests choose_piece() method in the PlayerMediumAI class
        """
        test = PlayerMediumAI(Game(), "Test")
        test.game.board = [['0000', '1000', '0001', '0101'],
                            [None, '0010', '0111', None],
                            ['1001', None, '0100', '1111'],
                            ['1011', '0110', None, '1110']]
        test.game.pieces = {'3': '0011', '10': '1010',
                            '12': '1100', '13': '1101'}
        self.assertEqual('12', test.get_best(dict({str(pce): test.
                select_best_sim_count(test.easy(test.game.pieces[pce]), False,
                test.game.pieces[pce]) for pce in test.game.pieces}.items()),
                                             False))
        self.assertEqual('3', test.get_best(dict({str(pce): test.
                select_best_sim_count(test.hard(test.game.pieces[pce]), True,
                test.game.pieces[pce]) for pce in test.game.pieces}.items()),
                                             True))

    def test_place_piece(self):
        """
        Tests choose_piece() method in the PlayerMediumAI class
        """
        test = PlayerMediumAI(Game(), "Test")
        test.game.board = [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]
        test.game.pieces = {'10': '1010', '12': '1100', '13': '1101'}
        test.place_piece('1010')
        self.assertTrue(((test.game.board == [[None, '1000', '0001', '0101'],
                           ['1010', '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']] or test.game.board
                          == [['1010', '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]) and not
                          test.game.has_won_game('1010')) or (test.game.board
                          == [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', '1010', '1111', '1011'],
                           ['0100', '0110', '0011', '1110']] and
                            test.game.has_won_game('1010')))

    def test_player_ai_medium_play(self):
        """
        Tests average PlayerMediumAI player wins 50% +/- 15% in non-drawn games
        Usually between 40-60% win rate, but can by chance be just below/over
        """
        p_one, p_two, count, wins = "Player One", "Player Two", 0, 0
        samples = 100  # the number of samples of won games in each test

        while count < samples:
            test = Play()
            test.players = [PlayerMediumAI(test.game, p_one),
                            PlayerMediumAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto():
                count += 1

                if test.current_player.name == p_one:
                    wins += 1
        self.assertTrue((35 <= (wins / samples * 100) <= 65))

    def test_player_ai_medium_vs_ai_easy_play(self):
        """
        Tests average MediumAI player wins against EasyAI >= 15%
        Is usually above 90% win rate, but can by chance be just below 90%
        """
        p_one, p_two, wins = "Player One", "Player Two", 0
        samples = 100  # the number of samples of won games in each test

        for i in range(samples):
            test = Play()
            test.players = [PlayerMediumAI(test.game, p_one),
                            PlayerEasyAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto() and test.current_player.name == p_one:
                wins += 1
        self.assertTrue((wins / samples * 100) >= 85)

    def test_player_ai_medium_vs_ai_hard_play(self):
        """
        Tests average MediumAI player wins against HardAI <= 10%
        Theoretically, should never win against the hard (minimax) AI
        """
        p_one, p_two, wins = "Player One", "Player Two", 0
        samples = 100  # the number of samples of won games in each test

        for i in range(samples):
            test = Play()
            test.players = [PlayerMediumAI(test.game, p_one),
                            PlayerHardAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto() and test.current_player.name == p_two:
                wins += 1
        self.assertTrue(((samples - wins) / samples * 100) <= 10)
