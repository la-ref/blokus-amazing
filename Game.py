from Player import Player
from Board import Board
joueurs = [Player(5,"yes"),Player(6,"ok")]#,Player(5,"wow"),Player(8,"yes")]
b = Board(10)
while True:
    for joueur in joueurs:
        print("c'est a : ",joueur.getNom())
        ajout = False
        while not ajout:
            pieceid = input("Choisir piece : ")
            piece = joueur.getPiece(pieceid)
            x = input("x = ")
            y = input("y = ")
            ajout = (b.ajouterPiece(piece,int(x),int(y),joueur,1,1))
        if ajout:
            joueur.ajoutTour()
        print(b.getBoard())
