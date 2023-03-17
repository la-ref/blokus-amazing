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
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None


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

        self.modal_active = False
        self.canvas.place(x = 0, y = 0)
        self.canvas.bind("<Button-1>",self.clique)
        self.Arriere_plan = self.canvas.create_image(720.0,512.0,image= config.Config.image[14])

        self.Bouton_Jouer = self.canvas.create_image(719.0, 464.0,image= config.Config.image[17])
        self.canvas.tag_bind(self.Bouton_Jouer, "<Button-1>", self.jouer)
        self.canvas.tag_bind(self.Bouton_Jouer, "<Enter>",lambda *_: self.hoverBouton("entre","jouer",self.Bouton_Jouer))
        self.canvas.tag_bind(self.Bouton_Jouer, "<Leave>",lambda *_: self.hoverBouton("sort","jouer",self.Bouton_Jouer))


        self.Bouton_Quitter = self.canvas.create_image(717.0,577.0,image= config.Config.image[19])
        # self.canvas.tag_bind(self.Bouton_Quitter, "<Button-1>", self.QuitterBouton)
        self.canvas.tag_bind(self.Bouton_Quitter, "<Button-1>",lambda *_: self.create_modal())
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


        self.bouton_bleu = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[2],15,hb="bas",droiteg="droite")
        self.bouton_bleu.move(1156,883)
        self.namezone_bleu = self.bouton_bleu.getNameZone()
        self.namezone_bleu_text = self.bouton_bleu.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_bleu, "<Button-1>",lambda *_: self.Boutonselect("bleu"))
        self.canvas.tag_bind(self.namezone_bleu_text, "<Button-1>",lambda *_: self.Boutonselect("bleu"))

        self.bouton_rouge = lobbyUser.lobbyUser(self.window,self.canvas,config.Config.image,self.joueurs[3],22,hb="bas",droiteg="gauche")
        self.bouton_rouge.move(279,883)
        self.namezone_rouge = self.bouton_rouge.getNameZone()
        self.namezone_rouge_text = self.bouton_rouge.getNameZone_Text()
        self.canvas.tag_bind(self.namezone_rouge, "<Button-1>",lambda *_: self.Boutonselect("rouge"))
        self.canvas.tag_bind(self.namezone_rouge_text, "<Button-1>",lambda *_: self.Boutonselect("rouge"))


        BoutonInfo = self.canvas.create_image(
            (config.Config.largueur/2)-(config.Config.image[4].width()/2), 
            821, 
            image=config.Config.image[4],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(BoutonInfo, "<Enter>",lambda *_: self.hoverBouton("entre","info",BoutonInfo))
        self.canvas.tag_bind(BoutonInfo, "<Leave>",lambda *_: self.hoverBouton("sort","info",BoutonInfo))

        self.RegleFondBlokus = self.canvas.create_image(
            (config.Config.largueur/2)-config.Config.image[54].width()/2, 
            config.Config.hauteur/2-config.Config.image[54].height()/2, 
            image=config.Config.image[54],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(self.RegleFondBlokus, "<Button-1>", self.fermerRegle)

        self.RegleBlokus = self.canvas.create_image(
            (config.Config.largueur/2)-config.Config.image[52].width()/2, 
            config.Config.hauteur/2-config.Config.image[52].height()/2, 
            image=config.Config.image[52],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(BoutonInfo, "<Button-1>", self.infoBouton)
        self.canvas.itemconfigure(self.RegleBlokus,state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.RegleFondBlokus,state=tkinter.HIDDEN)
        
    def fermerRegle(self,event):
        """ Fonction qui permet le callback du bouton "Info" permettant de fermer les règles
        
        """
        if not self.hidden: # fermer les règles
            self.modal_active = False
            self.hidden = True
            self.canvas.itemconfigure(self.RegleBlokus,state=tkinter.HIDDEN)
            self.canvas.itemconfigure(self.RegleFondBlokus,state=tkinter.HIDDEN)
        if self.scrollable_frame:
            self.scrollable_frame.destroye()
            self.scrollable_frame.destroy()
            self.canvas.delete(self.windowRegle)
    
    def infoBouton(self,event):
        """Méthode pour permettre d'afficher les règles du jeu blokus et de crée une frame de scroll
        """
        if self.hidden: # afficher les règles
            self.modal_active = True
            self.hidden = False
            self.canvas.itemconfigure(self.RegleBlokus,state=tkinter.NORMAL)
            self.canvas.itemconfigure(self.RegleFondBlokus,state=tkinter.NORMAL)
            self.canvas.tag_raise(self.RegleFondBlokus)
            self.canvas.tag_raise(self.RegleBlokus)

            self.scrollable_frame = ScrollableFrame(self.canvas,config.Config.image[53])
            self.windowRegle = self.canvas.create_window(((config.Config.largueur/2)-1, 
            (config.Config.hauteur/2)-4),window=self.scrollable_frame)
            

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
        if self.modal_active == False:
            if len(event.widget.find_withtag('current')) > 0:
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
        config.Config.controller.game.start()
    
    def QuitterBouton(self):
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
            elif typ2 == "info":
                self.canvas.itemconfigure(idButton, image=config.Config.image[55])
                self.canvas.moveto(idButton,(((config.Config.largueur/2)-(config.Config.image[55].width()/2))),815)
                self.canvas.config(cursor="hand2")
        elif typ == "sort":
            if typ2 == "quitter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[19])
                self.canvas.config(cursor="")
            elif typ2 == "jouer":
                self.canvas.itemconfigure(idButton, image=config.Config.image[17])
                self.canvas.config(cursor="")
            elif typ2 == "info":
                self.canvas.itemconfigure(idButton, image=config.Config.image[4])
                self.canvas.moveto(idButton,((config.Config.largueur/2)-(config.Config.image[4].width()/2)),821)
                self.canvas.config(cursor="")


    """ Fonction permettant de créer un modal en fonction du paramètre reçu :
        paramètres valables : abandon, quitter.
    """
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

    """ Fonction permettant de détruire le modal actif
    """
    def remove_modal(self):
        self.canvas.delete(self.modal,self.modal_no,self.modal_yes,self.text_modal)


    """ Fonction callback de confirmation des modaux
    """
    def yes(self):
        self.remove_modal()
        self.QuitterBouton()
        self.modal_active = False
    
    """ Fonction callback d' infirmation des modaux
    """
    def no(self):
        self.remove_modal()
        self.modal_active = False


if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyLocal(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
