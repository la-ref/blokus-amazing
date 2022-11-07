import numpy as np
from __future__ import annotations
from Player import Player 
class Board:

    def __init__(self : Board, size : int) -> None:
        self.__size : int = size | 14
        self.__board = np.empty( (self.__size,self.__size), dtype=Player)
        self.__board.fill(np.nan)

    def __checkBoardLimit(self : Board, row : int, column : int) -> bool:
        return ((row < self.__size and row >= 0) and (column < self.__size and column >= 0))

    def getPlayerAt(self : Board, row : int, column : int) -> Player|None:
        if (self.__checkBoardLimit(row, column)):
            return self.__board[row][column] 
    
    def isEmptyAt(self : Board, row : int, column : int) -> bool:
        if (self.__checkBoardLimit(row, column)):
            return self.__board[row][column] == np.nan
        return False
    
    def addPlayerAt(self : Board, player : Player, row : int, column : int) -> None:
        if (self.__checkBoardLimit(row, column) and not self.isEmptyAt(row, column)):
            self.__board[row][column] = player

    def isInCorner(self : Board, row : int, column : int) -> bool:
        if (self.__checkBoardLimit(row, column)):
            return ((row == self.__size-1 and column == self.__size-1) 
                    or (row == 0 and column == 0)
                    or (row == self.__size-1 and column == 0)
                    or (row == 0 and column == self.__size-1))
        return False
            