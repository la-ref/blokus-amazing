class Player:
        
    def __init__(self, nb : int):
        self.__name : str = "Joueur "+str(nb)
        self.__nb : int = nb
                 
    @classmethod
    def Player(self, nb: int, name : str):
        res = self(nb)
        res.__name = name
        return res


    @property
    def name(self): return self.__name
    
    def setName(self, n:str) -> None:
        self.__name = n