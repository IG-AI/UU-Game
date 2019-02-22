from unittest import TestCase
from game_engine.game import Game


class TestGameClass(TestCase):
    """
    Tests the Game class, its init variables and has_next_play() method
    Author: Adam Ross
    Date: 08/02/19
    """

    def test_game(self):
        """
        Tests Game class instance
        """
        test = Game()
        self.assertTrue(isinstance(test, Game))

    def test_pieces(self):
        """
        Tests pieces dictionary variable in Game class instance
        """
        test = Game()
        expctd = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                  '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                  '8': '1000', '9': '1001', '10': '1010', '11': '1011',
                  '12': '1100', '13': '1101', '14': '1110', '15': '1111'}
        self.assertEqual(test.pieces, expctd)
        expctd.pop('11')
        self.assertNotEqual(test.pieces, expctd)
        test.pieces.pop('11')
        self.assertEqual(test.pieces, expctd)

    def test_board(self):
        """
        Tests board multidimensional array variable in Game class instance
        """
        test = Game()
        expctd = [[None, None, None, None], [None, None, None, None],
                  [None, None, None, None], [None, None, None, None]]
        self.assertEqual(test.board, expctd)
        expctd = [['0000', None, None, None], [None, None, None, None],
                  [None, None, None, None], [None, None, None, None]]
        self.assertNotEqual(test.board, expctd)
        test.board[0][0] = '0000'
        self.assertEqual(test.board, expctd)
        expctd = [['0000', None, None, None], [None, None, None, None],
                  [None, None, '1111', None], [None, None, None, None]]
        self.assertNotEqual(test.board, expctd)
        test.board[2][2] = '1111'
        self.assertEqual(test.board, expctd)

    def test_has_next_play(self):
        """
        Tests has_next_play() method in Game class instance
        """
        test = Game()
        self.assertEqual(len(test.pieces), 16)
        self.assertTrue(test.has_next_play())
        test.pieces.pop('0')
        self.assertEqual(len(test.pieces), 15)
        self.assertTrue(test.has_next_play())
        test.pieces = {}
        self.assertFalse(test.has_next_play())
