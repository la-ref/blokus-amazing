import tkinter as tk
import Elements.PiecesListGUI as PG
import MouvementManager as Mv

class GridInterface(tk.Canvas):
    
    def __init__(self, parent : tk.Misc):
        super(GridInterface,self).__init__(parent)
        for i in range(20):
            for j in range(20):
                widget = tk.Frame(self,highlightthickness=1)
                widget.config(width=25,height=25 , bg="white",highlightbackground = "grey")
                widget.grid(row = i, column = j, padx=1, pady=1)
        self.config(highlightbackground = "grey",highlightthickness=1)


if __name__=="__main__":
    from tkinter import PhotoImage
    
    window = tk.Tk()
    images = []

    images.append(PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_yellow.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_green.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_red.png"))
    images.append(PhotoImage(file="build/assets/frame0/game_board.png"))

    
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
    
    List1 = PG.PiecesListGUI(border,images,"Joueur 1",1)
    List1.move(x=70,y=80)
    # List1.place(x=70,y=80,anchor=tk.NW)
    
    List2 = PG.PiecesListGUI(border,images,"Joueur 2",2)
    List2.move(x=1047,y=80)
    
    List3 = PG.PiecesListGUI(border,images,"Joueur 3",3)
    List3.move(x=1047,y=524)
    
    List4 = PG.PiecesListGUI(border,images,"Joueur 4",4)
    List4.move(x=70,y=524)
    border.tag_bind(List4.list,'<Button1-Motion>',List4.drag)

    board = GridInterface(border)
    board.place(x=720,y=512,anchor=tk.CENTER)
    

    # drag1 = Mv.MouvementManager(List4,True,True)
    window.mainloop()