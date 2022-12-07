from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
import tkinter as tk
import Player
class lobbyUser(Frame):
    def __init__(self, window, parent : tk.Canvas, images : list, joueurs : Player.Player, nb_player : int, height : int = 420, width : int = 317, droiteg : str = "haut", hb : str = "droite"):
        super(lobbyUser,self).__init__(parent)
        self.parent = parent
        self.window = window
        self.window.bind("<Key>", self.touches)
        self.image_list = images
        self.joueurs = joueurs
        self.activeclavier = False
        self.boutonUser = "noir"
        self.width = width
        self.hb = hb
        self.dg = droiteg
        self.rwidth = 64-20
        self.uwidth = width/2
        self.rheight = 107
        self.x=0
        self.y=0
        
        self.nameZone = self.parent.create_image(
            15,
            10,
            image=images[nb_player],
        )
        self.parent.tag_bind(self.nameZone, "<Button-1>", self.boutonChangerText)
        
        self.text = self.parent.create_text((width-220)/2,3,fill="white",font=('Lilita One', 40),text=self.joueurs.name,anchor=tk.CENTER)

        if self.hb == "haut":
            if self.dg == "droite":
                self.rwidth = width/2
                self.uwidth = 64-20
            if self.dg == "gauche":
                self.rwidth = 64-20
                self.uwidth = width/2
            self.rheight = 107
        if self.hb == "bas":
            if self.dg == "droite":
                self.rwidth = width/2
                self.uwidth = 64-20
            if self.dg == "gauche":
                self.rwidth = 64-20
                self.uwidth = width/2
            self.rheight = -107
        
        self.Bouton_Robot = self.parent.create_image(self.rwidth,self.rheight, image=self.image_list[21])
        self.parent.tag_bind(self.Bouton_Robot, "<Button-1>", self.boutonSwitchIA)
        self.Bouton_User = self.parent.create_image(self.uwidth,self.rheight,image= self.image_list[23])
        self.parent.tag_bind(self.Bouton_User, "<Button-1>", self.BoutonIA)
    

    def changeName(self, newName : str):
        self.parent.itemconfig(self.text, text=newName)
        
    def move(self, x : int, y : int):
        self.x = x
        self.y = y
        self.parent.move(self.text,x,y)
        self.parent.move(self.nameZone,x,y)
        self.parent.move(self.Bouton_Robot,x,y)
        self.parent.move(self.Bouton_User,x,y)
    
    def moverobot(self, x : int, y : int):
        self.x = x
        self.y = y
        self.parent.move(self.Bouton_Robot,x,y)
        self.parent.move(self.Bouton_User,x,y)
  
    
    # Fonction utiliser par Mouvement Manager (à supprimer plus tard)


    def bind(self,event_tag,call):
        self.parent.tag_bind(self.text,event_tag,call)

    def boutonChangerText(self,event):
        print(self.activeclavier)
        if self.activeclavier == True:
            self.activeclavier = False
        else:
            self.activeclavier = True  
    
    def touches(self,event):
        self.touche = str(event.keysym)
        if self.activeclavier == True:
            if len(self.touche) == 1:
                if len(self.joueurs.name) < 10:
                    self.joueurs.setName(str(self.joueurs.name+self.touche))
            elif self.touche == "space":
                if len(self.joueurs.name) < 10:
                    self.joueurs.setName(str(self.joueurs.name)+" ")
            else:
                if len(self.joueurs.name) > 0:
                    self.joueurs.setName(str(self.joueurs.name)[:-1])
            # print(self.parent.itemcget(self.text))

            tailles = self.parent.bbox(self.text)
            width = tailles[2] - tailles[0]
            if width > 300:
                self.parent.itemconfigure(self.text, text=self.joueurs.name.upper(), font=('Lilita One', 32))
            else:
                self.parent.itemconfigure(self.text, text=self.joueurs.name.upper(), font=('Lilita One', 40))
                if width > 300:
                    self.parent.itemconfigure(self.text, text=self.joueurs.name.upper(), font=('Lilita One', 32))


    def boutonSwitchIA(self,event):
        if self.boutonUser == "gris":
            pass
        else:
            self.BoutonIA(self,event)

    def BoutonIA(self,event):
        self.parent.itemconfigure(self.Bouton_User, state=tk.HIDDEN)
        self.parent.itemconfigure(self.Bouton_Robot, state=tk.HIDDEN)
        if self.boutonUser == "gris":
            self.Bouton_User = self.parent.create_image(self.uwidth,self.rheight,image=self.image_list[24])
            self.Bouton_Robot = self.parent.create_image(self.rwidth,self.rheight, image= self.image_list[20])
            self.boutonUser = "noir"
        else:
            self.Bouton_User = self.parent.create_image(self.uwidth,self.rheight,image=self.image_list[23])
            self.Bouton_Robot = self.parent.create_image(self.rwidth,self.rheight, image= self.image_list[21])
            self.boutonUser = "gris"
        self.moverobot(self.x,self.y)
        self.parent.tag_bind(self.Bouton_User, "<Button-1>", self.BoutonIA)
        self.parent.tag_bind(self.Bouton_Robot, "<Button-1>", self.BoutonIA)
        
        # prec = self.touche
        # while self.activeclavier == True:
        #     if prec == self.touche:
        #         self.parent.itemconfigure(self.text_vert, Text=self.touche)

        

if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyUser(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
