from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *

class Accueil(Frame):
    def __init__(self,window):
        super(Accueil, self).__init__()
        self.window = window

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

        canvas.place(x = 0, y = 0)
        background = canvas.create_image(
            720.0,
            512.0,
            image=config.Config.image[0]
        )

        HorsLigneBouton = canvas.create_image(
            470, 
            324, 
            image=config.Config.image[5],
            anchor=tkinter.NW
        )
        canvas.tag_bind(HorsLigneBouton, "<Button-1>", self.HorsLigneBouton)


        EnLigneBouton = canvas.create_image(
            470, 
            488, 
            image=config.Config.image[1],
            anchor=tkinter.NW
        )


        QuitterBouton = canvas.create_image(
            470, 
            652, 
            image=config.Config.image[2],
            anchor=tkinter.NW
        )
        canvas.tag_bind(QuitterBouton, "<Button-1>", self.QuitterBouton)

        

        BoutonScore = canvas.create_image(
            1032, 
            821, 
            image=config.Config.image[3],
            anchor=tkinter.NW
        )


        BoutonInfo = canvas.create_image(
            334, 
            821, 
            image=config.Config.image[4],
            anchor=tkinter.NW
        )

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