#!/usr/bin/env python3

import socket as s
import time as t
import pickle

class Client:
    NICK = ''
    HOST = '127.0.0.1'
    PORT = 65000
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
        print("Connecting to server...")
        self.CONNECTION.connect((self.HOST, self.PORT))
        print("Connected to server")

        if self.NICK != "HANDLER":
            self.CONNECTION.sendall(pickle.dumps(self.NICK))

    def simulate(self, con):
        i = 0
        while True:
            con.sendall(pickle.dumps(i)) # Send encoded integer
            data = con.recv(self.BUFSIZ) # Receive endoded data
            i = pickle.loads(data)       # Decode data
            print(i)
            i += 1

    def send(self, data):
        self.CONNECTION.sendall(pickle.dumps(data))

    def receive(self):
        data = self.CONNECTION.recv(self.BUFSIZ)
        data = pickle.loads(data)
        return data


if __name__ == "__main__":
	Client()
