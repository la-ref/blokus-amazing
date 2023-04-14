from Elements.Pieces.Pieces import Pieces
import numpy as np

# Constante qui est un dictionnaire comportant l'ensemble des 21 pièces du jeu blokus 
LISTEPIECES : dict[str,Pieces] = {
    
    "1" : Pieces(np.array([[1]]),1,1,1,1),
    "2" : Pieces(np.array([[1],[1]]),2,2,1,1),
    "3" : Pieces(np.array([[1],[1],[1]]),3,2,1,2),
    "4" : Pieces(np.array([[1],[1],[1],[1]]),4,2,1,3),
    "5" : Pieces(np.array([[1],[1],[1],[1],[1]]),5,2,1,4),
    "6" : Pieces(np.array([[1,1],
                           [1,1]]),6,1,1,3),  
    "7" :Pieces(np.array([[1,1],
                          [1,0]]),7,4,2,2),
    "8" :Pieces(np.array([[1,1],
                          [1,0],
                          [1,0]]),8,4,2,3),
    "9" :Pieces(np.array([[1,1,1],
                          [1,0,0],
                          [1,0,0]]),9,4,1,5),
    "10" : Pieces(np.array([[1,0],
                            [1,1],
                            [1,1]]),10,4,1,5),
    "11" : Pieces(np.array([[1,0],
                            [1,1],
                            [1,0]]),11,4,1,6),
    "12" : Pieces(np.array([[1,1],
                            [0,1],
                            [1,1]]),12,4,1,6),
    "13" : Pieces(np.array([[1,1,1,1],
                            [0,1,0,0]]),13,4,2,6),
    "14" : Pieces(np.array([[1,1,0,0],
                            [0,1,1,1]]),14,4,2,6),
    "15" : Pieces(np.array([[1,1,1,1],
                            [1,0,0,0]]),15,4,2,5),
    "16" : Pieces(np.array([[0,1,0],
                            [1,1,1],
                            [0,1,0]]),16,1,1,8),
    "17" : Pieces(np.array([[0,1,1],
                            [0,1,0],
                            [1,1,0]]),17,4,2,6),
    "18" : Pieces(np.array([[0,1,0],
                            [0,1,0],
                            [1,1,1]]),18,4,1,6),
    "19" : Pieces(np.array([[1,0,0],
                            [1,1,0],
                            [0,1,1]]),19,4,2,7),
    "20" : Pieces(np.array([[1,1,0],
                            [0,1,1],
                            [0,1,0]]),20,4,2,7),
    "21" : Pieces(np.array([[1,0],
                            [1,1],
                            [0,1]]),21,2,2,6),
}
