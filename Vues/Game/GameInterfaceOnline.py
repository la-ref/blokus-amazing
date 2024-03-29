from __future__ import annotations
from tkinter import PhotoImage
import tkinter as tk
import Elements.Pieces.PiecesListGUI as PG
from PIL import ImageTk
from Vues.Game.GridInterfaceOnline import GridInterfaceOnline
from config import config
from Elements.Board import Board
import Vues.accueil as accueil 
from Vues.ScrollableFrame import ScrollableFrame


class GameInterfaceOnline(tk.Frame):
    """Classe qui est une frame étant la page de jeu régroupant les joueurs et les pièces ainsi que la grille de jeu de manière graphique 
    """
    def __init__(self : GameInterfaceOnline, window : tk.Misc):
        """Constructeur qui crée une page de jeu en fonction de la fenêtre de l'application

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
            window (tk.Misc): fenêtre principale de l'application
        """
        super(GameInterfaceOnline,self).__init__(window)
        self.window = window
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None
        self.surrendered = []
        
        
    def initialize(self : GameInterfaceOnline) -> None:
        """Méthode permettant d'initialiser la page de jeu avec le placement de la grille de jeu, liste des pièces des joueurs ainsi que les boutons d'abandon 
        et de leave
        voir : GridInterfaceOnline, PieceListGUI

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
        """
        for widgets in self.winfo_children():
            widgets.destroy()

        self.couleur : dict = {
            10:"#FFC700",
            11:"#32BF00",
            12:"#0045CC",
            13:"#BC0000"
        }
        
            
        self.border = tk.Canvas()
        self.information = self.border.create_text((config.Config.largueur/2),140,fill="black",font=('Lilita One', config.Config.taillePolice[0]),text="Initialisation de la partie en cours...",anchor=tk.CENTER)

        
        self.border.create_image(0,0,image=config.Config.image[26],anchor=tk.NW)

        self.border.config(bg="white")
        self.border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
        self.board = GridInterfaceOnline(self.border)
        self.board.move(x=720-270,y=512-270)
        
        self.myId = config.Config.controller.getOnlineId()
        
        self.List1 = PG.PiecesListGUI(self.window,self.border,config.Config.controller.getOnlinePlayerName(0),0)
        self.List1.move(x=70,y=80) # jaune

        self.List2 = PG.PiecesListGUI(self.window,self.border,config.Config.controller.getOnlinePlayerName(1),1)
        self.List2.move(x=1047,y=80) # vert

        self.List3 = PG.PiecesListGUI(self.window,self.border,config.Config.controller.getOnlinePlayerName(2),2)
        self.List3.move(x=1047,y=524) #  rouge

        self.List4 = PG.PiecesListGUI(self.window,self.border,config.Config.controller.getOnlinePlayerName(3),3)
        self.List4.move(x=70,y=524) #bleu

        

        self.giveUp = self.border.create_image(
            411, 
            845, 
            image=config.Config.image[6],
            anchor=tk.NW
        )
    
        self.border.tag_bind(self.giveUp, "<Button-1>",lambda *_: self.ceate_modal("abandon"))
        self.border.tag_bind(self.giveUp, "<Enter>",lambda *_: self.hoverSurrender("enter"))
        self.border.tag_bind(self.giveUp, "<Leave>",lambda *_: self.hoverSurrender("leave"))

        self.quitter = self.border.create_image(
            800, 
            845, 
            image=config.Config.image[7],
            anchor=tk.NW
        )
        self.border.tag_bind(self.quitter, "<Button-1>",lambda *_: self.ceate_modal("quitter"))
        self.border.tag_bind(self.quitter, "<Enter>",lambda *_: self.hoverLeave("enter"))
        self.border.tag_bind(self.quitter, "<Leave>",lambda *_: self.hoverLeave("leave"))

        BoutonInfo = self.border.create_image(
            690,
            852,
            image=config.Config.image[59],
            anchor=tk.NW
        )
        self.border.tag_bind(BoutonInfo, "<Enter>",lambda *_: self.hoverBouton("entre","info",BoutonInfo))
        self.border.tag_bind(BoutonInfo, "<Leave>",lambda *_: self.hoverBouton("sort","info",BoutonInfo))

        self.RegleFondBlokus = self.border.create_image(
            (config.Config.largueur/2)-config.Config.image[54].width()/2, 
            config.Config.hauteur/2-config.Config.image[54].height()/2, 
            image=config.Config.image[54],
            anchor=tk.NW
        )
        self.border.tag_bind(self.RegleFondBlokus, "<Button-1>", self.fermerRegle)

        self.RegleBlokus = self.border.create_image(
            (config.Config.largueur/2)-config.Config.image[52].width()/2, 
            config.Config.hauteur/2-config.Config.image[52].height()/2, 
            image=config.Config.image[52],
            anchor=tk.NW
        )
        self.border.tag_bind(BoutonInfo, "<Button-1>", self.infoBouton)
        self.border.itemconfigure(self.RegleBlokus,state=tk.HIDDEN)
        self.border.itemconfigure(self.RegleFondBlokus,state=tk.HIDDEN)
        
    def deletePieceOnline(self,pieceId,player):
        if player >= 0 and player <=3:
            if player == 0:
                self.List1.deletePieceOnline(pieceId,player)
            elif player == 1:
                self.List2.deletePieceOnline(pieceId,player)
            elif player == 2:
                self.List3.deletePieceOnline(pieceId,player)
            elif player == 3:
                self.List4.deletePieceOnline(pieceId,player)

    def fermerRegle(self,event):
        """ Fonction qui permet le callback du bouton "Info" permettant de fermer les règles
        
        """
        if not self.hidden: # fermer les règles
            self.hidden = True
            self.border.itemconfigure(self.RegleBlokus,state=tk.HIDDEN)
            self.border.itemconfigure(self.RegleFondBlokus,state=tk.HIDDEN)
        if self.scrollable_frame:
            self.scrollable_frame.destroye()
            self.scrollable_frame.destroy()
            self.border.delete(self.windowRegle)
    
    def infoBouton(self,event):
        """Méthode pour permettre d'afficher les règles du jeu blokus et de crée une frame de scroll
        """
        if self.hidden: # afficher les règles
            self.hidden = False
            self.border.itemconfigure(self.RegleBlokus,state=tk.NORMAL)
            self.border.itemconfigure(self.RegleFondBlokus,state=tk.NORMAL)
            self.scrollable_frame = ScrollableFrame(self.border,config.Config.image[53])
            self.windowRegle = self.border.create_window(((config.Config.largueur/2)-1, 
            (config.Config.hauteur/2)-4),window=self.scrollable_frame)
            

    def callBackGiveUp(self : GameInterfaceOnline) -> None:
        """Methode de callback qui a chaque joueur qui abandonne le controlleur sera prévenu pour faire enlever le joueur des joueurs non abandonnées

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
        """
        if config.Config.controller:
            config.Config.controller.surrender()

    def hoverSurrender(self : GameInterfaceOnline,typ : str) -> None:
        """Méthode permettant de modifier le bouton surrender bouton en fonction du hover de celui ci en quitter et entrer

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
            typ (str): évènement à prendre en compte : "entrer" ou "quitter" 
        """
        if typ == "enter":
            self.border.itemconfigure(self.giveUp, image=config.Config.image[27])
            self.border.config(cursor="hand2")
        elif typ == "leave":
            self.border.itemconfigure(self.giveUp, image=config.Config.image[6])
            self.border.config(cursor="")

    def hoverLeave(self : GameInterfaceOnline,typ : str) -> None:
        """Méthode permettant de modifier le bouton quitter bouton en fonction du hover de celui ci en quitter et entrer

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
            typ (str): évènement à prendre en compte : "entrer" ou "quitter" 
        """
        if typ == "enter":
            self.border.itemconfigure(self.quitter, image=config.Config.image[28])
            self.border.config(cursor="hand2")
        elif typ == "leave":
            self.border.itemconfigure(self.quitter, image=config.Config.image[7])
            self.border.config(cursor="")
    
    def hoverBouton(self,typ : str,typ2 : str,idButton : int):
        """ Méthode permettant de modifier l'image au survol de la souris sur l'objet

        Args:
            typ (str): "entre" ou "sort"
            typ2 (str): "jouer" ou "quitter"
            idButton (int): l'identifiant du bouton cliqué
        """
        if typ == "entre":
            if typ2 == "info":
                self.border.itemconfigure(idButton, image=config.Config.image[58])
                self.border.moveto(idButton,680,845)
                self.border.config(cursor="hand2")
        elif typ == "sort":
            if typ2 == "info":
                self.border.itemconfigure(idButton, image=config.Config.image[59])
                self.border.moveto(idButton,690,852)
                self.border.config(cursor="")
            
    def surrender(self : GameInterfaceOnline,player : int) -> None:
        """Méthode callback qui va être appeller par le controlleur pour permettre d'obtenir un joueur qui à abandonner
        et de graphiquement le modifier pour lui indiquer qu'il a abandonné

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
            player (int): id du joueur qui a abandonné
        """
        if player >= 0 and player <= 3:
            if player not in self.surrendered:
                self.surrendered.append(player)
            match player:
                case 0:
                    self.List1.surrender()
                case 1:
                    self.List2.surrender()
                case 2:
                    self.List3.surrender()
                case 3:
                    self.List4.surrender()

    def leave(self : GameInterfaceOnline) -> None:
        """Méthode callback qui permet quand on click sur le bouton de leave de quitter la page de jeu en informant le controlleur
        de changer la page

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
        """
        self.List1.remettrePiece_copy()
        self.List2.remettrePiece_copy()
        self.List3.remettrePiece_copy()
        self.List4.remettrePiece_copy()
        config.Config.controller.leaveOnline()

    def changeTextPartie(self, message : str, couleur : int) -> None:
        """ Méthode permettant de modifier le text affiché à l'écran. 

        Args:
            self (GameInterface) : GameInterface
            message (str) : Le message affiché 
        """
        self.border.itemconfig(self.information, text=message, fill=self.couleur[10+couleur])

    def refreshBoard(self : GameInterfaceOnline,plateau) -> None:
        """Méthode callback pour GridInterfaceOnline qui le met à jour permettant 
        d'afficher l'ensemble des pièces présentes sur un plateau directement graphiquement sur la grille

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
            plateau (Board): plateau de jeu à afficher
        """
        self.board.refreshBoard(plateau)

    def refreshPlayer(self : GameInterfaceOnline,idPlayer : int,affiche : bool, pseudo :str) -> None:
        """Méthode callback pour GridInterfaceOnline qui le met à jour permettant 
        de mettre à jour le joueur courant et de l'afficher graphiquement au tour de la grille

        Args:
            self (GameInterfaceOnline): GameInterfaceOnline
            couleur (int): couleur du joueur courant
            affiche (bool): vrai s'il faut l'afficher sinon faux, en cas de victoire pour ne plus l'afficher
        """
        self.board.refreshPlayer(idPlayer,affiche)
        self.changeTextPartie("C'est à " + pseudo + " de jouer",idPlayer)

    
    def partieTermine(self, listPlayer):
        self.border.create_image(
            0, 
            0, 
            image=config.Config.image[46],
            anchor=tk.NW
        )
        
        if len(listPlayer)==1:
            self.text_winners = self.border.create_text(config.Config.largueur/2,(config.Config.hauteur/2)-config.Config.taillePolice[0]/2,text="Le gagnant de la partie est : \n"+listPlayer[0]+"\nBravo ! ",fill="#000000",font=("Lilita One", config.Config.taillePolice[0]),anchor=tk.CENTER,justify='center')
        else:
            winStr = "Les gagnants de la partie sont :\n"
            for pl in listPlayer:
                winStr+=pl+", "
            self.text_winners = self.border.create_text(config.Config.largueur/2,(config.Config.hauteur/2)-config.Config.taillePolice[0],text=winStr+"\nBravo ! ",fill="#000000",font=("Lilita One", config.Config.taillePolice[1]),anchor=tk.CENTER,justify='center')
        
        self.border.tag_raise(self.quitter)

    def ceate_modal(self,type):
        self.modal = self.border.create_image(
            0, 
            0, 
            image=config.Config.image[46],
            anchor=tk.NW
        )

        self.modal_no = self.border.create_image(
            config.Config.largueur/2-372,
            config.Config.hauteur/2+25,
            image=config.Config.image[56],
            anchor=tk.NW
        )

        self.modal_yes =self.border.create_image(
            config.Config.largueur/2+100,
            config.Config.hauteur/2+25,
            image=config.Config.image[57],
            anchor=tk.NW
        )

        if type == "abandon":
            self.border.tag_bind(self.modal_yes, "<Button-1>",lambda *_: self.yes("abandon"))
            self.border.tag_bind(self.modal_no, "<Button-1>", self.no)
            self.text_modal = self.border.create_text(config.Config.largueur/2,(config.Config.hauteur/2)-config.Config.taillePolice[0]/2-25,text="Êtes vous sûr de vouloir abandonner ?",fill="#000000",font=("Lilita One", config.Config.taillePolice[0]),anchor=tk.CENTER,justify='center')
        
        if type == "quitter":
            self.border.tag_bind(self.modal_yes, "<Button-1>",lambda *_: self.yes("quitter"))
            self.border.tag_bind(self.modal_no, "<Button-1>", self.no)
            self.text_modal = self.border.create_text(config.Config.largueur/2,(config.Config.hauteur/2)-config.Config.taillePolice[0]/2-25,text="Êtes vous sûr de vouloir quitter ?",fill="#000000",font=("Lilita One", config.Config.taillePolice[0]),anchor=tk.CENTER,justify='center')
        


    def remove_modal(self):
        self.border.delete(self.modal,self.modal_no,self.modal_yes,self.text_modal)

    def yes(self,type):
        self.remove_modal()
        if type == "abandon":
            self.callBackGiveUp()
        if type == "quitter":
            self.leave()
    
    def no(self,event):
        self.remove_modal()
        



if __name__=="__main__":

    window = tk.Tk()
    window.geometry("1440x1024")
    
    accueil=GameInterfaceOnline(window)
    accueil.pack()


    window.mainloop()