from unittest import TestCase
from game_engine.game import Game


class TestBinaryCharacteristicCount(TestCase):
    """
    Tests the bin_count() method in the Game class
    Author: Adam Ross
    Date: 08/02/19
    """

    def test_top_row(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the top row of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', '0101'],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([2, 1, 0, 1], test.bin_count('0110', 0, 0, 0, 1, 3))

    def test_second_row(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the second row of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', '0101'],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([3, 1, 2, 2], test.bin_count('0110', 1, 0, 0, 1, 3))

    def test_third_row(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the third row of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', '0101'],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([0, 1, 2, 0], test.bin_count('0110', 2, 1, 0, 1, 3))

    def test_fourth_row(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the fourth row of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', '0101'],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', None]]
        self.assertEqual([3, 2, 2, 2], test.bin_count('0110', 3, 3, 0, 1, 3))

    def test_first_column(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the first column of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', '0101'],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([1, 1, 0, 1], test.bin_count('0110', 1, 0, 1, 0, 3))

    def test_second_column(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the second column of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', '0101'],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([2, 1, 1, 3], test.bin_count('0110', 2, 1, 1, 0, 3))

    def test_third_column(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the third column of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', '0101'],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', None, '1110']]
        self.assertEqual([2, 1, 2, 1], test.bin_count('0110', 3, 2, 1, 0, 3))

    def test_fourth_column(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along the fourth column of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', None],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([1, 2, 3, 1], test.bin_count('0110', 0, 3, 1, 0, 3))

    def test_horizontal_one(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along a horizontal row of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', None],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([2, 1, 1, 2], test.bin_count('0110', 0, 3, 1, -1, 3))

    def test_horizontal_two(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along a horizontal row of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', None],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([1, 2, 2, 2], test.bin_count('0110', 0, 0, 1, 1, 3))

    def test_two_blocks(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along two blocks of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', None],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([1, 1, 1, 1], test.bin_count('0110', 0, 0, 1, 1, 2))

    def test_one_block(self):
        """
        Tests the number of similarities between pieces for each characteristic
        along one block of pieces is the expected number of similarities
        """
        test = Game()
        test.board = [[None, '1000', '0001', None],
                      [None, '0000', '0010', '0111'],
                      ['1001', None, '1111', '1011'],
                      ['0100', '0110', '0011', '1110']]
        self.assertEqual([1, 0, 0, 1], test.bin_count('0110', 0, 0, 1, 1, 1))
