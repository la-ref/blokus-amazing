import numpy as np
from config import config
from AI.utils.nbPossible import nbPossible
from random import choices
MinMaxCeof = 10

def valuation_jeu(tableau, joueurId : int):
    """permet de remplir un tableau test avec le poids de chaque case, et de calculer la valeur d'une partie

    Args:
        tableau (ndarray) : le tableau à évaluer
        joueur (int) : le numéro du joueur actuel

    Returns:
        int: la valeur du tableau
    """
    sumPoint = 0
    for j in config.Config.controller.game.getCurrentPlayers():
        if j.getID()==joueurId:
            sumPoint+= len(nbPossible(j))*MinMaxCeof
            sumPoint+= len(np.argwhere(tableau==j.getID()))
        else:
            sumPoint-= len(nbPossible(j))*MinMaxCeof
            sumPoint -= len(np.argwhere(tableau==j.getID()))
    
    return sumPoint


def minmax(joueurId : int, listJoueur: list, plateau, profondeur : int) -> int:

    if profondeur >= 0:
        listValeur = []
        listPoss = nbPossible(listJoueur[joueurId])
        if listPoss:
            # for piece in listPoss:
            for piece in choices(listPoss,k=2): 
                print("profondeur :", profondeur, piece)   
                # Boucle des pièce possible du joueur
                # tempPlat = plateau.copy()  # Copie du tableau sans les références
                # # tempPlat.ajouterPiece(piece[0],piece[1],piece[2],piece[3],piece[4],piece[5]) # On test l'ajout de la pièce dans le plateau de jeu
                plateau = ajouterPTest(plateau,piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
                listValeur.append(minmax(config.Config.controller.game.getNextPlayer(joueurId), listJoueur, plateau, profondeur-1)) # On ajoute la valuation de la pièce

            if profondeur%len(config.Config.controller.game.getCurrentPlayers())==0:
                # cas joueur évalué 
                return max(listValeur)
            else: # Cas opposant
                return min(listValeur)
            
        else: # cas ou le joueur ne peut pas jouer
            return minmax(listJoueur[(joueurId+1)%len(listJoueur)].getID(), listJoueur, plateau, profondeur-1)

    else: # cas de sortie
        return valuation_jeu(plateau,config.Config.controller.game.getNextPlayer(joueurId))
    
    
def joue(joueurId : int, profondeur : int = 1) -> list:

    listJoueur=config.Config.controller.game.getCurrentPlayers()
    for playe in listJoueur:
        print(playe.getName())
    print(joueurId)
    listPoss = nbPossible(listJoueur[joueurId])
    listPoss=choices(listPoss,k=2)
    print("liste possibilite : ", listPoss)
    listValeur = []
    # for piece in listPoss:
    for piece in listPoss:
        print("profondeur :", profondeur, piece)
        tempPlat = config.Config.controller.game.getBoard().copy()
        print(tempPlat)
        tempPlat.ajouterPiece(piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
        listValeur.append(minmax(config.Config.controller.game.getNextPlayer(joueurId), listJoueur, tempPlat.getBoard(), profondeur*len(config.Config.controller.game.getCurrentPlayers())-1))

    return listPoss[np.argmax(listValeur)]




def ajouterPTest(board: np.ndarray,piece,column:int,row:int,player,declageX : int,declageY : int):
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
        if (verifyApplication(board,piece,column,row,player,declageX,declageY)):
            x : int = column-declageX
            y : int = row-declageY
            delimitation : np.ndarray = piece.getDelimitation()
            for i in range(len(delimitation)):
                for v in range(len(delimitation[0])):
                    if ((y+i >=0) and (y+i < config.Config.controller.game.getBoard().getBoardSize()) and (x+v >=0) and (x+v < config.Config.controller.game.getBoard().getBoardSize())):
                        if (delimitation[i][v] == 3):
                            board[y+i][x+v] = player.getColor()
        return board

def verifyApplication(board: np.ndarray,piece,column : int,row : int,player,declageX : int,declageY : int) -> bool:
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
    for i in range(len(delimitation)):
        for v in range(len(delimitation[0])):
            # vérfication du positionnement de la pièce en fonction de sa délimitation sur le plateau
            if ((y+i >=0) and (y+i < config.Config.controller.game.getBoard().getBoardSize()) and (x+v >=0) and (x+v < config.Config.controller.game.getBoard().getBoardSize())):
                if (delimitation[i][v] == 3 and board[y+i][x+v] > 0):
                    return False
                if (delimitation[i][v] == 1 and board[y+i][x+v] > 0 and board[y+i][x+v] == player.getColor()):
                    return False
                if (delimitation[i][v] == 2):
                    if (board[y+i][x+v] != player.getColor()):
                        countCorners+= 1
            else:
                if (delimitation[i][v] == 3):
                    return False
                if (delimitation[i][v] == 2):
                    cornerReduction+=1 

    if verifyApplicationStart(y,x,player,delimitation): #self.__verifyApplicationStart(y+declageY,x+declageX,player): # Vérification si le joueur 
        return True
    if ((nbCorners-cornerReduction) == countCorners): # Vérification si la pièce est rattaché à un coin
        return False
    return True

def verifyApplicationStart(row : int,column : int,player,delim : np.ndarray) -> bool:
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
            if ((row+i >=0) and (row+i < config.Config.controller.game.getBoard().getBoardSize()) and (column+v >=0) and (column+v < config.Config.controller.game.getBoard().getBoardSize())):
                if delim[i][v] == 3 and isInCorner((row+i),(column+v)):
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

def isInCorner(row : int, column : int) -> bool:
        """Méthode retournant un boolean pour savoir si pour une coordonnée choisie ce situe dans les coins du plateau

        Args:
            self (Board): plateau
            row (int): ligne du plateau correspond à y
            column (int): colonne du plateau correspond à x 

        Returns:
            bool: vrai si les coordonnées sont dans les coins du plateau sinon faux
        """
        if (checkBoardLimit(row, column)):
            return ((row == 20-1 and column == config.Config.controller.game.getBoard().getBoardSize()-1) 
                    or (row == 0 and column == 0)
                    or (row == config.Config.controller.game.getBoard().getBoardSize()-1 and column == 0)
                    or (row == 0 and column == config.Config.controller.game.getBoard().getBoardSize()-1))
        return False