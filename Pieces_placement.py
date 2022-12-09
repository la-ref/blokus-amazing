import tkinter as tk
from PIL import ImageTk,Image
import PiecesDeclaration as PD
from tkinter import PhotoImage
import Pieces as p
import numpy as np
import Block as b
class Pieces_placement(tk.Frame):
    def __init__(self, window, parent : tk.Canvas, nb_player : int, la_piece: str):
        super(Pieces_placement,self).__init__(parent)
        self.window = window
        self.window.bind("<Motion>", self.on_drag)
        self.parent = parent
        self.nb_player = nb_player
        self.imagepiece = { 11:(PhotoImage(file="build/assets/piece/yellow.png")),
                            12:(PhotoImage(file="build/assets/piece/green.png")),
                            13:(PhotoImage(file="build/assets/piece/red.png")),
                            14:(PhotoImage(file="build/assets/piece/blue.png"))}
        self.x = 0
        self.y = 0

        self.le_x = 0
        self.le_y = 0
        
        self.state = 0
        self.tableau_piece = [[]]
        self.tableau_piece_forme = []
        # self.tableau_piece_co = []
        self.mon_state = 0

        self.tableau_piece=PD.LISTEPIECES[la_piece].getDelimitation()
        self.image = self.imagepiece[self.nb_player]
        self.image = self.image.subsample(2)
        self.image2 = self.image.subsample(28)
        
        for i in range(len(self.tableau_piece[0])):
            self.y+=self.image.height()
            self.x=0
            for v in range(len(self.tableau_piece)):
                self.x+=self.image.width()
                if (self.tableau_piece[v][i] == 3):
                    # test = self.parent.create_image(x,y,image=self.image,anchor=tk.NW)
                    # print("1", self.x,self.y)
                    test = b.Block(self.parent,self.image,self.nb_player,self.x,self.y)
                    self.parent.tag_bind(test.bl, "<Motion>", self.on_drag)
                    self.parent.tag_bind(test.bl, "<ButtonPress-1>", self.on_click)
                    self.tableau_piece_forme.append(test)
                    # self.tableau_piece_co.append((self.x,self.y))

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
        print("1", self.le_x,self.le_y)
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            x2,y2=self.parent.coords(piece.bl)
            piece.move(x-x2-piece.base_x,y-y2-piece.base_y)

    def move_init(self, x : int, y : int):
        self.le_x=x
        self.le_y=y
        for piece in self.tableau_piece_forme:
            piece.move(x,y)


    def on_click(self,event):
        '''
        Fonction interne pour permettre le deplacement des blocks au clique
        '''
        ## si pas en mvt, enregistre la position relative avec la souris
        for block in self.tableau_piece_forme:
            block.on_click(event)
        # self.delta = 
        # x2,y2=self.parent.coords()
        # self.delta_x = event.x-
        if not self.mon_state:
            self.le_x = self.le_x-event.x
            self.le_y = self.le_y-event.y
            print(self.x,self.y, "|", event.x, event.y)
        self.mon_state=(self.mon_state+1)%2


    def on_drag(self, event):
        '''
        Fonction interne pour permettre le deplacement des blocks au mvt de la souris
        '''
        if self.mon_state == True:
            for piece in self.tableau_piece_forme:
                x2,y2=self.parent.coords(piece.bl)
                piece.move(event.x-x2-piece.base_x+self.le_x,event.y-y2-piece.base_y+self.le_y)


                print(event.x-x2-piece.base_x+self.le_x,event.y-y2-piece.base_y+self.le_y)        
            

        # self.parent.move(event.x,event.y)
        

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
    
    accueil=Pieces_placement(window,border,11,"21")
    accueil.move(300,300)  
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