from __future__ import annotations
import json
import string
from Elements.Player import Player

# Exemple de fonction pour gérer les Json

# class fonctionJson():
#     """Classe principale qui est l'application qui garantie la gestion de la logique et des vue et
#     donc de la communication entre les différents élèments de l'application
#     """

#     def __init__(self: fonctionJson) -> None:
#         self.__plateau = [[]]
#         self.__winners = [Player(11,"PERSONNE 1")]
#     def __repr__(self) -> str:
#         res = ""
#         if self.__genre == g.Genre.M : res += "M. "
#         elif self.__genre == g.Genre.F : res += "Mme "
#         else : res += "_ "
#         res += self.__prenom +" "+ self.__nom+",("
#         res += str(self.__naissance)
#         if self.__mort:
#             res += "/ "+str(self.__mort)+")"
#         else: res += ")"
#         res += ':"'+self.__bio+'".'
#         return res
    


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

