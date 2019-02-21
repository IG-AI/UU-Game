import unittest
import io
import sys
import peer
import graphics as g
import tournament as tour
from threading import Thread
import time

class TestPeer(unittest.TestCase):
    def test_data_integrity(self):
        s = peer.Peer(True)
        t = Thread(target=run_client, args=())
        t.start()
        time.sleep(0.2)
        s.accept_client()

        data_orig = [1,2,3]
        s.send(data_orig)
        data = s.receive()
        self.assertEqual(data, data_orig)

        data_orig = "test string"
        s.send(data_orig)
        data = s.receive()
        self.assertEqual(data, data_orig)

        data_orig = 123
        s.send(data_orig)
        data = s.receive()
        self.assertEqual(data, data_orig)
        s.teardown()

    def test_graphics(self):
        expected_length = 161
        terminal_text = io.StringIO()
        sys.stdout = terminal_text

        g.make_header("test")
        self.assertNotEqual("test", terminal_text.getvalue())
        self.assertGreaterEqual(len(terminal_text.getvalue()), expected_length-1)
        self.assertLessEqual(len(terminal_text.getvalue()), expected_length+1)
        terminal_text.truncate(0)
        terminal_text.seek(0)

        g.make_header("")
        self.assertGreaterEqual(len(terminal_text.getvalue()), expected_length-1)
        self.assertLessEqual(len(terminal_text.getvalue()), expected_length+1)
        terminal_text.truncate(0)
        terminal_text.seek(0)

        g.make_header("testtesttesttesttest")
        self.assertGreaterEqual(len(terminal_text.getvalue()), expected_length-1)
        self.assertLessEqual(len(terminal_text.getvalue()), expected_length+1)

        sys.stdout = sys.__stdout__

    def test_tournament(self):
        player_list = ["Erik", "Johan", "Fredrik", "Ilda", "Emma", "Sandra", "Davide", "Viktor", "Sam"]
        with self.assertRaises(Exception):
            tour.Tournament(player_list)

        player_list = ["Erik", "Johan"]
        with self.assertRaises(Exception):
            tour.Tournament(player_list)

        player_list = []
        with self.assertRaises(Exception):
            tour.Tournament(player_list)

        player_list = [[],[],[]]
        with self.assertRaises(Exception):
            tour.Tournament(player_list)
        
        player_list = ["Erik", "Johan", "Fredrik", "Ilda", "Emma", "Sandra", "Davide", "Viktor"]
        t8 = tour.Tournament(player_list)
        initial_bracket = t8.get_scoreboard()
        players = t8.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t8.next_game(players[0])
        players = t8.opponents
        self.assertNotEqual(initial_bracket, t8.get_scoreboard())
        t8.next_game(players[0])
        players = t8.opponents
        t8.next_game(players[0])
        players = t8.opponents
        t8.next_game(players[0])
        players = t8.opponents
        t8.next_game(players[0])
        players = t8.opponents
        t8.next_game(players[0])
        players = t8.opponents
        t8.next_game(players[0])
        players = t8.opponents
        self.assertEqual(0, len(players))

        player_list = ["Erik", "Johan", "Fredrik", "Ilda", "Emma", "Sandra", "Davide"]
        t7 = tour.Tournament(player_list)
        initial_bracket = t7.get_scoreboard()
        players = t7.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t7.next_game(players[0])
        players = t7.opponents
        self.assertNotEqual(initial_bracket, t7.get_scoreboard())
        t7.next_game(players[0])
        players = t7.opponents
        t7.next_game(players[0])
        players = t7.opponents
        t7.next_game(players[0])
        players = t7.opponents
        t7.next_game(players[0])
        players = t7.opponents
        t7.next_game(players[0])
        players = t7.opponents
        self.assertEqual(0, len(players))

        player_list = ["Erik", "Johan", "Fredrik", "Ilda", "Emma", "Sandra"]
        t6 = tour.Tournament(player_list)
        initial_bracket = t6.get_scoreboard()
        players = t6.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t6.next_game(players[0])
        players = t6.opponents
        self.assertNotEqual(initial_bracket, t6.get_scoreboard())
        t6.next_game(players[0])
        players = t6.opponents
        t6.next_game(players[0])
        players = t6.opponents
        t6.next_game(players[0])
        players = t6.opponents
        t6.next_game(players[0])
        players = t6.opponents
        self.assertEqual(0, len(players))

        player_list = ["Erik", "Johan", "Fredrik", "Ilda", "Emma"]
        t5 = tour.Tournament(player_list)
        initial_bracket = t5.get_scoreboard()
        players = t5.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t5.next_game(players[0])
        players = t5.opponents
        self.assertNotEqual(initial_bracket, t5.get_scoreboard())
        t5.next_game(players[0])
        players = t5.opponents
        t5.next_game(players[0])
        players = t5.opponents
        t5.next_game(players[0])
        players = t5.opponents
        self.assertEqual(0, len(players))

        player_list = ["Erik", "Johan", "Fredrik", "Ilda"]
        t4 = tour.Tournament(player_list)
        initial_bracket = t4.get_scoreboard()
        players = t4.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t4.next_game(players[0])
        players = t4.opponents
        self.assertNotEqual(initial_bracket, t4.get_scoreboard())
        t4.next_game(players[0])
        players = t4.opponents
        t4.next_game(players[0])
        players = t4.opponents
        self.assertEqual(0, len(players))

        player_list = ["Erik", "Johan", "Fredrik"]
        t3 = tour.Tournament(player_list)
        initial_bracket = t3.get_scoreboard()
        players = t3.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t3.next_game(players[0])
        players = t3.opponents
        self.assertNotEqual(initial_bracket, t3.get_scoreboard())
        t3.next_game(players[0])
        players = t3.opponents
        self.assertEqual(0, len(players))

def run_client():
    c = peer.Peer(False)
    c.connect_to_server()
    data = c.receive()
    c.send(data)
    data = c.receive()
    c.send(data)
    data = c.receive()
    c.send(data)
    c.teardown()
    return

if __name__ == "__main__":
    unittest.main()