class Player:
    nbJoueur = 1
    def __init__(self, id : int,nom):
        self.__name : str =  nom
        self.__id : int =  id
        self.__nbTour : int = 0 
        Player.nbJoueur +=1

    @property
    def name(self): return self.__name
    
    @name.setter
    def name(self, n:str) -> None:
        self.__name = n

    def getColor(self):
        return self.__id

    def getNbTour(self):
        return self.__nbTour