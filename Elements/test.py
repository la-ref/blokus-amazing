# import numpy as np
# from Pieces import Pieces
# from Board import Board
# from Player import Player
# # def findCorners(test):
# #     liste = []
# #     for i in range(len(test)):
# #         for y in range(len(test[i])):
# #             counter = 0
# #             if test[i][y] != 0:
# #                 for k in [-1,1]:
# #                     if i+k <= len(test)-1 and i+k >= 0:
# #                         if test[i+k][y] == 1:
# #                             counter+=1
# #                     if y+k <= len(test[i])-1 and y+k >= 0:
# #                         if test[i][y+k] == 1:
# #                             counter+=1
# #                     if (y+k <= len(test[i])-1 and y+k >= 0) and (i+k <= len(test)-1 and i+k >= 0):
# #                         if test[i+k][y+k] == 1:
# #                             counter+=1
# #                     if (y+k <= len(test[i])-1 and y+k >= 0) and (i-k <= len(test)-1 and i-k >= 0):
# #                         if test[i-k][y+k] == 1:
# #                             counter+=1
# #                 print(i,y,counter)
# #                 if counter < 4:
# #                     liste.append([i,y])
# #     return liste

# # def findCorners2(test):
# #     liste = []
# #     for i in range(len(test)):
# #         for y in range(len(test[i])):
# #             if test[i][y] != 0:
# #                 counter1 = 0
# #                 counter2 = 0
# #                 for k in [-1,1]:
# #                     if (y+k > len(test[i])-1 or y+k < 0) and (i+k > len(test)-1 or i+k < 0):
# #                         for z in [-1,1]:
# #                             if i+z <= len(test)-1 and i+z >= 0:
# #                                 if test[i+z][y] == 1:
# #                                     counter1+=1
# #                             if y+z <= len(test[i])-1 and y+z >= 0:
# #                                 if test[i][y+z] == 1:
# #                                     counter1+=1
# #                     if (y+k > len(test[i])-1 or y+k < 0) and (i-k > len(test)-1 or i-k < 0):
# #                         print(i,y,"test")
# #                         for z in [-1,1]:
# #                             if i+z <= len(test)-1 and i+z >= 0:
# #                                 if test[i+z][y] == 1:
# #                                     counter2+=1
# #                             if y+z <= len(test[i])-1 and y+z >= 0:
# #                                 if test[i][y+z] == 1:
# #                                     counter2+=1

# #                 #if counter <:
# #                 #    liste.append([i,y])
# #     return liste

# # print(findCorners2(np.array([[0,1,1],
# #                             [1,1,1]])))

# def compteCoin(piece):
#     counter = 0
#     for v in piece:
#         for k in v:
#             if k == 2:
#                 counter+=1
#     return counter

# def appliquePiece(plateau,piece,x,y,couleur):
#     x = x-1
#     y = y-1
#     nbCorners = compteCoin(piece)
#     kk = np.copy(plateau)
#     countCorners = 0
#     cornerReduction = 0
#     for i in range(len(piece)):
#         for v in range(len(piece)):
#             if ((y+i >=0) and (y+i <= len(plateau)) and (x+v >=0) and (x+v <= len(plateau[0]))):
#                 if piece[i][v] == 3 and plateau[y+i][x+v] > 0:
#                     return False
#                 if piece[i][v] == 1 and plateau[y+i][x+v] == couleur: 
#                     return False
#                 if piece[i][v] == 2:
#                     #print("kk")
#                     if plateau[y+i][x+v] != couleur:
#                         countCorners+= 1
#             else:
#                 if piece[i][v] == 2:
#                     print("kk")
#                     cornerReduction+=1

#     print(countCorners,nbCorners)
#     #{print(nbCorners,countCorners,cornerReduction)
#     #return kk
#     # if ((countCorners-cornerReduction) == nbCorners):
#     #     return False
#     # return True
#     return (not ((nbCorners-cornerReduction) == countCorners))
# # kk = np.array([
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# # ])

# # piecee= np.array([
# #     [2,1,1,2],
# #     [1,3,3,1],
# #     [1,3,1,2],
# #     [2,1,2,0]
# # ])

# # print(appliquePiece(kk,piecee,0,0,5))


# # def findCorners(piece):
# #     delim = np.empty( (len(piece)+2,len(piece[0])+2), dtype=int)
# #     delim.fill(1)
# #     for i in range(len(piece)):
# #         for y in range(len(piece[0])):
# #             if piece[i][y]:
# #                 delim[i+1][y+1] = 3
# #     for i in range(len(delim)):
# #         for y in range(len(delim[0])):
# #             countCorners = 0
# #             for v in [-1,1]:
# #                 for k in [-1,1]:
# #                     if ((i+v >= 0 and i+v <= len(delim)-1) and (y+k >= 0 and y+k <= len(delim[0])-1)):
# #                         if delim[i+v][y+k] == 3:
# #                             countCorners+=1
# #             borderCounter = 0
# #             noneCounter = 0
# #             for k in [-1,1]:
# #                 if (i+k >= 0 and i+k <= len(delim)-1):
# #                         if delim[i+k][y] == 3 and  countCorners > 0:
# #                             borderCounter+=1
# #                         elif countCorners == 0 and delim[i+k][y] == 3:
# #                             noneCounter+=1
# #                 if (y+k >= 0 and y+k <= len(delim[0])-1):
# #                         if delim[i][y+k] == 3 and  countCorners > 0:
# #                             borderCounter+=1
# #                         elif countCorners == 0 and delim[i][y+k] == 3:
# #                             noneCounter+=1
# #             if borderCounter == 0 and countCorners > 0:
# #                 delim[i][y] = 2
# #             elif noneCounter == 0 and countCorners == 0:
# #                 delim[i][y] = 0      
# #     return delim
# # print(findCorners(np.array([
# #                             [0,1,0],
# #                             [1,1,1],
# #                             [0,1,0]])))


# b = Board(10)
# p = Pieces(np.array([[1]]),1)
# pl = Player(5,"yes")

# a = p.getDelimitation()
# print(pl.getPieces())

# # print(p.rotate90())
# # print(p.getDelimitation())
# # print(p.rotate90())
# # print(p.getDelimitation())
# # print(p.flip())
# # print(p.getDelimitation())

# # print(b.getBoard())

# print(b.verifyApplication(p,-5,1,pl,1,1))

# # kk = np.array([
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0],
# # ])

# # print(a)
# # print(appliquePiece(kk,a,0,0,5))
from Elements.Game import Game
game = Game(None,None,20)
game.jeu()