#!/usr/bin/env python3

import socket as s
import time as t
import pickle

class Peer:
    """
    A class which acts as a either a server or client.
    Only serves to send of receive data.
    Only difference between server and client is that server is set up to\
    accept a connection from the client.

    Attributes
    ----------
    HOST : string
        String containing the IP address intended to connect with. '127.0.0.1' is\
        loop back interface
    PORT : int
        Port number used to connect
    BUFSIZ : int
        Maximum number of bytes allowed to send over socket
    CONNECTION : socket
        socket housing remote connection, used to send data
    ACCEPT_SOCKET : socket
        socket used by server in order to accept connection from client
    SERVER : Bool
        Boolean to determine whether peer is acting as client of server

    Methods
    -------
    accept_client(self)
        Method to accept client as server
    connect_to_server(self)
        Method to connect to server as client
    send(self, data)
        method to send data over connection
    receive(self)
        method to receive data over connection
    teardown(self)
        method to close sockets when peer is no longer needed
    """
    HOST = '127.0.0.1'
    PORT = 65001
    BUFSIZ = 4096
    CONNECTION = None
    ACCEPT_SOCKET = None
    SERVER = False

    def __init__(self, server):
        """
        Setup, if not server, no setup is needed as client creates socket when \
        connecting to server.
        Parameters
        ----------
        server : Bool
            Determine whether peer should act as server or client
        """
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
        """
        Accepts client as server.
        """
        print("Waiting for incoming connection...")
        try:
            self.CONNECTION, _ = self.ACCEPT_SOCKET.accept()
            print("Client connected!")

        except KeyboardInterrupt:
            print("\nStopped incoming connections")
            self.ACCEPT_SOCKET.close()
            return

    def connect_to_server(self):
        """
        Connect to server as client
        """
        print("Connecting to server...")
        self.CONNECTION = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.CONNECTION.connect((self.HOST, self.PORT))
        print("Connected to server")

    def send(self, data):
        """
        Send data over socket. pickle.dumps encodes data as byte stream
        """
        self.CONNECTION.sendall(pickle.dumps(data))

    def receive(self):
        """
        Receive data from socket. recv() is blocking. pickle.loads preserves data types.
        """
        data = self.CONNECTION.recv(self.BUFSIZ)
        data = pickle.loads(data)
        return data

    def teardown(self):
        """
        Closes socket or sockets
        """
        self.CONNECTION.close()
        if self.SERVER:
            self.ACCEPT_SOCKET.close()


if __name__ == "__main__":
	Peer(False)
