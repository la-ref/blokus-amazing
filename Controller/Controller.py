from __future__ import annotations
from Elements.Game import Game
from Controller.OnlineGame import OnlineGame
import tkinter as tk
from Vues.accueil import Accueil
from Elements.Player import Player
from config import config
from Elements.Pieces.Pieces import Pieces
from Vues.Lobby.lobbyLocal import lobbyLocal
from Vues.Game.GameInterface import GameInterface
from HighScore.fonctionJson import fonctionJson
from Vues.Lobby.lobbyOnline import lobbyOnline
from Vues.Game.GameInterfaceOnline import GameInterfaceOnline
from Vues.connexion import Connexion
from client import Client
from Vues.LeaderboardInterface import LeaderboardInterface
import multiprocessing as mp

import threading

class Controller(tk.Tk):
    """Classe principale qui est l'application qui garantie la gestion de la logique et des vue et
    donc de la communication entre les différents élèments de l'application
    """

    def __init__(self: Controller, NB_CPU) -> None:
        tk.Tk.__init__(self)
        config.initialisation(self, NB_CPU)
        self.pool = mp.Pool(NB_CPU)
        self.onlineGame = None
        self.title("Blokus")
        self.wm_iconphoto(True, config.Config.image[47])
        self.frames = { "Accueil" : Accueil(self), "lobbyLocal" : lobbyLocal(self), "GameInterface" : GameInterface(self), "GameInterfaceOnline" : GameInterfaceOnline(self),"connexion" : Connexion(self),"lobbyOnline" : lobbyOnline(self), "LeaderboardInterface" : LeaderboardInterface(self)}
        self.game : Game
        self.geometry(str(config.Config.largueur)+"x"+str(config.Config.hauteur))
        self.connection = None
        self.currentPage = ""
        
        self.leaving = False
        self.json = []
        self.termine = True
        self.tour = 1
        self.etat = None
        self.protocol("WM_DELETE_WINDOW", self.on_closing_window)
        self.changePage('Accueil')
        self.mainloop()
        
        

    def on_closing_window(self):
        self.pool.terminate()
        self.pool.join()
        self.destroy()
        
        
            
    def changePage(self : Controller, nomFrame : str, online = False):
        """Méthode permettant de changer la page qui va être afficher sur l'application

        Args:
            self (Controller): Controller
            nomFrame (str): nom de la page
        """
        if self.connection == None and nomFrame == "lobbyOnline" and self.onlineGame:
            self.connectLobby(self.onlineGame.userName)
        elif self.connection and not online:
            self.connection.error = True
            self.connection.stopSock()
            self.connection = None
            self.onlineGame = None
            self.changePage("Accueil")
        if nomFrame != "lobbyOnline" or online:
            self.vueJeu = self.frames[nomFrame]
            self.vueJeu.initialize()
            self.vueJeu.tkraise()
        if nomFrame=='GameInterface':
            self.termine = False
        self.currentPage = nomFrame
            
    def changeUserName(self,name):
        self.onlineGame = OnlineGame(userName=name)   
    
    def setIPAndPort(self,ip,port):
        self.onlineGame.setIPAndPort(ip,port)   
            
    
    def changePlayer(self : Controller, players : list[Player]) -> None:
        """Méthode permettant de changer les joueurs de la partie

        Args:
            self (Controller): Controller
            players (list[Player]): liste des joueurs qui vont jouer
        """
        self.joueurs = players
        
    def connectLobby(self,name):
        self.connection = Client(name)
        if self.connection and self.connection.error == False:
            self.changePage("lobbyOnline",True)
            self.onlineGame.id = int(self.connection.getId())
            self.changeCurrentPlayer(self.onlineGame.id)
            self.frames["lobbyOnline"].changeUserName(self.onlineGame.id,self.onlineGame.userName)
            #time.sleep(1)
            t1 = threading.Thread(target=self.connection.receive)
            t1.daemon = True
            t1.start()
            self.connection.send("getUserNames")
        else:
            self.leaveOnline(send=False,error="Erreur fatale : Aucun serveur trouvé")
        pass
        
    def changeCurrentPlayer(self,nb):
        if self.currentPage == "lobbyOnline":
            self.frames["lobbyOnline"].changeCurrentPlayer(int(nb))
        
    def changeUserNames(self,players):
        if self.currentPage == "lobbyOnline":
            self.setAdmin(int(players["admin"]))
            players.pop("admin")
            self.frames["lobbyOnline"].changeUserNames(players)
        
    def setAdmin(self,id):
        if self.currentPage == "lobbyOnline":
            if self.onlineGame.id == id:
                self.frames["lobbyOnline"].giveAdmin(id)
    
    def launchOnlineGame(self):
        self.connection.send("play")
        
    def launchGame(self,info):
        if self.onlineGame:
            self.onlineGame.refreshInfo(info)
            self.changePage("GameInterfaceOnline",True)
            self.refreshGame(info)
        else:
            self.leaveOnline(send=False,error="Erreur fatale : Vous n'êtes pas en ligne")
            
            
    def refreshGame(self,info, pieceId = False):
        try:
            self.frames["GameInterfaceOnline"].refreshBoard(self.onlineGame.board)
            self.frames["GameInterfaceOnline"].refreshPlayer(int(info["playing"]),self.onlineGame.winners,self.onlineGame.players[int(info["playing"])])
            
            if pieceId:
                self.frames["GameInterfaceOnline"].deletePieceOnline(int(pieceId),int(info["played"]))
            if self.onlineGame.surrender:
                for k in self.onlineGame.surrender.keys():
                    self.frames["GameInterfaceOnline"].surrender(k)
            if self.onlineGame.winners:
                self.frames["GameInterfaceOnline"].partieTermine(self.onlineGame.winners)
        except:
            self.leaveOnline(send=False,error="Erreur fatale : Erreur lancement de partie")
            
    
    
    def currentlyPlaying(self):
        return self.onlineGame.isPlaying()


    

    def updateBoard(self: Controller) -> None:
        """Méthode callback permettant de mettre à jour le plateau avec les pièces et le joueur courant à afficher

        Args:
            self (Controller): Controller
        """
        self.vueJeu.refreshBoard(self.game.getBoard())
        self.vueJeu.refreshPlayer(self.game.getCurrentPlayerId(),self.game.isGameFinished())
        self.update()

    def surrender(self : Controller) -> None:
        """Méthode callback qui pour chaque personne qui on abandonné de mettre à jour leur status sur le jeu
        et sur l'affichage de la page

        Args:
            self (Controller): Controller
        """
        if (self.connection and self.currentPage == "GameInterfaceOnline" and self.onlineGame):
            if not self.onlineGame.surrendered:
                self.connection.send("surrender.")
            
        elif not self.game.isPlayerSurrendered():
            self.vueJeu.surrender(self.game.getCurrentPlayerId())
            self.game.addSurrenderedPlayer()
            self.endGame()


    def endGame(self):
        win = self.game.getWinners()
        tab = []
        if (not self.termine and win):
            self.termine=True
            for k in win:
                tab.append(k.getName())
            list_joueur = self.game.getPlayers()
            list_nomjoueurs = []
            for i in list_joueur :
                nom = i.getName()
                list_nomjoueurs.append(nom)
            self.json[0].update({"joueurs" : list_nomjoueurs})
            self.json[0].update({"winners" : tab})
            self.json[0].update({"tableau" : self.getBoard().getBoard().tolist()})
            fonctionJson().JsonAjout(self.json)                
            self.vueJeu.partieTermine(self.game.getWinners())
            self.json = []
            self.tour=1


    def getBoard(self : Controller):
        """Méthode getter qui permet d'obtenir le plateau de la parite

        Args:
            self (Controller): Controller

        Returns:
            _type_: plateau de jeu de la partie
        """
        return self.game.getBoard()
    
    def getOnlineBoard(self):
        return self.onlineGame.board
    
    def getOnlinePlayerName(self,id):
        if id >= 0 and id <= 3:
            return self.onlineGame.players[id]
        return None
    
    def getOnlineId(self):
        return self.onlineGame.id
        
    
    def getGame(self : Controller) -> Game:
        """Méthode getter qui permet d'obtenir la game en cours

        Args:
            self (Controller): Controller

        Returns:
            Game: game en cours
        """
        return self.game
    
    
    def placement(self,info):
        if info["playing"] == "Nope":
            return
        else:
            self.onlineGame.refreshInfo(info)
            self.refreshGame(info,info["piece"])
            
    def changeIALevel(self,IaNb,lvl):
        if self.connection:
            info = "changeIA."+str(IaNb)+"-"+str(lvl)
            self.connection.send(info)
        
    def leaveOnline(self,send=True, error :str|bool= False):
        if (self.connection and self.onlineGame) and not self.leaving:
            self.leaving = True
            legitLeave = False
            if send:
                self.connection.send("leave")
                legitLeave = True
            self.connection.error = True
            self.connection.stopSock()
            self.connection = None
            if self.onlineGame:
                winner = self.onlineGame.winners
            self.onlineGame = None
            self.changePage("Accueil")
            if error and not winner and not legitLeave:
                self.frames["Accueil"].errorPop(error)
            self.leaving = False
            
            

    def placePiece(self, piece : Pieces,joueur: int, colonne : int, ligne : int, dc : int, dl : int) -> bool:
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
        if self.onlineGame and self.onlineGame.isPlaying():
            pId = piece.getIdentifiant()
            info = {
                "pieceId": pId,
                "colonne": colonne,
                "ligne": ligne,
                "dc": dc,
                "dl": dl,
                "rotation": piece.getRotation(),
                "flip": piece.getFlip()
            }
            self.connection.send("placePiece."+str(info))
        elif self.onlineGame and not self.onlineGame.isPlaying():
            return False
        else :
            if joueur == self.game.getCurrentPlayerId():
                play = self.game.playTurn(piece, colonne, ligne, dc, dl)
                self.endGame()
                return play
            else:
                return False
    
    def changeState(self,info):
        """Méthode qui permet de changer l'état de la partie
        
        Args:
            - info : str -> état de la partie
        """
        if info == "Nope":
            self.etat = None
        else:
            self.etat = info
    
    def getState(self):
        """Méthode qui permet d'obtenir l'état de la partie
        """
        return self.etat
        
if __name__ == "__main__":
    global CT
    CT = Controller()