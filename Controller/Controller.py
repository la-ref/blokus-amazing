from __future__ import annotations
from Elements.Game import Game
from Controller.OnlineGame import OnlineGame
from tkinter import PhotoImage
import tkinter as tk
import Elements.Pieces.PiecesListGUI as PG
from PIL import ImageTk
from Vues.accueil import Accueil
from Elements.Player import Player
from config import config
from Elements.Pieces.Pieces import Pieces
from Vues.Lobby.lobbyLocal import lobbyLocal
from Vues.Lobby.lobbyOnline import lobbyOnline
from Vues.Game.GameInterface import GameInterface
from Vues.Game.GameInterfaceOnline import GameInterfaceOnline
from Vues.connexion import Connexion
from clientcopy import Client

import time
import icecream
import threading

class Controller(tk.Tk):
    """Classe principale qui est l'application qui garantie la gestion de la logique et des vue et
    donc de la communication entre les différents élèments de l'application
    """

    def __init__(self: Controller) -> None:
        tk.Tk.__init__(self)
        
        config.initialisation(self)

        self.frames = { "Acceuil" : Accueil(self), "lobbyLocal" : lobbyLocal(self), "GameInterface" : GameInterface(self), "GameInterfaceOnline" : GameInterfaceOnline(self),"connexion" : Connexion(self),"lobbyOnline" : lobbyOnline(self)}
        self.game : Game
        self.geometry(str(config.Config.largueur)+"x"+str(config.Config.hauteur))
        self.connection = None
        self.currentPage = ""
        self.onlineGame = None
        self.changePage('Acceuil')
        self.mainloop()
            
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
            self.changePage("Acceuil")
        if nomFrame != "lobbyOnline" or online:
            self.vueJeu = self.frames[nomFrame]
            self.vueJeu.initialize()
            self.vueJeu.tkraise()
        self.currentPage = nomFrame
            
    def changeUserName(self,name):
        self.onlineGame = OnlineGame(userName=name)      
            
    
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
            time.sleep(1)
            t1 = threading.Thread(target=self.connection.receive)
            t1.daemon = True
            t1.start()
            self.connection.send("getUserNames")
            #players = self.connection.getUserNames()
            #self.changeUserNames(players)
        else:
            self.changePage("connexion")
            self.frames["connexion"].showError("Aucun serveur disponible")
        # self.t1 = threading.Thread(target=self.connection.receive)
        # self.t1.daemon = True
        # self.t1.start()

        # self.t23 = threading.Thread(target=self.connection.inp)
        # self.t23.daemon = True
        # self.t23.start()
        pass
        
    def changeCurrentPlayer(self,nb):
        if self.currentPage == "lobbyOnline":
            self.frames["lobbyOnline"].changeCurrentPlayer(int(nb))
        
    def changeUserNames(self,players):
        if self.currentPage == "lobbyOnline":
            self.frames["lobbyOnline"].changeUserNames(players)
        
    def setAdmin(self,id):
        if self.currentPage == "lobbyOnline":
            if self.onlineGame.id == id:
                print("VAL = ",id)
                self.frames["lobbyOnline"].giveAdmin(id)
    
    def launchOnlineGame(self):
        self.connection.send("play")
        
    def launchGame(self,info):
        if self.onlineGame:
            self.onlineGame.refreshInfo(info)
            self.changePage("GameInterfaceOnline",True)
            self.refreshGame(info)
        else:
            pass
            ###################################
            #### ENVOI PAGE ERREUR ACCEUIL ####
            ###################################
        # joue = []
        # for k,player in joueurs.items():
        #     joue.append(Player(k,player))
        # self.onlineGame.setBoard(Game(joue,None,20)) ##############
        # self.changePage("GameInterface")
        # config.Config.controller.changePage("GameInterface")
            
    def refreshGame(self,info):
        print("je passe")
        self.frames["GameInterfaceOnline"].refreshBoard(self.onlineGame.board)
        self.frames["GameInterfaceOnline"].refreshPlayer(int(info["playing"]),True)
    
    
    def currentlyPlaying(self):
        return self.onlineGame.isPlaying()


    

    def updateBoard(self: Controller) -> None:
        """Méthode callback permettant de mettre à jour le plateau avec les pièces et le joueur courant à afficher

        Args:
            self (Controller): Controller
        """
        self.vueJeu.refreshBoard(self.game.getBoard())
        self.vueJeu.refreshPlayer(self.game.getCurrentPlayerId(),self.game.isGameFinished())

    def surrender(self : Controller) -> None:
        """Méthode callback qui pour chaque personne qui on abandonné de mettre à jour leur status sur le jeu
        et sur l'affichage de la page

        Args:
            self (Controller): Controller
        """
        if not self.game.isPlayerSurrendered():
            self.vueJeu.surrender(self.game.getCurrentPlayerId())
            self.game.addSurrenderedPlayer()
            if self.game.getWinners():
                # call fonction pour win
                self.vueJeu.partieTermine(self.game.getWinners())


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
        if id > 0 and id <= 3:
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
            print("vaffanculo")
            return
        else:
            self.onlineGame.refreshInfo(info)
            
    def changeIALevel(self,IaNb,lvl):
        if self.connection:
            info = "changeIA."+str(IaNb)+"-"+str(lvl)
            self.connection.send(info)
        
    

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
        print("yes super")
        if self.onlineGame and self.onlineGame.isPlaying():
            pId = piece.getIdentifiant()
            info = {
                "pieceId":pId,
                "colonne":colonne,
                "ligne":ligne,
                "dc":dc,
                "dl":dl
            }
            print("je vais send",self.connection)
            self.connection.send("placePiece."+str(info))
        else :
            if joueur == self.game.getCurrentPlayerId():
                play = self.game.playTurn(piece, colonne, ligne, dc, dl)
                win = self.game.getWinners()
                
                if (win):
                    self.vueJeu.partieTermine(win)
                return play
            else:
                return False

if __name__ == "__main__":
    global CT
    CT = Controller()