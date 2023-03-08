class OnlineGame:
    def __init__(self,id = None,userName = None,board = None,players = None,surrender = None) -> None:
        self.id = id
        self.userName = userName
        self.board = board
        self.players = players
        self.surrender = surrender
        self.winners = False
        self.surrendered = False
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
        else:
            self.myTurn = False
    
    def setIsSurrendered(self):
        if not self.surrendered:
            if self.id in self.surrender.keys():
                self.surrendered = True
            
    def refreshInfo(self,info):
        self.board = info["board"]
        self.players = info["players"]
        self.surrender = info["surrendered"]
        self.winners = info["winner"]
        self.setIsPlaying(int(info["playing"]))
        self.setIsSurrendered()
        
        