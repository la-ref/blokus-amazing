import numpy as np

def nbPossible(game, joueur):
    coins = game.getBoard().findCorners(joueur)
    listePossib = []

    for coin in coins:

        for piece in joueur.getPieces().values():

            for rot in range(4):
                for flip in range(2):
                    for dec in np.argwhere(piece.getDelimitation()==3):
                        if game.getBoard().verifyApplication(piece,coin[1],coin[0],joueur,dec[1],dec[0]): 
                            listePossib.append([piece,coin[1],coin[0],joueur,dec[1],dec[0],rot,flip])
                    piece.flip()
                piece.rotate90()
    return listePossib