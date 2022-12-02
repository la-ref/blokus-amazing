from __future__ import annotations
import numpy as np
from Player import Player 
from Pieces import Pieces
class Board:

    def __init__(self : Board, size : int|None = None) -> None:
        self.__size : int = size or 20
        self.__board = np.empty( (self.__size,self.__size), dtype=Player)
        self.__board.fill(0)

    def __checkBoardLimit(self : Board, row : int, column : int) -> bool:
        return ((row < self.__size and row >= 0) and (column < self.__size and column >= 0))

    def getColorAt(self : Board, row : int, column : int) -> int|None:
        if (self.__checkBoardLimit(row, column)):
            return self.__board[row][column] 
    
    def isEmptyAt(self : Board, row : int, column : int) -> bool:
        if (self.__checkBoardLimit(row, column)):
            return self.__board[row][column] == 0
        return False

    def isInCorner(self : Board, row : int, column : int) -> bool:
        if (self.__checkBoardLimit(row, column)):
            return ((row == self.__size-1 and column == self.__size-1) 
                    or (row == 0 and column == 0)
                    or (row == self.__size-1 and column == 0)
                    or (row == 0 and column == self.__size-1))
        return False

    def __verifyApplicationStart(self: Board,x,y,player : Player) -> bool:
        return player.getNbTour() == 0 and self.isInCorner(y,x)

    def verifyApplication(self: Board,piece : Pieces,column:int,row:int,player : Player,declageX : int,declageY : int) -> bool:
        if not (self.__checkBoardLimit(row, column)): return False
        x : int = column-declageX
        y : int = row-declageY
        delimitation : np.ndarray = piece.getDelimitation()
        nbCorners : int = piece.getNbCorners()
        countCorners : int = 0
        cornerReduction : int = 0
        for i in range(len(delimitation)):
            for v in range(len(delimitation[0])):
                if ((y+i >=0) and (y+i < self.__size) and (x+v >=0) and (x+v < self.__size)):
                    if (delimitation[i][v] == 3 and self.__board[y+i][x+v] > 0):
                        return False
                    if (delimitation[i][v] == 1 and self.__board[y+i][x+v] > 0 and self.__board[y+i][x+v] == player.getColor()): 
                        return False
                    if (delimitation[i][v] == 2):
                        print(self.__board[y+i][x+v])
                        if (self.__board[y+i][x+v] != player.getColor()):
                            countCorners+= 1
                else:
                    if (delimitation[i][v] == 3):
                        return False
                    if (delimitation[i][v] == 2):
                        cornerReduction+=1

        if delimitation[declageY][declageX] == 3 and self.__verifyApplicationStart(x+declageX,y+declageY,player):
            print("ahah")
            return True
        if ((nbCorners-cornerReduction) == countCorners):
            return False
        print((nbCorners,cornerReduction,countCorners))
        return True
    
    def ajouterPiece(self: Board,piece : Pieces,column:int,row:int,player : Player,declageX : int,declageY : int) -> bool:
        if (self.verifyApplication(piece,column,row,player,declageX,declageY)):
            x : int = column-declageX
            y : int = row-declageY
            delimitation : np.ndarray = piece.getDelimitation()
            for i in range(len(delimitation)):
                for v in range(len(delimitation)):
                    if ((y+i >=0) and (y+i < self.__size) and (x+v >=0) and (x+v < self.__size)):
                        if (delimitation[i][v] == 3):
                            self.__board[y+i][x+v] = player.getColor()
            return True
        return False
    
    def getBoard(self) -> np.ndarray:
        return self.__board