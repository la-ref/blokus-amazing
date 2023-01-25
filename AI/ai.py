import Elements.Player as Pl
from config import config

class ai():
    
    def __init__(self,difficulty : str, player: Pl.Player) -> None:
        self.difficulty = difficulty
        self.player = player
    
    def verifPlay(self):
        coins = config.Config.controller.game.setBoard().findCorners(self.player.getColor())
        
        for piece in self.player.getPieces():
            config.Config.controller.game.boar #todo (parcours piece pour vérif si posable)