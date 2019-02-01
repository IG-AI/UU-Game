#!/usr/bin/env python3

import socket as s
import time as t
import pickle
from threading import Thread

class Server:
    HOST = '127.0.0.1'
    PORT = 65001
    BUFSIZ = 4096

    client_list = {}

    def __init__(self):
        try:
            #ACCEPT_THREAD = Thread(target=self.accept_clients)
            #ACCEPT_THREAD.daemon = True
            #ACCEPT_THREAD.start()
            #while True: t.sleep(100)
            self.accept_clients()
        except (KeyboardInterrupt, SystemExit):
            print("\nShutting down server")

    def accept_clients(self):
        # AF_INET = IPv4, SOCK_STREAM = TCP Socket
        ACCEPT_SOCKET = s.socket(s.AF_INET, s.SOCK_STREAM)
        ACCEPT_SOCKET.bind((self.HOST, self.PORT))
        ACCEPT_SOCKET.listen()

        nr_connections = 0 # 
        while nr_connections < 2:
            print("Waiting for incoming connections...")
            try:
                client_socket, _ = ACCEPT_SOCKET.accept()
                print("client:", "connected")
                nick = client_socket.recv(self.BUFSIZ)
                nick = pickle.loads(nick)
                self.client_list[nick] = client_socket
                nr_connections += 1

            except KeyboardInterrupt:
                print("\nStopped incoming connections")
                ACCEPT_SOCKET.close()
                return

        print("All clients connected!")

        # Clients must choose name "a" and "b" for the relay test to work
        self.relay_game("a", "b")

    def relay_game(self, player_1, player_2):
        # Get the sockets
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
