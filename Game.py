from __future__ import annotations
from typing import Callable
from Pieces import Pieces
from Player import Player
from Board import Board
from GridInterface import GridInterface
from config import config
class Game:

    """Classe de gestion des parties de jeu blokus
    """
    def __init__(self : Game, joueurs : list[Player]|None,plateau : Board|None,taille : int) -> None:
        """Constructeur créant une partie avec des joueurs et un plateau de taille n

        Args:
            self (Game): game
            joueurs (list[Player] | None): liste de joueurs ou rien
            plateau (Board | None): plateau de jeu ou rien
            taille (int): taille du plateau de jeu
        """
        self.__joueurs : list[Player] = joueurs or [Player(11,"matthieu"),Player(12,"aurelian"),Player(13,"gauthier")]#,Player(14,"inconnu")]
        self.__joueursAbandon : list[Player] = []
        self.__currentPlayerPos : int = 0
        self.__plateau : Board = plateau or Board(taille)
        self.joueur = self.getCurrentPlayer()
    
    def getPlayers(self : Game) -> list[Player]:
        """Méthode getter permettant d'avoir la liste contenant les joueurs dans le jeu

        Args:
            self (Game): game

        Returns:
            list[Player]: liste contenant les joueurs de la partie
        """
        return self.__joueurs
    
    def getCurrentPlayer(self : Game) -> Player:
        """Méthode getter permettant d'avoir la liste contenant les joueurs dans le jeu

        Args:
            self (Game): game

        Returns:
            list[Player]: liste contenant les joueurs de la partie
        """
        return self.__joueurs[self.__currentPlayerPos]
    
    def getBoard(self : Game) -> Board:
        """Méthode getter permettant d'obtenir le plateau du jeu

        Args:
            self (Game): game

        Returns:
            Board: plateau du jeu
        """
        return self.__plateau

    def getCurrentPlayerId(self : Game) -> int:
        return self.__currentPlayerPos

    def addSurrenderedPlayer(self : Game) -> None:
        self.__joueursAbandon.append(self.__joueurs[self.__currentPlayerPos])

    def isPlayerSurrendered(self : Game) -> bool:
        return self.__joueurs[self.__currentPlayerPos] in self.__joueursAbandon

    def __nextPlayer(self):
        self.__currentPlayerPos = (self.__currentPlayerPos+1)%4


    # def jeu(self : Game):
    #     joueurs = self.__joueurs
    #     plateau = self.__plateau
    #     for joueur in joueurs:
    #         if not self.isPlayerSurrendered(joueur):
    #             self.__currentPlayer = joueur
    #             self.__callBackController("PLAYERS",joueur.getColor())
    #             print("c'est a : ",joueur.getName())
    #             ajout = False
    #             pieceid = 1
    #             fini = False
    #             while not fini:
    #                 if self.isPlayerSurrendered(joueur): break
    #                 if not self.isPlayerSurrendered(joueur):
    #                     pieceid = input("Choisir pièce : ")
    #                     piece = joueur.getPiece(pieceid)
    #                     x = input("x = ")
    #                     y = input("y = ")
    #                     if self.isPlayerSurrendered(joueur):
    #                         fini = True
    #                     if piece:
    #                         if self.isPlayerSurrendered(joueur):
    #                             fini = True
    #                         if not self.isPlayerSurrendered(joueur):
    #                             ajout = (plateau.ajouterPiece(piece,int(x),int(y),joueur,1,1))
    #                         if ajout:
    #                             fini = True
    #                 else:
    #                     fini = True
    #             if not self.isPlayerSurrendered(joueur):
    #                 if ajout:
    #                     joueur.ajoutTour()
    #                     joueur.removePiece(str(pieceid))
    #                     self.__callBackController("BOARD")

    def jeu(self : Game):
        joueur = self.__joueurs[self.__currentPlayerPos]
        if not self.isPlayerSurrendered():
            print("c'est a : ",joueur.getName())
            ajout = False
            pieceid = 1
            fini = False
            while not fini:
                if self.isPlayerSurrendered(): break
                if not self.isPlayerSurrendered():
                    pieceid = input("Choisir pièce : ")
                    piece = joueur.getPiece(pieceid)
                    x = input("x = ")
                    y = input("y = ")
                    if self.isPlayerSurrendered():
                        fini = True
                    if piece:
                        if self.isPlayerSurrendered():
                            fini = True
                        if not self.isPlayerSurrendered():
                            ajout = (self.__plateau.ajouterPiece(piece,int(x),int(y),joueur,1,1))
                        if ajout:
                            fini = True
                else:
                    fini = True
            if not self.isPlayerSurrendered():
                if ajout:
                    joueur.ajoutTour()
                    joueur.removePiece(str(pieceid))
        self.__nextPlayer()
        
        
    def playTurn(self : Game, piece : Pieces , colonne : int, ligne : int, dc : int, dl : int):

        if not self.isPlayerSurrendered():
            print("c'est a : ",self.joueur.getName()) 
            
            d= self.__plateau.ajouterPiece(piece,int(colonne),int(ligne),self.joueur,int(dc),int(dl))
            if d:
                self.joueur.removePiece(str(piece.getIdentifiant()))
                
                print("passe !")
                # prep tour suivant
                self.__nextPlayer()
                self.joueur = self.getCurrentPlayer()
                config.Config.controller.updateBoard()
                # config.Config.controller.updatePlayers(self.joueur)
                return True
           
        else:
            # cas de joueur fantôme
            self.__nextPlayer()
            self.joueur = self.getCurrentPlayer()
            self.playTurn(piece,colonne,ligne,dc,dl)
        return False
            

    # def setPiece():