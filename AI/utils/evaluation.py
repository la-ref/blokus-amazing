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
        
        if not game.enCours():
            print("Aucune partie en cours !!!")
            raise KeyboardInterrupt()
        listVal.append(alphaBeta(game,profondeur,joueurId,listJoueur,alpha,beta,plateaux[i]))
    return listVal
    
          
          
def joueDifficile(joueurId : int, listPoss, profond : int = 1, pool = None) -> list | None:
    

    listJoueur=config.Config.controller.game.getPlayers()

    listPoss=getSorted(listPoss, 40)

    
    listTab = []
    
    
    
    # création des copies de tableaux et ajout des à tester
    for piece in listPoss:
        tempPlat = np.copy(config.Config.controller.game.getBoard().getBoard())
        tempPlat= ajouterPTest(config.Config.controller.game,tempPlat,piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
        listTab.append(tempPlat)
    
    
    
    
    game = config.Config.controller.game
    depth = profond*len(config.Config.controller.game.getCurrentPlayers())-1
    nextId = config.Config.controller.game.getNextPlayer(joueurId)
    
    
    if len(listTab)>config.Config.NB_CPU:
        div_list = np.array_split(listTab, config.Config.NB_CPU)
        
    else:
        div_list = np.array_split(listTab, len(listTab))
        # pool = mp.Pool(len(listTab))
        
    # try:
    if pool:
        res = pool.map(partial(workAlphaBeta, game , depth , nextId , listJoueur, -10000, 10000), div_list)
    else:   
        res = config.Config.controller.pool.map(partial(workAlphaBeta, game , depth , nextId , listJoueur, -10000, 10000), div_list)

    return listPoss[np.argmax(res)]

def joueDifficileOnline(joueurId : int, listPoss, pool,game,profond : int = 1) -> list | None:
    

    listJoueur=game.getPlayers()

    listPoss=getSorted(listPoss, 40)

    
    listTab = []
    
    
    
    # création des copies de tableaux et ajout des à tester
    for piece in listPoss:
        tempPlat = np.copy(game.getBoard().getBoard())
        tempPlat= ajouterPTest(game,tempPlat,piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
        listTab.append(tempPlat)
    
    
    
    depth = profond*len(game.getCurrentPlayers())-1
    nextId = game.getNextPlayer(joueurId)
    
    
    if len(listTab)>6:
        div_list = np.array_split(listTab, 6)
        
    else:
        div_list = np.array_split(listTab, len(listTab))
        # pool = mp.Pool(len(listTab))
        
    # try:
    res = pool.map(partial(workAlphaBeta, game , depth , nextId , listJoueur, -10000, 10000), div_list)
    return listPoss[np.argmax(res)]

    

def getSorted(listPoss : list, limit : int):
    """ Renvoie un extrait des coups trié par difficulté de la liste des coups possibles
        Renvoie les plus difficiles

    Args:
        listPoss (list): liste des coups possible
        limit (int): limites max de coup à prendre

    Returns:
        list : extrait de listPoss
    """
    
    
    ch = len(listPoss)//4
    if ch <=4:
        listPoss=sorted(listPoss, key= lambda x : x[0].getDifficulty())
    elif ch >= limit:
        listPoss=sorted(listPoss, key= lambda x : x[0].getDifficulty())[-limit:]
    else:
        listPoss=sorted(listPoss, key= lambda x : x[0].getDifficulty())[-ch:]
    
    return listPoss
          
          
    


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