from __future__ import annotations
import tkinter as tk
import Elements.Pieces.PiecesListGUI as PG
from config import config
from Elements.Board import Board
from HighScore.fonctionJson import fonctionJson
from Vues.Game.GridInterface import GridInterface
from HighScore.Leaderboard import *
from config import config
from Elements.Pieces.PiecesDeclaration import LISTEPIECES
from Elements.Game import Game

class LeaderboardInterface(tk.Frame):
    """ 
    """
    def __init__(self,window):
        """ 


        """
        super(LeaderboardInterface,self).__init__()
        self.window = window
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None
        
        
        
    def initialize(self, nbgame = 1):
        """ Initialisation de la partie
        """

        self.border = tk.Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.changePrecSuiv(nbgame)
    
    def changePrecSuiv(self, nbgame = 1):
        children = self.border.find_all()  # Obtenir les ID de tous les objets enfants
        for child in children:
            self.border.delete(child)
        self.retour = self.border.create_image(719.0, 875.0,image= config.Config.image[74])
        self.border.tag_bind(self.retour, "<Button-1>",lambda *_: self.create_modal())
        self.border.tag_bind(self.retour, "<Enter>",lambda *_: self.hoverBouton2("entre","retour",self.retour))
        self.border.tag_bind(self.retour, "<Leave>",lambda *_: self.hoverBouton2("sort","retour",self.retour))
        
        self.fleche_droite = self.border.create_image(935.0, 875.0,image= config.Config.image[75])
        self.border.tag_bind(self.fleche_droite, "<Button-1>",lambda *_: self.suivant())
        self.border.tag_bind(self.fleche_droite, "<Enter>",lambda *_: self.hoverBouton2("entre","droite",self.fleche_droite))
        self.border.tag_bind(self.fleche_droite, "<Leave>",lambda *_: self.hoverBouton2("sort","droite",self.fleche_droite))

        self.fleche_gauche = self.border.create_image(500.0, 875.0,image= config.Config.image[76])
        self.border.tag_bind(self.fleche_gauche, "<Button-1>",lambda *_: self.precedent())
        self.border.tag_bind(self.fleche_gauche, "<Enter>",lambda *_: self.hoverBouton2("entre","gauche",self.fleche_gauche))
        self.border.tag_bind(self.fleche_gauche, "<Leave>",lambda *_: self.hoverBouton2("sort","gauche",self.fleche_gauche))
        self.nbgame = nbgame
        self.json = fonctionJson()
        self.joueurs = self.json.getPlayers("Game"+str(self.nbgame))
        self.createPieces(self.joueurs)
        self.border.tkraise(self.fleche_droite)
        self.border.tkraise(self.fleche_gauche)
        self.border.tkraise(self.retour)


        
        
        
        
    def Retour(self):
        """ Méthode permettant de revenir à la page d'Accueil
        """
        config.Config.controller.changePage("Accueil")
        
    def createPieces(self,joueurs):
        
        
        
        self.joueurs = joueurs
        config.Config.controller.game = Game(self.joueurs,None,20)
        
        # config.Config.controller.game.start()
        self.border.create_image(0,0,image=config.Config.image[26],anchor=tk.NW)

        self.border.config(bg="white")
        self.border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
        self.board = GridInterface(self.border,config.Config.controller.getBoard())
        self.board.move(x=720-270,y=512-270)
        config.Config.controller.changeState("Leaderboard")
        self.Lists=[]
        self.Lists.append(PG.PiecesListGUI(self.window,self.border,config.Config.controller.getGame().getPlayers()[0].getName(),0))
        self.Lists[0].move(x=70,y=80) # jaune

        self.Lists.append(PG.PiecesListGUI(self.window,self.border,config.Config.controller.getGame().getPlayers()[1].getName(),1))
        self.Lists[1].move(x=1047,y=80) # vert

        self.Lists.append(PG.PiecesListGUI(self.window,self.border,config.Config.controller.getGame().getPlayers()[2].getName(),2))
        self.Lists[2].move(x=1047,y=524) #  rouge

        self.Lists.append(PG.PiecesListGUI(self.window,self.border,config.Config.controller.getGame().getPlayers()[3].getName(),3))
        self.Lists[3].move(x=70,y=524)
        self.board : Board = config.Config.controller.getBoard()
        self.pieces = []
        for i in range(self.board.getBoardSize()):
            for y in range(self.board.getBoardSize()):
                valeur : int|None = self.board.getColorAt(i,y)
                if valeur:
                    piece = config.Config.image[valeur+47]
                    if ((i,y) not in self.pieces):
                        self.border.tag_lower(self.parent.create_image(463+y*(piece.width()),255+i*(piece.height()),image=piece))
                        self.pieces.append((i,y))
        for widgets in self.winfo_children():
            widgets.unbind('<ButtonPress-1>')
            widgets.destroy()
        self.boutonUser = []
        self.activeclavier = False

        self.touche = None
        self.modal_active = False
        

        listPlayer = self.json.getWinners("Game"+str(self.nbgame))
        if len(listPlayer)==1:
            self.text_winners = self.border.create_text(config.Config.largueur/2,150,text="Le gagnant de la partie est : \n"+listPlayer[0]+"\nBravo ! ",fill="#000000",font=("Lilita One", config.Config.taillePolice[0]),anchor=tk.CENTER,justify='center')
        else:
            winStr = "Les gagnants de la partie sont :\n"
            for pl in listPlayer:
                winStr+=pl+", "
            self.text_winners = self.border.create_text(config.Config.largueur/2,150,text=winStr+"\nBravo ! ",fill="#000000",font=("Lilita One", config.Config.taillePolice[1]),anchor=tk.CENTER,justify='center')

        # Récupération des informations de la partie
        self.pieces, self.joueurs, self.tableau = self.json.getPieces("Game"+str(self.nbgame))
        

        # Ajout des pièces dans le plateau
        for x in range(len(self.tableau)):
            for y in range(len(self.tableau[0])):
                self.board.ajoutCouleur(x,y,self.tableau[x][y])
            # for dec in np.argwhere(self.pieces[i].getDelimitation()==3):
            #     print(self.board.ajouterPiece(self.pieces[i],int(self.positions[i][0]),int(self.positions[i][1]),self.joueurs[i],int(dec[1]),int(dec[0])))

        # Affichage des pièces
        for i in range(self.board.getBoardSize()):
            for y in range(self.board.getBoardSize()):
                valeur : int|None = self.board.getColorAt(i,y)
                if valeur:
                    piece = config.Config.image[valeur+47]
                    self.border.tag_lower(self.border.create_image(463+y*(piece.width()),255+i*(piece.height()),image=piece))

    def refreshBoard(self,plateau : Board) -> None:
        """Méthode callback pour GridInterface qui le met à jour permettant 
        d'afficher l'ensemble des pièces présentes sur un plateau directement graphiquement sur la grille

        Args:
            self (GameInterface): GameInterface
            plateau (Board): plateau de jeu à afficher
        """
        pass
    def refreshPlayer(self,couleur : int,affiche : bool) -> None:
        """Méthode callback pour GridInterface qui le met à jour permettant 
        de mettre à jour le joueur courant et de l'afficher graphiquement au tour de la grille

        Args:
            self (GameInterface): GameInterface
            couleur (int): couleur du joueur courant
            affiche (bool): vrai s'il faut l'afficher sinon faux, en cas de victoire pour ne plus l'afficher
        """
        pass

    def create_modal(self):
        self.modal_active = True
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
        
        self.border.tag_bind(self.modal_yes, "<Button-1>",lambda *_: self.yes())
        self.border.tag_bind(self.modal_no, "<Button-1>",lambda *_: self.no())
        self.text_modal = self.border.create_text(config.Config.largueur/2,(config.Config.hauteur/2)-config.Config.taillePolice[0]/2-25,text="Êtes vous sûr de vouloir quitter ?",fill="#000000",font=("Lilita One", config.Config.taillePolice[0]),anchor=tk.CENTER,justify='center')
        self.modal_active = True

    

    def suivant(self):
        """ Méthode permettant de passer à la parite suivante
        
        """
        
        if self.json.getNbGames() == self.nbgame:
            self.nbgame = 1
        else:
            self.nbgame += 1
        self.changePrecSuiv(self.nbgame)
        

    def precedent(self):
        """ Méthode permettant de passer à la partie précédente

        """
        if self.nbgame-1 <= 0:
            self.nbgame = self.json.getNbGames()
        else:
            self.nbgame -= 1
        self.changePrecSuiv(self.nbgame)

    """ Fonction permettant de détruire le modal actif """
   
    def remove_modal(self):
        self.border.delete(self.modal,self.modal_no,self.modal_yes,self.text_modal)


    """ Fonction callback de confirmation des modaux
    """
    def yes(self):
        self.remove_modal()
        self.Retour()
        self.modal_active = False
    
    """ Fonction callback d' infirmation des modaux
    """
    def no(self):
        self.remove_modal()
        self.modal_active = False

    def hoverBouton2(self,typ : str,typ2 : str,idButton : int):
        """ Méthode permettant de modifier l'image au survol de la souris sur l'objet

        Args:
            typ (str): "entre" ou "sort"
            typ2 (str): "jouer" ou "quitter"
            idButton (int): l'identifiant du bouton cliqué
        """
        if typ == "entre":
            if typ2 == "retour":
                self.border.itemconfigure(idButton, image=config.Config.image[77])
                self.border.config(cursor="hand2")
            elif typ2 == "droite":
                self.border.itemconfigure(idButton, image=config.Config.image[78])
                self.border.config(cursor="hand2")
            elif typ2 == "gauche":
                self.border.itemconfigure(idButton, image=config.Config.image[79])
                self.border.config(cursor="hand2")
        elif typ == "sort":
            if typ2 == "retour":
                self.border.itemconfigure(idButton, image=config.Config.image[74])
                self.border.config(cursor="")
            elif typ2 == "droite":
                self.border.itemconfigure(idButton, image=config.Config.image[75])
                self.border.config(cursor="")
            elif typ2 == "gauche":
                self.border.itemconfigure(idButton, image=config.Config.image[76])
                self.border.config(cursor="")
    
        pass

        
