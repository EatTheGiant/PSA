#! /usr/bin/env python3

import socket

ADRESA = "0.0.0.0"
PORT = 9999

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ADRESA, PORT))
    sock.listen(10)
    while(True):
        (clientSock, clientAdd) = sock.accept()
        sprava = clientSock.recv(1500)
        print("Sprava od {}:{} {}".format(clientAdd[0], clientAdd[1], clientAdd[sprava]))
        clientSock.close()