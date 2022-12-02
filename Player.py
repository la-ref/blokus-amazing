from PiecesDeclaration import LISTEPIECES
from Pieces import Pieces
class Player:
    nbJoueur = 1
    def __init__(self, idCouleur : int|None,nom: str|None):
        self.__name : str =  nom or ("Joueur"+str(Player.nbJoueur))
        self.__idCouleur : int = idCouleur or 1
        self.__nbTour : int = 0 
        self.__pieces : dict[str,Pieces] = LISTEPIECES.copy()
        Player.nbJoueur +=1

    @property
    def name(self): return self.__name
    
    @name.setter
    def name(self, n:str) -> None:
        self.__name = n

    def getColor(self):
        return self.__idCouleur

    def getNbTour(self):
        return self.__nbTour

    def getPieces(self):
        return self.__pieces

    def getPiece(self,id):
        return self.__pieces[id]

    def getNom(self):
        return self.__name

    def removePiece(self,id):
        del self.__pieces[id]

    def ajoutTour(self):
        self.__nbTour+=1