from unittest import TestCase
from game_engine.game import Game


class TestWinCondition(TestCase):
    """
    Tests the win_condition() method in the Game class
    Author: Adam Ross
    Date: 12/02/19
    """

    def test_most_pieces_wins(self):
        """
        Tests a won mostly full board does result in a game win declaration
        """
        test = Game()
        test.board = [['0001', '1000', None, '0100'],
                      ['1110', '0001', '0010', '0111'],
                      ['1001', '1100', '1110', '1011'],
                      ['0100', '0110', '0011', '1111']]
        self.assertTrue(test.has_won_game('1110'))

    def test_most_pieces_loses(self):
        """
        Tests a mostly full board does not result in a game win declaration
        """
        test = Game()
        test.board = [['0001', '1000', None, '0100'],
                      ['1110', '0001', '0010', '0111'],
                      ['1001', None, '1110', '1011'],
                      ['0100', '0110', '0011', '1111']]
        self.assertFalse(test.has_won_game('1111'))

    def test_top_row_wins(self):
        """
        Tests a won top row does result in a game win declaration
        """
        test = Game()
        test.board = [['0001', '1000', '0000', '0011'],
                      [None, None, None, None],
                      [None, None, None, None],
                      [None, None, None, None]]
        self.assertTrue(test.has_won_game('0011'))

    def test_top_row_loses(self):
        """
        Tests a not won top row does not result in a game win declaration
        """
        test = Game()
        test.board = [['0001', '1010', '0100', '0011'],
                      [None, None, None, None],
                      [None, None, None, None],
                      [None, None, None, None]]
        self.assertFalse(test.has_won_game('1010'))

    def test_second_row_wins(self):
        """
        Tests a won second row does result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, None],
                      ['1110', '1010', '1100', '0100'],
                      [None, None, None, None],
                      [None, None, None, None]]
        self.assertTrue(test.has_won_game('1100'))

    def test_second_row_loses(self):
        """
        Tests a not won second row does not result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, None],
                      ['1110', '1010', '1101', '0100'],
                      [None, None, None, None],
                      [None, None, None, None]]
        self.assertFalse(test.has_won_game('0100'))

    def test_third_row_wins(self):
        """
        Tests a won third row does result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, None],
                      [None, None, None, None],
                      ['0000', '1000', '0100', '0010'],
                      [None, None, None, None]]
        self.assertTrue(test.has_won_game('0000'))

    def test_third_row_loses(self):
        """
        Tests a not won third row does not result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, None],
                      [None, None, None, None],
                      ['0000', '1000', '0101', '0010'],
                      [None, None, None, None]]
        self.assertFalse(test.has_won_game('0101'))

    def test_fourth_row_wins(self):
        """
        Tests a won fourth row does result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, None],
                      [None, None, None, None],
                      [None, None, None, None],
                      ['1111', '1000', '1100', '1010']]
        self.assertTrue(test.has_won_game('1010'))

    def test_fourth_row_loses(self):
        """
        Tests a not won fourth row does not result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, None],
                      [None, None, None, None],
                      [None, None, None, None],
                      ['1111', '1000', '0100', '1010']]
        self.assertFalse(test.has_won_game('1111'))

    def test_first_column_wins(self):
        """
        Tests a won first column does result in a game win declaration
        """
        test = Game()
        test.board = [['1010', None, None, None],
                      ['1100', None, None, None],
                      ['1000', None, None, None],
                      ['1111', None, None, None]]
        self.assertTrue(test.has_won_game('1111'))

    def test_first_column_loses(self):
        """
        Tests a not won first column does not result in a game win declaration
        """
        test = Game()
        test.board = [['1010', None, None, None],
                      ['1100', None, None, None],
                      ['0010', None, None, None],
                      ['1111', None, None, None]]
        self.assertFalse(test.has_won_game('1111'))

    def test_second_column_wins(self):
        """
        Tests a won second column does result in a game win declaration
        """
        test = Game()
        test.board = [[None, '1010', None, None],
                      [None, '1100', None, None],
                      [None, '1000', None, None],
                      [None, '1111', None, None]]
        self.assertTrue(test.has_won_game('1111'))

    def test_second_column_loses(self):
        """
        Tests a not won second column does not result in a game win declaration
        """
        test = Game()
        test.board = [[None, '1010', None, None],
                      [None, '0100', None, None],
                      [None, '1000', None, None],
                      [None, '1111', None, None]]
        self.assertFalse(test.has_won_game('0100'))

    def test_third_column_wins(self):
        """
        Tests a won third column does result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, '1010', None],
                      [None, None, '1100', None],
                      [None, None, '1000', None],
                      [None, None, '1111', None]]
        self.assertTrue(test.has_won_game('1010'))

    def test_third_column_loses(self):
        """
        Tests a not won third column does not result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, '1010', None],
                      [None, None, '0100', None],
                      [None, None, '1010', None],
                      [None, None, '1111', None]]
        self.assertFalse(test.has_won_game('1111'))

    def test_fourth_column_wins(self):
        """
        Tests a won fourth column does result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, '1010'],
                      [None, None, None, '1100'],
                      [None, None, None, '1000'],
                      [None, None, None, '1111']]
        self.assertTrue(test.has_won_game('1000'))

    def test_fourth_column_loses(self):
        """
        Tests a not won fourth column does not result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, '0010'],
                      [None, None, None, '1100'],
                      [None, None, None, '1000'],
                      [None, None, None, '1111']]
        self.assertFalse(test.has_won_game('0010'))

    def test_horizontal_one_wins(self):
        """
        Tests a won horizontal does result in a game win declaration
        """
        test = Game()
        test.board = [['1010', None, None, None],
                      [None, '1100', None, None],
                      [None, None, '1000', None],
                      [None, None, None, '1111']]
        self.assertTrue(test.has_won_game('1100'))

    def test_horizontal_one_loses(self):
        """
        Tests a not won horizontal does not result in a game win declaration
        """
        test = Game()
        test.board = [['1010', None, None, None],
                      [None, '0100', None, None],
                      [None, None, '1000', None],
                      [None, None, None, '1111']]
        self.assertFalse(test.has_won_game('1111'))

    def test_horizontal_two_wins(self):
        """
        Tests a won horizontal does result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, '1010'],
                      [None, None, '1100', None],
                      [None, '1000', None, None],
                      ['1111', None, None, None]]
        self.assertTrue(test.has_won_game('1000'))

    def test_horizontal_two_loses(self):
        """
        Tests a not won horizontal does not result in a game win declaration
        """
        test = Game()
        test.board = [[None, None, None, '1010'],
                      [None, None, '0100', None],
                      [None, '1000', None, None],
                      ['1111', None, None, None]]
        self.assertFalse(test.has_won_game('1010'))
