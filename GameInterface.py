import tkinter as tk
import GridInterface as GI
import Elements.PiecesListGUI as P
from tkinter import PhotoImage
import GridInterface as Gi
import Block as Bl

class GameInterface(tk.Canvas):
    
    def __init__(self, parent : tk.Misc, images : list):
        tk.Canvas.__init__(self, parent)
        self.config(bg="white")
        self.create_image(
                0,
                0,
                image=images[5],
                anchor=tk.NW
            )
        self.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
        
        board = Gi.GridInterface(self,images)
        board.move(x=450,y=242)
        
        List1 = P.PiecesListGUI(self,images,"Joueur 1",1)
        List1.move(x=70,y=80)
        
        List2 = P.PiecesListGUI(self,images,"Joueur 2",2)
        List2.move(x=1047,y=80)
        
        List3 = P.PiecesListGUI(self,images,"Joueur 3",3)
        List3.move(x=1047,y=524)
        
        List4 = P.PiecesListGUI(self,images,"Joueur 4",4)
        List4.move(x=70,y=524)
        


if __name__=="__main__":
    from tkinter import PhotoImage
    
    window = tk.Tk()
    images = []

    images.append(PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_yellow.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_green.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_red.png"))
    images.append(PhotoImage(file="build/assets/frame0/Appborder.png"))
    images.append(PhotoImage(file="build/assets/frame0/blue_1.png"))
    images.append(PhotoImage(file="build/assets/frame0/board.png"))#270x270
    images.append(PhotoImage(file="build/assets/frame0/blue_1.png"))#270x270
    
    window.geometry("1440x1024")
    border = GameInterface(window,images)

    

    

    
    window.mainloop()