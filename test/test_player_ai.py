from unittest import TestCase
from game_engine.game import Game
from game_engine.player_ai import PlayerAI
from random import choice


class TestPlayerAIClass(TestCase):
    """
    Tests the PlayerAI class
    Author(s): Adam Ross
    Date: 13/02/19
    """

    def test_player_ai(self):
        """
        Tests PlayerAI class instance
        """
        test = PlayerAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerAI))

    def test_max_similarities_one(self):
        """
        Tests the max_similarities() method with three empty board cells
        """
        test = PlayerAI(Game(), "Test")
        test.game.board = [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]
        self.assertEqual([((0, 0), 2, 4), ((1, 0), 2, 2), ((2, 1), 3, 2)],
                         test.max_similarities('1100'))
        self.assertEqual([((0, 0), 2, 4), ((1, 0), 2, 1), ((2, 1), 3, 2)],
                         test.max_similarities('1101'))
        self.assertEqual([((0, 0), 2, 4), ((1, 0), 1, 3), ((2, 1), 3, 2)],
                         test.max_similarities('1010'))

    def test_max_similarities_two(self):
        """
        Tests the max_similarities() method with one empty board cell
        """
        test = PlayerAI(Game(), "Test")
        test.game.board = [['0001', '1000', None, '0100'],
                           ['1110', '0001', '0010', '0111'],
                           ['1001', '1100', '1110', '1011'],
                           ['0100', '0110', '0011', '1111']]
        self.assertEqual([((0, 2), 3, 1)], test.max_similarities('1101'))

    def test_max_similarities_three(self):
        """
        Tests the max_similarities() method with fourteen empty board cells
        """
        test = PlayerAI(Game(), "Test")
        test.game.board = [['0000', None, None, None],
                           [None, None, None, None],
                           [None, None, '1111', None],
                           [None, None, None, None]]
        self.assertEqual([((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                          ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                          ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                          ((2, 3), 1, 1), ((3, 3), 1, 4)],
                         test.max_similarities('0001'))
        self.assertEqual([((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                          ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                          ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                          ((2, 3), 1, 1), ((3, 3), 1, 4)],
                         test.max_similarities('0010'))
        self.assertEqual([((1, 0), 1, 2), ((2, 0), 1, 4), ((3, 0), 1, 2),
                          ((0, 1), 1, 2), ((1, 1), 1, 4), ((2, 1), 1, 2),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 2),
                          ((3, 2), 1, 2), ((0, 3), 1, 2), ((1, 3), 0, 16),
                          ((2, 3), 1, 2), ((3, 3), 1, 4)],
                         test.max_similarities('0011'))
        self.assertEqual([((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                          ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                          ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                          ((2, 3), 1, 1), ((3, 3), 1, 4)],
                         test.max_similarities('0100'))
        self.assertEqual([((1, 0), 1, 2), ((2, 0), 1, 4), ((3, 0), 1, 2),
                          ((0, 1), 1, 2), ((1, 1), 1, 4), ((2, 1), 1, 2),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 2),
                          ((3, 2), 1, 2), ((0, 3), 1, 2), ((1, 3), 0, 16),
                          ((2, 3), 1, 2), ((3, 3), 1, 4)],
                         test.max_similarities('0101'))
        self.assertEqual([((1, 0), 1, 2), ((2, 0), 1, 4), ((3, 0), 1, 2),
                          ((0, 1), 1, 2), ((1, 1), 1, 4), ((2, 1), 1, 2),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 2),
                          ((3, 2), 1, 2), ((0, 3), 1, 2), ((1, 3), 0, 16),
                          ((2, 3), 1, 2), ((3, 3), 1, 4)],
                         test.max_similarities('0110'))
        self.assertEqual([((1, 0), 1, 1), ((2, 0), 1, 4), ((3, 0), 1, 1),
                          ((0, 1), 1, 1), ((1, 1), 1, 4), ((2, 1), 1, 3),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 3),
                          ((3, 2), 1, 3), ((0, 3), 1, 1), ((1, 3), 0, 16),
                          ((2, 3), 1, 3), ((3, 3), 1, 4)],
                         test.max_similarities('0111'))
        self.assertEqual([((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                          ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                          ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                          ((2, 3), 1, 1), ((3, 3), 1, 4)],
                         test.max_similarities('1000'))
        self.assertEqual([((1, 0), 1, 2), ((2, 0), 1, 4), ((3, 0), 1, 2),
                          ((0, 1), 1, 2), ((1, 1), 1, 4), ((2, 1), 1, 2),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 2),
                          ((3, 2), 1, 2), ((0, 3), 1, 2), ((1, 3), 0, 16),
                          ((2, 3), 1, 2), ((3, 3), 1, 4)],
                         test.max_similarities('1001'))
        self.assertEqual([((1, 0), 1, 2), ((2, 0), 1, 4), ((3, 0), 1, 2),
                          ((0, 1), 1, 2), ((1, 1), 1, 4), ((2, 1), 1, 2),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 2),
                          ((3, 2), 1, 2), ((0, 3), 1, 2), ((1, 3), 0, 16),
                          ((2, 3), 1, 2), ((3, 3), 1, 4)],
                         test.max_similarities('1010'))
        self.assertEqual([((1, 0), 1, 1), ((2, 0), 1, 4), ((3, 0), 1, 1),
                          ((0, 1), 1, 1), ((1, 1), 1, 4), ((2, 1), 1, 3),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 3),
                          ((3, 2), 1, 3), ((0, 3), 1, 1), ((1, 3), 0, 16),
                          ((2, 3), 1, 3), ((3, 3), 1, 4)],
                         test.max_similarities('1011'))
        self.assertEqual([((1, 0), 1, 2), ((2, 0), 1, 4), ((3, 0), 1, 2),
                          ((0, 1), 1, 2), ((1, 1), 1, 4), ((2, 1), 1, 2),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 2),
                          ((3, 2), 1, 2), ((0, 3), 1, 2), ((1, 3), 0, 16),
                          ((2, 3), 1, 2), ((3, 3), 1, 4)],
                         test.max_similarities('1100'))
        self.assertEqual([((1, 0), 1, 1), ((2, 0), 1, 4), ((3, 0), 1, 1),
                          ((0, 1), 1, 1), ((1, 1), 1, 4), ((2, 1), 1, 3),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 3),
                          ((3, 2), 1, 3), ((0, 3), 1, 1), ((1, 3), 0, 16),
                          ((2, 3), 1, 3), ((3, 3), 1, 4)],
                         test.max_similarities('1101'))
        self.assertEqual([((1, 0), 1, 1), ((2, 0), 1, 4), ((3, 0), 1, 1),
                          ((0, 1), 1, 1), ((1, 1), 1, 4), ((2, 1), 1, 3),
                          ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 3),
                          ((3, 2), 1, 3), ((0, 3), 1, 1), ((1, 3), 0, 16),
                          ((2, 3), 1, 3), ((3, 3), 1, 4)],
                         test.max_similarities('1110'))

    def test_select_max_similarity_occurrence_count_one(self):
        """
        Tests max_similarity_occurrence_count() method at hard difficulty
        choice and with fourteen empty board cells
        """
        test = PlayerAI(Game(), "Test")
        test.game.pieces = dict()
        sims = [((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                ((2, 3), 1, 1), ((3, 3), 1, 4)]
        self.assertEqual(4, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if (len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 1, '1111')
                [2])
        sims = [((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                ((2, 3), 1, 1), ((3, 3), 1, 4)]
        self.assertEqual(4, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if (len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 1, '1111')
                [2])

    def test_select_max_similarity_occurrence_count_two(self):
        """
        Tests max_similarity_occurrence_count() method at hard difficulty
        choice and with three empty board cells
        """
        test = PlayerAI(Game(), "Test")
        test.game.pieces = dict()
        sims = [((0, 0), 2, 4), ((1, 0), 2, 2), ((2, 1), 3, 2)]
        self.assertEqual(2, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if(len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 1, '1111')
                [2])

    def test_select_max_similarity_occurrence_count_three(self):
        """
        Tests max_similarity_occurrence_count() method at hard difficulty
        choice and with one empty board cell
        """
        test = PlayerAI(Game(), "Test")
        test.game.pieces = dict()
        sims = [((0, 2), 3, 1)]
        self.assertEqual(1, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if(len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 1, '1111')
                [2])

    def test_select_max_similarity_occurrence_count_four(self):
        """
        Tests max_similarity_occurrence_count() method at easy difficulty
        choice and with fourteen empty board cells
        """
        test = PlayerAI(Game(), "Test")
        test.game.pieces = dict()
        sims = [((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                ((2, 3), 1, 1), ((3, 3), 1, 4)]
        self.assertEqual(1, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if(len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 0, '1111')
                [2])
        sims = [((1, 0), 1, 3), ((2, 0), 1, 4), ((3, 0), 1, 3),
                ((0, 1), 1, 3), ((1, 1), 1, 4), ((2, 1), 1, 1),
                ((3, 1), 0, 16), ((0, 2), 1, 4), ((1, 2), 1, 1),
                ((3, 2), 1, 1), ((0, 3), 1, 3), ((1, 3), 0, 16),
                ((2, 3), 1, 1), ((3, 3), 1, 4)]
        self.assertEqual(1, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if(len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 0, '1111')
                [2])

    def test_select_max_similarity_occurrence_count_five(self):
        """
        Tests max_similarity_occurrence_count() method at easy difficulty
        choice and with three empty board cells
        """
        test = PlayerAI(Game(), "Test")
        test.game.pieces = dict()
        sims = [((0, 0), 2, 4), ((1, 0), 2, 2), ((2, 1), 3, 2)]
        self.assertEqual(2, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if (len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 0, '1111')
                [2])

    def test_select_max_similarity_occurrence_count_six(self):
        """
        Tests max_similarity_occurrence_count() method at easy difficulty
        choice and with one empty board cell
        """
        test = PlayerAI(Game(), "Test")
        test.game.pieces = dict()
        sims = [((0, 2), 3, 1)]
        self.assertEqual(1, test.select_best_sim_count([(i, j,
                k) for i, j, k in sims if (len([m for l, m, n in sims if m != 2
                ]) > 0 and j == max([m for l, m, n in sims if m != 2])) or j ==
                max([m for l, m, n in sims])] if len(test.game.pieces) < 15
                else [choice([((y, x), 0, 0) for x in range(test.game.N) for y
                in range(test.game.N) if test.game.is_cell_empty(y, x)])], 0, '1111')
                [2])
