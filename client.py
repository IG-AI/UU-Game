#!/usr/bin/env python3

import socket as s
import time as t
import pickle

class Client:
    NICK = ''
    HOST = '127.0.0.1'
    PORT = 65005
    BUFSIZ = 4096
    CONNECTION = None

    def __init__(self, nick_name):
        try:
            self.NICK = nick_name
            CONNECTION = self.connect_to_server()
        except(KeyboardInterrupt, SystemExit):
            print("\nShutting down client")

    def connect_to_server(self):
        # AF_INET = IPv4, SOCK_STREAM = TCP Socket
        self.CONNECTION = s.socket(s.AF_INET, s.SOCK_STREAM)
        print(self.NICK, "connecting to server...")
        self.CONNECTION.connect((self.HOST, self.PORT))
        print(self.NICK, "Connected to server")

        self.CONNECTION.sendall(pickle.dumps(self.NICK))

    def send(self, data):
        self.CONNECTION.sendall(pickle.dumps(data))

    def receive(self):
        data = self.CONNECTION.recv(self.BUFSIZ)
        data = pickle.loads(data)
        return data

    def teardown(self):
        self.CONNECTION.close()


if __name__ == "__main__":
	Client()
