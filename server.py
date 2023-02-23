from datetime import datetime
import socket,pickle,ast
import threading
import time
from Elements.Game import Game
import Elements.Player as Player
import numpy

class Server:
    lobbies = []
    PORT = 5005

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print(socket.gethostbyname(socket.gethostname()))
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
            Server.lobbies[lobbyId]["admin"] = list(Server.lobbies[lobbyId]["clients"].keys())[0]
        else:
            Server.lobbies[lobbyId]["admin"] = 0
            
    def sendAdmin(self,lobbyId,client):
        self.sendToAll("admin."+str(Server.lobbies[lobbyId]["admin"]), client, lobbyId)
    
    def removeClient(self,client,lobbyId, username = False):
        if client in Server.lobbies[lobbyId]["clients"].values():
            # Server.lobbies[lobbyId]["clients"][client].close()
            clientId = self.getClientId(client,lobbyId)
            del Server.lobbies[lobbyId]["clients"][clientId]
            if username:
                #self.sendToOther(str(Server.lobbies[lobbyId]["players"][clientId]) + " - déconnecter",client,lobbyId)
                del Server.lobbies[lobbyId]["players"][clientId]
                self.sendToOther("userNames."+str(Server.lobbies[lobbyId]["players"]), client, lobbyId)
                t = threading.Timer(0.5,self.sendAdmin,[lobbyId,client])
                t.start()
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
                #print("client déconnecter : , {}".format(Server.lobbies[lob]["clients"][cli]))
                self.removeClient(cli,lob)
                return
        else:
            data = str(data.decode())
            Server.lobbies[lob]["players"][cli]=data
            #self.sendToOther(str(data) + " est entré dans le lobby", self.getClientFromId(cli,lob), lob)
            self.sendToClient(str(cli), self.getClientFromId(cli,lob), lob)
            self.sendToOther("userNames."+str(Server.lobbies[lob]["players"]), self.getClientFromId(cli,lob), lob)
            self.receiveV2(self.getClientFromId(cli,lob),lob)
            t = threading.Timer(0.5,self.sendAdmin,[lob,self.getClientFromId(cli,lob)])
            t.start()
            print("insert", "({}) : {} connected.\n".format(str(datetime.now())[:-7], str(data)[1:]))
            print(Server.lobbies[lob]["players"])
            
    def constructCall(self,nbLobby,playing):
        sendDict = {}
        if playing:
            playerName = {}
            playerSurrender = {}
            for p in (Server.lobbies[nbLobby]["game"].getPlayers()):
                playerName[p.getID()] = p.getName()
            for p in (Server.lobbies[nbLobby]["game"].getSurrenderedPlayer()):
                playerSurrender[p.getID()] = p.getName()
            sendDict["players"] = playerName
            sendDict["surrendered"] = playerSurrender
            sendDict["board"] = Server.lobbies[nbLobby]["game"].getBoard().getBoard().tolist()
            sendDict["playing"] = Server.lobbies[nbLobby]["game"].getCurrentPlayer().getID()
        else:
            sendDict["playing"] = "Nope"
        return sendDict
    def createGame(self,nbLobby):
        from random import randint
        
        while True:
            try:
                joueurs = []
                for i in range(len(Server.lobbies[nbLobby]["players"])):
                    joueurs.append(Player.Player(i,Server.lobbies[nbLobby]["players"][i]))
                while len(joueurs) != 4:
                    joueurs.append(Player.Player(len(joueurs),"IA"+str(len(joueurs)+1)))
                game = Game(joueurs,None,20)
                Server.lobbies[nbLobby]["game"] = game
                sendDict = self.constructCall(nbLobby,True)
                print(sendDict)
                return str(sendDict)
            except:
                print("hudhshd")
            
    def convertJson(self,msg):
        return ast.literal_eval(str(msg))
        
    def f(self, client, nbLobby):
        while True:
            data = None
            try:
                data = client.recv(8192)
                if len(data) == 0:
                    self.removeClient(client,nbLobby,True)
                    return
                data = str(data.decode())
            except:
                #print("client déconnecter : , {}".format(str(self.getClientUserName(client,nbLobby))))
                self.removeClient(client,nbLobby,True)
                return
            if data :
                if data == "getid":
                    self.sendToClient(str(self.getClientId(client,nbLobby)), client, nbLobby)
                elif data == "getUserNames":
                    self.sendToClient("userNames."+str(Server.lobbies[nbLobby]["players"]), client, nbLobby)
                elif data == "play":
                    if self.getClientId(client,nbLobby) == Server.lobbies[nbLobby]["admin"] and not Server.lobbies[nbLobby]["game"]:
                        game = self.createGame(nbLobby)
                        self.sendToAll("launchGame."+str(game), client, nbLobby)
                elif "placePiece." in data:
                    data = data.replace("placePiece.", '')
                    self.placePiece(client,nbLobby,self.convertJson(data))
                    
                #self.send(str(self.getClientUserName(client,nbLobby)) + " - " + data, client, nbLobby)

    def receive(self):
        for nbLobby in range(len(Server.lobbies)): 
            for k in Server.lobbies[nbLobby]["clients"]:
                t1_2_1 = threading.Thread(target=self.f,args=(Server.lobbies[nbLobby]["clients"][k],nbLobby))
                t1_2_1.start()
                
    def receiveV2(self,cli,lob):
        t1_2_1 = threading.Thread(target=self.f,args=(cli,lob))
        t1_2_1.start()

    def condition(self):
        while True:
            t1_1 = threading.Thread(target=self.accept)
            t1_1.daemon = True
            t1_1.start()
            t1_1.join(1)
            
            # t1_2 = threading.Thread(target=self.receive)
            # t1_2.daemon = True
            # t1_2.start()
            # t1_2.join(1)
            

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
    
    def sendToAll(self,msg,client,lobby):
        self.sendToOther(msg,client,lobby)                  
        self.sendToClient(msg,client,lobby)      

    def placePiece(self,client,nbLobby,placement) -> bool:
        """Fonction de liaison entre le placement d'une piece graphique et moteur
        
        Args:
            - piece : Pieces -> pièce jouée
            - joueur : Player -> joueur de la pièce
            - colonne : int -> colonne du premier cube de la piece
            - ligne : int -> ligne du premier cube de la piece
            - dc : int -> décalage entre la colonne du premier cube de la piece et celle de l'origine de la piece.
            - dl : int -> décalage entre la ligne du premier cube de la piece et celle de l'origine de la piece.
        
        Returns: 
            - bool: vrai si la pièce est ajouter sur le plateau,sinon faux
        """
        game = Server.lobbies[nbLobby]["game"]
        if game:     
            if self.getClientId(client,nbLobby) == game.getCurrentPlayerId():
                pieceId = placement["pieceId"]
                colonne = placement["colonne"]
                ligne = placement["ligne"]
                dc = placement["dc"]
                dl = placement["dl"]
                piece = game.getCurrentPlayer().getPiece(str(pieceId))
                play = game.playTurn(piece, colonne, ligne, dc, dl)
                #win = game.getWinners()
                
                # if (win):
                #     self.vueJeu.partieTermine(win)
                info = self.constructCall(nbLobby,play)
                print(info,"ODOODSDJFKSDJFSDFHDS")
                self.sendToAll("placement."+str(info), client, nbLobby)
                print("j'ai send !!!")
                return play
            else:
                info = self.constructCall(nbLobby,False)
                self.sendToClient("placement."+str(info), client, nbLobby)
                return False
        
s1 = Server()
s1.condition()


# if __name__ == "__main__":

#     t0 = threading.Thread(target=root.mainloop)
#     t0.run()