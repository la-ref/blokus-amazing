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
from HighScore.Leaderboard import *
import Elements.Pieces.PiecesDeclaration as PD
from tkinter import PhotoImage
import Elements.Pieces.Pieces as p
import numpy as np
import Vues.Game.Block as b
from config import config
import platform
import copy
import Vues.Game.Pieces_placement as PP
from Elements.Pieces.Pieces import Pieces
from Elements.Pieces.PiecesDeclaration import LISTEPIECES

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
        self.canvas.tag_bind(self.retour, "<Enter>",lambda *_: self.hoverBouton("entre","retour",self.retour))
        self.canvas.tag_bind(self.retour, "<Leave>",lambda *_: self.hoverBouton("sort","retour",self.retour))
        
        self.fleche_droite = self.canvas.create_image(935.0, 850.0,image= config.Config.image[61])
        
        self.fleche_droite = self.canvas.create_image(500.0, 850.0,image= config.Config.image[62])
        


        self.createPieces()
        
        
        
    def Retour(self):
        """ Méthode permettant de revenir à la page d'Accueil
        """
        config.Config.controller.changePage("Acceuil")
        
    def createPieces(self):

        self.Lists=[]
        for i in range(4):
            nb_player = i
            self.list = list
            self.x = 0
            self.y = 0
            self.le_x = 0
            self.le_y = 0
            self.rotate = False
            self.souris_x = 0
            self.sourix_y = 0
            self.state = 0
            self.tableau_piece = [[]]
            self.tableau_piece_forme = []
            self.mon_state = 0

            decalageX = 2
            decalageY = 100
            self.tableau_piece_forme = []

            i1 = 0
            maxheight = 0
            for valeur in LISTEPIECES.copy():
                
                self.tableau_piece_forme.append(PP.Pieces_placement(self.window,self.canvas,nb_player,valeur,self))

                self.tableau_piece_forme[i1].move_init(decalageX,decalageY)
                decalageX+=self.tableau_piece_forme[i1].getWidth_Petit()*self.tableau_piece_forme[i1].getImage().width() + 10
                if self.tableau_piece_forme[i1].getHeight_Petit() > maxheight:
                    maxheight = self.tableau_piece_forme[i1].getHeight_Petit()

                i1+=1

                if (decalageX) >= 317-(20*3):
                    decalageX= 2
                    decalageY+= (maxheight*self.tableau_piece_forme[i1-1].getImage().height())+10
                    maxheight = 0
            self.Lists.append(self.tableau_piece_forme)

        for i in self.Lists[0]:
            i.moveHigh(x=70,y=80) # jaune
        for i in self.Lists[1]:
            i.moveHigh(x=100,y=100) # vert
        for i in self.Lists[2]:
            i.moveHigh(x=200,y=200) # rouge
        for i in self.Lists[3]:
            i.moveHigh(x=300,y=300)

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

    def hoverBouton(self,typ : str,typ2 : str,idButton : int):
        """ Méthode permettant de modifier l'image au survol de la souris sur l'objet

        Args:
            typ (str): "entre" ou "sort"
            typ2 (str): "jouer" ou "quitter"
            idButton (int): l'identifiant du bouton cliqué
        """
        if typ == "entre":
            if typ2 == "retour":
                self.canvas.itemconfigure(idButton, image=config.Config.image[63])
                self.canvas.config(cursor="hand2")        
        elif typ == "sort":
            if typ2 == "retour":
                self.canvas.itemconfigure(idButton, image=config.Config.image[60])
                self.canvas.config(cursor="")

        

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