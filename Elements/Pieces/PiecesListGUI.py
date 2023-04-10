import copy
import tkinter as tk
from PIL import ImageTk,Image
import Elements.Pieces.PiecesDeclaration as PD
from tkinter import PhotoImage
import Elements.Pieces.Pieces as p
import numpy as np
import Vues.Game.Pieces_placement as PP
from config import config

class PiecesListGUI(tk.Frame):
    
    def __init__(self, window, parent : tk.Canvas, playerName : str, nb_player : int, height : int = 420, width : int = 317):
        """ Constructeur qui génère l'emplacement du joueur sur la page de jeu
        avec notamment l'arrière plan de sa zone, le pseudo du joueur et ses pièces.

        Args:
            window: La fenêtre de jeu
            parent (tk.Canvas): La fauille de dessin de la pièce
            playerName (str): Nom du joueur
            nb_player (int): Numéro du joueur
            height (int): Hauteur de la fenêtre
            width (int): Largueur de la fenêtre
        """
        super(PiecesListGUI,self).__init__(parent)
        
        self.parent = parent
        self.list = self.parent.create_image(
            0,
            0,
            image=config.Config.image[9],
            anchor=tk.NW
        )
        
        self.nameZone = self.parent.create_image(
            15,
            10,
            image=config.Config.image[nb_player+10],
            anchor=tk.NW
        )
        
        
        self.text = parent.create_text((width+50)/2,55,fill="white",font=('Lilita One', config.Config.taillePolice[3]),text=playerName,anchor=tk.CENTER)
        
        decalageX = 2
        decalageY = 100
        self.tableau_piece_forme = []

        i1 = 0
        maxheight = 0
        
        for valeur in (copy.deepcopy(PD.LISTEPIECES) if config.Config.controller.onlineGame else config.Config.controller.getGame().getPlayers()[nb_player].getPieces()):
            
            self.tableau_piece_forme.append(PP.Pieces_placement(window,self.parent,nb_player,valeur,self))
            self.tableau_piece_forme[i1].move_init(decalageX,decalageY)
            decalageX+=self.tableau_piece_forme[i1].getWidth_Petit()*self.tableau_piece_forme[i1].getImage().width() + 10
            if self.tableau_piece_forme[i1].getHeight_Petit() > maxheight:
                maxheight = self.tableau_piece_forme[i1].getHeight_Petit()
            i1+=1

            if (decalageX) >= 317-(20*3):
                decalageX= 2
                decalageY+= (maxheight*self.tableau_piece_forme[i1-1].getImage().height())+10
                maxheight = 0
            self.nb_player=nb_player


    def deletePieceOnline(self,pieceId,player):
        if pieceId >= 0 and pieceId <= len(self.tableau_piece_forme): 
            print(pieceId,"piece =")
            self.tableau_piece_forme[pieceId-1].deletePieceOnline()
            

        
    def changeName(self, newName : str):
        """ Changer le nom affiché sur la zone du joueur

        Args:
            newName (str): Nom du joueur
        """
        self.parent.itemconfig(self.text, text=newName)
        
    def surrender(self):
        """ Changer l'arrière plan de la zone du joueur 
        """
        self.parent.itemconfig(self.nameZone,image=config.Config.image[32])
        
    def remettrePiece_copy(self):  #! inutilisée
        """ Fonction qui permet de remettre les pièces par défaut
        """
        for piece in self.tableau_piece_forme:
            piece.remettrePiece_copy()

    def move(self, x : int, y : int):
        """ Déplacement de toute la zone du joueur

        Args:
            x (int): Coordonnées en X
            y (int): Coordonnées en Y
        """
        self.parent.move(self.text,x,y)
        self.parent.move(self.list,x,y)
        self.parent.move(self.nameZone,x,y)
        for piece in self.tableau_piece_forme:
            piece.move_init2(x,y)

    def removePiece_placement(self,piece : int):
        config.Config.controller.game.getPlayers()[self.nb_player].removePiece(piece)

    def removePiece(self,piece : int):
        self.tableau_piece_forme[piece-1].enlever_piece()

    def bind(self,event_tag,call):
        """ Gestion des paramètres de liaison au bloc 

        Args:
            event_tag (Tkinter event): Évènement attaché au joueur
            call (Tkinter callback): Callback attaché à l'évènement
        """
        self.parent.tag_bind(self.list,event_tag,call)
        self.parent.tag_bind(self.nameZone,event_tag,call)
        self.parent.tag_bind(self.text,event_tag,call)
        


