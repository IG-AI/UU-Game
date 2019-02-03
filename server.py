#!/usr/bin/env python3

import socket as s
import time as t
import pickle
from threading import Thread

class Server:
    HOST = ''
    PORT = 65005
    BUFSIZ = 4096
    HANDLER = None
    # AF_INET = IPv4, SOCK_STREAM = TCP Socket
    ACCEPT_SOCKET = s.socket(s.AF_INET, s.SOCK_STREAM)

    client_list = {}

    def __init__(self):
        try:
            print("Booting server")
            self.ACCEPT_SOCKET.bind((self.HOST, self.PORT))
            self.ACCEPT_SOCKET.listen()
        except (KeyboardInterrupt, SystemExit):
            print("\nShutting down server")

    def accept_clients(self, nr_players):
        nr_connections = 0
        while nr_connections < nr_players:
            print("Waiting for incoming connections...", nr_connections, "out of", nr_players, "connected.")
            try:
                client_socket, _ = self.ACCEPT_SOCKET.accept()
                nick = client_socket.recv(self.BUFSIZ)
                nick = pickle.loads(nick)
                print("client:", nick, "connected")
                self.client_list[nick] = client_socket
                nr_connections += 1

            except KeyboardInterrupt:
                print("\nStopped incoming connections")
                self.ACCEPT_SOCKET.close()
                return

        print("All clients connected!")

    def get_player_list(self):
        return list(self.client_list.keys())

    def relay_game(self, players):
        # Get the sockets
        player_1 = players[0]
        player_2 = players[1]
        player_1 = self.client_list[player_1]
        player_2 = self.client_list[player_2]
        player_1.sendall(pickle.dumps("SYNC")) # Synchronize
        player_2.sendall(pickle.dumps("SYNC"))
        tmp = player_1.recv(self.BUFSIZ)        # Acknowledgement
        tmp = player_2.recv(self.BUFSIZ)
        player_1.sendall(pickle.dumps("FIRST")) # Start game
        while True:
            # Bounce game state between players
            data = player_1.recv(self.BUFSIZ)
            data = pickle.loads(data)
            if data[0] == "WIN":
                player_2.sendall(pickle.dumps(data[1]))
                return players[0]
            player_2.sendall(pickle.dumps(data))

            data = player_2.recv(self.BUFSIZ)
            data = pickle.loads(data)
            if data[0] == "WIN":
                player_1.sendall(pickle.dumps(data[1]))
                return players[1]
            player_1.sendall(pickle.dumps(data))

    def teardown(self):
        self.ACCEPT_SOCKET.close()


if __name__ == "__main__":
	Server()
