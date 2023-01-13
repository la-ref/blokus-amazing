from __future__ import annotations
import numpy as np
from Player import Player 
from Pieces import Pieces
class Board:
    """Classe représentant le plateau de jeu du jeu blokus
    """

    def __init__(self : Board, size : int|None = None) -> None:
        """Constructeur créant un plateau (tableau 2d carré) de taille 20 ou de taille choisie comportant des entiers (couleur de joueur)

        Args:
            self (Board): plateau
            size (int | None, optional): Taille du plateau carré. Default à 20.
        """
        self.__size : int = size or 20
        self.__board = np.empty( (self.__size,self.__size), dtype=int)
        self.__board.fill(0)

    def __checkBoardLimit(self : Board, row : int, column : int) -> bool:
        """Méthode privé retournant si les coordonnées mises en paramètre ce situe dans le plateau ou non

        Args:
            self (Board): plateau
            row (int): ligne du plateau correspond à y
            column (int): colonne du plateau correspond à x 

        Returns:
            bool: vrai si les coordonnées sont dans le plateau,sinon faux
        """
        return ((row < self.__size and row >= 0) and (column < self.__size and column >= 0))

    def getColorAt(self : Board, row : int, column : int) -> int|None:
        """Méthode getter retournant la couleur d'une pièce / un joueur à une coordonnée du plateau choisie

        Args:
            self (Board): plateau
            row (int): ligne du plateau correspond à y
            column (int): colonne du plateau correspond à x 

        Returns:
            int|None: entier représentant une couleur du plateau ou 0 pour aucune couleur ou None si les coordonées ne sont pas correctes
        """
        if (self.__checkBoardLimit(row, column)):
            return self.__board[row][column] 
    
    def isEmptyAt(self : Board, row : int, column : int) -> bool:
        """Méthode retournant un boolean pour savoir si à une coordonnée choisie il y a un joueur/couleur 

        Args:
            self (Board): plateau
            row (int): ligne du plateau correspond à y
            column (int): colonne du plateau correspond à x 

        Returns:
            bool: vrai si c'est vide sinon faux
        """
        if (self.__checkBoardLimit(row, column)):
            return self.__board[row][column] == 0
        return False

    def isInCorner(self : Board, row : int, column : int) -> bool:
        """Méthode retournant un boolean pour savoir si pour une coordonnée choisie ce situe dans les coins du plateau

        Args:
            self (Board): plateau
            row (int): ligne du plateau correspond à y
            column (int): colonne du plateau correspond à x 

        Returns:
            bool: vrai si les coordonnées sont dans les coins du plateau sinon faux
        """
        if (self.__checkBoardLimit(row, column)):
            return ((row == self.__size-1 and column == self.__size-1) 
                    or (row == 0 and column == 0)
                    or (row == self.__size-1 and column == 0)
                    or (row == 0 and column == self.__size-1))
        return False

    def __verifyApplicationStart(self: Board,row : int,column : int,player : Player,delim : np.ndarray) -> bool:
        """Méthode privé permettant de vérifier pour un joueur souhaitant placer une pièce sur la plateau
        si c'est son 1er tour et en conséquence de déterminer si il commence dans les coins du plateau ou non

        Args:
            self (Board): plateau
            row (int): colonne du plateau correspond à y
            column (int): ligne du plateau correspond à x
            player (Player): joueur qui souhaite placer une pièce sur le plateau

        Returns:
            bool: vrai si le joueur est dans les coins et que c'est son 1er tour,faux sinon
        """
        for i in range(len(delim)):
            for v in range(len(delim[0])):
                if ((row+i >=0) and (row+i < self.__size) and (column+v >=0) and (column+v < self.__size)):
                    if delim[i][v] == 3 and self.isInCorner((row+i),(column+v)):
                        return player.getNbTour() == 0
        return False

    def verifyApplication(self: Board,piece : Pieces,column : int,row : int,player : Player,declageX : int,declageY : int) -> bool:
        """Méthode retournant un boolean permettant de savoir si un joueur à une coordonnée choisie peut poser sa pièce
        conformément aux règles du blokus via la plateau et la matrice de délimiation d'une pièce

        voir : __findCorners() dans la classe Pieces

        Args:
            self (Board): plateau
            piece (Pieces): pièce à placer sur le plateau
            column (int): colonne du plateau correspond à x 
            row (int): ligne du plateau correspond à y
            player (Player): joueur qui souhaite placer une pièce sur le plateau
            declageX (int): déclage de la sélection de la pièce en x en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)
            declageY (int): déclage de la sélection de la pièce en y en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)

        Returns:
            bool: vrai si la pièce peut être posé,sinon faux
        """
        if not (self.__checkBoardLimit(row, column)): return False
        x : int = column-declageX
        y : int = row-declageY
        delimitation : np.ndarray = piece.getDelimitation()
        nbCorners : int = piece.getNbCorners()
        countCorners : int = 0
        cornerReduction : int = 0
        for i in range(len(delimitation)):
            for v in range(len(delimitation[0])):
                # vérfication du positionnement de la pièce en fonction de sa délimitation sur le plateau
                if ((y+i >=0) and (y+i < self.__size) and (x+v >=0) and (x+v < self.__size)):
                    if (delimitation[i][v] == 3 and self.__board[y+i][x+v] > 0):
                        return False
                    if (delimitation[i][v] == 1 and self.__board[y+i][x+v] > 0 and self.__board[y+i][x+v] == player.getColor()):
                        return False
                    if (delimitation[i][v] == 2):
                        if (self.__board[y+i][x+v] != player.getColor()):
                            countCorners+= 1
                else:
                    if (delimitation[i][v] == 3):
                        return False
                    if (delimitation[i][v] == 2):
                        cornerReduction+=1

        if self.__verifyApplicationStart(y,x,player,delimitation): #self.__verifyApplicationStart(y+declageY,x+declageX,player): # Vérification si le joueur 
            return True
        if ((nbCorners-cornerReduction) == countCorners): # Vérification si la pièce est rattaché à un coin
            return False
        return True
    
    def ajouterPiece(self: Board,piece : Pieces,column:int,row:int,player : Player,declageX : int,declageY : int) -> bool:
        """Méthode qui permet d'ajouter à une coordonnée choisie une pièce jouer par un joueur en effectuant les vérifications de placement

        voir : verifyApplication()
        Args:
            self (Board): plateau
            piece (Pieces): pièce à placer sur le plateau
            column (int): colonne du plateau correspond à x 
            row (int): ligne du plateau correspond à y
            player (Player): joueur qui souhaite placer une pièce sur le plateau
            declageX (int): déclage de la sélection de la pièce en x en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)
            declageY (int): déclage de la sélection de la pièce en y en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)

        Returns:
            bool: vrai si la pièce est ajouter sur le plateau,sinon faux
        """
        #print(f"colonne : {column}, ligne : {row}, dc : {declageX}, dl : {declageY}") 
        if (self.verifyApplication(piece,column,row,player,declageX,declageY)):
            x : int = column-declageX
            y : int = row-declageY
            delimitation : np.ndarray = piece.getDelimitation()
            for i in range(len(delimitation)):
                for v in range(len(delimitation[0])):
                    if ((y+i >=0) and (y+i < self.__size) and (x+v >=0) and (x+v < self.__size)):
                        if (delimitation[i][v] == 3):
                            self.__board[y+i][x+v] = player.getColor()
            return True
        return False
    
    def getBoard(self : Board) -> np.ndarray:
        """Méthode getter qui retourne un plateau

        Args:
            self (Board): plateau

        Returns:
            np.ndarray: tableau 2d représentant le plateau
        """
        return self.__board

    def getBoardSize(self : Board) -> int:
        """Méthode getter permettant d'avoir la taille du plateau

        Args:
            self (Board): plateau

        Returns:
            int: taille du plateau
        """
        return self.__size

    def ajoutCouleur(self : Board,row : int,column : int,couleur : int) -> None:
        """Méthode permettant d'ajouter une couleur sur une coordonnées du plateau

        Args:
            self (Board): plateau
            row (int): ligne du plateau correspond à y
            column (int): colonne du plateau correspond à x 
            couleur (int): couleur d'un joueur
        """
        self.__board[row][column] = couleur