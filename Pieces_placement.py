import tkinter as tk
from PIL import ImageTk,Image
import PiecesDeclaration as PD
from tkinter import PhotoImage
import Pieces as p
import numpy as np

class Pieces_placement(tk.Frame):
    def __init__(self, parent : tk.Canvas, nb_player : int, la_piece: str):
        super(Pieces_placement,self).__init__(parent)
        self.parent = parent
        self.nb_player = nb_player
        self.imagepiece = { 11:(PhotoImage(file="build/assets/piece/yellow.png")),
                            12:(PhotoImage(file="build/assets/piece/green.png")),
                            13:(PhotoImage(file="build/assets/piece/red.png")),
                            14:(PhotoImage(file="build/assets/piece/blue.png"))}
        
        x = 0
        y = 0

        self.tableau_piece = [[]]
        self.tableau_piece_forme = [[]]

        self.tableau_piece=PD.LISTEPIECES[la_piece].getDelimitation()
        self.image = self.imagepiece[self.nb_player]
        self.image = self.image.subsample(2)
        for i in range(len(self.tableau_piece[0])):
            y+=self.image.height()
            x=0
            for v in range(len(self.tableau_piece)):
                x+=self.image.width()
                if (self.tableau_piece[v][i] == 3):
                    test = self.parent.create_image(x,y,image=self.image,anchor=tk.NW)
                    self.tableau_piece_forme.append(test)

    def getImage(self):
        return self.image
    
    def getWidth(self):
        return len(self.tableau_piece)

    def getHeight(self):
        return len(self.tableau_piece[0])
    
    def getWidth_Petit(self):
        return len(self.tableau_piece)-2

    def getHeight_Petit(self):
        return len(self.tableau_piece[0])-2

    def move(self, x : int, y : int):
        for piece in self.tableau_piece_forme:
            self.parent.move(piece,x,y)

if __name__=="__main__":
    from tkinter import PhotoImage
    window = tk.Tk()
    window.geometry("1440x1024")
    
    border = tk.Canvas()
    border.config(bg="white")
    border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
    
    images = []
    images.append(Image.open("build/assets/frame0/empty_list.png"))
    images.append(Image.open("build/assets/frame0/player_blue.png"))
    Photo_images = []
    Photo_images.append(ImageTk.PhotoImage(images[0]))
    Photo_images.append(ImageTk.PhotoImage(images[1].rotate(angle=00, expand=True)))
    
    accueil=Pieces_placement(border,11,"21")

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