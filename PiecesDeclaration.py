from Pieces import Pieces
import numpy as np

LISTEPIECES : dict[str,Pieces] = {
    "PIECE_1" : Pieces(np.array([[1]]),1),
    "PIECE_2" : Pieces(np.array([[1,1]]),2),
    "PIECE_3" : Pieces(np.array([[1,1,1]]),3),
    "PIECE_4" : Pieces(np.array([[1,1,1,1]]),4),
    "PIECE_5" : Pieces(np.array([[1,1,1,1,1]]),5),
    "PIECE_6" : Pieces(np.array([[1,1],
                                 [1,1]]),6),
    "PIECE_7" :Pieces(np.array([[1,1],
                                [1,0]]),7),
    "PIECE_8" :Pieces(np.array([[1,1,1],
                                [1,0,0]]),8),
    "PIECE_9" :Pieces(np.array([[1,1,1],
                                [1,0,0],
                                [1,0,0]]),9),
    "PIECE_10" : Pieces(np.array([[1,0],
                                  [1,1],
                                  [1,1]]),10),
    "PIECE_11" : Pieces(np.array([[1,0],
                                  [1,1],
                                  [1,0]]),11),
    "PIECE_12" : Pieces(np.array([[1,1],
                                  [0,1],
                                  [1,1]]),12),
    "PIECE_13" : Pieces(np.array([[1,1,1,1],
                                  [0,1,0,0]]),13),
    "PIECE_14" : Pieces(np.array([[0,1,1,1],
                                  [1,1,0,0]]),14),
    "PIECE_15" : Pieces(np.array([[1,1,1,1],
                                  [1,0,0,0]]),15),
    "PIECE_16" : Pieces(np.array([[0,1,0],
                                  [1,1,1],
                                  [0,1,0]]),16),
    "PIECE_17" : Pieces(np.array([[0,1,1],
                                  [0,1,0],
                                  [1,1,0]]),17),
    "PIECE_18" : Pieces(np.array([[0,1,0],
                                  [0,1,0],
                                  [1,1,1]]),18),
    "PIECE_19" : Pieces(np.array([[1,0,0],
                                  [1,1,0],
                                  [0,1,1]]),19),
    "PIECE_20" : Pieces(np.array([[1,1,0],
                                  [0,1,1],
                                  [0,1,0]]),20),
    "PIECE_21" : Pieces(np.array([[1,0],
                                  [1,1],
                                  [0,1]]),21),
}