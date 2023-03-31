from __future__ import annotations
import json
import string
from Elements.Player import Player
import os

# Exemple de fonction pour gérer les Json

class fonctionJson:
    """Classe principale qui est l'application qui garantie la gestion de la logique et des vue et
    donc de la communication entre les différents élèments de l'application
    """
    def __init__(self: fonctionJson) -> None:
        self.val : int

    def JsonAjout(self, donne):
        path = os.getcwd()+"\\HighScore\\highscore.json"
        print("AJOUT")
        with open(path, "r") as mon_fichier:
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
            print(val_test)
            print(data)
            
        mon_fichier.close()
            
        with open(path,"w") as mon_fichier: 
            json.dump(data, mon_fichier)  
        mon_fichier.close()