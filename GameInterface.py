from tkinter import PhotoImage
import tkinter as tk
import PiecesListGUI as PG
import MouvementManager as Mv
from PIL import ImageTk
from GridInterface import GridInterface
from config import config
import accueil 


class GameInterface(tk.Frame):
    
    def __init__(self, window : tk.Misc):
        super(GameInterface,self).__init__(window)
        self.window = window
        
        
    def initialize(self):
        for widgets in self.winfo_children():
            widgets.destroy()
            
        self.border = tk.Canvas()
        self.border.create_image(0,0,image=config.Config.image[26],anchor=tk.NW)

        self.border.config(bg="white")
        self.border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
        self.board = GridInterface(self.border,config.Config.controller.getBoard())
        self.board.move(x=720-270,y=512-270)
        
        List1 = PG.PiecesListGUI(self.window,self.border,"Joueur 1",10)
        List1.move(x=70,y=80)
        
        List2 = PG.PiecesListGUI(self.window,self.border,"Joueur 2",11)
        List2.move(x=1047,y=80)
        
        List3 = PG.PiecesListGUI(self.window,self.border,"Joueur 3",12)
        List3.move(x=1047,y=524)
        
        List4 = PG.PiecesListGUI(self.window,self.border,"Joueur 4",13)
        List4.move(x=70,y=524)

        self.giveUp = self.border.create_image(
            (1440//2)-(config.Config.image[6].width()//2), 
            120, 
            image=config.Config.image[6],
            anchor=tk.NW
        )
        self.border.tag_bind(self.giveUp, "<Button-1>",lambda *_: self.callBackGiveUp())
        self.border.tag_bind(self.giveUp, "<Enter>",lambda *_: self.hoverSurrender("enter"))
        self.border.tag_bind(self.giveUp, "<Leave>",lambda *_: self.hoverSurrender("leave"))

        self.quitter = self.border.create_image(
            (1440//2)-(config.Config.image[7].width()//2), 
            820, 
            image=config.Config.image[7],
            anchor=tk.NW
        )
        self.border.tag_bind(self.quitter, "<Button-1>",lambda *_: self.leave())
        self.border.tag_bind(self.quitter, "<Enter>",lambda *_: self.hoverLeave("enter"))
        self.border.tag_bind(self.quitter, "<Leave>",lambda *_: self.hoverLeave("leave"))


    def callBackGiveUp(self):
        print(config.Config.controller)
        if config.Config.controller:
            from Controller import Controller
            config.Config.controller.surrender()

    def hoverSurrender(self,typ : str):
        self.border.delete(self.giveUp)
        if typ == "enter":
            self.giveUp = self.border.create_image(
                (1440//2)-(config.Config.image[27].width()//2), 
                120, 
                image=config.Config.image[27],
                anchor=tk.NW
            )
            self.border.config(cursor="hand2")
            self.border.tag_bind(self.giveUp, "<Leave>",lambda *_: self.hoverSurrender("leave"))
        elif typ == "leave":
            self.giveUp = self.border.create_image(
                (1440//2)-(config.Config.image[6].width()//2), 
                120, 
                image=config.Config.image[6],
                anchor=tk.NW
            )
            self.border.config(cursor="")
            self.border.tag_bind(self.giveUp, "<Enter>",lambda *_: self.hoverSurrender("enter"))
        self.border.tag_bind(self.giveUp, "<Button-1>",lambda *_: self.callBackGiveUp())

    def hoverLeave(self,typ : str):
        self.border.delete(self.quitter)
        if typ == "enter":
            self.quitter = self.border.create_image(
                (1440//2)-(config.Config.image[28].width()//2), 
                820, 
                image=config.Config.image[28],
                anchor=tk.NW
            )
            self.border.config(cursor="hand2")
            self.border.tag_bind(self.quitter, "<Leave>",lambda *_: self.hoverLeave("leave"))
        elif typ == "leave":
            self.quitter = self.border.create_image(
                (1440//2)-(config.Config.image[7].width()//2), 
                820, 
                image=config.Config.image[7],
                anchor=tk.NW
            )
            self.border.config(cursor="")
            self.border.tag_bind(self.quitter, "<Enter>",lambda *_: self.hoverLeave("enter"))
        self.border.tag_bind(self.quitter, "<Button-1>",lambda *_: self.leave())

    def leave(self):
        print("wohoho")
            # self.controller.surrender() for online
        # config.Config.controller.updateWindows()
        #self.destroy()
        config.Config.controller.changePage("Acceuil")

    def refreshBoard(self,plateau):
        self.board.refreshBoard(plateau)

    def refreshPlayer(self,couleur):
        self.board.refreshPlayer(couleur)

    


if __name__=="__main__":

    window = tk.Tk()
    window.geometry("1440x1024")
    
    accueil=GameInterface(window)
    accueil.pack()


    window.mainloop()