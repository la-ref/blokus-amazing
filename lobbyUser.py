from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
import tkinter as tk
import Player
class lobbyUser(Frame):
    """Méthode qui permet d'initialiser tout l'objet lobbyUser

        Args:
            self: l'utilisateur tout entier
            window: la fenêtre
            parent: l'objet parent
            image: la liste d'images générée sous photoimages
            joueurs: l'objet de type joueur
            nb_player: l'index d'attribution du joueur
            height: la hauteur de l'objet
            width: la longueur de l'objet
            droiteg: si l'objet et haut ou bas
            hb: si l'objet et à droite ou à gauche
        
    """
    def __init__(self, window, parent : tk.Canvas, images : list, joueurs : Player.Player, nb_player : int, height : int = 420, width : int = 317, droiteg : str = "haut", hb : str = "droite"):
        super(lobbyUser,self).__init__(parent)
        self.parent = parent
        self.window = window
        self.iatype = "facile"
        self.joueurType = "joueur"
        self.stateactuel = 0
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
        self.nameZone = self.parent.create_image(15,10,image=images[nb_player])
        self.parent.tag_bind(self.nameZone, "<Button-1>", self.boutonChangerText)


        self.text = self.parent.create_text((width-220)/2,3,fill="white",font=('Lilita One', 40),text=self.joueurs.getName(),anchor=tk.CENTER)
        self.parent.tag_bind(self.text, "<Button-1>", self.boutonChangerText)
        
        

        if self.hb == "haut":
            if self.dg == "droite":
                self.uwidth = 64-20
                self.rwidth = width/2
            if self.dg == "gauche":
                self.uwidth = 64-20-30-20
                self.rwidth = (-width/2)+64-30
            self.rheight = 107
        if self.hb == "bas":
            if self.dg == "droite":
                self.uwidth = 64-20
                self.rwidth = width/2

                self.iawidth = self.uwidth+32
            if self.dg == "gauche":
                self.rwidth = (-width/2)+64-30
                self.uwidth = 64-20-30-20
            self.rheight = -107
        
        if self.hb == "haut":
            if self.dg == "droite":
                self.w2 = 128
                self.h2 = (width/2)+32
            if self.dg == "gauche":
                self.w2 = -128+30
                self.h2 = 192
            self.hf = self.h2
            self.hm = self.h2+64
            self.he = self.h2+64+64
        if self.hb == "bas":
            if self.dg == "droite":
                self.w2 = 128
                self.h2 = -192
            if self.dg == "gauche":
                self.w2 = -128+30
                self.h2 = -192
            self.hf = self.h2
            self.hm = self.h2-64
            self.he = self.h2-64-64

        self.Noir_IA_1 = self.parent.create_image(self.w2,self.hf,image= self.image_list[18],state=tk.HIDDEN)
        self.parent.tag_bind(self.Noir_IA_1, "<Button-1>", self.facile)
        
        self.text_facile = self.parent.create_text(self.w2,self.hf,text="FACILE",fill="#BBBBBB",font=("LilitaOne", 32),state=tk.HIDDEN)
        self.parent.tag_bind(self.text_facile, "<Button-1>", self.facile)
        
        self.Noir_IA_2 = self.parent.create_image(self.w2,self.hm,image= self.image_list[18],state=tk.HIDDEN)
        self.parent.tag_bind(self.Noir_IA_2, "<Button-1>", self.moyen)
        
        self.text_moyen = self.parent.create_text(self.w2,self.hm,text="MOYEN",fill="#FFFFFF",font=("LilitaOne", 32),state=tk.HIDDEN)
        self.parent.tag_bind(self.text_moyen, "<Button-1>", self.moyen)
        
        self.Noir_IA_3 = self.parent.create_image(self.w2,self.he,image= self.image_list[18],state=tk.HIDDEN)
        self.parent.tag_bind(self.Noir_IA_3, "<Button-1>", self.moyen)
        
        self.text_expert = self.parent.create_text(self.w2,self.he,text="EXPERT",fill="#FFFFFF",font=("LilitaOne", 32),state=tk.HIDDEN)
        self.parent.tag_bind(self.text_expert, "<Button-1>", self.expert)
        
        self.Bouton_Robot = self.parent.create_image(self.rwidth,self.rheight, image=self.image_list[20])
        self.parent.tag_bind(self.Bouton_Robot, "<Button-1>", self.boutonSwitchIA)
        self.Bouton_User = self.parent.create_image(self.uwidth,self.rheight,image= self.image_list[24])
        self.parent.tag_bind(self.Bouton_User, "<Button-1>", self.BoutonIA)
        
    

    def changeName(self, newName : str):
        """Méthode qui permet de changer le text de l'utilisateur sans changer la valeur de l'objet

        Args:
            self: l'utilisateur tout entier
            newName: le nouveau pseudo graphique du joueur
        
        """
        self.parent.itemconfig(self.text, text=newName)
        
    def move(self, x : int, y : int):
        """Méthode qui permet de changer l'emplacement uniquement de tout les objets graphique de l'utilsiateur

        Args:
            self: l'utilisateur tout entier
            x: valeur horizontal
            y: valeur vertical
        
        """
        self.x = x
        self.y = y
        self.parent.move(self.text,x,y)
        self.parent.move(self.nameZone,x,y)
        self.parent.move(self.Bouton_Robot,x,y)
        self.parent.move(self.Bouton_User,x,y)

        self.parent.move(self.Noir_IA_1,x,y)
        self.parent.move(self.Noir_IA_2,x,y)
        self.parent.move(self.Noir_IA_3,x,y)
        self.parent.move(self.text_facile,x,y)
        self.parent.move(self.text_moyen,x,y)
        self.parent.move(self.text_expert,x,y)
    
    def moverobot(self, x : int, y : int):
        """Méthode qui permet de changer l'emplacement uniquement des boutons robot et utilisateur

        Args:
            self: l'utilisateur tout entier
            x: valeur horizontal
            y: valeur vertical
        
        """
        self.x = x
        self.y = y
        self.parent.move(self.Bouton_Robot,x,y)
        self.parent.move(self.Bouton_User,x,y)

    def bind(self,event_tag,call):
        """Méthode qui permet de changer l'attribue (le tag bind) d'un objet

        Args:
            self: l'utilisateur tout entier
            event_tag: le tag bind
            call: l'évènement
        """
        self.parent.tag_bind(self.text,event_tag,call)

    def boutonChangerText(self,event):
        """Méthode qui est relié au bouton et qui permet d'activer ou non la saisie pour cette utilisateur

        Args:
            self: l'utilisateur tout entier
        """
        if self.activeclavier == True:
            self.activeclavier = False
        else:
            self.activeclavier = True  
    
    def getActiveClavier(self):
        """Fonction qui permet de savoir si le clavier est activé ou non

        Args:
            self: l'utilisateur tout entier
        
        Returns:
            self.activeclavier: retourne True si le clavier est activé
        """
        return self.activeclavier
    
    def setActiveClavier(self,boolean):
        """Méthode qui permet d'activer ou non la saisie du clavier pour un utilisateur
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        self.activeclavier = boolean

    def touches(self,event):
        """Méthode qui actualise le pseudo du joueur à chaque touche appuyé de l'ordinateur
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        self.touche = str(event.keysym)
        if self.activeclavier == True:
            if len(self.touche) == 1:
                if len(self.joueurs.getName()) < 10:
                    self.joueurs.setName(str(self.joueurs.getName()+self.touche))
            elif self.touche == "space":
                if len(self.joueurs.getName()) < 10:
                    self.joueurs.setName(str(self.joueurs.getName())+" ")
            else:
                if len(self.joueurs.getName()) > 0:
                    self.joueurs.setName(str(self.joueurs.getName())[:-1])


            tailles = self.parent.bbox(self.text)
            width = tailles[2] - tailles[0]
            if width > 300:
                self.parent.itemconfigure(self.text, text=self.joueurs.getName().upper(), font=('Lilita One', 30))

            else:
                self.parent.itemconfigure(self.text, text=self.joueurs.getName().upper(), font=('Lilita One', 40))
                tailles = self.parent.bbox(self.text)
                width = tailles[2] - tailles[0]
                if width > 300:
                    self.parent.itemconfigure(self.text, text=self.joueurs.getName().upper(), font=('Lilita One', 30))


    def boutonSwitchIA(self,event):
        """Méthode qui permet de faire apparaitre les types de l'ia du joueur
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        if self.boutonUser == "gris":
            self.joueurType = "ia"
            if self.stateactuel == 0:
                self.parent.itemconfigure(self.text_expert, state=tk.NORMAL)
                self.parent.itemconfigure(self.Noir_IA_3, state=tk.NORMAL)
                self.parent.itemconfigure(self.text_moyen, state=tk.NORMAL)
                self.parent.itemconfigure(self.Noir_IA_2, state=tk.NORMAL)
                self.parent.itemconfigure(self.text_facile, state=tk.NORMAL)
                self.parent.itemconfigure(self.Noir_IA_1, state=tk.NORMAL)
                self.stateactuel = 1
            else:
                self.hiddenAll()
                self.stateactuel = 0
        
        else:
            self.BoutonIA(event)
    
    def joueurEstIA(self):
        """Fonction qui permet de savoir si un joueur est unIA

        Args:
            self: l'utilisateur tout entier
        
        Returns:
            boolean: True = c'est une IA | False = c'est un joueur
        """
        if self.joueurType == "ia":
            return True
        return False

    def joueurEstJoueur(self):
        """Fonction qui permet de savoir si un joueur est un joueur

        Args:
            self: l'utilisateur tout entier
        
        Returns:
            boolean: True = c'est un joueur | False = c'est une IA
        """
        if self.joueurType == "joueur":
            return True
        return False


    def hiddenAll(self):
        """Méthode qui permet de cacher tout les types d'ia graphiquement
        
        Args:
            self: l'utilisateur tout entier
        """
        self.stateactuel = 0
        self.parent.itemconfigure(self.text_expert, state=tk.HIDDEN)
        self.parent.itemconfigure(self.Noir_IA_3, state=tk.HIDDEN)
        self.parent.itemconfigure(self.text_moyen, state=tk.HIDDEN)
        self.parent.itemconfigure(self.Noir_IA_2, state=tk.HIDDEN)
        self.parent.itemconfigure(self.text_facile, state=tk.HIDDEN)
        self.parent.itemconfigure(self.Noir_IA_1, state=tk.HIDDEN)   

    def facile(self,event):
        """Méthode qui permet de changer le type de l'ia et la couleur du text
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        self.iatype = "facile"
        self.parent.itemconfigure(self.text_facile, fill="#bbbbbb")

        self.parent.itemconfigure(self.text_moyen, fill="#ffffff")
        self.parent.itemconfigure(self.text_expert, fill="#ffffff")

    def moyen(self,event):
        """Méthode qui permet de changer le type de l'ia et la couleur du text
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        self.iatype = "moyen"
        self.parent.itemconfigure(self.text_moyen, fill="#bbbbbb")

        self.parent.itemconfigure(self.text_facile, fill="#ffffff")
        self.parent.itemconfigure(self.text_expert, fill="#ffffff")

    def expert(self,event):
        """Méthode qui permet de changer le type de l'ia et la couleur du text
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        self.iatype = "expert"
        self.parent.itemconfigure(self.text_expert, fill="#bbbbbb")

        self.parent.itemconfigure(self.text_moyen, fill="#ffffff")
        self.parent.itemconfigure(self.text_facile, fill="#ffffff")
    
    def getIAType(self):
        """Fonction qui permet de retourner sous forme d'STR le type de l'ia que le joueur a selectionné

        Args:
            self: l'utilisateur tout entier
        
        Returns:
            self.iatype: type de l'ia sous forme STR
        """
        return self.iatype
    

    def BoutonIA(self,event):
        """Méthode qui permet de créer un bouton IA ou Joueur à l'appui d'un des deux boutons

        Args:
            self (Player): joueur
            event: évènement du clique
        """
        self.parent.itemconfigure(self.Bouton_User, state=tk.HIDDEN)
        self.parent.itemconfigure(self.Bouton_Robot, state=tk.HIDDEN)
        self.hiddenAll()

        if self.boutonUser == "gris":
            self.Bouton_User = self.parent.create_image(self.uwidth,self.rheight,image=self.image_list[24])
            self.Bouton_Robot = self.parent.create_image(self.rwidth,self.rheight, image= self.image_list[20])
            self.boutonUser = "noir"
            self.joueurType = "joueur"
        else:
            self.Bouton_User = self.parent.create_image(self.uwidth,self.rheight,image=self.image_list[23])
            self.Bouton_Robot = self.parent.create_image(self.rwidth,self.rheight, image= self.image_list[21])
            self.boutonUser = "gris"
            self.joueurType = "ia"
        self.moverobot(self.x,self.y)
        self.parent.tag_bind(self.Bouton_User, "<Button-1>", self.BoutonIA)
        self.parent.tag_bind(self.Bouton_Robot, "<Button-1>", self.boutonSwitchIA)
        

if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyUser(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()