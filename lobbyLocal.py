from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
import tkinter as tk

class lobbyLocal(Frame):
    def __init__(self,window,image_list):
        self.boutonUser = []
        self.window = window
        self.image_list = image_list
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

        self.Bouton_Rouge = self.canvas.create_image(279.0,883.0,image= self.image_list[22])

        self.text_rouge = self.canvas.create_text(
            157.639892578125,
            840.0,
            anchor="nw",
            text="PERSONNE 3",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )

        self.Bouton_Jouer = self.canvas.create_image(719.0, 464.0,image= self.image_list[17])
        self.Bouton_Quitter = self.canvas.create_image(
            717.0,
            577.0,
            image= self.image_list[19]
        )
        self.canvas.tag_bind(self.Bouton_Quitter, "<Button-1>", self.QuitterBouton)


        self.Bouton_Bleu = self.canvas.create_image(1156.0,883.0,image= self.image_list[15])
        self.text_bleu = self.canvas.create_text(
            1034.639892578125,
            840.0,
            anchor="nw",
            text="PERSONNE 4",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )


        self.Noir_IA_Bleu_1 = self.canvas.create_image(1266.0,683.04345703125,image= self.image_list[18])
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

        self.Bouton_Vert = self.canvas.create_image(1156.0,147.0,image= self.image_list[25])

        self.text_vert = self.canvas.create_text(
            1034.639892578125,
            104.0,
            anchor="nw",
            text="PERSONNE 2",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )

        self.Bouton_Jaune = self.canvas.create_image(
            279.0,
            147.0,
            image= self.image_list[16]
        )

        self.text_jaune = self.canvas.create_text(
            157.639892578125,
            104.0,
            anchor="nw",
            text="PERSONNE 1",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )

        self.Bouton_Robot_gris_X = self.canvas.create_image(
            139.0,
            256.0,
            image= self.image_list[20]
        )

        self.Bouton_Robot_noir_Vert = self.canvas.create_image(1295.0,256.0, image= self.image_list[21])
        self.canvas.tag_bind(self.Bouton_Robot_noir_Vert, "<Button-1>", self.boutonSwitchIAVert)
        self.Bouton_User_noir_Jaune = self.canvas.create_image(
            249.0,
            256.0,
            image= self.image_list[24]
        )
        self.canvas.tag_bind(self.Bouton_User_noir_Jaune, "<Button-1>", self.BoutonIAJaune)
        self.boutonUser.append("noir")

        self.Bouton_User_gris_Vert = self.canvas.create_image(
            1185.0,
            256.0,
            image= self.image_list[23]
        )
        self.canvas.tag_bind(self.Bouton_User_gris_Vert, "<Button-1>", self.BoutonIAVert)
        self.boutonUser.append("gris")

        self.Bouton_User_noir_Rouge = self.canvas.create_image(
            249.0,
            775.0,
            image= self.image_list[24]
        )
        self.canvas.tag_bind(self.Bouton_User_noir_Rouge, "<Button-1>", self.BoutonIARouge)
        self.boutonUser.append("noir")

        self.Bouton_User_gris_Bleu = self.canvas.create_image(
            1185.0,
            775.0,
            image= self.image_list[23]
        )
        self.canvas.tag_bind(self.Bouton_User_gris_Bleu, "<Button-1>", self.BoutonIABleu)
        self.boutonUser.append("gris")

        self.Bouton_Robot_gris_X = self.canvas.create_image(139.0,775.0,image= self.image_list[20])
        self.Bouton_IA_noir_Bleu = self.canvas.create_image(1295.0,775.0,image= self.image_list[21])
        self.canvas.tag_bind(self.Bouton_IA_noir_Bleu, "<Button-1>", self.boutonSwitchIABleu)


    def QuitterBouton(self):
        pass
        #retour accueil

    def boutonSwitchIAJaune(self,event):
        if self.boutonUser[0] == "gris":
            pass
        else:
            self.BoutonIAJaune(self,event)
    def boutonSwitchIARouge(self,event):
        if self.boutonUser[2] == "gris":
            pass
        else:
            self.BoutonIARouge(self,event)
    def boutonSwitchIAVert(self,event):
        print("vert")
        if self.boutonUser[1] == "gris":
            pass
        else:
            self.BoutonIAVert(self,event)
    def boutonSwitchIABleu(self,event):
        print("bleu")
        if self.boutonUser[3] == "gris":
            pass
        else:
            self.BoutonIABleu(self,event)

    def BoutonIAJaune(self,event):
        print("jaune")
        self.canvas.itemconfigure(self.Bouton_User_noir_Jaune, state=tk.HIDDEN)
        if self.boutonUser[0] == "gris":
            self.Bouton_User_noir_Jaune = self.canvas.create_image(249.0,256.0,image=self.image_list[24])
            self.boutonUser[0] = "noir"
        else:
            self.Bouton_User_noir_Jaune = self.canvas.create_image(249.0,256.0,image=self.image_list[23])
            self.boutonUser[0] = "gris"
        self.canvas.tag_bind(self.Bouton_User_noir_Jaune, "<Button-1>", self.BoutonIAJaune)
    def BoutonIARouge(self,event):
        print("rouge")
        self.canvas.itemconfigure(self.Bouton_User_noir_Rouge, state=tk.HIDDEN)
        if self.boutonUser[2] == "gris":
            self.Bouton_User_noir_Rouge = self.canvas.create_image(249.0,775.0,image=self.image_list[24])
            self.boutonUser[2] = "noir"
        else:
            self.Bouton_User_noir_Rouge = self.canvas.create_image(249.0,775.0,image=self.image_list[23])
            self.boutonUser[2] = "gris"
        self.canvas.tag_bind(self.Bouton_User_noir_Rouge, "<Button-1>", self.BoutonIARouge)

    def BoutonIAVert(self,event):
        print("vert", event)
        # self.Bouton_User_gris_Vert.destroy()
        self.canvas.itemconfigure(self.Bouton_User_gris_Vert, state=tk.HIDDEN)
        self.canvas.itemconfigure(self.Bouton_Robot_noir_Vert, state=tk.HIDDEN)
        if self.boutonUser[1] == "gris":
            self.Bouton_User_gris_Vert = self.canvas.create_image(1185.0,256.0,image=self.image_list[24])
            self.Bouton_Robot_noir_Vert = self.canvas.create_image(1295.0,256.0, image= self.image_list[20])
            self.boutonUser[1] = "noir"
        else:
            self.Bouton_User_gris_Vert = self.canvas.create_image(1185.0,256.0,image=self.image_list[23])
            self.Bouton_Robot_noir_Vert = self.canvas.create_image(1295.0,256.0, image= self.image_list[21])
            self.boutonUser[1] = "gris"
        self.canvas.tag_bind(self.Bouton_User_gris_Vert, "<Button-1>", self.BoutonIAVert)
        
    def BoutonIABleu(self,event):
        print("bleu")
        self.canvas.itemconfigure(self.Bouton_User_gris_Bleu, state=tk.HIDDEN)
        self.canvas.itemconfigure(self.Bouton_IA_noir_Bleu, state=tk.HIDDEN)
        
        if self.boutonUser[3] == "gris":
            self.Bouton_User_gris_Bleu = self.canvas.create_image(1185.0,775.0,image=self.image_list[24])
            self.Bouton_IA_noir_Bleu = self.canvas.create_image(1295.0,775.0,image= self.image_list[20])
            self.boutonUser[3] = "noir"
        else:
            self.Bouton_User_gris_Bleu = self.canvas.create_image(1185.0,775.0,image=self.image_list[23])
            self.Bouton_IA_noir_Bleu = self.canvas.create_image(1295.0,775.0,image= self.image_list[21])
            self.boutonUser[3] = "gris"
        self.canvas.tag_bind(self.Bouton_User_gris_Bleu, "<Button-1>", self.BoutonIABleu)


if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyLocal(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
