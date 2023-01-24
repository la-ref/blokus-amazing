from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
from Vues.ScrollableFrame import ScrollableFrame

class Connexion(Frame):
    """ Classe étant une frame réprésentant la page d'acceuil
    """
    def __init__(self,window):
        super(Connexion, self).__init__()
        self.window = window
        self.window.title("Blokus")
        self.window.wm_iconphoto(True, config.Config.image[47])
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None

    def initialize(self):
        """ Fonction qui initialise la page de Connexion
        """
        for widgets in self.winfo_children():
            widgets.destroy()
        
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        background = self.canvas.create_image(
            720.0,
            512.0,
            image=config.Config.image[0]
        )
        
        
        entrerPseudo_image = self.canvas.create_image(
            510, 
            344, 
            image=config.Config.image[61],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(entrerPseudo_image, "<Button-1>", self.Entrerpseudo)
        self.canvas.tag_bind(entrerPseudo_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerpseudo",entrerPseudo_image))
        self.canvas.tag_bind(entrerPseudo_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerpseudo",entrerPseudo_image))

        entrerip_image = self.canvas.create_image(
            510, 
            344, 
            image=config.Config.image[60],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(entrerip_image, "<Button-1>", self.Entrerip)
        self.canvas.tag_bind(entrerip_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerip",entrerip_image))
        self.canvas.tag_bind(entrerip_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerip",entrerip_image))

        entrerPort_image = self.canvas.create_image(
            510, 
            344, 
            image=config.Config.image[62],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(entrerPort_image, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(entrerPort_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerport",entrerPort_image))
        self.canvas.tag_bind(entrerPort_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerport",entrerPort_image))

        ConnecterBouton = self.canvas.create_image(
            510, 
            642, 
            image=config.Config.image[63],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(ConnecterBouton, "<Button-1>", self.ConnecterBouton)
        self.canvas.tag_bind(ConnecterBouton, "<Enter>",lambda *_: self.hoverBouton("entre","connecter",ConnecterBouton))
        self.canvas.tag_bind(ConnecterBouton, "<Leave>",lambda *_: self.hoverBouton("sort","connecter",ConnecterBouton))

        
        QuitterBouton = self.canvas.create_image(
            510, 
            642, 
            image=config.Config.image[7],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(QuitterBouton, "<Button-1>", self.QuitterBouton)
        self.canvas.tag_bind(QuitterBouton, "<Enter>",lambda *_: self.hoverBouton("entre","quitter",QuitterBouton))
        self.canvas.tag_bind(QuitterBouton, "<Leave>",lambda *_: self.hoverBouton("sort","quitter",QuitterBouton))



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
        """ Fonction qui permet le callback du bouton "Quitter"
        
        """
        self.window.destroy()
        exit(1)
        

        
    def fermerRegle(self,event):
        """ Fonction qui permet le callback du bouton "Info" permettant de fermer les règles
        
        """
        if not self.hidden: # fermer les règles
            self.hidden = True
            self.canvas.itemconfigure(self.RegleBlokus,state=tkinter.HIDDEN)
            self.canvas.itemconfigure(self.RegleFondBlokus,state=tkinter.HIDDEN)
        if self.scrollable_frame:
            self.scrollable_frame.destroye()
            self.scrollable_frame.destroy()
            self.canvas.delete(self.windowRegle)

    def BoutonScore(self,event):
        """ Fonction qui permet le callback du bouton "Score"
        
        """
        self.window.destroy()
    
    def EnLigneBouton(self,event):
        """ Fonction qui permet le callback du bouton "En ligne"
        
        """
        self.window.destroy()

    def infoBouton(self,event):
        """Méthode pour permettre d'afficher les règles du jeu blokus et de crée une frame de scroll
        """
        if self.hidden: # afficher les règles
            self.hidden = False
            self.canvas.itemconfigure(self.RegleBlokus,state=tkinter.NORMAL)
            self.canvas.itemconfigure(self.RegleFondBlokus,state=tkinter.NORMAL)
            self.scrollable_frame = ScrollableFrame(self.canvas,config.Config.image[53])
            self.windowRegle = self.canvas.create_window(((config.Config.largueur/2)-1, 
            (config.Config.hauteur/2)-4),window=self.scrollable_frame)
            
    
    def HorsLigneBouton(self,event):
        """ Fonction qui permet le callback du bouton "Hors ligne"
        
        """
        import Vues.Lobby.lobbyLocal as lobbyLocal
        config.Config.controller.changePage("lobbyLocal")
        
        
        
        

if __name__ == "__main__":
    from config import config
    from Controller.Controller import Controller
    window = Tk(className='Connexion')

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    config.initialisation(None)
    image = config.Config.image

    MonAccueil = Connexion(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()