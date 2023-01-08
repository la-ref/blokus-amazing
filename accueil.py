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
        canvas.tag_bind(HorsLigneBouton, "<Enter>",lambda *_: self.hoverLeave("enter","horsligne"))
        canvas.tag_bind(HorsLigneBouton, "<Leave>",lambda *_: self.hoverLeave("leave","horsligne"))


        EnLigneBouton = canvas.create_image(
            470, 
            488, 
            image=config.Config.image[1],
            anchor=tkinter.NW
        )
        canvas.tag_bind(EnLigneBouton, "<Enter>",lambda *_: self.hoverLeave("enter","enligne"))
        canvas.tag_bind(EnLigneBouton, "<Leave>",lambda *_: self.hoverLeave("leave","enligne"))


        QuitterBouton = canvas.create_image(
            470, 
            652, 
            image=config.Config.image[2],
            anchor=tkinter.NW
        )
        canvas.tag_bind(QuitterBouton, "<Button-1>", self.QuitterBouton)
        canvas.tag_bind(QuitterBouton, "<Enter>",lambda *_: self.hoverLeave("enter","quitter"))
        canvas.tag_bind(QuitterBouton, "<Leave>",lambda *_: self.hoverLeave("leave","quitter"))

        

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
    # def hoverLeave(self,typ : str,typ2 : str):
    #     if typ2 == ""
    #     self.border.delete(self.quitter)
    #     if typ == "enter":
    #         self.quitter = self.border.create_image(
    #             (1440//2)-(config.Config.image[28].width()//2), 
    #             820, 
    #             image=config.Config.image[28],
    #             anchor=tk.NW
    #         )
    #         self.border.config(cursor="hand2")
    #         self.border.tag_bind(self.quitter, "<Leave>",lambda *_: self.hoverLeave("leave"))
    #     elif typ == "leave":
    #         self.quitter = self.border.create_image(
    #             (1440//2)-(config.Config.image[7].width()//2), 
    #             820, 
    #             image=config.Config.image[7],
    #             anchor=tk.NW
    #         )
    #         self.border.config(cursor="")
    #         self.border.tag_bind(self.quitter, "<Enter>",lambda *_: self.hoverLeave("enter"))
    #     self.border.tag_bind(self.quitter, "<Button-1>",lambda *_: self.leave())
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