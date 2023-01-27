#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import socket
import threading
import time
from config import *

class Client:
    Compteur = 5

    def __init__(self, adresse, port, pseudo):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pseudo = pseudo
        print("\x1B[F\x1B[2K", end="")
        Client.Compteur = Client.Compteur+ 1
        now = str(datetime.now())[:-7]
        self.error = False
        try:
            self.s.connect((adresse, port))
            print("connect", "({}) : Connected.\n".format(now))
            self.send(self.pseudo)
            config.Config.controller.receiveClient("Connect")
        except ConnectionRefusedError:
            self.error = True
            print("error connect", "({}) : The server is not online.\n".format(now))
            config.Config.controller.receiveClient("noConnect")


    def receive(self):
        while not self.error:
            try:
                data = str(self.s.recv(1024))
                now = str(datetime.now())[:-7]
                if len(data) == 0:
                    self.error = True
                    self.s.close()
                    break
                else:
                    print("{}\n".format(data.decode()))
            except:
                self.error = True
                print(("error receive", "({}) : Server has been disconnected.\n".format(now)))
                self.s.close()
                break
                
    def send(self,msg = None):
        now = str(datetime.now())[:-7]
        sended = False
        try:
            self.s.send(bytes(msg, 'utf-8'))
            print("Moi - {}".format(msg))
            sended = True
        except:
            self.error = True
            print(("error send", "({}) : Server has been disconnected.\n".format(now)))
            self.s.close()
        return sended
            
    def inp(self):
        while not self.error:
            msg = input("\n")
            print("\x1B[F\x1B[2K", end="")
            if not self.send(msg):
                break

    def checkJeu(self):
        if "MESSAGE" in self.message:
            pass

if __name__ == "__main__":
    c1 = Client("lcoalhost",6000,None)
    t1 = threading.Thread(target=c1.receive)
    t1.start()

    t23 = threading.Thread(target=c1.inp)
    t23.start()