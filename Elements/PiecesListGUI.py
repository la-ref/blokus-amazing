import tkinter as tk





class PiecesListGUI(tk.Frame):
    
    
    
    #   Creer l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, parent : tk.Canvas, images : list, playerName : str, nb_player : int, height : int = 420, width : int = 317):
        super(PiecesListGUI,self).__init__(parent)
        self.parent = parent
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
        
        # self.config(width=width,height=height,bg="white",borderwidth=0,highlightthickness=0)
        # self.place(x=-4,y=-4,height=height,width=width)
        
        self.text = parent.create_text((width+50)/2,55,fill="white",font=('Lilita One', 32),text=playerName,anchor=tk.CENTER)
        
    def changeName(self, newName : str):
        self.parent.itemconfig(self.text, text=newName)
        
    def move(self, x : int, y : int):
        self.parent.move(self.text,x,y)
        self.parent.move(self.list,x,y)
        self.parent.move(self.nameZone,x,y)
        
    def drag(self, event):
        # self.move(event.x,event.y)
        self.move(300,800)
        # print(event.x,event.y)

if __name__=="__main__":
    from tkinter import PhotoImage
    window = tk.Tk()
    window.geometry("1440x1024")
    
    border = tk.Canvas()
    border.config(bg="white")
    border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
    
    images = []
    images.append(PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
    
    accueil=PiecesListGUI(border,images,"Caaka",1)
    accueil.changeName("Joueur 1")


    window.mainloop()