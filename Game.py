from __future__ import annotations
from Player import Player
from Board import Board
from GridInterface import GridInterface
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

    def jeu(self : Game, window):
        from tkinter import PhotoImage
        import tkinter as tk
        import PiecesListGUI as PG
        import MouvementManager as Mv
        from PIL import ImageTk
    
        self.window = window
        images = []

        images.append(ImageTk.PhotoImage(file="build/assets/frame0/empty_list.png"))
        images.append(PhotoImage(file="build/assets/frame0/player_yellow.png"))
        images.append(PhotoImage(file="build/assets/frame0/player_green.png"))
        images.append(PhotoImage(file="build/assets/frame0/player_red.png"))
        images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
        images.append(PhotoImage(file="build/assets/frame0/AppBorder.png"))
        images.append(PhotoImage(file="build/assets/frame0/board.png"))#270x270
        
        border = tk.Canvas()
        border.config(bg="white")
        border.create_image(
                0,
                0,
                image=images[5],
                anchor=tk.NW
            )
        border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
        board = GridInterface(border,self.__plateau,images)
        board.move(x=720-270,y=512-270)
        
        List1 = PG.PiecesListGUI(self.window,border,images,"Joueur 1",1)
        List1.move(x=70,y=80)
        
        List2 = PG.PiecesListGUI(self.window,border,images,"Joueur 2",2)
        List2.move(x=1047,y=80)
        
        List3 = PG.PiecesListGUI(self.window,border,images,"Joueur 3",3)
        List3.move(x=1047,y=524)
        
        List4 = PG.PiecesListGUI(self.window,border,images,"Joueur 4",4)
        List4.move(x=70,y=524)

        

        def task():
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
                board.refreshBoard()
            self.window.update()

        while 1:
            task()  
