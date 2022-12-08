import tkinter as tk
from PIL import ImageTk,Image




class PiecesListGUI(tk.Frame):
    
    
    
    #   Creer l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, parent : tk.Canvas, images : list, playerName : str, nb_player : int):
        super(PiecesListGUI,self).__init__(parent)
        self.parent = parent
        self.nb_player=nb_player
        self.list = self.parent.create_image(
            0,
            0,
            image=images[0],
            anchor=tk.NW
        )
        
        self.nameZone = self.parent.create_image(
            15,
            10,
            image=images[nb_player],
            anchor=tk.NW
        )
        
        
        self.text = parent.create_text((367)/2,55,fill="white",font=('Lilita One', 32),text=playerName,anchor=tk.CENTER)
        
        
    def changeName(self, newName : str):
        '''
        Fonction pour changer le nom affiché
        '''
        self.parent.itemconfig(self.text, text=newName)
        
        
    def move(self, x : int, y : int):
        '''
        Fonction pour déplacer toute l'instance
        '''
        self.parent.move(self.text,x,y)
        self.parent.move(self.list,x,y)
        self.parent.move(self.nameZone,x,y)

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
    
    accueil=PiecesListGUI(border,Photo_images,"dls",1)
    accueil.changeName("Joueur 1")


    window.mainloop()
