class Player:
        
    def __init__(self, nb : int):
        self.__name : str = "Joueur "+str(nb)
        self.__nb : int = nb
                 
    @classmethod
    def Player(cls, nb: int, name : str):
        res = cls(nb)
        res.__name = name
        return res


    @property
    def name(self): return self.__name
    
    @name.setter
    def name(self, n:str) -> None:
        self.__name = n