import tkinter as tk
import Elements.PiecesListGUI as PG
import MouvementManager as Mv
from tkinter import PhotoImage
from Board import Board
from PIL import ImageTk
from config import config

class GridInterface(tk.Frame):
    def __init__(self, parent : tk.Canvas,board):
        super(GridInterface,self).__init__(parent)
        self.parent = parent
        self.images = []
        self.imageplateau = self.parent.create_image(  #270x270
            0,
            0,
            image=config.Config.image[8],
            anchor=tk.NW
        )
        self.board = board
        self.imagepiece = config.Config.imagepiece
        self.couleur = {
            11:"#FFC700",
            12:"#32BF00",
            13:"#BC0000",
            14:"#0045CC"
        }
        self.bordure = [self.parent.create_rectangle(439, 241, 1000, 231,outline=self.couleur[11], fill=self.couleur[11]),
                        self.parent.create_rectangle(440, 792, 999, 782,outline=self.couleur[11], fill=self.couleur[11]),
                        self.parent.create_rectangle(439, 241, 449, 791,outline=self.couleur[11], fill=self.couleur[11]),
                        self.parent.create_rectangle(990, 242, 1000, 791,outline=self.couleur[11], fill=self.couleur[11])]
        self.pieces = []


    def setBoard(self,board):
        self.board = board

    def refreshBoard(self,board):
        self.board = board
        for i in range(self.board.getBoardSize()):
            for y in range(self.board.getBoardSize()):
                valeur = self.board.getColorAt(i,y)
                if valeur:
                    piece = self.imagepiece[valeur]
                    if ((i,y) not in self.pieces):
                        self.parent.tag_lower(self.parent.create_image(463+y*(piece.width()),255+i*(piece.height()),image=piece))
                        self.pieces.append((i,y))
    
    def refreshPlayer(self,playerColor,affiche):
        for bord in self.bordure:
            if not affiche:
                self.parent.itemconfig(bord,fill=self.couleur[11+playerColor],outline=self.couleur[11+playerColor])
                self.parent.tag_raise(bord)
            else:
                self.parent.delete(bord)
    
        
    def move(self, x : int, y : int):
        self.parent.move(self.imageplateau,x,y)


if __name__=="__main__":
    from tkinter import PhotoImage
    
    window = tk.Tk()
    images = []

    images.append(ImageTk.PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_yellow.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_green.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_red.png"))
    images.append(PhotoImage(file="build/assets/frame0/AppBorder.png"))
    images.append(PhotoImage(file="build/assets/frame0/board.png"))#270x270
    
    window.geometry("1440x1024")
    
    border = tk.Canvas()
    border.config(bg="white")
    border.create_image(
            0,
            0,
            image=images[5],
            anchor=tk.NW
        )
    border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
    board = GridInterface(border,Board())
    board.move(x=720-270,y=512-270)
    

    def task():
        #board.jouer()
        window.update()
        #board.refreshBoard()

    while 1:
        task()  