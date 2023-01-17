from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
import tkinter as tk
import Elements.Player as Player
import Vues.Lobby.lobbyUser as lobbyUser
from Vues.accueil import *
from Vues.Game.GameInterface import GameInterface

class lobbyLocal(Frame):
    def __init__(self,window):
        super(lobbyLocal, self).__init__()
        self.window = window


    def initialize(self):
        """ Fonction qui initialise le lobby Hors Ligne
        """
        for widgets in self.winfo_children():
            widgets.unbind('<ButtonPress-1>')
            widgets.destroy()
        self.boutonUser = []
        self.activeclavier = False

        self.touche = None
        self.joueurs = [Player.Player(0,"PERSONNE 1"),Player.Player(1,"PERSONNE 2"),Player.Player(2,"PERSONNE 3"),Player.Player(3,"PERSONNE 4")]
        self.window.bind("<Key>", self.touches)
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
        self.canvas.bind("<Button-1>",self.clique)
        self.Arriere_plan = self.canvas.create_image(720.0,512.0,image= config.Config.image[14])

        self.Bouton_Jouer = self.canvas.create_image(719.0, 464.0,image= config.Config.image[17])
        self.canvas.tag_bind(self.Bouton_Jouer, "<Button-1>", self.jouer)
        self.canvas.tag_bind(self.Bouton_Jouer, "<Enter>",lambda *_: self.hoverBouton("entre","jouer",self.Bouton_Jouer))
        self.canvas.tag_bind(self.Bouton_Jouer, "<Leave>",lambda *_: self.hoverBouton("sort","jouer",self.Bouton_Jouer))


        self.Bouton_Quitter = self.canvas.create_image(717.0,577.0,image= config.Config.image[19])
        self.canvas.tag_bind(self.Bouton_Quitter, "<Button-1>", self.QuitterBouton)
        self.canvas.tag_bind(self.Bouton_Quitter, "<Enter>",lambda *_: self.hoverBouton("entre","quitter",self.Bouton_Quitter))
        self.canvas.tag_bind(self.Bouton_Quitter, "<Leave>",lambda *_: self.hoverBouton("sort","quitter",self.Bouton_Quitter))


        self.bouton_jaune = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[0],16,hb="haut",droiteg="gauche")
        self.bouton_jaune.move(279,147)
        self.namezone_jaune = self.bouton_jaune.getNameZone()
        self.namezone_jaune_text = self.bouton_jaune.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_jaune, "<Button-1>",lambda *_: self.Boutonselect("jaune"))
        self.canvas.tag_bind(self.namezone_jaune_text, "<Button-1>",lambda *_: self.Boutonselect("jaune"))


        self.bouton_vert = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[1],25,hb="haut",droiteg="droite")
        self.bouton_vert.move(1156,147)
        self.namezone_vert = self.bouton_vert.getNameZone()
        self.namezone_vert_text = self.bouton_vert.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_vert, "<Button-1>",lambda *_: self.Boutonselect("vert"))
        self.canvas.tag_bind(self.namezone_vert_text, "<Button-1>",lambda *_: self.Boutonselect("vert"))


        self.bouton_rouge = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[2],22,hb="bas",droiteg="gauche")
        self.bouton_rouge.move(279,883)
        self.namezone_rouge = self.bouton_rouge.getNameZone()
        self.namezone_rouge_text = self.bouton_rouge.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_rouge, "<Button-1>",lambda *_: self.Boutonselect("rouge"))
        self.canvas.tag_bind(self.namezone_rouge_text, "<Button-1>",lambda *_: self.Boutonselect("rouge"))


        self.bouton_bleu = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[3],15,hb="bas",droiteg="droite")
        self.bouton_bleu.move(1156,883)
        self.namezone_bleu = self.bouton_bleu.getNameZone()
        self.namezone_bleu_text = self.bouton_bleu.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_bleu, "<Button-1>",lambda *_: self.Boutonselect("bleu"))
        self.canvas.tag_bind(self.namezone_bleu_text, "<Button-1>",lambda *_: self.Boutonselect("bleu"))


    def Boutonselect(self, typ):
        """ Méthode qui permet d'activer la saisie du clavier sur chacun des blocs d'utilisateur
        
        Args:
            typ (str): Le nom en couleur du type de joueur "bleu", "jaune", "vert", "rouge"
        """
        if typ == "bleu":
            self.bouton_bleu.setActiveClavier(True)
        else:
            self.bouton_bleu.setActiveClavier(False)
        if typ == "jaune":
            self.bouton_jaune.setActiveClavier(True)
        else:
            self.bouton_jaune.setActiveClavier(False)
        if typ == "vert":
            self.bouton_vert.setActiveClavier(True)
        else:
            self.bouton_vert.setActiveClavier(False)
        if typ == "rouge":
            self.bouton_rouge.setActiveClavier(True)
        else:
            self.bouton_rouge.setActiveClavier(False)

    def clique(self,event):
        """ Méthode qui permet de vérifier le clic du joueur et d'activer la saisie ou non du clavier
        si le widget cliqué est le bon

        Args:
            event (x,y): Les coordonnées en X et Y du clic du joueur
        """
        actuelwidget = event.widget.find_withtag('current')[0]
        # print(actuelwidget)
        if self.bouton_jaune.getActiveClavier() == True:
            if (actuelwidget != 5) and (actuelwidget != 4):
                self.bouton_jaune.setActiveClavier(False)
        if self.bouton_vert.getActiveClavier() == True:
            if (actuelwidget != 15) and (actuelwidget != 14):
                self.bouton_vert.setActiveClavier(False)
        if self.bouton_rouge.getActiveClavier() == True:
            if (actuelwidget != 25) and (actuelwidget != 24):
                self.bouton_rouge.setActiveClavier(False)
        if self.bouton_bleu.getActiveClavier() == True:
            if (actuelwidget != 35) and (actuelwidget != 34):
                self.bouton_bleu.setActiveClavier(False)
        
        
    def touches(self,event):
        """ Méthode qui permet d'inverser au clic la saisie de chacun des blocs
        """
        self.bouton_bleu.touches(event)
        self.bouton_rouge.touches(event)
        self.bouton_jaune.touches(event)
        self.bouton_vert.touches(event)

    def jouer(self,event):
        """ Méthode permettant de lancer la partie au clic du bouton "joueur"
        """
        from Elements.Game import Game
        config.Config.controller.game = Game(self.joueurs,None,20)
        config.Config.controller.changePage("GameInterface")
    
    def QuitterBouton(self,event):
        """ Méthode permettant re venir à la page d'Accueil (initialisation de la page d'accueil)
        """
        config.Config.controller.changePage("Acceuil")

    def hoverBouton(self,typ : str,typ2 : str,idButton : int):
        """ Méthode permettant de modifier l'image au survol de la souris sur l'objet

        Args:
            typ (str): "entre" ou "sort"
            typ2 (str): "jouer" ou "quitter"
            idButton (int): l'identifiant du bouton cliqué
        """
        if typ == "entre":
            if typ2 == "quitter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[40])
                self.canvas.config(cursor="hand2")
            elif typ2 == "jouer":
                self.canvas.itemconfigure(idButton, image=config.Config.image[39])
                self.canvas.config(cursor="hand2")
        elif typ == "sort":
            if typ2 == "quitter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[19])
                self.canvas.config(cursor="")
            elif typ2 == "jouer":
                self.canvas.itemconfigure(idButton, image=config.Config.image[17])
                self.canvas.config(cursor="")

if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyLocal(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
