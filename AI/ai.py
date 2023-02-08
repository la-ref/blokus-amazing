from config import config
import numpy as np
import random as r
import time
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
    
    def verifPlay(self):
        coins = config.Config.controller.game.getBoard().findCorners(self.player)
        listePossib = []

        for coin in coins:

            for piece in self.player.getPieces().values():

                for rot in range(4):
                    for flip in range(2):
                        for dec in np.argwhere(piece.getDelimitation()==3):
                            if config.Config.controller.game.getBoard().verifyApplication(piece,coin[1],coin[0],self.player,dec[1],dec[0]): 
                                listePossib.append([piece,coin[1],coin[0],self.player,dec[1],dec[0],rot,flip])
                        # elif config.Config.controller.game.getBoard().verifyApplication(piece,coin[1]-len(piece.getForme())+1,coin[0]-len(piece.getForme()[0])+1,self.player,dec[1],dec[0]): 
                        #    listePossib.append([piece,coin[1]-len(piece.getForme())+1,coin[0]-len(piece.getForme()[0])+1,self.player,dec[1],dec[0],rot,flip])
                        
                        piece.flip()
                    piece.rotate90()
        # print("listePossib :",len(listePossib))
        if len(listePossib)==0:
            print(self.player.getName()+" abandonne !")
            config.Config.controller.surrender()
        return listePossib
        # listePossib.append([piece,coin[0]-len(piece.getForme())+1,coin[1]-len(piece.getForme())+1,self.player,dec[0],dec[1],rot,flip])
        
    def play(self):
        poss = self.verifPlay()
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
                    print(config.Config.controller.game.getBoard().getBoard())
                    print("plaçable pas placé")
                    exit(-6)
            else: 
                print("erreur : ia sans difficulté")
                exit(-6)
                
        else:
            pass