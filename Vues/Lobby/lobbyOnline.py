from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
import tkinter as tk
import Elements.Player as Player
import Vues.Lobby.lobbyUserOnline as lobbyUser
from Vues.accueil import *
from Vues.Game.GameInterface import GameInterface

class lobbyOnline(Frame):
    def __init__(self,window):
        super(lobbyOnline, self).__init__()
        self.window = window


    def initialize(self):
        """ Fonction qui initialise le lobby Online
        """
        for widgets in self.winfo_children():
            widgets.unbind('<ButtonPress-1>')
            widgets.destroy()
        self.boutonUser = []
        self.activeclavier = False
        self.admin = False
        self.touche = None
        self.currentPlayerID = 0
        self.joueurs = ["","","",""]
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
        self.refreshAdmin()


        self.Bouton_Quitter = self.canvas.create_image(717.0,577.0,image= config.Config.image[19])
        self.canvas.tag_bind(self.Bouton_Quitter, "<Button-1>", self.QuitterBouton)
        self.canvas.tag_bind(self.Bouton_Quitter, "<Enter>",lambda *_: self.hoverBouton("entre","quitter",self.Bouton_Quitter))
        self.canvas.tag_bind(self.Bouton_Quitter, "<Leave>",lambda *_: self.hoverBouton("sort","quitter",self.Bouton_Quitter))


        self.bouton_jaune = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[0],0,16,hb="haut",droiteg="gauche",edit= (lambda: True if self.currentPlayerID == 0 else False)())
        self.bouton_jaune.move(279,147)
        self.namezone_jaune = self.bouton_jaune.getNameZone()
        self.namezone_jaune_text = self.bouton_jaune.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_jaune, "<Button-1>",lambda *_: self.Boutonselect(0))
        self.canvas.tag_bind(self.namezone_jaune_text, "<Button-1>",lambda *_: self.Boutonselect(0))


        self.bouton_vert = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[1],1,25,hb="haut",droiteg="droite",edit= (lambda: True if self.currentPlayerID == 1 else False)())
        self.bouton_vert.move(1156,147)
        self.namezone_vert = self.bouton_vert.getNameZone()
        self.namezone_vert_text = self.bouton_vert.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_vert, "<Button-1>",lambda *_: self.Boutonselect(1))
        self.canvas.tag_bind(self.namezone_vert_text, "<Button-1>",lambda *_: self.Boutonselect(1))


        self.bouton_bleu = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[3],3,22,hb="bas",droiteg="gauche",edit= (lambda: True if self.currentPlayerID == 3 else False)())
        self.bouton_bleu.move(279,883)
        self.namezone_rouge = self.bouton_bleu.getNameZone()
        self.namezone_rouge_text = self.bouton_bleu.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_rouge, "<Button-1>",lambda *_: self.Boutonselect(2))
        self.canvas.tag_bind(self.namezone_rouge_text, "<Button-1>",lambda *_: self.Boutonselect(2))


        self.bouton_rouge = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[2],2,15,hb="bas",droiteg="droite",edit= (lambda: True if self.currentPlayerID == 2 else False)())
        self.bouton_rouge.move(1156,883)
        self.namezone_bleu = self.bouton_rouge.getNameZone()
        self.namezone_bleu_text = self.bouton_rouge.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_bleu, "<Button-1>",lambda *_: self.Boutonselect(3))
        self.canvas.tag_bind(self.namezone_bleu_text, "<Button-1>",lambda *_: self.Boutonselect(3))

    def getUserName(self):
        return self.joueurs[self.currentPlayerID]
    def changeUserName(self,id,name):
        if id == 0:
            self.bouton_jaune.changeName(name)
        elif id == 1:
            self.bouton_vert.changeName(name)
        elif id == 2:
            self.bouton_rouge.changeName(name)
        elif id == 3:
            self.bouton_bleu.changeName(name)
            
    def iaButtons(self,k,val,val2):
        if k == 0:
            self.bouton_jaune.showIAButtons(val,val2)
        if k == 1:
            self.bouton_vert.showIAButtons(val,val2)
        if k == 2:
            self.bouton_rouge.showIAButtons(val,val2)
        if k == 3:
            self.bouton_bleu.showIAButtons(val,val2)
            
    def changeUserNames(self,userList):
        for i in range(4):
            self.changeUserName(i,"IA-"+str(i))
            self.iaButtons(i, self.currentPlayerID == i,self.admin)
        for k,v in userList.items():
            self.changeUserName(k,v)
            self.iaButtons(k,False,False)
            
    def changeCurrentPlayer(self ,id):
        if id >= 0 and id < 4:
            self.currentPlayerID = id
            
    def refreshAdmin(self):
        if self.admin:
            self.canvas.itemconfigure(self.Bouton_Jouer,state=tk.NORMAL)
        else:
            self.canvas.itemconfigure(self.Bouton_Jouer,state=tk.HIDDEN)
            
    def giveAdmin(self,id):
        if self.currentPlayerID == id:
            self.admin = True
        else:
            self.admin = False
        
            
        # self.bouton_jaune.showIAButtons(self.currentPlayerID == 0,self.admin)
        # self.bouton_vert.showIAButtons(self.currentPlayerID == 1,self.admin)
        # self.bouton_bleu.showIAButtons(self.currentPlayerID == 2,self.admin)
        # self.bouton_rouge.showIAButtons(self.currentPlayerID == 3,self.admin)
        self.refreshAdmin()
            
    

    def Boutonselect(self, typ):
        if typ == 3 and self.currentPlayerID == 3:
            self.bouton_bleu.setActiveClavier(True)
        else:
            self.bouton_bleu.setActiveClavier(False)
        if typ == 2 and self.currentPlayerID == 2:
            self.bouton_jaune.setActiveClavier(True)
        else:
            self.bouton_jaune.setActiveClavier(False)
        if typ == 1 and self.currentPlayerID == 1:
            self.bouton_vert.setActiveClavier(True)
        else:
            self.bouton_vert.setActiveClavier(False)
        if typ == 0 and self.currentPlayerID == 0:
            self.bouton_rouge.setActiveClavier(True)
        else:
            self.bouton_rouge.setActiveClavier(False)

    def clique(self,event):
        actuelwidget = event.widget.find_withtag('current')[0]
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
        if self.currentPlayerID == 3:
            self.bouton_bleu.touches(event)
        if self.currentPlayerID == 0:
            self.bouton_rouge.touches(event)
        if self.currentPlayerID == 2:
            self.bouton_jaune.touches(event)
        if self.currentPlayerID == 1:
            self.bouton_vert.touches(event)

    def jouer(self,event):
        if self.admin:
            config.Config.controller.launchOnlineGame()
        #from Elements.Game import Game
        # config.Config.controller.game = Game(self.joueurs,None,20)
        # # self.window = GameInterface(self.window)
        # config.Config.controller.changePage("GameInterface")
    
    def QuitterBouton(self,event):
        config.Config.controller.leaveOnline()

    def hoverBouton(self,typ : str,typ2 : str,idButton : int):
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