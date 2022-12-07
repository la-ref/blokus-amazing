import tkinter as tk
import Elements.PiecesListGUI as PG
import MouvementManager as Mv
from PIL import ImageTk

class GridInterface(tk.Frame):
    
    def __init__(self, parent : tk.Canvas):
        super(GridInterface,self).__init__(parent)
        self.parent = parent
        self.board = self.parent.create_image(  #270x270
            0,
            0,
            image=images[-1],
            anchor=tk.NW
        )
        # self.config(highlightbackground = "grey",highlightthickness=2)
        
    def move(self, x : int, y : int):
        self.parent.move(self.board,x,y)


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
    
    board = GridInterface(border)
    board.move(x=720-270,y=512-270)
    
    List1 = PG.PiecesListGUI(border,images,"Joueur 1",1)
    List1.move(x=70,y=80)
    
    List2 = PG.PiecesListGUI(border,images,"Joueur 2",2)
    List2.move(x=1047,y=80)
    
    List3 = PG.PiecesListGUI(border,images,"Joueur 3",3)
    List3.move(x=1047,y=524)
    
    List4 = PG.PiecesListGUI(border,images,"Joueur 4",4)
    List4.move(x=70,y=524)
    

    

    
    window.mainloop()