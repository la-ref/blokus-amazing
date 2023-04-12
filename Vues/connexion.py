from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
from Vues.ScrollableFrame import ScrollableFrame

class Connexion(Frame):
    """ Classe étant une frame réprésentant la page de connexion pour le lobby en ligne
    """
    def __init__(self,window):
        super(Connexion, self).__init__()
        self.window = window
        self.window.title("Blokus")
        self.window.wm_iconphoto(True, config.Config.image[47])
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None
        self.actuel_touche = ""
        self.activeclavier = False
        self.modal_active = False
        self.ip = ""
        self.port = ""
        self.pseudo = ""

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

        self.canvas.bind("<Button-1>",self.clique)
        background = self.canvas.create_image(
            720.0,
            512.0,
            image=config.Config.image[0]
        )
        
        
        self.entrerPseudo_image = self.canvas.create_image(
            362, 
            333, 
            image=config.Config.image[61],
            anchor=tkinter.NW
        )
        # self.canvas.tag_bind(entrerPseudo_image, "<Button-1>", self.Entrerpseudo)
        self.canvas.tag_bind(self.entrerPseudo_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerpseudo",self.entrerPseudo_image))
        self.canvas.tag_bind(self.entrerPseudo_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerpseudo",self.entrerPseudo_image))
        
        self.text_pseudo = self.canvas.create_text(362+(config.Config.image[61].width()/2),333+(config.Config.image[61].height()/2),fill="black",font=('Lilita One', config.Config.taillePolice[0]),text= (lambda : self.pseudo if self.pseudo else "Entrez votre pseudo")() ,anchor=tkinter.CENTER)
        # self.canvas.tag_bind(self.text_pseudo, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(self.text_pseudo, "<Enter>",lambda *_: self.hoverBouton("entre","entrerpseudo",self.entrerPseudo_image))
        self.canvas.tag_bind(self.text_pseudo, "<Leave>",lambda *_: self.hoverBouton("sort","entrerpseudo",self.entrerPseudo_image))
        
        self.entrerip_image = self.canvas.create_image(
            360, 
            455, 
            image=config.Config.image[60],
            anchor=tkinter.NW
        )
        # self.canvas.tag_bind(entrerip_image, "<Button-1>", self.Entrerip)
        self.canvas.tag_bind(self.entrerip_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerip",self.entrerip_image))
        self.canvas.tag_bind(self.entrerip_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerip",self.entrerip_image))

        self.text_ip = self.canvas.create_text(360+(config.Config.image[60].width()/2),455+(config.Config.image[60].height()/2),fill="black",font=('Lilita One', config.Config.taillePolice[0]),text="Adresse",anchor=tkinter.CENTER)
        # self.canvas.tag_bind(self.text_ip, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(self.text_ip, "<Enter>",lambda *_: self.hoverBouton("entre","entrerip",self.entrerip_image))
        self.canvas.tag_bind(self.text_ip, "<Leave>",lambda *_: self.hoverBouton("sort","entrerip",self.entrerip_image))
        

        self.entrerPort_image = self.canvas.create_image(
            810, 
            455, 
            image=config.Config.image[62],
            anchor=tkinter.NW
        )
        # self.canvas.tag_bind(entrerPort_image, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(self.entrerPort_image, "<Enter>",lambda *_: self.hoverBouton("entre","entrerport",self.entrerPort_image))
        self.canvas.tag_bind(self.entrerPort_image, "<Leave>",lambda *_: self.hoverBouton("sort","entrerport",self.entrerPort_image))
        
        self.text_port = self.canvas.create_text(810+(config.Config.image[62].width()/2),455+(config.Config.image[62].height()/2),fill="black",font=('Lilita One', config.Config.taillePolice[0]),text="Port",anchor=tkinter.CENTER)
        # self.canvas.tag_bind(self.text_port, "<Button-1>", self.Entrerport)
        self.canvas.tag_bind(self.text_port, "<Enter>",lambda *_: self.hoverBouton("entre","entrerport",self.entrerPort_image))
        self.canvas.tag_bind(self.text_port, "<Leave>",lambda *_: self.hoverBouton("sort","entrerport",self.entrerPort_image))
        

        self.Param_avance = self.canvas.create_image(
            514, 
            473, 
            image=config.Config.image[64],
            anchor=tkinter.NW,
            state=tkinter.HIDDEN
        )
        self.canvas.tag_bind(self.Param_avance, "<Button-1>", self.EntreAvance)
        self.canvas.tag_bind(self.Param_avance, "<Enter>",lambda *_: self.hoverBouton("entre","entreravance",self.Param_avance))
        self.canvas.tag_bind(self.Param_avance, "<Leave>",lambda *_: self.hoverBouton("sort","entreravance",self.Param_avance))

        self.Param_simplifie_img = self.canvas.create_image(
            514, 
            577, 
            image=config.Config.image[65],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(self.Param_simplifie_img, "<Button-1>", self.EntreSimplif)
        self.canvas.tag_bind(self.Param_simplifie_img, "<Enter>",lambda *_: self.hoverBouton("entre","entrersimplifie",self.Param_simplifie_img))
        self.canvas.tag_bind(self.Param_simplifie_img, "<Leave>",lambda *_: self.hoverBouton("sort","entrersimplifie",self.Param_simplifie_img))


        self.ConnecterBouton_img = self.canvas.create_image(
            411,
            737,
            image=config.Config.image[63],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(self.ConnecterBouton_img, "<Button-1>", self.ConnecterBouton)
        self.canvas.tag_bind(self.ConnecterBouton_img, "<Enter>",lambda *_: self.hoverBouton("entre","connecter",self.ConnecterBouton_img))
        self.canvas.tag_bind(self.ConnecterBouton_img, "<Leave>",lambda *_: self.hoverBouton("sort","connecter",self.ConnecterBouton_img))

        
        self.QuitterBouton_img = self.canvas.create_image(
            822, 
            769, 
            image=config.Config.image[7],
            anchor=tkinter.NW
        )
        self.canvas.tag_bind(self.QuitterBouton_img, "<Button-1>", self.QuitterBouton)
        self.canvas.tag_bind(self.QuitterBouton_img, "<Enter>",lambda *_: self.hoverBouton("entre","quitter",self.QuitterBouton_img))
        self.canvas.tag_bind(self.QuitterBouton_img, "<Leave>",lambda *_: self.hoverBouton("sort","quitter",self.QuitterBouton_img))

        self.canvas.itemconfigure(self.Param_simplifie_img, state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.Param_avance, state=tkinter.NORMAL)

        self.canvas.itemconfigure(self.text_ip, state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.text_port, state=tkinter.HIDDEN)

        self.canvas.itemconfigure(self.entrerip_image, state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.entrerPort_image, state=tkinter.HIDDEN)
        
    
    def clique(self,event):
        """ Méthode qui permet de vérifier le clic du joueur et d'activer la saisie ou non du clavier
        si le widget cliqué est le bon

        Args:
            event (x,y): Les coordonnées en X et Y du clic du joueur
        """
        if self.modal_active == False:
            if len(event.widget.find_withtag('current')) > 0:
                actuelwidget = event.widget.find_withtag('current')[0]
            if ((actuelwidget == 3) or (actuelwidget == 2)):
                self.Entrerpseudo()
            elif ((actuelwidget == 5) or (actuelwidget == 4)):
                self.Entrerip()
            elif ((actuelwidget == 7) or (actuelwidget == 6)):
                self.Entrerport()
            else:
                self.desactiverAll()
            

    def desactiverAll(self):
        """Méthode qui permet de réinitialiser la saisie du clavier (plus rien n'est sélectionné)
        
        Args:
            self: l'utilisateur tout entier
        """
        self.activeclavier = False
        self.actuel_touche = ""
        if self.port == "":
            self.canvas.itemconfigure(self.text_port, text="Port", font=('Lilita One', config.Config.taillePolice[0]))
        if self.ip == "":
            self.canvas.itemconfigure(self.text_ip, text="Adresse", font=('Lilita One', config.Config.taillePolice[0]))
        if self.pseudo == "":
            self.canvas.itemconfigure(self.text_pseudo, text="Entrez votre pseudo", font=('Lilita One', config.Config.taillePolice[0]))
        self.canvas.itemconfigure(self.entrerPseudo_image, image=config.Config.image[61])
        self.canvas.itemconfigure(self.entrerip_image, image=config.Config.image[60])
        self.canvas.itemconfigure(self.entrerPort_image, image=config.Config.image[62])

    def EntreAvance(self,event):
        """Méthode qui permet de se mettre en mode "avancé"
        
        Args:
            self: l'utilisateur tout entier
        """
        self.canvas.itemconfigure(self.Param_simplifie_img, state=tkinter.NORMAL)
        self.canvas.itemconfigure(self.Param_avance, state=tkinter.HIDDEN)

        self.canvas.itemconfigure(self.text_ip, state=tkinter.NORMAL)
        self.canvas.itemconfigure(self.text_port, state=tkinter.NORMAL)

        self.canvas.itemconfigure(self.entrerip_image, state=tkinter.NORMAL)
        self.canvas.itemconfigure(self.entrerPort_image, state=tkinter.NORMAL)
        self.desactiverAll()

    def EntreSimplif(self,event):
        """Méthode qui permet de se mettre en mode "simplifié"
        
        Args:
            self: l'utilisateur tout entier
        """
        self.canvas.itemconfigure(self.Param_simplifie_img, state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.Param_avance, state=tkinter.NORMAL)

        self.canvas.itemconfigure(self.text_ip, state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.text_port, state=tkinter.HIDDEN)

        self.canvas.itemconfigure(self.entrerip_image, state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.entrerPort_image, state=tkinter.HIDDEN)
        self.desactiverAll()

    def Entrerpseudo(self):
        """Méthode qui permet d'activer ou non la saisie du clavier sur le pseudo du joueur
        
        Args:
            self: l'utilisateur tout entier
        """
        if self.actuel_touche == "pseudo":
            if self.pseudo == "":
                self.canvas.itemconfigure(self.text_pseudo, text="Entrez votre pseudo", font=('Lilita One', config.Config.taillePolice[0]))
            self.activeclavier = False
            self.actuel_touche = ""
            self.canvas.itemconfigure(self.entrerPseudo_image, image=config.Config.image[61])
        else:
            self.canvas.itemconfigure(self.text_pseudo, text=self.pseudo, font=('Lilita One', config.Config.taillePolice[0]))
            if self.port == "":
                self.canvas.itemconfigure(self.text_port, text="Port", font=('Lilita One', config.Config.taillePolice[0]))
            self.canvas.itemconfigure(self.entrerPort_image, image=config.Config.image[62])
            if self.ip == "":
                self.canvas.itemconfigure(self.text_ip, text="Adresse", font=('Lilita One', config.Config.taillePolice[0]))
            self.canvas.itemconfigure(self.entrerip_image, image=config.Config.image[60])
            self.actuel_touche = "pseudo"
            self.activeclavier = True
            self.canvas.itemconfigure(self.entrerPseudo_image, image=config.Config.image[67])

    def Entrerip(self):
        """Méthode qui permet d'activer ou non la saisie du clavier sur l'ip
        
        Args:
            self: l'utilisateur tout entier
        """
        if self.actuel_touche == "ip":
            if self.ip == "":
                self.canvas.itemconfigure(self.text_ip, text="Adresse", font=('Lilita One', int(config.Config.taillePolice[0]//(((len(self.ip)//3)+4)*0.2))))
            self.activeclavier = False
            self.actuel_touche = ""
            self.canvas.itemconfigure(self.entrerip_image, image=config.Config.image[60])
        else:
            self.canvas.itemconfigure(self.text_ip, text=self.ip, font=('Lilita One', int(config.Config.taillePolice[0]//(((len(self.ip)//3)+4)*0.2))))
            if self.pseudo == "":
                self.canvas.itemconfigure(self.text_pseudo, text="Entrez votre pseudo", font=('Lilita One', config.Config.taillePolice[0]))
            self.canvas.itemconfigure(self.entrerPseudo_image, image=config.Config.image[61])
            if self.port == "":
                self.canvas.itemconfigure(self.text_port, text="Port", font=('Lilita One', config.Config.taillePolice[0]))
            self.canvas.itemconfigure(self.entrerPort_image, image=config.Config.image[62])
            self.actuel_touche = "ip"
            self.activeclavier = True
            self.canvas.itemconfigure(self.entrerip_image, image=config.Config.image[66])


    def Entrerport(self):
        """Méthode qui permet d'activer ou non la saisie du clavier sur le port
        
        Args:
            self: l'utilisateur tout entier
        """
        if self.actuel_touche == "port":
            if self.port == "":
                self.canvas.itemconfigure(self.text_port, text="Port", font=('Lilita One', config.Config.taillePolice[0]))
            self.activeclavier = False
            self.actuel_touche = ""
            self.canvas.itemconfigure(self.entrerPort_image, image=config.Config.image[62])
        else:
            self.canvas.itemconfigure(self.text_port, text=self.port, font=('Lilita One', config.Config.taillePolice[0]))
            if self.pseudo == "":
                self.canvas.itemconfigure(self.text_pseudo, text="Entrez votre pseudo", font=('Lilita One', config.Config.taillePolice[0]))
            self.canvas.itemconfigure(self.entrerPseudo_image, image=config.Config.image[61])
            if self.ip == "":
                self.canvas.itemconfigure(self.text_ip, text="Adresse", font=('Lilita One', config.Config.taillePolice[0]))
            self.canvas.itemconfigure(self.entrerip_image, image=config.Config.image[60])
            self.actuel_touche = "port"
            self.activeclavier = True
            self.canvas.itemconfigure(self.entrerPort_image, image=config.Config.image[68])

    def ConnecterBouton(self,event):
        """Méthode qui permet d'accéder au lobby en ligne
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        config.Config.controller.changeUserName(self.pseudo)
        if self.modal_active:
            config.Config.controller.setIPAndPort(self.ip,self.port)
        config.Config.controller.changePage("lobbyOnline")
    
    def touches(self,event):
        """Méthode qui actualise le pseudo, l'ip ou le port à chaque touche appuyé de l'ordinateur
        
        Args:
            self: l'utilisateur tout entier
            event: évènement du clique
        """
        self.touche = str(event.char)
        self.touchedetails = str(event.keysym)
        if self.activeclavier == True:
            if self.actuel_touche == "ip":
                if len(self.touche) >=1:
                    if len(self.ip) < 32:
                        self.ip = self.ip + "" +self.touche
                if self.touche == "space":
                    if len(self.ip) < 32:
                        self.ip = self.ip + " "
                if self.touchedetails.lower() == "backspace":
                    self.ip = self.ip[:-1]
                if len(self.ip) < 32:
                    self.canvas.itemconfigure(self.text_ip, text=self.ip, font=('Lilita One', int(config.Config.taillePolice[0]//(((len(self.ip)//3)+4)*0.2))))
            if self.actuel_touche == "port":
                if len(self.touche) == 1:
                    if ((str.isdigit(self.touche) and int(self.touche) >= 0) and (int(self.touche) < 10)):
                        if len(self.port) < 5:
                            self.port = self.port + "" + self.touche
                if self.touchedetails.lower() == "backspace":
                    self.port = self.port[:-1]
                self.canvas.itemconfigure(self.text_port, text=self.port, font=('Lilita One', config.Config.taillePolice[0]))
            if self.actuel_touche == "pseudo":
                if len(self.touche) >=1 and self.touche != "-" and self.touche != "_":
                    if len(self.pseudo) < 10:
                        self.pseudo = self.pseudo + "" +self.touche
                if self.touche == "space":
                    if len(self.pseudo) < 10:
                        self.pseudo = self.pseudo + " "
                if self.touchedetails.lower() == "backspace":
                    self.pseudo = self.pseudo[:-1]
                self.canvas.itemconfigure(self.text_pseudo, text=self.pseudo, font=('Lilita One', config.Config.taillePolice[0]))


    def hoverBouton(self,typ : str,typ2 : str,idButton : int):
        """ Méthode permettant de modifier l'image au survol de la souris sur l'objet

        Args:
            typ (str): "entre" ou "sort"
            typ2 (str): "jouer" ou "quitter"
            idButton (int): l'identifiant du bouton cliqué
        """
        if typ == "entre":
            if typ2 == "entrerpseudo":
                self.canvas.itemconfigure(idButton, image=config.Config.image[67])
                self.canvas.config(cursor="hand2")
            elif typ2 == "entrerip":
                self.canvas.itemconfigure(idButton, image=config.Config.image[66])
                self.canvas.config(cursor="hand2")
            elif typ2 == "entrerport":
                self.canvas.itemconfigure(idButton, image=config.Config.image[68])
                self.canvas.config(cursor="hand2")
            elif typ2 == "entreravance":
                self.canvas.itemconfigure(idButton, image=config.Config.image[70])
                self.canvas.config(cursor="hand2")
            elif typ2 == "entrersimplifie":
                self.canvas.itemconfigure(idButton, image=config.Config.image[71])
                self.canvas.config(cursor="hand2")
            elif typ2 == "connecter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[69])
                self.canvas.config(cursor="hand2")
            elif typ2 == "quitter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[72])
                self.canvas.config(cursor="hand2")
        elif typ == "sort":
            if typ2 == "entrerpseudo":
                self.canvas.config(cursor="")
                if self.actuel_touche != "pseudo":
                    self.canvas.itemconfigure(idButton, image=config.Config.image[61])
                    self.canvas.config(cursor="")
            elif typ2 == "entrerip":
                self.canvas.config(cursor="")
                if self.actuel_touche != "ip":
                    self.canvas.itemconfigure(idButton, image=config.Config.image[60])
                    self.canvas.config(cursor="")
            elif typ2 == "entrerport":
                self.canvas.config(cursor="")
                if self.actuel_touche != "port":
                    self.canvas.itemconfigure(idButton, image=config.Config.image[62])
                    self.canvas.config(cursor="")
            elif typ2 == "entreravance":
                self.canvas.itemconfigure(idButton, image=config.Config.image[64])
                self.canvas.config(cursor="")
            elif typ2 == "entrersimplifie":
                self.canvas.itemconfigure(idButton, image=config.Config.image[65])
                self.canvas.config(cursor="")
            elif typ2 == "connecter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[63])
                self.canvas.config(cursor="")
            elif typ2 == "quitter":
                self.canvas.itemconfigure(idButton, image=config.Config.image[7])
                self.canvas.config(cursor="")

    def QuitterBouton(self,event):
        """ Fonction qui permet le callback du bouton "Quitter"
        
        """
        config.Config.controller.changePage("Accueil")
        

        
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