from __future__ import annotations
from Elements.Game import Game
from tkinter import PhotoImage
import tkinter as tk
import Elements.Pieces.PiecesListGUI as PG
from PIL import ImageTk
from Vues.accueil import Accueil
from Elements.Player import Player
from config import config
from Elements.Pieces.Pieces import Pieces
from Vues.Lobby.lobbyLocal import lobbyLocal
from Vues.Game.GameInterface import GameInterface
from HighScore.fonctionJson import fonctionJson

class Controller(tk.Tk):
    """Classe principale qui est l'application qui garantie la gestion de la logique et des vue et
    donc de la communication entre les différents élèments de l'application
    """

    def __init__(self: Controller) -> None:
        tk.Tk.__init__(self)
        
        config.initialisation(self)
        
        self.frames = { "Acceuil" : Accueil(self), "lobbyLocal" : lobbyLocal(self), "GameInterface" : GameInterface(self)}
        self.game : Game
        self.__json = []
        self.__tour = 1
        self.geometry(str(config.Config.largueur)+"x"+str(config.Config.hauteur))
        self.changePage('Acceuil')
        self.mainloop()

     
    def changePage(self : Controller, nomFrame : str):
        """Méthode permettant de changer la page qui va être afficher sur l'application

        Args:
            self (Controller): Contorller
            nomFrame (str): nom de la page
        """
        self.vueJeu = self.frames[nomFrame]
        self.vueJeu.initialize()
        self.vueJeu.tkraise()
    
    def changePlayer(self : Controller, players : list[Player]) -> None:
        """Méthode permettant de changer les joueurs de la partie

        Args:
            self (Controller): Contorller
            players (list[Player]): liste des joueurs qui vont jouer
        """
        self.joueurs = players

    def updateBoard(self: Controller) -> None:
        """Méthode callback permettant de mettre à jour le plateau avec les pièces et le joueur courant à afficher

        Args:
            self (Controller): Contorller
        """
        self.vueJeu.refreshBoard(self.game.getBoard())
        self.vueJeu.refreshPlayer(self.game.getCurrentPlayerId(),self.game.isGameFinished())

    def surrender(self : Controller) -> None:
        """Méthode callback qui pour chaque personne qui on abandonné de mettre à jour leur status sur le jeu
        et sur l'affichage de la page

        Args:
            self (Controller): Contorller
        """
        if not self.game.isPlayerSurrendered():
            self.vueJeu.surrender(self.game.getCurrentPlayerId())
            self.game.addSurrenderedPlayer()
            win = self.game.getWinners()
            tab = []
            if (win):
                for k in win:
                    tab.append(k.getName())
                self.__json[0].update({"winners" : tab})
                fonctionJson().JsonAjout(self.__json)                
                self.vueJeu.partieTermine(self.game.getWinners())


    def getBoard(self : Controller):
        """Méthode getter qui permet d'obtenir le plateau de la parite

        Args:
            self (Controller): Controller

        Returns:
            _type_: plateau de jeu de la partie
        """
        return self.game.getBoard()
    
    def getGame(self : Controller) -> Game:
        """Méthode getter qui permet d'obtenir la game en cours

        Args:
            self (Controller): Controller

        Returns:
            Game: game en cours
        """
        return self.game

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
        if joueur == self.game.getCurrentPlayerId():
            play = self.game.playTurn(piece, colonne, ligne, dc, dl)
            win = self.game.getWinners()
            tab = []
            rota = piece.getRotation()
            flip = piece.getFlip()
            self.__json.append({"num_tour" : self.__tour,
                "joueur" : joueur,
                "num_piece" : piece.getIdentifiant(),
                "position_plateau" : [int(colonne),int(ligne)],
                "rotation" : rota,
                "flip" : flip})
            self.__tour += 1 
            
            if (win):
                print("TEST")
                for k in win:
                    tab.append(k.getName())
                self.__json[0].update({"winners" : tab})
                fonctionJson().JsonAjout(self.__json)
                self.vueJeu.partieTermine(win)
            return play
        else:
            return False

if __name__ == "__main__":
    global CT
    CT = Controller()