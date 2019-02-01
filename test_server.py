#!/usr/bin/env python3

import socket
import time as t
import pickle

HOST = '127.0.0.1'
PORT = 65433

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("Waiting for incomming connection...")
        s.listen()
        conn, addr = s.accept() # conn = connected socket, addr = connected IP
        with conn:
            print("Connected by", addr)

            pingpong = True
            # Bounces incrementally increasing Integer back and forth
            if pingpong:
                while True:
                    data = conn.recv(1024)
                    data = pickle.loads(data)
                    print(repr(data))
                    data += 1
                    conn.sendall(pickle.dumps(data))

            # Receives and prints data
            while True:
                print("Waiting for data")
                data = conn.recv(1024)
                if not data:
                    continue
                data = pickle.loads(data)
                print("Received:", repr(data))
                print("Of type:", type(data))
                t.sleep(2)

if __name__ == "__main__":
	main()

