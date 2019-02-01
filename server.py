#!/usr/bin/env python3

import socket as s
import time as t
import pickle
from threading import Thread

class Server:
    HOST = ''
    PORT = 65000
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
            self.accept_handler()
            self.accept_clients()
        except (KeyboardInterrupt, SystemExit):
            print("\nShutting down server")

    def accept_handler(self):
        print("Waiting for handler to connect...")
        self.HANDLER, _ = self.ACCEPT_SOCKET.accept()
        print("Handler connected")


    def accept_clients(self):
        nr_connections = 0
        while nr_connections < 2:
            print("Waiting for incoming connections...")
            try:
                client_socket, _ = self.ACCEPT_SOCKET.accept()
                print("client:", "connected")
                nick = client_socket.recv(self.BUFSIZ)
                nick = pickle.loads(nick)
                self.client_list[nick] = client_socket
                nr_connections += 1

            except KeyboardInterrupt:
                print("\nStopped incoming connections")
                self.ACCEPT_SOCKET.close()
                return

        print("All clients connected!")
        data = pickle.dumps(list(self.client_list.keys()))
        self.HANDLER.sendall(data)


    def relay_game(self):
        # Get the sockets
        players = self.HANDLER.recv(self.BUFSIZ)
        players = pickle.loads(players)
        player_1 = players[1]
        player_2 = players[0]
        player_1 = self.client_list[player_1]
        player_2 = self.client_list[player_2]
        while True:
            # Relay messages between players. recv is blocking.
            data = player_1.recv(self.BUFSIZ)
            player_2.sendall(data)
            data = player_2.recv(self.BUFSIZ)
            player_1.sendall(data)

    def accept_message(self, client):
        while True:
            message = client.recv(self.BUFSIZ)
            print("Received")
            message = pickle.loads(message)
            print("Printing")
            print(message)


if __name__ == "__main__":
	Server()
