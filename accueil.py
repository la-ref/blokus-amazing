from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *

class Accueil(Frame):
    def __init__(self,window):
        super(Accueil, self).__init__()
        self.window = window
        self.window.title("Blockus")
        self.window.wm_iconphoto(True, config.Config.image[47])

    def initialize(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        
        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas = canvas

        canvas.place(x = 0, y = 0)
        background = canvas.create_image(
            720.0,
            512.0,
            image=config.Config.image[0]
        )

        HorsLigneBouton = canvas.create_image(
            510, 
            344, 
            image=config.Config.image[5],
            anchor=tkinter.NW
        )
        canvas.tag_bind(HorsLigneBouton, "<Button-1>", self.HorsLigneBouton)
        canvas.tag_bind(HorsLigneBouton, "<Enter>",lambda *_: self.hoverBouton("entre","horsligne",HorsLigneBouton))
        canvas.tag_bind(HorsLigneBouton, "<Leave>",lambda *_: self.hoverBouton("sort","horsligne",HorsLigneBouton))


        EnLigneBouton = canvas.create_image(
            510, 
            488, 
            image=config.Config.image[1],
            anchor=tkinter.NW
        )
        canvas.tag_bind(EnLigneBouton, "<Enter>",lambda *_: self.hoverBouton("entre","enligne",EnLigneBouton))
        canvas.tag_bind(EnLigneBouton, "<Leave>",lambda *_: self.hoverBouton("sort","enligne",EnLigneBouton))


        QuitterBouton = canvas.create_image(
            510, 
            642, 
            image=config.Config.image[2],
            anchor=tkinter.NW
        )
        canvas.tag_bind(QuitterBouton, "<Button-1>", self.QuitterBouton)
        canvas.tag_bind(QuitterBouton, "<Enter>",lambda *_: self.hoverBouton("entre","quitter",QuitterBouton))
        canvas.tag_bind(QuitterBouton, "<Leave>",lambda *_: self.hoverBouton("sort","quitter",QuitterBouton))

        

        BoutonScore = canvas.create_image(
            1032, 
            821, 
            image=config.Config.image[3],
            anchor=tkinter.NW
        )
        canvas.tag_bind(BoutonScore, "<Enter>",lambda *_: self.hoverBouton("entre","leader",BoutonScore))
        canvas.tag_bind(BoutonScore, "<Leave>",lambda *_: self.hoverBouton("sort","leader",BoutonScore))



        BoutonInfo = canvas.create_image(
            334, 
            821, 
            image=config.Config.image[4],
            anchor=tkinter.NW
        )
        canvas.tag_bind(BoutonInfo, "<Enter>",lambda *_: self.hoverBouton("entre","info",BoutonInfo))
        canvas.tag_bind(BoutonInfo, "<Leave>",lambda *_: self.hoverBouton("sort","info",BoutonInfo))

    def hoverBouton(self,typ : str,typ2 : str,idButton : int):
        if typ == "entre":
            if typ2 == "quitter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[31])
                self.canvas.config(cursor="hand2")
            elif typ2 == "horsligne":
                self.canvas.itemconfigure(idButton, image=config.Config.image[29])
                self.canvas.config(cursor="hand2")
            elif typ2 == "enligne":
                self.canvas.itemconfigure(idButton, image=config.Config.image[30])
                self.canvas.config(cursor="hand2")
            elif typ2 == "leader":
                self.canvas.itemconfigure(idButton, image=config.Config.image[33])
                self.canvas.config(cursor="hand2")
            elif typ2 == "info":
                self.canvas.itemconfigure(idButton, image=config.Config.image[34])
                self.canvas.config(cursor="hand2")
        elif typ == "sort":
            if typ2 == "quitter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[2])
                self.canvas.config(cursor="")
            elif typ2 == "horsligne":
                self.canvas.itemconfigure(idButton, image=config.Config.image[5])
                self.canvas.config(cursor="")
            elif typ2 == "enligne":
                self.canvas.itemconfigure(idButton, image=config.Config.image[1])
                self.canvas.config(cursor="")
            elif typ2 == "leader":
                self.canvas.itemconfigure(idButton, image=config.Config.image[3])
                self.canvas.config(cursor="")
            elif typ2 == "info":
                self.canvas.itemconfigure(idButton, image=config.Config.image[4])
                self.canvas.config(cursor="")

    def QuitterBouton(self,event):
        self.window.destroy()
    
    def BoutonInfo(self,event):
        self.window.destroy()
    
    def BoutonScore(self,event):
        self.window.destroy()
    
    def EnLigneBouton(self,event):
        self.window.destroy()
    
    def HorsLigneBouton(self,event):
        import lobbyLocal
        config.Config.controller.changePage("lobbyLocal")
        
        
        
        

if __name__ == "__main__":
    from config import config
    from Controller import Controller
    window = Tk(className='Accueil')

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    config.initialisation(None)
    image = config.Config.image

    MonAccueil = Accueil(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()