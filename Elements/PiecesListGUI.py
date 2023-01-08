import tkinter as tk
from PIL import ImageTk,Image
import PiecesDeclaration as PD
from tkinter import PhotoImage
import Pieces as p
import numpy as np
import Pieces_placement as PP
from config import config

class PiecesListGUI(tk.Frame):
    
    
    
    #   Creer l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, window, parent : tk.Canvas, playerName : str, nb_player : int, height : int = 420, width : int = 317):
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
        self.parent.itemconfig(self.text, text=newName)
        
    def surrender(self):
        self.parent.itemconfig(self.nameZone,image=config.Config.image[32])
        
        
    # Fonction utiliser par Mouvement Manager (à supprimer plus tard)
    def move(self, x : int, y : int):
        self.parent.move(self.text,x,y)
        self.parent.move(self.list,x,y)
        self.parent.move(self.nameZone,x,y)
        for piece in self.tableau_piece_forme:
            piece.move_init2(x,y)

        
    def on_click(self,event):
        x,y=self.parent.coords(self.list)
        self.delta=event.x-x,event.y-y
        
    # def on_drag(self, event):
    #     for piece in self.tableau_piece_forme:
    #         # x,y=self.parent.coords(piece.bl)
    #         self.move(event.x,event.y)
            
    def bind(self,event_tag,call):
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

# from tkinter import *
# from PIL import Image,ImageTk

# #Create an instance of tkinter frame
# win = Tk()

# #Set the geometry of tkinter frame
# win.geometry("750x250")

# #Create a canvas
# canvas= Canvas(win, width= 600, height= 400)
# canvas.pack()

# #Load an image in the script
# images=[]
# images.append(Image.open("build/assets/frame0/player_blue.png"))
# img= ImageTk.PhotoImage(images[0].rotate(90))

# #Add image to the Canvas Items
# canvas.create_image(10,10,anchor=NW,image=img)

# win.mainloop()