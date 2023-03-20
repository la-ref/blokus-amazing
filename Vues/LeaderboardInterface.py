from __future__ import annotations
from tkinter import PhotoImage
import tkinter as tk
import Elements.Pieces.PiecesListGUI as PG
from PIL import ImageTk
from config import config
from Elements.Board import Board
import Vues.accueil as accueil 
from HighScore.fonctionJson import fonctionJson
from Vues.Game.GridInterface import GridInterface

class LeaderboardInterface(tk.Frame):
    """ 
    """
    def __init__(self : LeaderboardInterface, window : tk.Misc):
        """


        """
        super(LeaderboardInterface,self).__init__(window)
        self.window = window
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None

    def initialize(self):
        """ 
        """
        for widgets in self.winfo_children():
            widgets.unbind('<ButtonPress-1>')
            widgets.destroy()
        self.boutonUser = []
        self.activeclavier = False

        self.touche = None
        self.canvas = tk.Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        
        self.modal_active = False
        self.canvas.place(x = 0, y = 0)
        #self.canvas.bind("<Button-1>",self.clique)
        self.Arriere_plan = self.canvas.create_image(720.0,512.0,image= config.Config.image[14])
        
        self.retour = self.canvas.create_image(719.0, 850.0,image= config.Config.image[60])
        self.canvas.tag_bind(self.retour, "<Button-1>",lambda *_: self.create_modal())
        
        self.fleche_droite = self.canvas.create_image(935.0, 850.0,image= config.Config.image[61])
        
        self.fleche_droite = self.canvas.create_image(500.0, 850.0,image= config.Config.image[62])
        
        
        
    def Retour(self):
        """ Méthode permettant de revenir à la page d'Accueil
        """
        config.Config.controller.changePage("Acceuil")
        
        
    def create_modal(self):
        self.modal_active = True
        self.modal = self.canvas.create_image(
            0, 
            0, 
            image=config.Config.image[46],
            anchor=tk.NW
        )

        self.modal_no = self.canvas.create_image(
            config.Config.largueur/2-372,
            config.Config.hauteur/2+25,
            image=config.Config.image[56],
            anchor=tk.NW
        )

        self.modal_yes =self.canvas.create_image(
            config.Config.largueur/2+100,
            config.Config.hauteur/2+25,
            image=config.Config.image[57],
            anchor=tk.NW
        )
        
        self.canvas.tag_bind(self.modal_yes, "<Button-1>",lambda *_: self.yes())
        self.canvas.tag_bind(self.modal_no, "<Button-1>",lambda *_: self.no())
        self.text_modal = self.canvas.create_text(config.Config.largueur/2,(config.Config.hauteur/2)-config.Config.taillePolice[0]/2-25,text="Êtes vous sûr de vouloir quitter ?",fill="#000000",font=("Lilita One", config.Config.taillePolice[0]),anchor=tk.CENTER,justify='center')
        self.modal_active = True
     
    """ Fonction permettant de détruire le modal actif """
   
    def remove_modal(self):
        self.canvas.delete(self.modal,self.modal_no,self.modal_yes,self.text_modal)


    """ Fonction callback de confirmation des modaux
    """
    def yes(self):
        self.remove_modal()
        self.Retour()
        self.modal_active = False
    
    """ Fonction callback d' infirmation des modaux
    """
    def no(self):
        self.remove_modal()
        self.modal_active = False
        

if __name__ == "__main__":
    from config import config
    from Controller.Controller import Controller
    window = tk.Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    config.initialisation(None)
    image = config.Config.image

    MonAccueil = LeaderboardInterface(window)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()