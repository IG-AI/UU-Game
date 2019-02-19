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
        
        player_list = ["Erik", "Johan", "Fredrik", "Ilda", "Emma", "Sandra", "Davide", "Viktor"]
        t = tour.Tournament(player_list)
        initial_bracket = t.get_scoreboard()
        players = t.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t.next_game(players[0])
        players = t.opponents
        self.assertNotEqual(initial_bracket, t.get_scoreboard())
        t.next_game(players[0])
        players = t.opponents
        t.next_game(players[0])
        players = t.opponents
        t.next_game(players[0])
        players = t.opponents
        t.next_game(players[0])
        players = t.opponents
        t.next_game(players[0])
        players = t.opponents
        t.next_game(players[0])
        players = t.opponents
        self.assertEqual(0, len(players))

        player_list = ["Erik", "Johan", "Fredrik", "Ilda", "Emma", "Sandra", "Davide"]
        t2 = tour.Tournament(player_list)
        initial_bracket = t2.get_scoreboard()
        players = t2.opponents
        self.assertEqual(2, len(players))
        self.assertNotEqual(players[0], players[1])
        t2.next_game(players[0])
        players = t2.opponents
        self.assertNotEqual(initial_bracket, t2.get_scoreboard())
        t2.next_game(players[0])
        players = t2.opponents
        t2.next_game(players[0])
        players = t2.opponents
        t2.next_game(players[0])
        players = t2.opponents
        t2.next_game(players[0])
        players = t2.opponents
        t2.next_game(players[0])
        players = t2.opponents
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