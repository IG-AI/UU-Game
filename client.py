#!/usr/bin/env python3

import socket as s
import time as t
import pickle

class Client:
    NICK = ''
    HOST = '127.0.0.1'
    PORT = 65001
    BUFSIZ = 4096

    def __init__(self):
        try:
            CONNECTION = self.connect_to_server()
            t.sleep(3)
            print("sending")
            self.simulate(CONNECTION)
        except(KeyboardInterrupt, SystemExit):
            print("\nShutting down client")

    def connect_to_server(self):
        # AF_INET = IPv4, SOCK_STREAM = TCP Socket
        CONNECTION = s.socket(s.AF_INET, s.SOCK_STREAM)
        print("Connecting to server...")
        CONNECTION.connect((self.HOST, self.PORT))
        print("Connected to server")

        self.NICK = raw_input("Select your name: ")
        CONNECTION.sendall(pickle.dumps(self.NICK))
        return CONNECTION

    def simulate(self, con):
        i = 0
        while True:
            con.sendall(pickle.dumps(i)) # Send encoded integer
            data = con.recv(self.BUFSIZ) # Receive endoded data
            i = pickle.loads(data)       # Decode data
            print(i)
            i += 1

    def send_message(self, message, con):
        con.sendall(pickle.dumps(message))
        t.sleep(3)
        return


if __name__ == "__main__":
	Client()
