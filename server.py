from datetime import datetime
import socket,ast
import struct
import threading
from Elements.Game import Game
import Elements.Player as Player
import copy
import sys
import ipaddress

class Server:
    lobbies = []
    IP = str(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] else "127.0.0.1"
    PORT = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else 5005
    def __init__(self):
        try:
            ipaddress.ip_address(Server.IP)
        except:
            exit("Adresse IP invalide, le format doit être similaire à ex : 192.1.21.100")
        if Server.PORT > 28000 or Server.PORT <= 22: exit("Port invalide, le port doit être compri entre 23 et 28000")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
        print("Allumé sur l'IP : PORT -> ",socket.gethostbyname(socket.gethostname()),":",Server.PORT)
        self.s.bind(("localhost", Server.PORT)) # n'importe quelle adresse
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
        try:
            self.sendToAll("admin."+str(Server.lobbies[lobbyId]["admin"]), client, lobbyId)
        except:
            raise ValueError("Erreur message")
    
    def removeClient(self,client,lobbyId, username = False):
        if lobbyId >= 0 and lobbyId < len(Server.lobbies):
            if client in Server.lobbies[lobbyId]["clients"].values():
                #client.close()
                clientId = self.getClientId(client,lobbyId)
                game = Server.lobbies[lobbyId]["game"]
                if game:
                    game.addSurrenderedPlayerOnline(game.getPlayers()[clientId])
                    info = self.constructCall(lobbyId,True)
                    self.sendToOther("refreshgame."+str(info), client, lobbyId)
                    self.deleteLobby(lobbyId)
                if lobbyId >= 0 and lobbyId < len(Server.lobbies) and client in Server.lobbies[lobbyId]["clients"].values():
                    del Server.lobbies[lobbyId]["clients"][clientId]
                if not game and lobbyId >= 0 and lobbyId < len(Server.lobbies) and clientId == Server.lobbies[lobbyId]["admin"]:
                    self.changeAdmin(lobbyId)
                if username and lobbyId >= 0 and lobbyId < len(Server.lobbies):
                    #self.sendToOther(str(Server.lobbies[lobbyId]["players"][clientId]) + " - déconnecter",client,lobbyId)
                    del Server.lobbies[lobbyId]["players"][clientId]
                    if not game:
                        players = copy.deepcopy(Server.lobbies[lobbyId]["players"])
                        players["admin"] = Server.lobbies[lobbyId]["admin"]
                        #self.sendAdmin(lobbyId,client)
                        self.sendToOther("userNames."+str(players),client, lobbyId)
                        #t = threading.Timer(1.2,self.sendToOther,["userNames."+str(Server.lobbies[lobbyId]["players"]),client, lobbyId])
                        #t.start()
                
    def removeLobby(self,lobbyId):
        Server.lobbies.pop(lobbyId)
        

                
    def addLobby(self,connection):
        print(Server.lobbies)
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
                "iaLevels" : {0:"facile",1:"facile",2:"facile",3:"facile"},
                "admin" : 0,
                "game": None
            })
            lob = len(Server.lobbies)-1
            cli = self.chooseANumber(lob)
            Server.lobbies[lob]["clients"][cli] = connection
            
        return lob,cli
        
    def accept(self):
        try:
            c, addr = self.s.accept()
            print(c)
            lob = 0
            cli = 0
            
            lengthbuf = self.recvall(c, 4)
            length, = struct.unpack('!I', lengthbuf)
            data = self.recvall(c, length)
            depart = str(data.decode())
            print(depart)
            if "blokus." in depart:
                lob,cli = self.addLobby(c)
            else:
                raise ValueError("Connexion non autorisé")
            if len(data) == 0:
                if c in Server.lobbies[lob]["clients"].values():
                    #print("client déconnecter : , {}".format(Server.lobbies[lob]["clients"][cli]))
                    self.removeClient(cli,lob)
                    return
            else:
                data = str(data.decode())
                data = data.replace("blokus.", '')
                Server.lobbies[lob]["players"][cli]=data
                #self.sendToOther(str(data) + " est entré dans le lobby", self.getClientFromId(cli,lob), lob)
                self.sendToClient(str(cli), self.getClientFromId(cli,lob), lob)
                players = copy.deepcopy(Server.lobbies[lob]["players"])
                players["admin"] = Server.lobbies[lob]["admin"]
                self.sendToOther("userNames."+str(players), self.getClientFromId(cli,lob), lob)
                self.receiveV2(self.getClientFromId(cli,lob),lob)
                #t = threading.Timer(1.2,self.sendAdmin,[lob,self.getClientFromId(cli,lob)])
                #t.start()
                print("insert", "({}) : {} connected.\n".format(str(datetime.now())[:-7], str(data)[1:]))
                print(Server.lobbies[lob])
        except:
            self.removeClient(cli,lob)
            
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
            sendDict["winner"] = Server.lobbies[nbLobby]["game"].getWinnersName()
            sendDict["piece"] = False
            sendDict["played"] = False
                                        
        else:
            sendDict["playing"] = "Nope"
        return sendDict
    
    def createGame(self,nbLobby):
        from random import randint
        
        try:
            joueurs = []
            for i in range(len(Server.lobbies[nbLobby]["players"])):
                joueurs.append(Player.Player(i,Server.lobbies[nbLobby]["players"][i]))
            while len(joueurs) != 4:
                joueurs.append(Player.Player(len(joueurs),"IA-"+str(len(joueurs))))
            game = Game(joueurs,None,20,True)
            Server.lobbies[nbLobby]["game"] = game
            sendDict = self.constructCall(nbLobby,True)
            print(sendDict)
            return str(sendDict)
        except:
            raise ValueError("Erreur network création")
        
    def deleteLobby(self,nbLobby):
        if Server.lobbies[nbLobby]["game"] and Server.lobbies[nbLobby]["game"].getWinnersName():
            print('okKOKOKOKOKOKOKOKOKKOKOOKOKOKOOKOKOKO KOK OOK OK OKO KO KO KO KO O  OKO K OK O')
            for c in Server.lobbies[nbLobby]["clients"]:
                self.removeClient(c,nbLobby,True)
            self.removeLobby(nbLobby)
            
    def convertJson(self,msg):
        return ast.literal_eval(str(msg))
    
    def recvall(self,sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        print(buf)
        return buf
        
    def f(self, client, nbLobby):
        while True:
            data = None
            try:
                lengthbuf = self.recvall(client, 4)
                length, = struct.unpack('!I', lengthbuf)
                data = self.recvall(client, length)
                if len(data) == 0:
                    self.removeClient(client,nbLobby,True)
                    return
                data = str(data.decode())
            except:
                #print("client déconnecter : , {}".format(str(self.getClientUserName(client,nbLobby))))
                self.removeClient(client,nbLobby,True)
                return
            if data :
                try:
                    print(data)
                    if data == "getid":
                        self.sendToClient(str(self.getClientId(client,nbLobby)), client, nbLobby)
                    elif data == "getUserNames":
                        players = copy.deepcopy(Server.lobbies[nbLobby]["players"])
                        players["admin"] = Server.lobbies[nbLobby]["admin"]
                        self.sendToClient("userNames."+str(players), client, nbLobby)
                    elif data == "play":
                        if self.getClientId(client,nbLobby) == Server.lobbies[nbLobby]["admin"] and not Server.lobbies[nbLobby]["game"]:
                            game = self.createGame(nbLobby)
                            self.sendToAll("launchGame."+str(game), client, nbLobby)
                    elif data == "leave":
                        self.removeClient(client,nbLobby,True)              
                    elif "placePiece." in data:
                        data = data.replace("placePiece.", '')
                        self.placePiece(client,nbLobby,self.convertJson(data)) 
                    elif "surrender." in data:
                        game = Server.lobbies[nbLobby]["game"]
                        if game:
                            game.addSurrenderedPlayerOnline(game.getPlayers()[self.getClientId(client,nbLobby)])
                            info = self.constructCall(nbLobby,True)
                            self.sendToAll("refreshgame."+str(info), client, nbLobby)
                            self.deleteLobby(nbLobby)
                    elif "changeIA." in data:
                        if self.getClientId(client,nbLobby) == Server.lobbies[nbLobby]["admin"] and not Server.lobbies[nbLobby]["game"]:
                            data = data.replace("changeIA.", '')
                            info : list = data.split("-")
                            if info and len(info) > 1 and int(info[1]) >= 0 and int(info[1]) <= 3:
                                Server.lobbies[nbLobby]["iaLevels"][int(info[1])] = info[0]
                                print(Server.lobbies[nbLobby])
                    else:
                        self.sendToClient("errormsg.Cheating is not allowed", client, nbLobby)
                        self.removeClient(client,nbLobby,True)
                except ValueError as e:
                    self.sendToClient("errormsg."+str(e), client, nbLobby)
                    self.removeClient(client,nbLobby,True)
                    return
                    
                #self.send(str(self.getClientUserName(client,nbLobby)) + " - " + data, client, nbLobby)

    def receive(self):
        try:
            for nbLobby in range(len(Server.lobbies)): 
                if nbLobby >= 0 and nbLobby < len(Server.lobbies):
                    for k in Server.lobbies[nbLobby]["clients"]:
                        t1_2_1 = threading.Thread(target=self.f,args=(Server.lobbies[nbLobby]["clients"][k],nbLobby))
                        t1_2_1.start()
                
        except:
            pass
                
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
        try:
            if lobby >= 0 and lobby < len(Server.lobbies):
                for k, v in Server.lobbies[lobby]["clients"].items():
                    if v != client:
                        try:
                            v.sendall(struct.pack("!I",len(bytes(msg, "utf-8"))))
                            v.sendall(bytes(msg, "utf-8"))
                        except :
                            self.removeClient(client,lobby,True)
        except:
            self.removeClient(client,lobby,True)
    
    def sendToClient(self,msg, client, lobby):
        try:
            print("my len : ",len(bytes(msg, "utf-8")))
            client.sendall(struct.pack("!I",len(bytes(msg, "utf-8"))))
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
        try:
            if game:     
                if self.getClientId(client,nbLobby) == game.getCurrentPlayerId():
                    pieceId = placement["pieceId"]
                    colonne = placement["colonne"]
                    ligne = placement["ligne"]
                    dc = placement["dc"]
                    dl = placement["dl"]
                    rotation = placement["rotation"]
                    flip = placement["flip"]
                    piece = game.getCurrentPlayer().getPiece(str(pieceId))
                    play = game.playTurn(piece, colonne, ligne, dc, dl,rotation,flip)
                    #win = game.getWinners()
                    
                    # if (win):
                    #     self.vueJeu.partieTermine(win)
                    info = self.constructCall(nbLobby,play)
                    print(info,"ODOODSDJFKSDJFSDFHDS")
                    info["piece"] = pieceId
                    info["played"] = self.getClientId(client,nbLobby)
                    self.sendToAll("placement."+str(info), client, nbLobby)
                    print("j'ai send !!!")
                    return play
                else:
                    info = self.constructCall(nbLobby,False)
                    self.sendToClient("placement."+str(info), client, nbLobby)
                    return False
        except:
            raise ValueError("Erreur network placement")
        
s1 = Server()
s1.condition()


# if __name__ == "__main__":

#     t0 = threading.Thread(target=root.mainloop)
#     t0.run()