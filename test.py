

from Elements.Game import Game
import Elements.Player as Player
import json

joueurs = [Player.Player(0,"PERSONNE 1"),Player.Player(1,"PERSONNE 2"),Player.Player(2,"PERSONNE 3"),Player.Player(3,"PERSONNE 4")]
game = Game(joueurs,None,20)
print(joueurs[0].toJson())