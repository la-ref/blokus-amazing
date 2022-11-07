class Joueur:
        
    def __init__(self, nb : int):
        self.__name = "Joueur "+str(nb)
        self.__ = nb
        
    @classmethod
    def Joueur(cls, nb: int, name : str):
        res = cls(nb)
        res.__name = name
        return res


    @property
    def name(self): return self.__name
    
    @name.setter
    def name(self, n:str) -> None:
        self.__name = n