from __future__ import annotations
import tkinter as tk
import Elements.Pieces.PiecesListGUI as PG
from tkinter import PhotoImage
from Elements.Board import Board
from PIL import ImageTk
from config import config

class GridInterfaceOnline(tk.Frame):
    """Classe qui est une frame étant le plateau de jeu de manière graphique ainsi que le joueur courant
    """
    def __init__(self: GridInterfaceOnline, parent : tk.Canvas,board : Board):
        """Constructeur par paramètre qui créer GridInterfaceOnline en fonction d'une fenêtre parent et du plateau de jeu

        Args:
            self (GridInterfaceOnline): _description_
            parent (tk.Canvas): fenêtre qui affiche la GridInterfaceOnline
            board (Board): plateau de jeu
        """
        super(GridInterfaceOnline,self).__init__(parent)
        self.parent = parent
        self.images : list = []
        self.imageplateau = self.parent.create_image(  #270x270
            0,
            0,
            image=config.Config.image[8],
            anchor=tk.NW
        )
        self.board = board
        self.imagepiece : dict = config.Config.imagepiece
        self.couleur : dict = {
            11:"#FFC700",
            12:"#32BF00",
            13:"#BC0000",
            14:"#0045CC"
        }
        self.bordure : list = [self.parent.create_rectangle(439, 241, 1000, 231,outline=self.couleur[11], fill=self.couleur[11]),
                        self.parent.create_rectangle(440, 792, 999, 782,outline=self.couleur[11], fill=self.couleur[11]),
                        self.parent.create_rectangle(439, 241, 449, 791,outline=self.couleur[11], fill=self.couleur[11]),
                        self.parent.create_rectangle(990, 242, 1000, 791,outline=self.couleur[11], fill=self.couleur[11])] # bordure affichant le joueur courant
        self.pieces : list = [] # pieces placer sur la grille


    def setBoard(self : GridInterfaceOnline,board) -> None:
        """Méthode setter permettant d'attribuer un board à l'affiche de GridInterfaceOnline

        Args:
            self (GridInterfaceOnline): GridInterfaceOnline
            board (Board): plateau de jeu à afficher
        """
        self.board = board

    def refreshBoard(self : GridInterfaceOnline,board) -> None:
        """Méthode permettant d'afficher l'ensemble des pièces présentes sur un plateau directement graphiquement sur la grille

        Args:
            self (GridInterfaceOnline): GridInterfaceOnline
            board (Board): plateau de jeu à afficher
        """
        self.board = board
        for i in range(len(self.board)):
            for y in range(len(self.board[0])):
                valeur : int|None = self.board[i][y] 
                if valeur:
                    piece = config.Config.image[valeur+47]
                    if ((i,y) not in self.pieces):
                        self.parent.tag_lower(self.parent.create_image(463+y*(piece.width()),255+i*(piece.height()),image=piece))
                        self.pieces.append((i,y))
    
    def refreshPlayer(self : GridInterfaceOnline,playerColor : int,affiche : bool) -> None:
        """Méthode permettant de mettre à jour le joueur courant et de l'afficher graphiquement au tour de la grille

        Args:
            self (GridInterfaceOnline): GridInterfaceOnline
            playerColor (int): couleur du joueur courant
            affiche (bool): vrai s'il faut l'afficher sinon faux, en cas de victoire pour ne plus l'afficher
        """
        for bord in self.bordure:
            if not affiche:
                self.parent.itemconfig(bord,fill=self.couleur[11+playerColor],outline=self.couleur[11+playerColor])
                self.parent.tag_raise(bord)
            else:
                self.parent.delete(bord)
    
    def move(self : GridInterfaceOnline, x : int, y : int) -> None:
        """Méthode pour placer le grille donc GridInterfaceOnline en fonction du père à une coordonnée précise

        Args:
            self (GridInterfaceOnline): GridInterfaceOnline
            x (int): coordonnée en x sur la fenêtre
            y (int): coordonnée en y sur la fenêtre
        """
        self.parent.move(self.imageplateau,x,y)