from __future__ import annotations
import numpy as np
class Pieces:
    """Classe représentant une pièce du jeu blokus
    """

    def __init__(self: Pieces, forme : np.ndarray, identifiant: int, nbRot : int, nbFlip: int) -> None:
        """Constructeur créant une pièce identifié par un entier est étant sous forme d'un tableau 2d

        Args:
            self (Pieces): pieces
            forme (np.ndarray): forme de la pièce représenter sous un tableau 2d 
            ex : [[1,1],
                  [1,0]]
            les 1 représente un cube de la pièce, le 0 représente du vide
            identifiant (int): numéro qui identifie la pièce
        """
        self.__id : int = identifiant
        self.__forme : np.ndarray = forme
        self.__delimitation : np.ndarray = self.__findCorners() # matrice permettant de connaitre les coins de la pièces voir _findCorners()
        self.nbFlip = nbFlip # pour parcours ia
        self.nbRot = nbRot   # pour parcours ia
        self.__flipped = 0   # pour parcours ia
        self.__rotation : int = 0 # pour parcours ia
    
    def __findCorners(self : Pieces) -> np.ndarray:
        """Méthode privé qui permet de créer une matrice de délimitation d'une pièce, pour déterminer les coins et les bordures d'une pièce

        Args:
            self (Pieces): pieces

        Returns:
            np.ndarray: Matrice de délimitation de la pièce
              ex : [[2,1,1,2],
                    [1,3,3,1],
                    [1,3,1,2],
                    [2,1,2,0]]
            1 : bordure de la pièce
            2 : coin de la pièce
            3 : pièce
        """
        delim : np.ndarray = np.empty( (len(self.__forme)+2,len(self.__forme[0])+2), dtype=int)
        delim.fill(1)
        for i in range(len(self.__forme)):
            for y in range(len(self.__forme[0])):
                if self.__forme[i][y]:
                    delim[i+1][y+1] = 3
        # Recherche des coins "potentiels" (qui possède la pièce dans sa diagonale) de chaque élèment du tableau
        for i in range(len(delim)):
            for y in range(len(delim[0])):
                countCorners : int = 0
                for v in [-1,1]:
                    for k in [-1,1]:
                        if ((i+v >= 0 and i+v <= len(delim)-1) and (y+k >= 0 and y+k <= len(delim[0])-1)):
                            if delim[i+v][y+k] == 3 and delim[i][y] != 3:
                                countCorners+=1
                borderCounter : int = 0
                noneCounter : int = 0
                # verification des coins "potentiels" pour vérifier si ils sont pas voisins avec une partie de la pièce pour déterminer les coins
                for k in [-1,1]:
                    if (i+k >= 0 and i+k <= len(delim)-1):
                            if delim[i+k][y] == 3 and  countCorners > 0:
                                borderCounter+=1
                            elif countCorners == 0 and delim[i+k][y] == 3:
                                noneCounter+=1
                    if (y+k >= 0 and y+k <= len(delim[0])-1):
                            if delim[i][y+k] == 3 and  countCorners > 0:
                                borderCounter+=1
                            elif countCorners == 0 and delim[i][y+k] == 3:
                                noneCounter+=1
                if borderCounter == 0 and countCorners > 0:
                    delim[i][y] = 2
                elif noneCounter == 0 and countCorners == 0 and delim[i][y] != 3:
                    delim[i][y] = 0 
                         
        return delim

    def getDelimitation(self: Pieces) -> np.ndarray:
        """Méthode getter permettant d'avoir la délimitation d'une pièce

        Args:
            self (Pieces): pieces

        Returns:
            np.ndarray: Matrice de délimitation de la pièce
              ex : [[2,1,1,2],
                    [1,3,3,1],
                    [1,3,1,2],
                    [2,1,2,0]]
            1 : bordure de la pièce
            2 : coin de la pièce
            3 : pièce
        """
        return self.__delimitation

    def rotate90(self : Pieces) -> None:
        """Méthode permettant de tourner une pièce et la delimitation de 90 degrès sens horaire 

        Args:
            self (Pieces): pieces
        """
        self.__delimitation : np.ndarray = np.rot90(self.__delimitation,1,axes=(1,0))
        self.__forme : np.ndarray = np.rot90(self.__forme,1,axes=(1,0))
        self.__rotation=(self.__rotation+1)%4

    def flip(self : Pieces) -> None:
        """Méthode permettant de retourner horizontalement une piece et la delimitation

        Args:
            self (Pieces): pieces
        """
        self.__delimitation : np.ndarray = np.fliplr(self.__delimitation)
        self.__forme : np.ndarray = np.fliplr(self.__forme)
        self.__flipped=(self.__flipped+1)%2

    def getNbCorners(self : Pieces) -> int:
        """Méthode permettant de connaître le nombre de coin d'une pièce

        Args:
            self (Pieces): pieces

        Returns:
            int: nombre de coin de la pièce
        """
        return np.count_nonzero(self.__delimitation == 2)

    def getForme(self : Pieces) -> np.ndarray:
        """Méthode getter permettant de récupérer une pièce sous forme de tableau 2d

        Args:
            self (Pieces): pieces

        Returns:
            np.ndarray: forme de la pièce représenter sous un tableau 2d 
            ex : [[1,1],
                  [1,0]]
        """
        return self.__forme
    
    def getIdentifiant(self : Pieces) -> int:
        """Méthode getter permettant d'avoir l'identifiant d'une pièce

        Args:
            self (Pieces): pieces

        Returns:
            int: identifiant de la pièce
        """
        return self.__id

    def getRotation(self : Pieces) -> int:
        """Méthoge getter permettant d'obtenir le degrès de rotation de la pièce
        Args:
            self (Pieces): pieces
        Returns:
            int: degrè de rotation
        """
        return self.__rotation
    
    def getFlip(self : Pieces) -> int:
        """Méthode getter pour obtenir si la pièces est flip ou non
        Args:
            self (Pieces): pieces
        Returns:
            bool: True si elle est flip, False si elle ne l'est pas
        """
        return self.__flipped
