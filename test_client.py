#!/usr/bin/env python3

import socket
import pickle

HOST = '127.0.0.1'
PORT = 65433

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        pingpong = True
        # Bounces incrementally increasing Integer back and forth
        if pingpong:
            data = 0
            while True:
                s.sendall(pickle.dumps(data))
                data = pickle.loads(s.recv(1024))
                print(repr(data))
                data += 1


        while True:
            choice = input("Do you wish to send? [Y]es/[N]o\n")
            if choice == "Y":
                send(s)
            else: continue
        receive(s)

def send(s):
    # Sends different data types to server
    while True:
        choice = input("What do you wish to send?\n [A]rray. [D]ictionary. [S]tring\n")
        print(choice, type(choice))
        if choice == "A":
            array = [1,2,3]
            array = pickle.dumps(array)
            s.sendall(array)

        elif choice == "D":
            diction = {1:"Hey,", 2:"cool", 3:"kille!"}
            diction = pickle.dumps(diction)
            s.sendall(diction)

        elif choice == "S":
            string = "This should be a string!"
            string = pickle.dumps(string)
            s.sendall(string)
        else: break


def receive(s):
    data = s.recv(1024)
    print("Received", repr(data))

if __name__ == "__main__":
	main()
