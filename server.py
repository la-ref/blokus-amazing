#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import socket
import threading
import time

class Server:
    lobbies = []
    PORT = 5006

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostbyname(socket.gethostname()))
        self.s.bind(('localhost', Server.PORT)) # n'importe quelle adresse
        self.s.listen(10)

    def accept(self):
        c, addr = self.s.accept()
        added = False
        lob = 0
        cli = 0
        if len(Server.lobbies) > 0:
            for lobbyId in range(len(Server.lobbies)): 
                # if 1er joueur de la liste c'est lui l'admin
                
                if Server.lobbies[lobbyId]["game"] == None and len(Server.lobbies[lobbyId]["clients"]) < 4:
                    Server.lobbies[lobbyId]["clients"].append(c)
                    added = True
                    lob = lobbyId
                    cli = len(Server.lobbies[lobbyId]["clients"])-1
                if added:
                    break
                
        if not added:
            Server.lobbies.append( {
                "clients" : [],
                "players" : {},
                "game": None
            })
            lob = len(Server.lobbies)-1
            cli = 0
            Server.lobbies[lob]["clients"].append(c)
            
            
        #print(Server.lobbies,c)
        data = c.recv(8192)
        if len(data) == 0:
            
            print("ERREUR DEBUT !!!!!!!!")
            print("client déconnecter : , {}".format(Server.lobbies[lob]["clients"][cli]))
            Server.lobbies[lob]["clients"][cli].close()
            Server.lobbies[lob]["clients"].pop(cli)
        else:
            data = str(data.decode())
            Server.lobbies[lob]["players"][cli]=data
            self.send(str(data) + " est entré dans le lobby", cli, lob)
        
            print("cli & lob \n", cli, lob)
            print(Server.lobbies)
            print("insert", "({}) : {} connected.\n".format(str(datetime.now())[:-7], str(data)[1:]))
        
    # def joue(self):
    #     if Server.clients:
    
    def f(self, nbClient, nbLobby):
        
        try:
            data = Server.lobbies[nbLobby]["clients"][nbClient].recv(8192)
            now = str(datetime.now())[:-7]
            #print("message !!", "({}) : {}\n".format(now, data))
            data = str(data.decode())
            self.send(str(Server.lobbies[nbLobby]["players"][nbClient]) + " - " + data, nbClient, nbLobby)
        except:
            print("ERREUR READ !!!!!!!!")
            # check si le client est dedans
            print("client déconnecter : , {}".format(Server.lobbies[nbLobby]["clients"][nbClient]))
            Server.lobbies[nbLobby]["clients"][nbClient].close()
            Server.lobbies[nbLobby]["clients"].pop(nbClient)
            Server.lobbies[nbLobby]["players"].pop(nbClient)

    def receive(self):
        for nbLobby in range(len(Server.lobbies)): 
            for nbClient in range(len(Server.lobbies[nbLobby]["clients"])):
                t1_2_1 = threading.Thread(target=self.f,args=(nbClient,nbLobby))
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

    def send(self,msg, client, lobby):
        now = str(datetime.now())[:-7]
        for nbLobby in range(len(Server.lobbies)): 
            for nbClient in range(len(Server.lobbies[nbLobby]["clients"])):
                try:
                    if nbLobby == lobby and nbClient != client:
                        Server.lobbies[nbLobby]["clients"][nbClient].sendall(bytes(msg, "utf-8"))
                        #print("envoi", "({}) : {}\n".format(now,msg))
                except :
                    print("ERREUR SEND !!!!!!!!")
                    print("client déconnecter : , {}".format(Server.lobbies[nbLobby]["clients"][nbClient]))
                    Server.lobbies[nbLobby]["clients"][nbClient].close()
                    Server.lobbies[nbLobby]["clients"].pop(nbClient)
                    Server.lobbies[nbLobby]["players"].pop(nbClient)
                    


s1 = Server()
s1.condition()


if __name__ == "__main__":

    t0 = threading.Thread(target=root.mainloop)
    t0.run()