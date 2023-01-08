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
        self.window.bind("<Motion>", self.on_drag, add='+')
        self.window.bind("<MouseWheel>", self.on_rotate, add='+')
        self.parent = parent
        self.nb_player = nb_player
        self.imagepiece = { 11:(PhotoImage(file="build/assets/piece/yellow.png")),
                            12:(PhotoImage(file="build/assets/piece/green.png")),
                            13:(PhotoImage(file="build/assets/piece/red.png")),
                            14:(PhotoImage(file="build/assets/piece/blue.png"))}
        self.x = 0
        self.y = 0
        self.la_piece = la_piece
        self.le_x = 0
        self.le_y = 0

        self.rotate = False

        self.souris_x = 0
        self.sourix_y = 0
        
        
        self.state = 0
        self.tableau_piece = [[]]
        self.tableau_piece_forme = []
        # self.tableau_piece_co = []
        self.mon_state = 0

        self.piece=PD.LISTEPIECES[la_piece]
        self.tableau_piece=self.piece.getDelimitation()
        self.image = self.imagepiece[self.nb_player]
        self.image = self.image.subsample(2)
        self.image2 = self.image.subsample(28)
        
        for i in range(len(self.tableau_piece[0])):
            self.y+=self.image.height()
            self.x=0
            for v in range(len(self.tableau_piece)):
                self.x+=self.image.width()
                if (self.tableau_piece[v][i] == 3):
                    test = b.Block(self.parent,self.image,self.nb_player,self.x,self.y,self)
                    self.parent.tag_bind(test.bl, "<Motion>", self.on_drag)
                    self.parent.tag_bind(test.bl, "<ButtonPress-1>", self.on_click)
                    self.parent.tag_bind(test.bl, "<ButtonPress-2>", self.on_flip)
                    self.tableau_piece_forme.append(test)
    def getPieceBoardCoord(self):
        '''
        Fonction pour obtenir les coords du coin gauche de la piece sur le tableau 
        '''
        x,y=self.parent.coords(self.tableau_piece_forme[0].bl)
        dy,dx=np.argwhere(self.tableau_piece==3)[0]
        x,y=x-27*(dx-1),y-27*(dy-1) # calcul les coordonnées du coin haut gauche
        return [(x-450)//27,(y-242)//27]

    def getPieceCoord(self):
        '''
        Fonction pour obtenir les coords du coin gauche de la piece sur l'écran 
        '''
        x,y=self.parent.coords(self.tableau_piece_forme[0].bl)
        dy,dx=np.argwhere(self.tableau_piece==3)[0]
        x,y=x-27*(dx-1),y-27*(dy-1) # calcul les coordonnées du coin haut gauche
        return [x,y]

    def on_flip(self,event):
        if self.mon_state == True:
            self.x,self.y=self.getPieceCoord()
            self.ancienx,self.ancieny=self.getPieceCoord()

            for piece in self.tableau_piece_forme:
                objet = self.parent.find_withtag(piece.bl)
                ma_piece = objet[0]
                self.parent.delete(ma_piece)

            piece = PD.LISTEPIECES[self.la_piece]
            piece.flip()
            self.changement_piece_tourner(piece)

    def on_rotate(self,event):
        if self.mon_state == True:
            self.x,self.y=self.getPieceCoord()
            self.ancienx,self.ancieny=self.getPieceCoord()

            for piece in self.tableau_piece_forme:
                objet = self.parent.find_withtag(piece.bl)
                ma_piece = objet[0]
                self.parent.delete(ma_piece)

            piece = PD.LISTEPIECES[self.la_piece]
            piece.rotate90()

            self.changement_piece_tourner(piece)
    
    def changement_piece_tourner(self,piece):
        self.rotate = True

        self.tableau_piece = [[]]
        self.tableau_piece=piece.getDelimitation()
        
        self.tableau_piece_forme = []

        self.back_x = self.x
        self.back_y = self.y

        self.x=0
        self.y=0

        for i in range(len(self.tableau_piece[0])):
            self.y+=self.image.height()
            self.x = 0
            for v in range(len(self.tableau_piece)):
                self.x+=self.image.width()
                if (self.tableau_piece[v][i] == 3):
                    le_block = b.Block(self.parent,self.image,self.nb_player,0+self.x,0+self.y,self)
                    self.parent.tag_bind(le_block.bl, "<Motion>", self.on_drag)
                    self.parent.tag_bind(le_block.bl, "<ButtonPress-1>", self.on_click)
                    self.parent.tag_bind(le_block.bl, "<ButtonPress-2>", self.on_flip)
                    self.tableau_piece_forme.append(le_block)
                    le_block.move(self.back_x-self.x,self.back_y-self.y)
                    le_block.state = 1
            
        for piece in self.tableau_piece_forme:
            x2,y2=self.parent.coords(piece.bl)
            piece.move(piece.base_xoff,piece.base_yoff)
        
        self.premier = 0
        for piece in self.tableau_piece_forme:
            if self.premier == 0:
                self.ox2,self.oy2=self.parent.coords(piece.bl)
                differenceX = self.le_x+piece.base_xoff
                differenceY = self.le_y+piece.base_yoff
                self.le_x = self.le_x-differenceX
                self.le_y = self.le_y-differenceY
                self.premier = 1

        for piece in self.tableau_piece_forme:
            x2,y2=self.parent.coords(piece.bl)
            piece.move(self.souris_x-x2+piece.base_xoff+self.le_x,self.sourix_y-y2+piece.base_yoff+self.le_y)

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
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            x2,y2=self.parent.coords(piece.bl)
            piece.move(x-x2-piece.base_x,y-y2-piece.base_y)
    

    def move_init(self, x : int, y : int):
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            piece.move(x,y)
    
    def move_init2(self, x : int, y : int):
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            piece.move(x,y)
            piece.base_x += x
            piece.base_y += y
            piece.base_xoff2 = piece.base_x
            piece.base_yoff2 = piece.base_y
    
    def move_init3(self, x : int, y : int):
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            piece.move(x,y)
            piece.base_x += x
            piece.base_y += y
            self.base_xoff3 = self.le_x
            self.base_yoff3 = self.le_y


    def on_click(self,event):
        '''
        Fonction interne pour permettre le deplacement des blocks au clique
        '''
        ## si pas en mvt, enregistre la position relative avec la souris
        if (event.x<450 or event.x>990 or event.y<242 or event.y>782):
            self.image = self.image.subsample(2)
            self.ok = 0
            for block in self.tableau_piece_forme:
                block.on_click(event)
                self.parent.itemconfigure(block.bl, image=self.image)
        self.le_x = self.base_xoff3
        self.le_y = self.base_yoff3

        if not self.mon_state:
            if (event.x<450 or event.x>990 or event.y<242 or event.y>782):
                self.image = self.imagepiece[self.nb_player]
                self.ok = 0
                self.saveliste = self.tableau_piece_forme
                for piece in self.tableau_piece_forme:
                    if self.ok == 0:
                        self.ox2,self.oy2=self.parent.coords(piece.bl)
                        self.le_x = self.le_x-self.ox2
                        self.le_y = self.le_y-self.oy2
                        self.ok = 1
                for piece in self.tableau_piece_forme:
                    objet = self.parent.find_withtag(piece.bl)
                    ma_piece = objet[0]
                    self.parent.delete(ma_piece)
                
                self.tableau_piece_forme = []

                # for block in self.tableau_piece_forme:
                #     block.recreate(block.save_x,block.save_y,self.image)
                #     self.parent.tag_bind(block.bl, "<Motion>", self.on_drag)
                #     self.parent.tag_bind(block.bl, "<ButtonPress-1>", self.on_click)
                #     self.parent.tag_bind(block.bl, "<ButtonPress-2>", self.on_flip)
                self.changement_piece_tourner(self.piece)
        else:
            if (event.x<450 or event.x>990 or event.y<242 or event.y>782):
                for piece in self.tableau_piece_forme:
                    objet = self.parent.find_withtag(piece.bl)
                    ma_piece = objet[0]
                    self.parent.delete(ma_piece)
                
                self.tableau_piece_forme = self.saveliste

                for block in self.tableau_piece_forme:
                    block.recreate(block.save_x,block.save_y,self.image)
                    self.parent.tag_bind(block.bl, "<Motion>", self.on_drag)
                    self.parent.tag_bind(block.bl, "<ButtonPress-1>", self.on_click)
                    self.parent.tag_bind(block.bl, "<ButtonPress-2>", self.on_flip)
                    block.state = 0
        if (event.x<450 or event.x>990 or event.y<242 or event.y>782):
            self.mon_state=(self.mon_state+1)%2


    def on_drag(self, event):
        '''
        Fonction interne pour permettre le deplacement des blocks au mvt de la souris
        '''
        self.souris_x = event.x
        self.sourix_y = event.y
        self.premier2 = 0
        if self.mon_state == True:
            for piece in self.tableau_piece_forme:
                x2,y2=self.parent.coords(piece.bl)
                piece.move(event.x-x2+piece.base_xoff+self.le_x,event.y-y2+piece.base_yoff+self.le_y) 
        self.premier2 = 0
        

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