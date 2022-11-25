import tkinter as tk
from tkinter import PhotoImage




class PiecesListGUI(tk.Canvas):
    
    
    
    #   Creer l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, parent : tk.Misc, images : list, playerName : str, height : int = 420, width : int = 320):
        super(PiecesListGUI,self).__init__(parent)
        self.create_image(
            0,
            0,
            image=images[0],
            anchor=tk.NW
        )
        
        self.create_image(
            15,
            10,
            image=images[1],
            anchor=tk.NW
        )
        self.config(width=width,height=height,bg="#FFF")
        self.place(x=-4,y=-4,height=height,width=width)
        
        self.text = self.create_text((width+50)/2,55,fill="white",font=('Lilita One', 32),text=playerName,anchor=tk.CENTER)
        
    def changeName(self, newName : str):
        self.itemconfig(self.text, text=newName)


if __name__=="__main__":

    global window
    window = tk.Tk()
    window.geometry("1440x1024")
    
    images = []
    images.append(PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
    
    accueil=PiecesListGUI(window,images,"Caaka")
    accueil.changeName("Joueur 12")


    window.mainloop()