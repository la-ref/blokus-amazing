class OnlineGame:
    def __init__(self,id = None,userName = None,board = None,players = None,surrender = None) -> None:
        self.id = id
        self.userName = userName
        self.board = board
        self.players = players
        self.surrender = surrender
        self.myTurn = False
        
    def isPlaying(self):
        return self.board and len(self.players) != 0 and self.myTurn
        
    def setBoard(self,board):
        self.board = board
    
    def setPlayers(self,players):
        self.players = players
        
    def changeUserName(self,name):
        self.userName = name  
        
    def changeCurrentlyPlaying(self):
        pass
    
    def setIsPlaying(self,val):
        if val == self.id:
            self.myTurn = True
            
    def refreshInfo(self,info):
        self.board = info["board"]
        self.players = info["players"]
        self.surrender = info["surrendered"]
        self.setIsPlaying(int(info["playing"]))
        
        