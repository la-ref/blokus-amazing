from __future__ import annotations
import numpy as np
from Elements.Player import Player 
from Elements.Pieces.Pieces import Pieces
import os.path as path
import json

class Leaderboard :
    
    
    def __init__(self : Leaderboard):
        self.board = np.empty((20,20), dtype=int)
        self.board.fill(0)
        self.chemin = path.join("Highscore", "highscore.json")
        
        
    def recupJSON(self) -> dict :
        with open(self.chemin, mode = "r") as mon_fichier:
            data = json.load(mon_fichier)            
        return data
    
    def donneGameNumber(self, numpartie):
        val = self.recupJSON
        str = "Game" + numpartie
        fin = val.get(str)
        return fin
    
    def winner(self, numpartie):
        val = self.donneGameNumber(numpartie)
        tab = []
        tab = val.get("winners")
        return tab
        

    def getPlayers(self, index):
        val = self.recupJSON
        val.get("Game" + index)[0].get("Joueurs")
        return val
    
    def getPlayerPieceJouee(self, idplayer, num):
        val = self.donneGameNumber(num)
        tab = []
        for i in val:
            if i.get("joueur") == idplayer:
                tab.append(i.get("num_piece"))
        return tab
        
    def getPlayerPositionPieceJouee(self, idplayer, num):
        val = self.donneGameNumber(num)
        tab = []
        for i in val:
            if i.get("joueur") == idplayer:
                tab.append({"num_piece" : i.get("num_piece"), "position" : i.get("position_plateau"), "rotation" : i.get("rotation"), "flip" : i.get("flip")})
        return tab        
    
    def getBoard(self):
        return self.board