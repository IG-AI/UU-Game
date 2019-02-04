#!/usr/bin/env python3

import socket as s
import time as t
import pickle

class Peer:
    NICK = ''
    HOST = '127.0.0.1'
    PORT = 65000
    BUFSIZ = 4096
    CONNECTION = None
    ACCEPT_SOCKET = None
    SERVER = False

    def __init__(self, server):
        if server:
            try:
                print("Booting server")
                self.SERVER = True
                # AF_INET = IPv4, SOCK_STREAM = TCP Socket
                self.ACCEPT_SOCKET = s.socket(s.AF_INET, s.SOCK_STREAM)
                self.ACCEPT_SOCKET.bind((self.HOST, self.PORT))
                self.ACCEPT_SOCKET.listen()
            except (KeyboardInterrupt, SystemExit):
                print("\nShutting down server")

    def accept_client(self):
        print("Waiting for incoming connection...")
        try:
            self.CONNECTION, _ = self.ACCEPT_SOCKET.accept()

        except KeyboardInterrupt:
            print("\nStopped incoming connections")
            self.ACCEPT_SOCKET.close()
            return

    print("Client connected!")

    def connect_to_server(self):
        print("Connecting to server...")
        self.CONNECTION = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.CONNECTION.connect((self.HOST, self.PORT))
        print("Connected to server")

    def send(self, data):
        self.CONNECTION.sendall(pickle.dumps(data))

    def receive(self):
        data = self.CONNECTION.recv(self.BUFSIZ)
        data = pickle.loads(data)
        return data

    def teardown(self):
        self.CONNECTION.close()
        if self.SERVER:
            self.ACCEPT_SOCKET.close()


if __name__ == "__main__":
	Peer()
