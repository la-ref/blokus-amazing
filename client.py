#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import socket
import threading
import time

class Client:

    PORT = 5005
    Compteur = 5

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nom = "Client"+str(Client.Compteur)
        Client.Compteur = Client.Compteur+ 1
        now = str(datetime.now())[:-7]
        try:
            self.s.connect(("localhost", Client.PORT))
            print("connect", "({}) : Connected.\n".format(now))
            self.send()
            time.sleep(1)
            self.send("penis")
        except ConnectionRefusedError:
            print("error connect", "({}) : The server is not online.\n".format(now))

    def receive(self):
        while True:
            data = str(self.s.recv(1024).decode())
            now = str(datetime.now())[:-7]
            if len(data) == 0:
                pass
            else:
                print("receive", "({}) : {}\n".format(now, data))

    def send(self,msg = None):
        if msg:
            respond = msg
        else:
            respond = self.nom
        now = str(datetime.now())[:-7]
        try:
            self.s.send(bytes(respond, 'utf-8'))
            print(("send", "({}) : {}\n".format(now, respond)))
        except BrokenPipeError:
            print(("error send", "({}) : Server has been disconnected.\n".format(now)))
            self.s.close()


c1 = Client()
t1 = threading.Thread(target=c1.receive)
t1.start()
