from unittest import TestCase
from game_engine.game import Game
from game_engine.play import Play
from game_engine.player_ai_medium import PlayerMediumAI


class TestPlayClass(TestCase):
    """
    Tests the Play class, its init variables and change_player() method
    Author: Adam Ross
    Date: 08/02/19
    """

    def test_play(self):
        """
        Tests Play class instance
        """
        test = Play()
        self.assertTrue(isinstance(test, Play))

    def test_game_instance(self):
        """
        Tests Game instance in Play class instance
        """
        test = Play()
        self.assertTrue(isinstance(test.game, Game))

    def test_players(self):
        """
        Tests players array variable in Play class instance
        """
        test = Play()
        self.assertEqual(test.players, [])
        test.init_players(3, 2)
        self.assertEqual(len(test.players), 2)

        for i in range(2):
            self.assertTrue(isinstance(test.players[i], PlayerMediumAI))

    def test_current_and_change_player(self):
        """
        Tests current_player variable and change_player() method
        in Play class instance
        """
        test = Play()
        self.assertEqual(test.current_player, None)
        test.init_players(3, 2)
        player_one = test.current_player
        self.assertTrue(isinstance(player_one, PlayerMediumAI))
        player_two = test.change_player()
        self.assertTrue(isinstance(player_two, PlayerMediumAI))
        self.assertNotEqual(player_one, player_two)

    def test_selected_piece(self):
        """
        Tests selected_piece variable in Play class instance
        """
        test = Play()
        self.assertEqual(test.selected_piece, None)
        test.selected_piece = test.game.pieces['0']
        self.assertEqual(test.selected_piece, '0000')
        self.assertEqual(test.selected_piece, test.game.pieces['0'])

    def test_play_auto(self):
        """
        Tests that play_auto() returns only game result and winner if any
        play_auto() returns winner's name if game won, or None if game drawn
        """
        p_one, p_two = "Player One", "Player Two"
        test = Play()
        test.players = [PlayerMediumAI(test.game, p_one),
                        PlayerMediumAI(test.game, p_two)]
        test.current_player = test.players[0]
        result = test.play_auto()

        if result:
            self.assertTrue(result in [i.name for i in test.players])
        else:
            self.assertFalse(result)
