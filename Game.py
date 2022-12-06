from __future__ import annotations
from Player import Player
from Board import Board
class Game:
    """Classe de gestion des parties de jeu blokus
    """
    def __init__(self : Game,joueurs : list[Player]|None,plateau : Board|None,taille : int) -> None:
        """Constructeur créant une partie avec des joueurs et un plateau de taille n

        Args:
            self (Game): game
            joueurs (list[Player] | None): liste de joueurs ou rien
            plateau (Board | None): plateau de jeu ou rien
            taille (int): taille du plateau de jeu
        """
        self.__joueurs : list[Player] = joueurs or [Player(11,"matthieu"),Player(12,"aurelian"),Player(13,"gauthier"),Player(14,"inconnu")]
        self.__plateau : Board = plateau or Board(taille)
    
    def getPlayers(self : Game):
        """Méthode getter permettant d'avoir la liste contenant les joueurs dans le jeu

        Args:
            self (Game): game

        Returns:
            _type_: liste contenant les joueurs de la partie
        """
        return self.__joueurs
    
    def getBoard(self : Game):
        """Méthode getter permettant d'obtenir le plateau du jeu

        Args:
            self (Game): game

        Returns:
            _type_: plateau du jeu
        """
        return self.__plateau

    def jeu(self : Game):
        while True:
            for joueur in self.__joueurs:
                print("c'est a : ",joueur.getName())
                ajout = False
                pieceid = 1
                while not ajout:
                    pieceid = input("Choisir pièce : ")
                    piece = joueur.getPiece(pieceid)
                    x = input("x = ")
                    y = input("y = ")
                    if piece:
                        ajout = (self.__plateau.ajouterPiece(piece,int(x),int(y),joueur,1,1))
                if ajout:
                    joueur.ajoutTour()
                    print(str(pieceid))
                    joueur.removePiece(str(pieceid))
                print(self.__plateau.getBoard())
