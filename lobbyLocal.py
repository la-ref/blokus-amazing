from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
import tkinter as tk
import Player
import lobbyUser
class lobbyLocal(Frame):
    def __init__(self,window,image_list):
        self.boutonUser = []
        self.activeclavier = False
        self.window = window
        self.image_list = image_list
        self.touche = None
        self.joueur = Player.Player(4)
        self.joueurs = [self.joueur.Player(11,"PERSONNE 1"),self.joueur.Player(12,"PERSONNE 2"),self.joueur.Player(13,"PERSONNE 3"),self.joueur.Player(14,"PERSONNE 4")]

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
        self.Arriere_plan = self.canvas.create_image(720.0,512.0,image= self.image_list[14])
        self.Bouton_Jouer = self.canvas.create_image(719.0, 464.0,image= self.image_list[17])

        self.Bouton_Quitter = self.canvas.create_image(717.0,577.0,image= self.image_list[19])
        self.canvas.tag_bind(self.Bouton_Quitter, "<Button-1>", self.QuitterBouton)

        self.text_facile = self.canvas.create_text(
            1194.0,
            657.04345703125,
            anchor="nw",
            text="FACILE",
            fill="#FFFFFF",
            font=("LilitaOne", 32 * -1)
        )

        self.Noir_IA_Bleu_2 = self.canvas.create_image(1266.91796875,622.521728515625,image= self.image_list[18])

        self.text_moyen = self.canvas.create_text(
            1194.91796875,
            596.521728515625,
            anchor="nw",
            text="MOYEN",
            fill="#FFFFFF",
            font=("LilitaOne", 32 * -1)
        )

        self.Noir_IA_Bleu_3 = self.canvas.create_image(1266.0,562.0,image= self.image_list[18])

        self.text_expert = self.canvas.create_text(
            1194.0,
            536.0,
            anchor="nw",
            text="EXPERT",
            fill="#FFFFFF",
            font=("LilitaOne", 32 * -1)
        )

        self.bouton_jaune = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[0],25,hb="haut",droiteg="gauche")
        self.bouton_jaune.move(1156,147)

        self.bouton_vert = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[1],25,hb="haut",droiteg="droite")
        self.bouton_vert.move(279,147)

        self.bouton_rouge = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[2],25,hb="bas",droiteg="gauche")
        self.bouton_rouge.move(279,883)

        self.bouton_bleu = lobbyUser.lobbyUser(self.window,self.canvas,self.image_list,self.joueurs[3],25,hb="bas",droiteg="droite")
        self.bouton_bleu.move(1156,883)

    # def touches(self,event):
    #     self.touche = str(event.keysym)
    #     if self.activeclavier == True:
    #         if self.type == "Vert":
    #             if self.touche != "BackSpace" and self.touche != "space":
    #                 if len(self.joueurs[1].name) < 12:
    #                     self.joueurs[1].setName(str(self.joueurs[1].name+self.touche))
    #             elif self.touche == "space":
    #                 if len(self.joueurs[1].name) < 12:
    #                     self.joueurs[1].setName(str(self.joueurs[1].name)+" ")
    #             else:
    #                 if len(self.joueurs[1].name) > 0:
    #                     self.joueurs[1].setName(str(self.joueurs[1].name)[:-1])
    #             print(self.canvas.itemcget(self.text_vert))
    #             # self.text_vert
    #             # self.text_vert
    #             # self.text_vert
    #             self.canvas.itemconfigure(self.text_vert, text=self.joueurs[1].name.upper())

    def QuitterBouton(self):
        pass
        #retour accueil
if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyLocal(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
