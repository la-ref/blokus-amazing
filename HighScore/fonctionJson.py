from __future__ import annotations
import json
import string
from Elements.Player import Player
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
        print("AJOUT")
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
