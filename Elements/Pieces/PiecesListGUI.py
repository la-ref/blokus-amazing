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
            self (Game): game
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
            image=config.Config.image[nb_player],
            anchor=tk.NW
        )
        
        
        self.text = parent.create_text((width+50)/2,55,fill="white",font=('Lilita One', 22),text=playerName,anchor=tk.CENTER)
        
        decalageX = 2
        decalageY = 100
        self.tableau_piece = []
        self.tableau_piece_forme = []
        nb_player = nb_player+1
        i1 = 0
        maxheight = 0
        for valeur in PD.LISTEPIECES:
            self.tableau_piece_forme.append([])
            self.tableau_piece_forme[i1] = PP.Pieces_placement(window,self.parent,nb_player,valeur)

            self.tableau_piece_forme[i1].move_init(decalageX,decalageY)
            decalageX+=self.tableau_piece_forme[i1].getWidth_Petit()*self.tableau_piece_forme[i1].getImage().width() + 10
            print(decalageX)
            if self.tableau_piece_forme[i1].getHeight_Petit() > maxheight:
                maxheight = self.tableau_piece_forme[i1].getHeight_Petit()

            i1+=1

            if (decalageX) >= 317-(20*3):
                decalageX= 2
                decalageY+= (maxheight*self.tableau_piece_forme[i1-1].getImage().height())+10
                maxheight = 0



        
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



    def on_click(self,event):
        """ Gestion du clic d'un joueur

        Args:
            event (Tkinter): Coordonnées X et Y du clic
        """
        x,y=self.parent.coords(self.list)
        self.delta=event.x-x,event.y-y
        
    def bind(self,event_tag,call):
        """ Gestion des paramètres de liaison au bloc 

        Args:
            event_tag (Tkinter event): Évènement attaché au joueur
            call (Tkinter callback): Callback attaché à l'évènement
        """
        self.parent.tag_bind(self.list,event_tag,call)
        self.parent.tag_bind(self.nameZone,event_tag,call)
        self.parent.tag_bind(self.text,event_tag,call)

if __name__=="__main__":
    from tkinter import PhotoImage
    window = tk.Tk()
    window.geometry("1440x1024")
    
    border = tk.Canvas()
    border.config(bg="white")
    border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
    
    accueil=PiecesListGUI(window, border,"Caaka",1)
    accueil.changeName("Joueur 1")


    window.mainloop()
