from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
import tkinter as tk
import Player
import lobbyUser
from accueil import *

class lobbyLocal(Frame):
    def __init__(self,window,image_list):
        self.boutonUser = []
        self.activeclavier = False
        self.window = window
        self.image_list = image_list
        self.touche = None
        self.joueurs = [Player.Player(11,"PERSONNE 1"),Player.Player(12,"PERSONNE 2"),Player.Player(13,"PERSONNE 3"),Player.Player(14,"PERSONNE 4")]
        self.window.bind("<Key>", self.touches)
        self.canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.bind("<Button-1>",self.clique)
        self.Arriere_plan = self.canvas.create_image(720.0,512.0,image= self.image_list[14])
        self.Bouton_Jouer = self.canvas.create_image(719.0, 464.0,image= self.image_list[17])
        self.canvas.tag_bind(self.Bouton_Jouer, "<Button-1>", self.jouer)

        self.Bouton_Quitter = self.canvas.create_image(717.0,577.0,image= self.image_list[19])
        self.canvas.tag_bind(self.Bouton_Quitter, "<Button-1>", self.QuitterBouton)

        self.bouton_jaune = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[0],16,hb="haut",droiteg="gauche")
        self.bouton_jaune.move(279,147)

        self.bouton_vert = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[1],25,hb="haut",droiteg="droite")
        self.bouton_vert.move(1156,147)

        self.bouton_rouge = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[2],22,hb="bas",droiteg="gauche")
        self.bouton_rouge.move(279,883)

        self.bouton_bleu = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[3],15,hb="bas",droiteg="droite")
        self.bouton_bleu.move(1156,883)

    def clique(self,event):
        actuelwidget = event.widget.find_withtag('current')[0]
        print(actuelwidget)
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
        self.bouton_bleu.touches(event)
        self.bouton_rouge.touches(event)
        self.bouton_jaune.touches(event)
        self.bouton_vert.touches(event)

    def jouer(self,event):
        from Game import Game
        self.jeu = Game(self.joueurs,None,20)
        self.window = self.jeu.jeu(self.window)
    
    def QuitterBouton(self,event):
        self.window = Accueil(self.window, self.image_list)

if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyLocal(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
