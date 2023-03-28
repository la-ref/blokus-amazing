from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
from Vues.ScrollableFrame import ScrollableFrame

class Accueil(Frame):
    """ Classe étant une frame réprésentant la page d'acceuil
    """
    def __init__(self,window):
        super(Accueil, self).__init__()
        self.window = window
        self.window.title("Blokus")
        self.window.wm_iconphoto(True, config.Config.image[47])
        self.hidden = True
        self.errorPopUp = None
        self.scrollable_frame = None
        self.windowRegle = None
        self.pop_up_text = None

    def initialize(self):
        """ Fonction qui initialise la page d'accueil
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

        HorsLigneBouton = self.canvas.create_image(
            510, 
            344, 
            image=config.Config.image[5],
            anchor=tkinter.NW
        )
        
        self.canvas.tag_bind(HorsLigneBouton, "<Button-1>", self.HorsLigneBouton)
        self.canvas.tag_bind(HorsLigneBouton, "<Enter>",lambda *_: self.hoverBouton("entre","horsligne",HorsLigneBouton))
        self.canvas.tag_bind(HorsLigneBouton, "<Leave>",lambda *_: self.hoverBouton("sort","horsligne",HorsLigneBouton))


        EnLigneBouton = self.canvas.create_image(
            510, 
            488, 
            image=config.Config.image[1],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(EnLigneBouton, "<Button-1>", self.EnLigneBouton)
        self.canvas.tag_bind(EnLigneBouton, "<Enter>",lambda *_: self.hoverBouton("entre","enligne",EnLigneBouton))
        self.canvas.tag_bind(EnLigneBouton, "<Leave>",lambda *_: self.hoverBouton("sort","enligne",EnLigneBouton))


        QuitterBouton = self.canvas.create_image(
            510, 
            642, 
            image=config.Config.image[2],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(QuitterBouton, "<Button-1>", self.QuitterBouton)
        self.canvas.tag_bind(QuitterBouton, "<Enter>",lambda *_: self.hoverBouton("entre","quitter",QuitterBouton))
        self.canvas.tag_bind(QuitterBouton, "<Leave>",lambda *_: self.hoverBouton("sort","quitter",QuitterBouton))

        

        BoutonScore = self.canvas.create_image(
            1032, 
            821, 
            image=config.Config.image[3],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(BoutonScore, "<Enter>",lambda *_: self.hoverBouton("entre","leader",BoutonScore))
        self.canvas.tag_bind(BoutonScore, "<Leave>",lambda *_: self.hoverBouton("sort","leader",BoutonScore))



        BoutonInfo = self.canvas.create_image(
            334, 
            821, 
            image=config.Config.image[4],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(BoutonInfo, "<Enter>",lambda *_: self.hoverBouton("entre","info",BoutonInfo))
        self.canvas.tag_bind(BoutonInfo, "<Leave>",lambda *_: self.hoverBouton("sort","info",BoutonInfo))

        self.RegleFondBlokus = self.canvas.create_image(
            (config.Config.largueur/2)-config.Config.image[54].width()/2, 
            config.Config.hauteur/2-config.Config.image[54].height()/2, 
            image=config.Config.image[54],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(self.RegleFondBlokus, "<Button-1>", self.fermerRegle)

        self.RegleBlokus = self.canvas.create_image(
            (config.Config.largueur/2)-config.Config.image[52].width()/2, 
            config.Config.hauteur/2-config.Config.image[52].height()/2, 
            image=config.Config.image[52],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(BoutonInfo, "<Button-1>", self.infoBouton)
        self.canvas.itemconfigure(self.RegleBlokus,state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.RegleFondBlokus,state=tkinter.HIDDEN)
        

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
        
    def errorPop(self,error = "Erreur fatale : Le serveur a été deconnecté!"):
        if not self.errorPopUp and not self.pop_up_text and self.hidden:
            self.errorPopUp = self.canvas.create_image(
                0,  
                0, 
                image=config.Config.image[73],
                anchor=tkinter.NW
            )
            self.pop_up_text = self.canvas.create_text(config.Config.largueur/2,(config.Config.hauteur/2)-config.Config.taillePolice[0]/2,text=error,fill="#000000",font=("Lilita One", config.Config.taillePolice[0]),anchor=tkinter.CENTER,justify='center')
            self.canvas.tag_bind(self.errorPopUp, "<Button-1>", self.removeErrorPop)
        
            
    def removeErrorPop(self,e):
        if self.errorPopUp and self.pop_up_text:
            self.canvas.itemconfigure(self.RegleFondBlokus,state=tkinter.HIDDEN)
            self.canvas.delete(self.errorPopUp)
            self.canvas.delete(self.pop_up_text)
            self.errorPopUp = None
            self.pop_up_text = None

        
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
        print(self.errorPopUp, self.pop_up_text)

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
    
    def EnLigneBouton(self,event):
        """ Fonction qui permet le callback du bouton "Hors ligne"
        
        """
        import Vues.connexion as connexion
        config.Config.controller.changePage("connexion")
        
        
        
        

if __name__ == "__main__":
    from config import config
    from Controller.Controller import Controller
    window = Tk(className='Accueil')

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    config.initialisation(None)
    image = config.Config.image

    MonAccueil = Accueil(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()