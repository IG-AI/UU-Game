from unittest import TestCase
from game_engine.play import Play
from game_engine.player_human import PlayerHuman
from game_engine.player_ai_medium import PlayerMediumAI
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_hard import PlayerHardAI


class TestInitPlayers(TestCase):
    """
    Tests the init_players() method in the Play class
    Author(s): Adam Ross; Gustav From; Laurin Kerle
    Date: 14/02/19
    """

    def test_human_vs_human(self):
        """
        Tests initialisation of two human players in
        human vs human game play
        """
        test, count = Play(), 0
        test.init_players(1, None, "Andy", "Joe")

        for i in range(2):
            if test.current_player.name == "Andy":
                self.assertTrue(isinstance(test.current_player, PlayerHuman))
                count += 1
            elif test.current_player.name == "Joe":
                self.assertTrue(isinstance(test.current_player, PlayerHuman))
                count += 1
            test.change_player()
        self.assertEqual(len(test.players), 2)
        self.assertEqual(count, 2)

    def test_medium_difficulty_human_vs_ai(self):
        """
        Tests initialisation of human and AI players in
        human vs AI game play at medium difficulty
        """
        test, count = Play(), 0
        test.init_players(2, 2, "Pete")

        for i in range(2):
            if test.current_player.name == "Pete":
                self.assertTrue(isinstance(test.current_player, PlayerHuman))
                count += 1
            elif test.current_player.name == "Player Two":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerMediumAI))
                count += 1
            test.change_player()
        self.assertEqual(len(test.players), 2)
        self.assertEqual(count, 2)

    def test_medium_difficulty_ai_vs_ai(self):
        """
        Tests initialisation of two AI players in
        AI vs AI game play at medium difficulty
        """
        test, count = Play(), 0
        test.init_players(3, 2)

        for i in range(2):
            if test.current_player.name == "Player One":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerMediumAI))
                count += 1
            elif test.current_player.name == "Player Two":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerMediumAI))
                count += 1
            test.change_player()
        self.assertEqual(len(test.players), 2)
        self.assertEqual(count, 2)

    def test_easy_difficulty_human_vs_ai(self):
        """
        Tests initialisation of human and AI players in
        human vs AI game play at easy difficulty
        """
        test, count = Play(), 0
        test.init_players(2, 1, "Peter")

        for i in range(2):
            if test.current_player.name == "Peter":
                self.assertTrue(isinstance(test.current_player, PlayerHuman))
                count += 1
            elif test.current_player.name == "Player Two":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerEasyAI))
                count += 1
            test.change_player()
        self.assertEqual(len(test.players), 2)
        self.assertEqual(count, 2)

    def test_easy_difficulty_ai_vs_ai(self):
        """
        Tests initialisation of two AI players in
        AI vs AI game play at easy difficulty
        """
        test, count = Play(), 0
        test.init_players(3, 1)

        for i in range(2):
            if test.current_player.name == "Player One":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerEasyAI))
                count += 1
            elif test.current_player.name == "Player Two":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerEasyAI))
                count += 1
            test.change_player()
        self.assertEqual(len(test.players), 2)
        self.assertEqual(count, 2)

    def test_hard_difficulty_human_vs_ai(self):
        """
        Tests initialisation of human and AI players in
        human vs AI game play at hard difficulty
        """
        test, count = Play(), 0
        test.init_players(2, 3, "Pete")

        for i in range(2):
            if test.current_player.name == "Pete":
                self.assertTrue(isinstance(test.current_player, PlayerHuman))
                count += 1
            elif test.current_player.name == "Player Two":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerHardAI))
                count += 1
            test.change_player()
        self.assertEqual(len(test.players), 2)
        self.assertEqual(count, 2)

    def test_hard_difficulty_ai_vs_ai(self):
        """
        Tests initialisation of two AI players in
        AI vs AI game play at hard difficulty
        """
        test, count = Play(), 0
        test.init_players(3, 3)

        for i in range(2):
            if test.current_player.name == "Player One":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerHardAI))
                count += 1
            elif test.current_player.name == "Player Two":
                self.assertTrue(isinstance(test.current_player,
                                           PlayerHardAI))
                count += 1
            test.change_player()
        self.assertEqual(len(test.players), 2)
        self.assertEqual(count, 2)
