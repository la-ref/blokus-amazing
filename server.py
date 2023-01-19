#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import socket
import threading
import time

class Server:
    clients = []
    PORT = 5000

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(("localhost", Server.PORT)) # n'importe quelle adresse
        self.s.listen(10)

    def accept(self):
        c, addr = self.s.accept()
        self.clients.append(c)
        data = c.recv(1024)
        print("insert", "({}) : {} connected.\n".format(str(datetime.now())[:-7], str(data)[1:]))

    def receive(self):
        for i in self.clients:
            def f():
                data = str(i.recv(1024).decode())
                now = str(datetime.now())[:-7]
                if len(data) == 0:
                    pass
                else:
                    print("message !!", "({}) : {}\n".format(now, data))
                    time.sleep(1)
                    self.send("msg du serveur")


            t1_2_1 = threading.Thread(target=f)
            t1_2_1.start()

    def condition(self):
        while True:
            t1_1 = threading.Thread(target=self.accept)
            t1_1.daemon = True
            t1_1.start()
            t1_1.join(1)
            t1_2 = threading.Thread(target=self.receive)
            t1_2.daemon = True
            t1_2.start()
            t1_2.join(1)

    def send(self,msg):
        now = str(datetime.now())[:-7]
        try:
            for i in self.clients:
                i.send(bytes(msg, "utf-8"))
                print("envoi", "({}) : {}\n".format(now,msg))
        except BrokenPipeError:
            print("envoi error", "({}) : Client has been disconnected.\n".format(now))


s1 = Server()
s1.condition()


# def connect():
#     t1 = threading.Thread(target=s1.connect)
#     t1.start()


# def send():
#     t2 = threading.Thread(target=s1.send)
#     t2.start()


# def clear():
#     text.delete("1.0", "end")




if __name__ == "__main__":

    t0 = threading.Thread(target=root.mainloop)
    t0.run()