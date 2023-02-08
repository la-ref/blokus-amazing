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
                # Boucle des pièce possible du joueur
                tempPlat = plateau.copy()  # Copie du tableau sans les références
                tempPlat.ajouterPiece(piece[0],piece[1],piece[2],piece[3],piece[4],piece[5]) # On test l'ajout de la pièce dans le plateau de jeu
                listValeur.append(minmax(config.Config.controller.game.getNextPlayer(joueurId), listJoueur, tempPlat, profondeur-1)) # On ajoute la valuation de la pièce

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
    print(joueurId)
    listPoss = nbPossible(listJoueur[joueurId])
    
    listValeur = []
    # for piece in listPoss:
    for piece in choices(listPoss,k=2):
        tempPlat = config.Config.controller.game.getBoard().copy()
        print(tempPlat)
        tempPlat.ajouterPiece(piece[0],piece[1],piece[2],piece[3],piece[4],piece[5])
        listValeur.append(minmax(config.Config.controller.game.getNextPlayer(joueurId), listJoueur, tempPlat, profondeur*len(config.Config.controller.game.getCurrentPlayers())-1))
        
    print("iooigoijeio", listPoss[np.argmax(listValeur)])
    return listPoss[np.argmax(listValeur)]
    