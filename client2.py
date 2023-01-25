#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import socket
import threading
import time
from Vues.connexion import Connexion 

class Client:
    Compteur = 5

    def __init__(self, adresse, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nom = input("Ton pseudo : \n")
        print("\x1B[F\x1B[2K", end="")
        Client.Compteur = Client.Compteur+ 1
        now = str(datetime.now())[:-7]
        try:
            self.s.connect((adresse, port))
            print("connect", "({}) : Connected.\n".format(now))
            self.send(self.nom)
        except ConnectionRefusedError:
            print("error connect", "({}) : The server is not online.\n".format(now))

    def receive(self):
        while True:
            data = str(self.s.recv(1024).decode())
            now = str(datetime.now())[:-7]
            if len(data) == 0:
                pass
            else:
                self.message = format(data)
                print("{}\n".format(data))
                self.checkJeu()

    def send(self,msg = None):
        now = str(datetime.now())[:-7]
        try:
            self.s.send(bytes(msg, 'utf-8'))
            print("Moi - {}".format(msg))
        except BrokenPipeError:
            print(("error send", "({}) : Server has been disconnected.\n".format(now)))
            self.s.close()
            
    def inp(self):
        while True:
            msg = input("\n")
            print("\x1B[F\x1B[2K", end="")
            self.send(msg)

    def checkJeu(self):
        if "MESSAGE" in self.message:
            pass
            

if __name__ == "__main__":
    c1 = Client("lcoalhost",6000)
    t1 = threading.Thread(target=c1.receive)
    t1.start()

    t23 = threading.Thread(target=c1.inp)
    t23.start()
