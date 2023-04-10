from config import config
import numpy as np
import random as r
import time
from AI.utils.evaluation import joueDifficileOnline, getSorted
from AI.utils.nbPossible import nbPossible
from Elements.Pieces.Pieces import Pieces

class ai():
    
    def __init__(self,difficulty : str, player,lobby,pool,id,cbSurrender,cbPlacePiece) -> None:
        self.__difficulty : str = difficulty
        self.player = player
        self.lobby = lobby
        self.pool = pool
        self.id = id
        self.cbSurrender = cbSurrender
        self.cbPlacePiece = cbPlacePiece
    
    def setDifficulty(self, diff : str):
        self.__difficulty=diff
    
    def getDifficulty(self, diff : str):
        return self.__difficulty

    def getFirst(self,piece):
        for i in range(len(piece.getDelimitation())):
            for y in range(len(piece.getDelimitation()[i])):
                if piece.getDelimitation()[i][y] == 3:
                    return (i,y)
                
    def callPlacePiece(self):
        print("je callback piece")
        self.cbPlacePiece(None,self.lobby,None)

    def play(self,game):
        poss = nbPossible(game, self.player)
        if poss:
            if self.__difficulty.lower()=="facile":
                piece = r.choice(poss)
                time.sleep(0.5)
                if game.playTurn(piece[0],piece[1],piece[2],piece[4],piece[5],piece[6],piece[7]):
                    return piece[0].getIdentifiant()
                else:
                    print(piece[0].getForme(), piece[1],piece[2],piece[4],piece[5], game.getBoard().getBoard())
                    print("plaçable pas placé")
                    #exit(-6)
            elif self.__difficulty.lower()=="moyen":
                # Faire le choix du min max
                
                poss = getSorted(poss, 40)
                
                if type(poss[0])==Pieces:
                    piece=poss
                else:
                    piece = r.choice(poss)
                time.sleep(0.5)
                if game.playTurn(piece[0],piece[1],piece[2],piece[4],piece[5],piece[6],piece[7]):
                    return piece[0].getIdentifiant()
                else:
                    print(piece[0].getForme(),piece[1],piece[2],piece[4],piece[5], game.getBoard().getBoard())
                    print("plaçable pas placé")
                    #exit(-6)
            elif self.__difficulty.lower()=="expert":
                # Faire le choix du min max
                piece = joueDifficileOnline(self.player.getID(), poss,self.pool,game, 1)

                if piece!=None:
                    if game.playTurn(piece[0],piece[1],piece[2],piece[4],piece[5],piece[6],piece[7]):
                       return piece[0].getIdentifiant()
                    else:
                        print(piece[0].getForme(),piece[1],piece[2],piece[4],piece[5], game.getBoard().getBoard())
                        print("plaçable pas placé")
                        #exit(-6)
            else: 
                print("erreur : ia sans difficulté")
                #exit(-6)
                
        else:
            time.sleep(1)
            self.cbSurrender(self.lobby,game,self.id)