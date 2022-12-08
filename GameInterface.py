import tkinter as tk
import GridInterface as GI
# import Elements.nameGUI as B
import Elements.PiecesListGUI as P
from tkinter import PhotoImage

class GameInterface(tk.Frame):
    
    def __init__(self, parent : tk.Misc):
        tk.Frame.__init__(self, parent)
        
        
    
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)
        
        List1 = P.PiecesListGUI(window,images,420,315)
        List1.grid(row = 0, column = 0, pady = 2, padx=2)
        
        List2 = P.PiecesListGUI(window,images,420,315)
        List2.grid(row = 0, column = 2, pady = 2, padx=2)
        
        List3 = P.PiecesListGUI(window,images,420,315)
        List3.grid(row = 1, column = 2, pady = 2, padx=2)
        
        List4 = P.PiecesListGUI(window,images,420,315)
        List4.grid(row = 1, column = 0, pady = 2, padx=2)



        
        
        # give_up_button = B.RoundedButton(text="Hors ligne", radius=50, hauteur=70, largueur=400, fontsize=20, btnbackground="#0078ff", btnforeground="#ffffff", clicked=None)
        # give_up_button.place(x=720-200,y=0,height=70,width=400)
        
        board = GI.GridInterface(self)
        board.grid(row = 0, rowspan=2 , column = 1, pady = 10, padx=50)


if __name__=="__main__":

    window = tk.Tk()
    window.geometry("1440x1024")
    
    images = []
    images.append(PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
    
    accueil=GameInterface(window)
    accueil.pack()


    window.mainloop()