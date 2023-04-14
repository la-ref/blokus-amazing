from __future__ import annotations
import json
import string
from Elements.Player import Player
from Elements.Pieces.Pieces import Pieces
from Elements.Pieces.PiecesDeclaration import LISTEPIECES
import os.path as path

# Exemple de fonction pour gérer les Json

class fonctionJson:
    """Classe principale qui est l'application qui garantie la gestion de la logique et des vue et
    donc de la communication entre les différents élèments de l'application
    """
    def __init__(self: fonctionJson) -> None:
        self.val : int
        self.chemin = path.join("Highscore", "highscore.json")

    def JsonAjout(self, donne):
        """Fonction permettant de

        Args:
            donne (_type_): _description_
        """
        with open(self.chemin, mode = "r") as mon_fichier:
            data = json.load(mon_fichier)
            val_test = "Game1"
            num = 1
            existe = True
            while existe == True:
                if val_test not in data:
                    existe = False
                else:
                    num += 1
                    val_test = val_test[:4] + str(num)
            data[val_test] = donne
            
            
        with open(self.chemin, mode = "w") as mon_fichier:  
            json.dump(data, mon_fichier)  

    def getJSON(self):
        """Fonction permettant de

        Args:
            donne (_type_): _description_
        """
        with open(self.chemin, mode = "r") as mon_fichier:
            data = json.load(mon_fichier)
            return data
    
    def getPlayers(self, partie):
        """Fonction permettant de récupérer la liste des joueurs de la partie

        Args:
            Partie: Le nom de la partie (Game+numéro)
        """
        listjoueurs = []
        with open(self.chemin, mode = "r") as mon_fichier:
            data = json.load(mon_fichier)
            joueurs = data[partie][0]['joueurs']

        for i in range(len(joueurs)):
            listjoueurs.append(Player(i, data[partie][0]['joueurs'][i]))

        return listjoueurs

    def getNbGames(self):
        """Fonction permettant de récupérer le nombre de partie
        """
        with open(self.chemin, mode = "r") as mon_fichier:
            data = json.load(mon_fichier)
        return len(data)

    def getWinners(self, partie):
        """Fonction permettant de récupérer la liste des joueurs de la partie

        Args:
            Partie: Le nom de la partie (Game+numéro)
        """
        with open(self.chemin, mode = "r") as mon_fichier:
            data = json.load(mon_fichier)
            joueurs = data[partie][0]['winners']

        return joueurs

    def getPieces(self, partie):
        """Fonction permettant de récupérer la liste des joueurs de la partie

        Args:
            Partie: Le nom de la partie (Game+numéro)
        """
        pieces = []
        joueurs = []
        tableau = []
        with open(self.chemin, mode = "r") as mon_fichier:
            data = json.load(mon_fichier)
            for i in range (len(data[partie])):
                pieces.append(LISTEPIECES[f"{data[partie][i]['num_piece']}"])
                joueurs.append(Player(data[partie][i]['joueur'], data[partie][0]['joueurs'][data[partie][i]['joueur']]))
                tableau = data[partie][0]['tableau']
        return pieces, joueurs, tableau
