from config import config
import numpy as np
import random as r
import time
from AI.utils.evaluation import joueDifficile, getSorted
from AI.utils.nbPossible import nbPossible
from Elements.Pieces.Pieces import Pieces

class ai():
    
    def __init__(self,difficulty : str, player) -> None:
        self.__difficulty : str = difficulty
        self.player = player
    
    def setDifficulty(self, diff : str):
        self.__difficulty=diff
    
    def getDifficulty(self, diff : str):
        return self.__difficulty

    def getFirst(self,piece):
        for i in range(len(piece.getDelimitation())):
            for y in range(len(piece.getDelimitation()[i])):
                if piece.getDelimitation()[i][y] == 3:
                    return (i,y)

    def play(self):
        poss = nbPossible(config.Config.controller.game, self.player)
        if poss:
            if self.__difficulty=="Facile":
                piece = r.choice(poss)

                for i in range(piece[6]):
                    piece[0].rotate90()
                
                for i in range(piece[7]):
                    piece[0].flip()
                
                if config.Config.controller.placePiece(piece[0],piece[3].getID(),piece[1],piece[2],piece[4],piece[5]):
                    pass
                else:
                    print(piece[0].getForme(), piece[1],piece[2],piece[4],piece[5], config.Config.controller.game.getBoard().getBoard())
                    print("plaçable pas placé")
                    exit(-6)
            elif self.__difficulty=="Moyen":
                # Faire le choix du min max
                
                poss = getSorted(poss, 40)
                
                if type(poss[0])==Pieces:
                    piece=poss
                else:
                    piece = r.choice(poss)
                    
                for i in range(piece[6]):
                    piece[0].rotate90()
                
                for i in range(piece[7]):
                    piece[0].flip()
                
                if config.Config.controller.placePiece(piece[0],piece[3].getID(),piece[1],piece[2],piece[4],piece[5]):
                    pass
                else:
                    print(piece[0].getForme(),piece[1],piece[2],piece[4],piece[5], config.Config.controller.game.getBoard().getBoard())
                    print("plaçable pas placé")
                    exit(-6)
            elif self.__difficulty=="Expert":
                # Faire le choix du min max
                piece = joueDifficile(self.player.getID(), poss, 1)
                print(piece)

                for i in range(piece[6]):
                    piece[0].rotate90()
                
                for i in range(piece[7]):
                    piece[0].flip()
                
                if config.Config.controller.placePiece(piece[0],piece[3].getID(),piece[1],piece[2],piece[4],piece[5]):
                    pass
                else:
                    print(piece[0].getForme(),piece[1],piece[2],piece[4],piece[5], config.Config.controller.game.getBoard().getBoard())
                    print("plaçable pas placé")
                    exit(-6)
            else: 
                print("erreur : ia sans difficulté")
                exit(-6)
                
        else:
            print(self.player.getName()+" abandonne !")
            config.Config.controller.surrender()