import tkinter as tk
import Elements.PiecesListGUI as PG
import MouvementManager as Mv
from tkinter import PhotoImage
from Board import Board
from PIL import ImageTk

class GridInterface(tk.Frame):
    def __init__(self, parent : tk.Canvas,board):
        super(GridInterface,self).__init__(parent)
        self.parent = parent
        self.images = []

        self.images.append(ImageTk.PhotoImage(file="build/assets/frame0/empty_list.png"))
        self.images.append(PhotoImage(file="build/assets/frame0/player_yellow.png"))
        self.images.append(PhotoImage(file="build/assets/frame0/player_green.png"))
        self.images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
        self.images.append(PhotoImage(file="build/assets/frame0/player_red.png"))
        self.images.append(PhotoImage(file="build/assets/frame0/AppBorder.png"))
        self.images.append(PhotoImage(file="build/assets/frame0/board.png"))
        self.images.append(PhotoImage(file="build/assets/frame0/button_give_up.png"))
        # self.images.append(PhotoImage(file=""))
        self.imageplateau = self.parent.create_image(  #270x270
            0,
            0,
            image=self.images[6],
            anchor=tk.NW
        )
        self.board = board
        self.imagepiece = { 11:(PhotoImage(file="build/assets/piece/yellow.png")),
                            12:(PhotoImage(file="build/assets/piece/green.png")),
                            13:(PhotoImage(file="build/assets/piece/red.png")),
                            14:(PhotoImage(file="build/assets/piece/blue.png"))} # 11 jaune, 12 vert, 13 rouge, 14 bleu
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


    def setBoard(self,board):
        self.board = board

    def refreshBoard(self,board):
        self.board = board
        for i in range(self.board.getBoardSize()):
            for y in range(self.board.getBoardSize()):
                valeur = self.board.getColorAt(i,y)
                if valeur:
                    piece = self.imagepiece[valeur]
                    self.parent.tag_lower(self.parent.create_image(463+y*(piece.width()),255+i*(piece.height()),image=piece))
    
    def refreshPlayer(self,playerColor):
        print("caca",playerColor)
        if playerColor:
            for bord in self.bordure:
                self.parent.itemconfig(bord,fill=self.couleur[11+playerColor],outline=self.couleur[11+playerColor])
                self.parent.tag_raise(bord)
    
        
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
    
    List1 = PG.PiecesListGUI(border,images,"Joueur 1",1)
    List1.move(x=70,y=80)
    
    List2 = PG.PiecesListGUI(border,images,"Joueur 2",2)
    List2.move(x=1047,y=80)
    
    List3 = PG.PiecesListGUI(border,images,"Joueur 3",3)
    List3.move(x=1047,y=524)
    
    List4 = PG.PiecesListGUI(border,images,"Joueur 4",4)
    List4.move(x=70,y=524)
    Mv.MouvementManager(List4,True,True)
    

    def task():
        #board.jouer()
        window.update()
        #board.refreshBoard()

    while 1:
        task()  