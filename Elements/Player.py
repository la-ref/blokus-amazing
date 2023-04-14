from __future__ import annotations
import copy
from Elements.Pieces.PiecesDeclaration import LISTEPIECES
from Elements.Pieces.Pieces import Pieces
import AI.ai as ia
class Player:
    """Classe représentant un joueur du jeu blokus
    """
    nbJoueur : int = 1
    def __init__(self : Player, idJoueur : int,nom: str|None):
        """Constructeur permettant de créer un joueur avec une couleur et un nom

        Args:
            self (Player): joueur
            idJoueur (int): id du joueur
            nom (str | None): nom du joueur
        """
        self.__name : str =  nom or ("Joueur"+str(Player.nbJoueur))
        self.__idCouleur : int = idJoueur+1
        self.__id : int = idJoueur
        self.__nbTour : int = 0 
        self.__pieces : dict[str,Pieces]
        self.__ai : None | ia.ai = None
        Player.nbJoueur +=1
    
    def setIA(self : Player, ai : ia.ai):
        self.__ai = ai
    
    def getAI(self : Player):
        return self.__ai

    def getName(self : Player) -> str:
        """Méthode getter permettant d'avoir le nom d'un joueur

        Args:
            self (Player): joueur
        
        Returns:
            _type_: nom du joueur
        """
        return self.__name
    
    def setName(self : Player, nom:str) -> None:
        """Méthode setter permettant de changer le nom d'un joueur

        Args:
            self (Player): joueur
            nom (str): nom à remplacer
        """
        self.__name = nom.upper()
        
    def getID(self : Player) -> int:
        return self.__id
    
    def getColor(self : Player) -> int:
        """Méthode getter permettant d'avoir la couleur d'un joueur

        Args:
            self (Player): joueur

        Returns:
            int: couleur du joueur
        """
        return self.__idCouleur

    def getNbTour(self : Player) -> int:
        """Méthode getter permettant d'avoir le nombre de tour où un joueur à jouer

        Args:
            self (Player): joueur

        Returns:
            int: nombre de tour réaliser par le joueur
        """
        return self.__nbTour

    def getPieces(self : Player) -> dict[str,Pieces]:
        """Méthode getter permettant d'avoir la liste des pièces d'un joueur

        Args:
            self (Player): joueur

        Returns:
            dict[str,Pieces]: dictionnaire de pièces du joueur
        """
        return self.__pieces

    def getPiece(self : Player,id : str) -> Pieces|None:
        """Méthode getter permettant d'avoir une pièce choisie dans la liste des pièces d'un joueur

        Args:
            self (Player): joueur
            id (str): id de la pièce à choisir

        Returns:
            Pieces|None: pièce choisie dans la liste du joueur ou none si elle n'existe pas
        """
        if id in self.__pieces.keys():
            return self.__pieces[id]
        
    def resetPiece(self : Player) -> None:
        """Méthode qui remet à zero la liste des pièce du joueur

        Args:
            self (Player): joueur
            id (str): id de la pièce à choisir
        """
        self.__pieces : dict[str,Pieces] = copy.deepcopy(LISTEPIECES.copy())

    def removePiece(self : Player,id : str) -> None:
        """Méthode permettant de retirer une pièce choisie dans la liste des pièces d'un joueur

        Args:
            self (Player): joueur
            id (str):  id de la pièce choisie
        """
        self.__pieces.pop(id, None)

    def ajoutTour(self : Player) -> None:
        """Méthode permettant d'ajouter un tour à un joueur

        Args:
            self (Player): joueur
        """
        self.__nbTour+=1