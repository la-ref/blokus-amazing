import numpy as np
from config import config
import queue
from AI.utils.nbPossible import nbPossible
from random import choices
import multiprocessing as mp
from functools import partial
import time
MinMaxCeof = 10

    
def valuation_jeu(game,tableau, joueurId : int):
    """permet de remplir un tableau test avec le poids de chaque case, et de calculer la valeur d'une partie

    Args:
        tableau (ndarray) : le tableau à évaluer
        joueur (int) : le numéro du joueur actuel

    Returns:
        int: la valeur du tableau
    """
    sumPoint = 0
    for j in game.getCurrentPlayers():
        if j.getID()==joueurId:
            sumPoint+= len(nbPossible(game, j))*MinMaxCeof
            sumPoint+= len(np.argwhere(tableau==j.getID()))
        else:
            sumPoint-= len(nbPossible(game, j))*MinMaxCeof
            sumPoint -= len(np.argwhere(tableau==j.getID()))
    
    return sumPoint

"""
fonction alphabeta(nœud, α, β) /* α est toujours inférieur à β */
   si nœud est une feuille alors
       retourner la valeur de nœud
   sinon 
            si nœud est de type Min alors
                       v = +∞
                       pour tout fils de nœud faire
                           v = min(v, alphabeta(fils, α, β))                
                           si α ≥ v alors  /* coupure alpha */
                             retourner v
                           β = min(β, v)           
             sinon
                       v = -∞
                       pour tout fils de nœud faire
                           v = max(v, alphabeta(fils, α, β))                
                           si v ≥ β alors /* coupure beta */
                               retourner v
                           α = max(α, v)
    retourner v"""

