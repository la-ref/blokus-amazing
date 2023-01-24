from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
from Vues.ScrollableFrame import ScrollableFrame

class Connexion(Frame):
    """ Classe étant une frame réprésentant la page d'acceuil
    """
    def __init__(self,window):
        super(Connexion, self).__init__()
        self.window = window
        self.window.title("Blokus")
        self.window.wm_iconphoto(True, config.Config.image[47])
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None

    def initialize(self):
        """ Fonction qui initialise la page de Connexion
        """
        for widgets in self.winfo_children():
            widgets.destroy()
        
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
        background = self.canvas.create_image(
            720.0,
            512.0,
            image=config.Config.image[0]
        )
        
        
        entrerPseudo_image = self.canvas.create_image(
            362, 
            333, 
            image=config.Config.image[61],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(entrerPseudo_image, "<Button-1>", self.Entrerpseudo)
        self.canvas.tag_bind(entrerPseudo_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerpseudo",entrerPseudo_image))
        self.canvas.tag_bind(entrerPseudo_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerpseudo",entrerPseudo_image))
        
        self.text_pseudo = self.canvas.create_text(362+(362/2),333,fill="black",font=('Lilita One', config.Config.taillePolice[0]),text="",anchor=tkinter.CENTER)
        self.canvas.tag_bind(self.text_pseudo, "<Button-1>", self.boutonChangerText_pseudo)
        self.canvas.tag_bind(self.text_pseudo, "<Enter>",lambda *_: self.hoverBouton("entre","entrerpseudo",self.entrerPseudo_image))
        self.canvas.tag_bind(self.text_pseudo, "<Leave>",lambda *_: self.hoverBouton("sort","entrerpseudo",self.entrerPseudo_image))
        
        entrerip_image = self.canvas.create_image(
            360, 
            455, 
            image=config.Config.image[60],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(entrerip_image, "<Button-1>", self.Entrerip)
        self.canvas.tag_bind(entrerip_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerip",entrerip_image))
        self.canvas.tag_bind(entrerip_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerip",entrerip_image))

        entrerPort_image = self.canvas.create_image(
            810, 
            455, 
            image=config.Config.image[62],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(entrerPort_image, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(entrerPort_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerport",entrerPort_image))
        self.canvas.tag_bind(entrerPort_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerport",entrerPort_image))

        Param_avance = self.canvas.create_image(
            514, 
            473, 
            image=config.Config.image[64],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(Param_avance, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(Param_avance, "<Enter>",lambda *_: self.hoverBouton("entre","entrerport",Param_avance))
        self.canvas.tag_bind(Param_avance, "<Leave>",lambda *_: self.hoverBouton("sort","entrerport",Param_avance))

        Param_simplifie = self.canvas.create_image(
            514, 
            577, 
            image=config.Config.image[65],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(Param_simplifie, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(Param_simplifie, "<Enter>",lambda *_: self.hoverBouton("entre","entrerport",Param_simplifie))
        self.canvas.tag_bind(Param_simplifie, "<Leave>",lambda *_: self.hoverBouton("sort","entrerport",Param_simplifie))


        ConnecterBouton = self.canvas.create_image(
            411,
            737,
            image=config.Config.image[63],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(ConnecterBouton, "<Button-1>", self.ConnecterBouton)
        self.canvas.tag_bind(ConnecterBouton, "<Enter>",lambda *_: self.hoverBouton("entre","connecter",ConnecterBouton))
        self.canvas.tag_bind(ConnecterBouton, "<Leave>",lambda *_: self.hoverBouton("sort","connecter",ConnecterBouton))

        
        QuitterBouton = self.canvas.create_image(
            822, 
            769, 
            image=config.Config.image[7],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(QuitterBouton, "<Button-1>", self.QuitterBouton)
        self.canvas.tag_bind(QuitterBouton, "<Enter>",lambda *_: self.hoverBouton("entre","quitter",QuitterBouton))
        self.canvas.tag_bind(QuitterBouton, "<Leave>",lambda *_: self.hoverBouton("sort","quitter",QuitterBouton))
        self.actuel_touche = ""
        self.activeclavier = False
        self.ip = ""
        self.port = ""
        self.pseudo = ""
    
    def Entrerpseudo(self,event):
        self.actuel_touche = "pseudo"
        self.activeclavier = True
        print("okkkkk pseudo")

    def Entrerip(self,event):
        self.actuel_touche = "ip"
        self.activeclavier = True

    def Entrerport(self,event):
        self.actuel_touche = "port"
        self.activeclavier = True

    def ConnecterBouton(self,event):
        pass


    # def clique(self,event):
    #     """ Méthode qui permet de vérifier le clic du joueur et d'activer la saisie ou non du clavier
    #     si le widget cliqué est le bon

    #     Args:
    #         event (x,y): Les coordonnées en X et Y du clic du joueur
    #     """
    #     if self.modal_active == False:
    #         if len(event.widget.find_withtag('current')) > 0:
    #             actuelwidget = event.widget.find_withtag('current')[0]
    #         if self.bouton_jaune.getActiveClavier() == True:
    #             if (actuelwidget != 5) and (actuelwidget != 4):
    #                 self.bouton_jaune.setActiveClavier(False)
    #         if self.bouton_vert.getActiveClavier() == True:
    #             if (actuelwidget != 15) and (actuelwidget != 14):
    #                 self.bouton_vert.setActiveClavier(False)
    #         if self.bouton_rouge.getActiveClavier() == True:
    #             if (actuelwidget != 25) and (actuelwidget != 24):
    #                 self.bouton_rouge.setActiveClavier(False)
    #         if self.bouton_bleu.getActiveClavier() == True:
    #             if (actuelwidget != 35) and (actuelwidget != 34):
    #                 self.bouton_bleu.setActiveClavier(False)
    def boutonChangerText_pseudo(self,event):
        """Méthode qui est relié au bouton et qui permet d'activer ou non la saisie pour cette utilisateur

        Args:
            self: l'utilisateur tout entier
        """
        if self.activeclavier == True:
            self.activeclavier = False
            # self.canvas.itemconfigure(self.nameZone, image=config.Config.image[self.nb_player])
        else:
            self.activeclavier = True  
            # self.canvas.itemconfigure(self.nameZone, image=config.Config.image[self.nb_player_hover])
    
    def touches(self,event):
        """Méthode qui actualise le pseudo du joueur à chaque touche appuyé de l'ordinateur
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        self.touche = str(event.keysym)
        print(self.touche)
        if self.activeclavier == True:
            if self.actuel_touche == "pseudo":
                if len(self.pseudo) < 14:
                    if len(self.touche) == 1:
                        if ((int(self.touche) >= 0) and (int(self.touche) < 10)):
                            if ((self.pseudo[:-1] != ".") and (self.pseudo[:-2] != ".") and (self.pseudo[:-3] != ".") and (self.pseudo[:-4] == ".")):
                                self.pseudo = self.pseudo + "" + self.touche
                            elif ((self.pseudo[:-1] != ".") and (self.pseudo[:-2] != ".") and (self.pseudo[:-3] == ".")):
                                self.pseudo = self.pseudo + "" + self.touche
                            elif ((self.pseudo[:-1] != ".") and (self.pseudo[:-2] == ".")):
                                self.pseudo = self.pseudo + "" + self.touche
                            elif ((self.pseudo[:-1] != ".") and (self.pseudo[:-2] == "")):
                                self.pseudo = self.pseudo + "" + self.touche
                            elif (len(self.pseudo) < 1):
                                self.pseudo = self.pseudo + "" + self.touche 
                            elif (len(self.pseudo) == 1):
                                if self.pseudo != ".":
                                    self.pseudo = self.pseudo + "" + self.touche 
                            elif (self.pseudo[:-1] == "."):
                                self.pseudo = self.pseudo + "" + self.touche 
                    elif self.touche == "space":
                        self.pseudo = self.pseudo + " "
                    elif "shift" in self.touche.lower():
                        pass
                    elif "period" in self.touche:
                        if (self.pseudo[:-1] != "."):
                            self.pseudo = self.pseudo + "."
                    else:
                        if len(self.pseudo) > 0:
                            self.pseudo = self.pseudo[:-1]
                    self.canvas.itemconfigure(self.text_pseudo, text=self.pseudo, font=('Lilita One', config.Config.taillePolice[0]))
            #     if len(self.joueurs.getName()) < 10:
            #         self.joueurs.setName(str(self.joueurs.getName()+self.touche))
            # elif self.touche == "space":
            #     if len(self.joueurs.getName()) < 10:
            #         self.joueurs.setName(str(self.joueurs.getName())+" ")
            # else:
            #     if len(self.joueurs.getName()) > 0:
            #         self.joueurs.setName(str(self.joueurs.getName())[:-1])


            # tailles = self.parent.bbox(self.text)
            # width = tailles[2] - tailles[0]
            # if width > 300:
            #     self.parent.itemconfigure(self.text, text=self.joueurs.getName(), font=('Lilita One', config.Config.taillePolice[2]))

            # else:
            #     self.parent.itemconfigure(self.text, text=self.joueurs.getName(), font=('Lilita One', config.Config.taillePolice[0]))
            #     tailles = self.parent.bbox(self.text)
            #     width = tailles[2] - tailles[0]
            #     if width > 300:
            #         self.parent.itemconfigure(self.text, text=self.joueurs.getName(), font=('Lilita One', config.Config.taillePolice[2]))

            # config.Config.controller.changePlayer(self.joueurs)


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
        
        
        
        

if __name__ == "__main__":
    from config import config
    from Controller.Controller import Controller
    window = Tk(className='Connexion')

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    config.initialisation(None)
    image = config.Config.image

    MonAccueil = Connexion(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()