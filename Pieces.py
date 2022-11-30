from __future__ import annotations
import numpy as np
class Pieces:
    def __init__(self: Pieces, forme : np.ndarray, identifiant: int) -> None:
        self.__id : int = identifiant
        self.__forme : np.ndarray = forme
        self.__delimitation : np.ndarray = self.__findCorners()
    
    def __findCorners(self : Pieces):
        delim : np.ndarray = np.empty( (len(self.__forme)+2,len(self.__forme[0])+2), dtype=int)
        delim.fill(1)
        for i in range(len(self.__forme)):
            for y in range(len(self.__forme[0])):
                if self.__forme[i][y]:
                    delim[i+1][y+1] = 3
        for i in range(len(delim)):
            for y in range(len(delim[0])):
                countCorners : int = 0
                for v in [-1,1]:
                    for k in [-1,1]:
                        if ((i+v >= 0 and i+v <= len(delim)-1) and (y+k >= 0 and y+k <= len(delim[0])-1)):
                            if delim[i+v][y+k] == 3:
                                countCorners+=1
                borderCounter : int = 0
                noneCounter : int = 0
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
                elif noneCounter == 0 and countCorners == 0:
                    delim[i][y] = 0      
        return delim

    def getDelimitation(self: Pieces) -> np.ndarray:
        return self.__delimitation

    def rotate90(self : Pieces) -> None:
        self.__delimitation : np.ndarray = np.rot90(self.__delimitation,1,axes=(1,0))
        self.__forme : np.ndarray = np.rot90(self.__delimitation,1,axes=(1,0))

    def flip(self : Pieces) -> None:
        self.__delimitation : np.ndarray = np.fliplr(self.__delimitation)
        self.__forme : np.ndarray = np.fliplr(self.__delimitation)

    def getNbCorners(self : Pieces) -> int:
        return np.count_nonzero(self.__delimitation == 2)

    def getForme(self : Pieces) -> np.ndarray:
        return self.__forme
