from __future__ import annotations
import json
import string
from Elements.Player import Player

# Exemple de fonction pour gérer les Json

class fonctionJson:
    """Classe principale qui est l'application qui garantie la gestion de la logique et des vue et
    donc de la communication entre les différents élèments de l'application
    """
    def __init__(self: fonctionJson) -> None:
        self.__plateau = [[]]
        self.__winners = [Player(11,"PERSONNE 1")]

    def JsonAjout(self, donne):
        print("AJOUT")
        with open("C://Users//leand//OneDrive//Dokumente//GitHub//blokus-amazing//Highscore//highscore.json", "r") as mon_fichier:
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
            
        with open("C://Users//leand//OneDrive//Dokumente//GitHub//blokus-amazing//Highscore//highscore.json", "w") as mon_fichier:  
            json.dump(data, mon_fichier)  




         

#     def toJSON(self) -> str:
#         dictP = {
#             'plateau'  : [[]] ,
#             'winners' : self.__winners,
#         }
#         return json.dumps(dictP,ensure_ascii=False)

#     @staticmethod
#     def buildFromJSon(d: dict):
#         # genre
#         self.__plateau : str = d['plateau'] 
#         self.

#         return fonctionJson(prenom, nom, genre,dateNaissance,dateMort, bio)
