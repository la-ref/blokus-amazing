from datetime import datetime
import socket
import threading
import time

class Server:
    lobbies = []
    PORT = 5005

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostbyname(socket.gethostname()))
        self.s.bind(('localhost', Server.PORT)) # n'importe quelle adresse
        self.s.listen(40)
        
    def chooseANumber(self,lobbyId):
        for i in range(4):
            if i not in Server.lobbies[lobbyId]["clients"]:
                return i
            
    def getClientId(self,client,lobbyId):
        if client in Server.lobbies[lobbyId]["clients"].values():
            for k, v in Server.lobbies[lobbyId]["clients"].items():
                if v == client:
                    return k
        return None
    
    def getClientFromId(self,clientId,lobbyId):
        if clientId in Server.lobbies[lobbyId]["clients"]:
            return Server.lobbies[lobbyId]["clients"][clientId]
        return None
    
    def getClientUserName(self,client,lobbyId):
        clientId = self.getClientId(client,lobbyId)
        for k, v in Server.lobbies[lobbyId]["players"].items():
            if k == clientId:
                return v
        return None
    
    def changeAdmin(self,lobbyId):
        if len(Server.lobbies[lobbyId]["clients"]) > 0 and len(Server.lobbies[lobbyId]["players"]) > 0:
            Server.lobbies[lobbyId]["admin"] = Server.lobbies[lobbyId]["clients"][0]
        else:
            Server.lobbies[lobbyId]["admin"] = 0
            
                
    
    def removeClient(self,client,lobbyId, username = False):
        if client in Server.lobbies[lobbyId]["clients"].values():
            # Server.lobbies[lobbyId]["clients"][client].close()
            clientId = self.getClientId(client,lobbyId)
            del Server.lobbies[lobbyId]["clients"][clientId]
            if username:
                #self.sendToOther(str(Server.lobbies[lobbyId]["players"][clientId]) + " - déconnecter",client,lobbyId)
                del Server.lobbies[lobbyId]["players"][clientId]
                self.sendToOther("userNames."+str(Server.lobbies[lobbyId]["players"]), client, lobbyId)
            if clientId == Server.lobbies[lobbyId]["admin"]:
                self.changeAdmin(lobbyId)   


                
    def addLobby(self,connection):
        lob,cli,added = 0,0,False
        if len(Server.lobbies) > 0:
            for lobbyId in range(len(Server.lobbies)): 
                # if 1er joueur de la liste c'est lui l'admin
                if Server.lobbies[lobbyId]["game"] == None and len(Server.lobbies[lobbyId]["clients"]) < 4:
                    cli = self.chooseANumber(lobbyId)
                    lob = lobbyId
                    Server.lobbies[lobbyId]["clients"][cli] = connection
                    added = True
                if added:
                    break
                
        if not added:
            Server.lobbies.append( {
                "clients" : {},
                "players" : {},
                "admin" : 0,
                "game": None
            })
            lob = len(Server.lobbies)-1
            cli = self.chooseANumber(lob)
            Server.lobbies[lob]["clients"][cli] = connection
            
        return lob,cli
        
    def accept(self):
        c, addr = self.s.accept()
        lob = 0
        cli = 0
        lob,cli = self.addLobby(c)
            
        data = c.recv(8192)
        if len(data) == 0:
            if c in Server.lobbies[lob]["clients"].values():
                print("client déconnecter : , {}".format(Server.lobbies[lob]["clients"][cli]))
                self.removeClient(cli,lob)
        else:
            data = str(data.decode())
            Server.lobbies[lob]["players"][cli]=data
            #self.sendToOther(str(data) + " est entré dans le lobby", self.getClientFromId(cli,lob), lob)
            self.sendToClient(str(cli), self.getClientFromId(cli,lob), lob)
            self.sendToOther("userNames."+str(Server.lobbies[lob]["players"]), self.getClientFromId(cli,lob), lob)
            print("insert", "({}) : {} connected.\n".format(str(datetime.now())[:-7], str(data)[1:]))
        
    def f(self, client, nbLobby):
        data = None
        try:
            data = client.recv(8192)
            if len(data) == 0:
                self.removeClient(client,nbLobby,True)
                return
            data = str(data.decode())
        except:
            print("client déconnecter : , {}".format(str(self.getClientUserName(client,nbLobby))))
            self.removeClient(client,nbLobby,True)
            return
        if data :
            if data == "getid":
                self.sendToClient(str(self.getClientId(client,nbLobby)), client, nbLobby)
            if data == "getUserNames":
                self.sendToClient("userNames."+str(Server.lobbies[nbLobby]["players"]), client, nbLobby)
            #self.send(str(self.getClientUserName(client,nbLobby)) + " - " + data, client, nbLobby)

    def receive(self):
        for nbLobby in range(len(Server.lobbies)): 
            for k,v in Server.lobbies[nbLobby]["clients"].items():
                t1_2_1 = threading.Thread(target=self.f,args=(v,nbLobby))
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
            

    def sendToOther(self,msg, client, lobby):
        for k, v in Server.lobbies[lobby]["clients"].items():
            if v != client:
                try:
                    v.sendall(bytes(msg, "utf-8"))
                except :
                    self.removeClient(client,lobby,True)
    
    def sendToClient(self,msg, client, lobby):
        try:
            client.sendall(bytes(msg, "utf-8"))
        except :
            self.removeClient(client,lobby,True)                  


s1 = Server()
s1.condition()


# if __name__ == "__main__":

#     t0 = threading.Thread(target=root.mainloop)
#     t0.run()