def alphaBeta(game, profondeur : int, joueurId : int, listJoueur: list, alpha: int, beta : int, plateau) -> int:
    if profondeur >= 0:
        listPoss = nbPossible(game, listJoueur[joueurId])
        # vérifie si le noeud est une feuille
        if len(listPoss)==0:
            return alphaBeta(game,profondeur-1,game.getNextPlayer(joueurId),listJoueur,alpha,beta,plateau)
        else:
            # Max
            if profondeur%len(game.getCurrentPlayers())==0:
                v = -10000
                for piece in choices(listPoss,k=2):
                    plat = np.copy(plateau)
                    plat = ajouterPTest(game,plat,piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
                    v = max(v,alphaBeta(game,profondeur-1,game.getNextPlayer(joueurId),listJoueur,alpha,beta,plat))
                    if v<= alpha:
                        return v
                    alpha = min(beta,v)
            # Min
            else:
                v = 10000
                for piece in choices(listPoss,k=2):
                    plat = np.copy(plateau)
                    plat = ajouterPTest(game,plat,piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
                    v = min(v,alphaBeta(game, profondeur-1,game.getNextPlayer(joueurId),listJoueur,alpha,beta,plat))
                    if v>= beta:
                        return v
                    alpha = max(alpha,v)
            return v  
    else:
        return valuation_jeu(game, plateau, game.getNextPlayer(joueurId))
                
def workAlphaBeta(game, profondeur : int, joueurId : int, listJoueur: list, alpha: int, beta : int, plateaux):
    listVal= []
    for i in range(len(plateaux)):
        listVal.append(alphaBeta(game,profondeur,joueurId,listJoueur,alpha,beta,plateaux[i]))
    return listVal
    
          
          
def joue(joueurId : int, profond : int = 1) -> list:
    NB_CPU = 8

    listJoueur=config.Config.controller.game.getCurrentPlayers()

    listPoss = nbPossible(config.Config.controller.game, listJoueur[joueurId])
    listPoss=choices(listPoss,k=NB_CPU)
    listTab = []
    
    # création des copies de tableaux et ajout des à tester
    for piece in listPoss:
        tempPlat = np.copy(config.Config.controller.game.getBoard().getBoard())
        tempPlat= ajouterPTest(config.Config.controller.game,tempPlat,piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
        listTab.append(tempPlat)
    
    
    
    if mp.cpu_count() < NB_CPU:
        raise ValueError("The number of CPU's specified exceed the amount available")
    game = config.Config.controller.game
    depth = profond*len(config.Config.controller.game.getCurrentPlayers())-1
    nextId = config.Config.controller.game.getNextPlayer(joueurId)
    
    
    
    
    div_list = np.array_split(listTab, NB_CPU)
    pool = mp.Pool(NB_CPU)
    res = pool.map(partial(workAlphaBeta, game , depth , nextId , listJoueur, -10000, 10000), div_list)
    pool.close()
    pool.join()
    
    print(res)
    
        
    # # print(listValeur)
    # return listPoss[np.argmax(listValeur)]
    print(res)
    return listPoss[np.argmax(res)]
    

          
          
          
                
    

def minmax(game,q : queue.Queue, config, joueurId : int, listJoueur: list, plateau, profondeur : int, first : bool = True):

    if profondeur >= 0:
        listValeur = []
        listPoss = nbPossible(config, listJoueur[joueurId])
        if listPoss:
            # for piece in listPoss:
            for piece in choices(listPoss,k=2): 
                # print("profondeur :", profondeur, piece)   
                # Boucle des pièce possible du joueur
                # tempPlat = plateau.copy()  # Copie du tableau sans les références
                # # tempPlat.ajouterPiece(piece[0],piece[1],piece[2],piece[3],piece[4],piece[5]) # On test l'ajout de la pièce dans le plateau de jeu
                plateau = ajouterPTest(game,plateau,piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
                listValeur.append(minmax(game,q, config, config.controller.game.getNextPlayer(joueurId), listJoueur, plateau, profondeur-1, False)) # On ajoute la valuation de la pièce
                
            # print("\nIUHIUUYGUYGUYUYUYUYGUYUYYGUYGYGUYGTT\n",listValeur,"\n\n")
            if profondeur%len(config.controller.game.getCurrentPlayers())==0:
                # cas joueur évalué 
                if first:
                    q.put(max(listValeur))
                else:
                    return max(listValeur)
            else: # Cas opposant
                if first:
                    q.put(min(listValeur))
                else:
                    return min(listValeur)
            
        else: # cas ou le joueur ne peut pas jouer
            return minmax(game,q,config, listJoueur[(joueurId+1)%len(listJoueur)].getID(), listJoueur, plateau, profondeur-1, False)

    else: # cas de sortie
        return valuation_jeu(game,plateau, config.controller.game.getNextPlayer(joueurId))
    
    
    
# def joue2(joueurId : int, profondeur : int = 1) -> list:

#     listJoueur=config.Config.controller.game.getCurrentPlayers()
#     # for playe in listJoueur:
#     #     print(playe.getName())
#     # print(joueurId)
#     listPoss = nbPossible(config.Config, listJoueur[joueurId])
#     listPoss=choices(listPoss,k=2)
#     # print("liste possibilite : ", listPoss)
#     listValeur = []
    
#     q : queue.Queue = queue.Queue()
#     if mp.cpu_count() < 4:
#         raise ValueError("The number of CPU's specified exceed the amount available")

#     df_list = np.array_split(listPoss, 4)
#     pool = mp.Pool(4)
#     res = pool.map(partial(minmax, q=q, config=config.Config, joueurId=config.Config.controller.game.getNextPlayer(joueurId), listJoueur=listJoueur, plateau=tempPlat.getBoard(), profondeur=profondeur*len(config.Config.controller.game.getCurrentPlayers())-1), df_list)
#     pool.close()
#     pool.join()
    
    
#     # for piece in listPoss:
#     for piece in listPoss:
#         # print("profondeur :", profondeur, piece)
#         tempPlat = config.Config.controller.game.getBoard().copy()
#         # print(tempPlat)
#         tempPlat.ajouterPiece(piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
        
        
#         t = mp.Process(target=minmax ,args=(q, config.Config, config.Config.controller.game.getNextPlayer(joueurId), listJoueur, tempPlat.getBoard(), profondeur*len(config.Config.controller.game.getCurrentPlayers())-1))
#         t.start()
#         listTread.append(t)

#     # print(listTread)
#     for th in listTread:
#         th.join()
#         listValeur.append(q.get())
        
        
        
    
    
#     # print("\neisugusuigdiugihsiugjdhilugiudoihgdiohjiodriuohji", q.empty(), "\n\n")
#     # while not q.empty():
#     #     listValeur.append(q.get())
        
    
#     print(listValeur)
#     return listPoss[np.argmax(listValeur)]




def ajouterPTest(game,board: np.ndarray,piece,column:int,row:int,player,declageX : int,declageY : int):
        """Méthode qui permet d'ajouter à une coordonnée choisie une pièce jouer par un joueur en effectuant les vérifications de placement

        voir : verifyApplication()
        Args:
            self (Board): plateau
            piece (Pieces): pièce à placer sur le plateau
            column (int): colonne du plateau correspond à x 
            row (int): ligne du plateau correspond à y
            player (Player): joueur qui souhaite placer une pièce sur le plateau
            declageX (int): déclage de la sélection de la pièce en x en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)
            declageY (int): déclage de la sélection de la pièce en y en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)

        Returns:
            bool: vrai si la pièce est ajouter sur le plateau,sinon faux
        """
        if (verifyApplication(game,board,piece,column,row,player,declageX,declageY)):
            x : int = column-declageX
            y : int = row-declageY
            delimitation : np.ndarray = piece.getDelimitation()
            for i in range(len(delimitation)):
                for v in range(len(delimitation[0])):
                    if ((y+i >=0) and (y+i < game.getBoard().getBoardSize()) and (x+v >=0) and (x+v < game.getBoard().getBoardSize())):
                        if (delimitation[i][v] == 3):
                            board[y+i,x+v] = player.getColor()
        return board

def verifyApplication(game,board: np.ndarray,piece,column : int,row : int,player,declageX : int,declageY : int) -> bool:
    """Méthode retournant un boolean permettant de savoir si un joueur à une coordonnée choisie peut poser sa pièce
    conformément aux règles du blokus via la plateau et la matrice de délimiation d'une pièce

    voir : __findCorners() dans la classe Pieces

    Args:
        self (Board): plateau
        piece (Pieces): pièce à placer sur le plateau
        column (int): colonne du plateau correspond à x 
        row (int): ligne du plateau correspond à y
        player (Player): joueur qui souhaite placer une pièce sur le plateau
        declageX (int): déclage de la sélection de la pièce en x en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)
        declageY (int): déclage de la sélection de la pièce en y en fonction de la matrice de delimiation de la pièce (quel bout de la pièce à était choisie)

    Returns:
        bool: vrai si la pièce peut être posé,sinon faux
    """
    if not (checkBoardLimit(row, column)): 
        return False
    x : int = column-declageX
    y : int = row-declageY
    delimitation : np.ndarray = piece.getDelimitation()
    nbCorners : int = piece.getNbCorners()
    countCorners : int = 0
    cornerReduction : int = 0
    for i in range(len(delimitation)-1):
        for v in range(len(delimitation[0])):
           
            # vérfication du positionnement de la pièce en fonction de sa délimitation sur le plateau
            if ((y+i >=0) and (y+i < game.getBoard().getBoardSize()) and (x+v >=0) and (x+v < game.getBoard().getBoardSize())):
                if (delimitation[i][v] == 3 and board[y+i,x+v] > 0):
                    return False
                if (delimitation[i][v] == 1 and board[y+i,x+v] > 0 and board[y+i,x+v] == player.getColor()):
                    return False
                if (delimitation[i][v] == 2):
                    
                    if (board[y+i, x+v] != player.getColor()):
                        countCorners+= 1
            else:
                if (delimitation[i][v] == 3):
                    return False
                if (delimitation[i][v] == 2):
                    cornerReduction+=1 

    if verifyApplicationStart(game,y,x,player,delimitation): #self.__verifyApplicationStart(y+declageY,x+declageX,player): # Vérification si le joueur 
        return True
    if ((nbCorners-cornerReduction) == countCorners): # Vérification si la pièce est rattaché à un coin
        return False
    return True

def verifyApplicationStart(game,row : int,column : int,player,delim : np.ndarray) -> bool:
    """Méthode privé permettant de vérifier pour un joueur souhaitant placer une pièce sur la plateau
    si c'est son 1er tour et en conséquence de déterminer si il commence dans les coins du plateau ou non

    Args:
        self (Board): plateau
        row (int): colonne du plateau correspond à y
        column (int): ligne du plateau correspond à x
        player (Player): joueur qui souhaite placer une pièce sur le plateau

    Returns:
        bool: vrai si le joueur est dans les coins et que c'est son 1er tour,faux sinon
    """
    for i in range(len(delim)):
        for v in range(len(delim[0])):
            if ((row+i >=0) and (row+i < game.getBoard().getBoardSize()) and (column+v >=0) and (column+v < game.getBoard().getBoardSize())):
                if delim[i][v] == 3 and isInCorner(game,(row+i),(column+v)):
                    return player.getNbTour() == 0
    return False

def checkBoardLimit(row : int, column : int) -> bool:
    """Méthode privé retournant si les coordonnées mises en paramètre ce situe dans le plateau ou non

    Args:
        self (Board): plateau
        row (int): ligne du plateau correspond à y
        column (int): colonne du plateau correspond à x 

    Returns:
        bool: vrai si les coordonnées sont dans le plateau,sinon faux
    """
    return ((row < 20 and row >= 0) and (column < 20 and column >= 0))

def isInCorner(game,row : int, column : int) -> bool:
        """Méthode retournant un boolean pour savoir si pour une coordonnée choisie ce situe dans les coins du plateau

        Args:
            self (Board): plateau
            row (int): ligne du plateau correspond à y
            column (int): colonne du plateau correspond à x 

        Returns:
            bool: vrai si les coordonnées sont dans les coins du plateau sinon faux
        """
        if (checkBoardLimit(row, column)):
            return ((row == 20-1 and column == game.getBoard().getBoardSize()-1) 
                    or (row == 0 and column == 0)
                    or (row == game.getBoard().getBoardSize()-1 and column == 0)
                    or (row == 0 and column == game.getBoard().getBoardSize()-1))
        return False